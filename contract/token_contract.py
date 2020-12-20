import smartpy as sp
import json

FA12 = sp.import_script_from_url("file:./contract/FA1.2.py")

def inline(f, *args, **kwargs):
  res = sp.seq()
  with res:
      f(*args, **kwargs)
  return sp.bind(res)

class Error_message:
    def permit_missigned(self):        return "MISSIGNED"
    def duplicate_permit(self):        return "DUP_PERMIT"
    def expiry_exceeds_max(self):      return "MAX_SECONDS_EXCEEDED"
    def user_unauthorized(self):       return "USER_UNAUTHORIZED"
    def permit_nonexistent(self):      return "PERMIT_NONEXISTENT"
    def permit_revoked(self):          return "PERMIT_REVOKED"
    def unsafe_allowance_change(self): return "UNSAFE_ALLOWANCE_CHANGE"
    def balance_insufficient(self): return "BALANCE_INSUFFICIENT"

class Permit(FA12.FA12):
    def __init__(self, admin):
        self.error_message=Error_message()
        with open('metadata/metadata.json', 'r') as f:
          #loads then dumps to confirm correctly formatted json
          metadata = json.dumps(json.load(f))
          super().__init__(admin,
                  permit_data=sp.record(permits = sp.map(tkey=sp.TPair(sp.TAddress, sp.TBytes), tvalue=sp.TTimestamp),
                  user_expiries = sp.map(tkey=sp.TAddress, tvalue=sp.TOption(sp.TNat)),
                  permit_expiries = sp.map(tkey=sp.TPair(sp.TAddress, sp.TBytes), tvalue=sp.TOption(sp.TNat)),
                  counter = 0 ,
                  default_expiry = 50000,
                  max_expiry = 2628000),
                  metadata=sp.big_map(l={"": sp.bytes_of_string("tezos-storage:md-json"), "md-json": sp.bytes_of_string(metadata)}))


    @sp.entry_point
    def transfer(self, params):
        sp.set_type(params, sp.TRecord(from_=sp.TAddress, to_=sp.TAddress,
                                       value=sp.TNat)).layout(("from_ as from", ("to_ as to", "value")))
        sender = sp.local("sender", sp.sender)
        sp.if (self.transfer_presigned(params)):
            # Setting sender.value to from_ so call to transfer_helper will be authorized
            sender.value = params.from_
        sp.verify((sender.value == self.data.administrator) |
                  (~self.data.paused &
                   ((params.from_ == sender.value) |
                    (self.data.balances[params.from_].approvals[sender.value] >= params.value))), self.error_message.user_unauthorized())
        self.addAddressIfNecessary(params.to_)
        sp.verify(self.data.balances[params.from_].balance >= params.value, self.error_message.balance_insufficient())
        self.data.balances[params.from_].balance = sp.as_nat(
            self.data.balances[params.from_].balance - params.value)
        self.data.balances[params.to_].balance += params.value
        sp.if ((params.from_ != sender.value) & (self.data.administrator != sender.value)):
            self.data.balances[params.from_].approvals[sender.value] = sp.as_nat(
                self.data.balances[params.from_].approvals[sender.value] - params.value)

    def getEffectiveExpiry(self, params):
        address = sp.fst(params)
        sp.if self.data.permit_data.permit_expiries.contains(params) & self.data.permit_data.permit_expiries[params].is_some():
            permit_expiry = self.data.permit_data.permit_expiries[params].open_some()
            sp.result(permit_expiry)
        sp.else:
            sp.if self.data.permit_data.user_expiries.contains(address) & self.data.permit_data.user_expiries[address].is_some():
                user_expiry = self.data.permit_data.user_expiries[address].open_some()
                sp.result(user_expiry)
            sp.else:
                default_expiry = self.data.permit_data.default_expiry
                sp.result(default_expiry)

    def delete_permit(self, permit_key):
        sp.set_type(permit_key, sp.TPair(sp.TAddress, sp.TBytes))
        sp.if self.data.permit_data.permits.contains(permit_key):
            del self.data.permit_data.permits[permit_key]
        sp.if self.data.permit_data.permit_expiries.contains(permit_key):
            self.data.permit_data.permit_expiries[permit_key] = sp.none

    @sp.sub_entry_point
    def transfer_presigned(self, params):
        sp.set_type(params, sp.TRecord(
            from_=sp.TAddress, to_=sp.TAddress, value=sp.TNat))
        params_hash = sp.blake2b(sp.pack(params))
        permit_key = sp.pair(params.from_, params_hash)
        sp.if self.data.permit_data.permits.contains(permit_key):
            permit_submission_timestamp = self.data.permit_data.permits[permit_key]
            with inline(self.getEffectiveExpiry, permit_key) as effective_expiry:
              # Deleting permit regardless of whether or not its expired
              sp.if sp.as_nat(sp.now - permit_submission_timestamp) >= effective_expiry:
                  # Expired
                  self.delete_permit(permit_key)
                  sp.result(sp.bool(False))
              sp.else:
                  self.delete_permit(permit_key)
                  sp.result(sp.bool(True))
        sp.else:
            sp.result(sp.bool(False))

    @sp.entry_point
    def permit(self, params):
        sp.set_type(params, sp.TList(
            sp.TPair(sp.TKey, sp.TPair(sp.TSignature, sp.TBytes))))
        sp.verify(~self.data.paused)
        sp.for permit in params:
            public_key = sp.fst(permit)
            signature = sp.fst(sp.snd(permit))
            params_hash = sp.snd(sp.snd(permit))
            #unsigned = sp.blake2b(mi.operator("SELF; ADDRESS; CHAIN_ID; PAIR; PAIR; PACK", [sp.TPair(sp.TNat, sp.TBytes)], [sp.TBytes])(sp.pair(self.data.permit_data.counter, params_hash)))
            unsigned = sp.pack(sp.pair(sp.pair(sp.chain_id, sp.self_address), sp.pair(
                self.data.permit_data.counter, params_hash)))
            pk_address = sp.to_address(
                sp.implicit_account(sp.hash_key(public_key)))
            permit_key = sp.pair(pk_address, params_hash)
            permit_exists = self.data.permit_data.permits.contains(permit_key)
            permit_submission_timestamp = self.data.permit_data.permits[permit_key]
            with inline(self.getEffectiveExpiry, permit_key) as effective_expiry:
              sp.verify(~ (permit_exists & (sp.as_nat(sp.now - permit_submission_timestamp) < effective_expiry)),
                        sp.pair(self.error_message.duplicate_permit(), params_hash))
            sp.verify(sp.check_signature(public_key, signature, unsigned), sp.pair(self.error_message.permit_missigned(), unsigned))
            self.data.permit_data.permits[permit_key] = sp.now
            self.data.permit_data.counter = self.data.permit_data.counter + 1

    @sp.entry_point
    def setExpiry(self, params):
        sp.set_type(params, sp.TPair(sp.TAddress, sp.TPair(sp.TNat, sp.TOption(
            sp.TBytes))))
        sp.verify(~self.data.paused)
        address = sp.fst(params)
        new_expiry = sp.fst(sp.snd(params))
        possible_bytes = sp.snd(sp.snd(params))
        sp.verify(new_expiry <= self.data.permit_data.max_expiry, self.error_message.expiry_exceeds_max())
        sp.verify_equal(address, sp.sender, message=self.error_message.user_unauthorized())
        sp.if possible_bytes.is_some():
            some_permit = possible_bytes.open_some()
            permit_key = sp.pair(address, some_permit)
            sp.verify(self.data.permit_data.permits.contains(
                permit_key), self.error_message.permit_nonexistent())
            permit_submission_timestamp = self.data.permit_data.permits[permit_key]
            with inline(self.getEffectiveExpiry, permit_key) as effective_expiry:
              sp.verify(sp.as_nat(sp.now - permit_submission_timestamp)
                        < effective_expiry, self.error_message.permit_revoked())
            self.data.permit_data.permit_expiries[permit_key] = sp.some(new_expiry)
        sp.else:
            self.data.permit_data.user_expiries[address] = sp.some(new_expiry)

    @sp.view(sp.TNat)
    def getCounter(self, params):
        sp.set_type(params, sp.TUnit)
        sp.result(self.data.permit_data.counter)

    @sp.view(sp.TNat)
    def getDefaultExpiry(self, params):
        sp.set_type(params, sp.TUnit)
        sp.result(self.data.permit_data.default_expiry)

    @sp.view(sp.TNat)
    def getMaxExpiry(self, params):
        sp.set_type(params, sp.TUnit)
        sp.result(self.data.permit_data.max_expiry)

if "templates" not in __name__:
    @sp.add_test(name="Permit")
    def test():

        scenario = sp.test_scenario()
        scenario.h1("FA1.2 template - Fungible assets + Tzip-17 permits")

        scenario.table_of_contents()

        # sp.test_account generates ED25519 key-pairs deterministically:
        admin = sp.test_account("Administrator")
        alice = sp.test_account("Alice")
        bob = sp.test_account("Robert")
        carlos = sp.test_account("Carlos")

        # Let's display the accounts:
        scenario.h1("Accounts")
        scenario.show([admin, alice, bob, carlos])

        scenario.h1("Contract")
        c1 = Permit(admin.address)

        scenario.h1("Entry points")
        scenario += c1
        scenario.h2("Admin mints a few coins")
        scenario += c1.mint(address=alice.address, value=8).run(sender=admin)
        scenario += c1.mint(address=bob.address, value=9).run(sender=admin)

        scenario.h2("Permit Submissions")
        scenario += c1.mint(address=carlos.address, value=10).run(sender=admin)
        scenario.verify(c1.data.balances[carlos.address].balance == 10)
        # add permit for transfer of 10 from carlos to bob. alice submits with correct info and also calls.
        params_bytes_1 = sp.pack(
            sp.pair(carlos.address, sp.pair(bob.address, 10)))
        params_bytes_2 = sp.pack(
            sp.pair(bob.address, sp.pair(carlos.address, 10)))
        params_hash_1 = sp.blake2b(params_bytes_1)
        params_hash_2 = sp.blake2b(params_bytes_2)
        unsigned_1 = sp.pack(sp.pair(sp.pair(sp.chain_id_cst(
            "0x9caecab9"), c1.address), sp.pair(0, params_hash_1)))
        signature_1 = sp.make_signature(
            secret_key=carlos.secret_key, message=unsigned_1, message_format="Raw")
        unsigned_2 = sp.pack(sp.pair(sp.pair(sp.chain_id_cst(
            "0x9caecab9"), c1.address), sp.pair(1, params_hash_2)))
        signature_2 = sp.make_signature(
            secret_key=bob.secret_key, message=unsigned_2, message_format="Raw")
        permit_key_1 = sp.pair(carlos.address, params_hash_1)
        permit_key_2 = sp.pair(bob.address, params_hash_2)

        scenario += c1.permit([sp.pair(carlos.public_key, sp.pair(signature_1, params_hash_1)), sp.pair(bob.public_key, sp.pair(
            signature_2, params_hash_2))]).run(sender=alice, now=sp.timestamp(1571761674), chain_id=sp.chain_id_cst("0x9caecab9"))
        scenario.verify(c1.data.permit_data.counter == 2)
        scenario.verify_equal(c1.data.permit_data.permits[(
            permit_key_1)], sp.timestamp(1571761674))
        scenario.verify_equal(c1.data.permit_data.permits[(
            permit_key_2)], sp.timestamp(1571761674))

        scenario.h2("Execute transfer using permit")
        scenario += c1.transfer(from_=carlos.address, to_=bob.address,
                                value=10).run(sender=bob, now=sp.timestamp(1571761674))
        scenario.verify(c1.data.balances[carlos.address].balance == 0)
        scenario.verify(c1.data.balances[bob.address].balance == 19)
        # Permit deleted
        scenario.verify(~ c1.data.permit_data.permits.contains(
            permit_key_1))

        scenario += c1.transfer(from_=bob.address, to_=carlos.address,
                                value=10).run(sender=carlos, now=sp.timestamp(1571761674))
        scenario.verify(c1.data.balances[carlos.address].balance == 10)
        scenario.verify(c1.data.balances[bob.address].balance == 9)
        # Permit deleted
        scenario.verify(~ c1.data.permit_data.permits.contains(
            permit_key_2))

        # Set Expiry to 0 and try to execute transfer at time less than submission_time + default_expiry, expect invalid transfer
        scenario.h2("Expired Permit")
        unsigned_3 = sp.pack(sp.pair(sp.pair(sp.chain_id_cst(
            "0x9caecab9"), c1.address), sp.pair(2, params_hash_1)))
        signature_3 = sp.make_signature(
            secret_key=carlos.secret_key, message=unsigned_3, message_format="Raw")
        scenario += c1.permit([sp.pair(carlos.public_key, sp.pair(signature_3, params_hash_1))]).run(
            sender=alice, now=sp.timestamp(1571761674), chain_id=sp.chain_id_cst("0x9caecab9"))
        scenario.verify(c1.data.permit_data.counter == 3)
        scenario.verify_equal(c1.data.permit_data.permits[
            permit_key_1], sp.timestamp(1571761674))
        scenario += c1.setExpiry(sp.pair(carlos.address, sp.pair(0, sp.some(
            params_hash_1)))).run(sender=carlos, now=sp.timestamp(1571761674))
        scenario.verify(c1.data.permit_data.permit_expiries[permit_key_1].open_some() == 0)
        scenario += c1.transfer(from_=carlos.address, to_=bob.address, value=10).run(
            sender=bob, now=sp.timestamp(1571761680), valid=False)  # Uses later time stamp

        scenario.h1("Views")
        scenario.h2("Counter")
        view_counter = FA12.Viewer(sp.TNat)
        scenario += view_counter
        scenario += c1.getCounter(sp.pair(sp.unit, view_counter.typed))
        scenario.verify_equal(view_counter.data.last, sp.some(3))

        scenario.h2("Default Expiry")
        view_defaultExpiry = FA12.Viewer(sp.TNat)
        scenario += view_defaultExpiry
        scenario += c1.getDefaultExpiry(sp.pair(sp.unit, view_defaultExpiry.typed))
        scenario.verify_equal(view_defaultExpiry.data.last, sp.some(50000))

        scenario.h2("Max Expiry")
        view_maxExpiry = FA12.Viewer(sp.TNat)
        scenario += view_maxExpiry
        scenario += c1.getMaxExpiry(sp.pair(sp.unit, view_maxExpiry.typed))
        scenario.verify_equal(view_maxExpiry.data.last, sp.some(2628000))
