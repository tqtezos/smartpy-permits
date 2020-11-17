import smartpy as sp
import smartpy_michelson as mi

class FA12(sp.Contract):
    def __init__(self, admin):
        self.init(paused = False, balances = sp.big_map(tvalue = sp.TRecord(approvals = sp.TMap(sp.TAddress, sp.TNat), balance = sp.TNat)), administrator = admin, totalSupply = 0,
        permits = sp.big_map(tkey = sp.TPair(sp.TAddress, sp.TBytes), tvalue = sp.TTimestamp), user_expiries = sp.big_map(tkey = sp.TAddress, tvalue = sp.TOption(sp.TNat)),
        permit_expiries = sp.big_map(tkey = sp.TPair(sp.TAddress, sp.TBytes), tvalue = sp.TOption(sp.TNat)), counter = 0,
        default_expiry = 360, metadata = sp.big_map(l = {"" : sp.bytes_of_string("tezos-storage:md-json"), "md-json" : sp.bytes_of_string("{}")}) )

    @sp.entry_point
    def transfer(self, params):
        sp.set_type(params, sp.TRecord(from_ = sp.TAddress, to_ = sp.TAddress, value = sp.TNat)).layout(("from_ as from", ("to_ as to", "value")))
        sender = sp.local("sender", sp.sender)
        sp.if (self.transfer_presigned(params)):
            #Setting sender.value to from_ so call to transfer_helper will be authorized
            sender.value = params.from_
        sp.verify((sender.value == self.data.administrator) |
            (~self.data.paused &
                ((params.from_ == sender.value) |
                 (self.data.balances[params.from_].approvals[sender.value] >= params.value))))
        self.addAddressIfNecessary(params.to_)
        sp.verify(self.data.balances[params.from_].balance >= params.value)
        self.data.balances[params.from_].balance = sp.as_nat(self.data.balances[params.from_].balance - params.value)
        self.data.balances[params.to_].balance += params.value
        sp.if ((params.from_ != sender.value) & (self.data.administrator != sender.value)):
            self.data.balances[params.from_].approvals[sender.value] = sp.as_nat(self.data.balances[params.from_].approvals[sender.value] - params.value)

    """
    @sp.sub_entry_point
    def getEffectiveExpiry(self, params):
        sp.set_type(params, sp.TPair(sp.TAddress, sp.TBytes))
        address = sp.fst(params)
        sp.if self.data.permit_expiries.contains(params) & self.data.permit_expiries[params].is_some():
              permit_expiry = self.data.permit_expiries[params].open_some()
              sp.result(permit_expiry)
        sp.else:
            sp.if self.data.user_expiries.contains(address) & self.data.user_expiries[address].is_some():
                  user_expiry = self.data.user_expiries[address].open_some()
                  sp.result(user_expiry)
            sp.else:
                sp.result(self.data.default_expiry)
    """

    @sp.sub_entry_point
    def transfer_presigned(self, params):
        sp.set_type(params, sp.TRecord(from_ = sp.TAddress, to_ = sp.TAddress, value = sp.TNat))
        params_hash = sp.blake2b(sp.pack(params))
        #unsigned = sp.blake2b(mi.operator("SELF; ADDRESS; CHAIN_ID; PAIR; PAIR; PACK", [sp.TPair(sp.TNat, sp.TBytes)], [sp.TBytes])(sp.pair(self.data.counter, params_hash)))
        permit_key = sp.pair(params.from_, params_hash)
        sp.if self.data.permits.contains(permit_key):
            permit_submission_timestamp = self.data.permits[permit_key]
            effective_expiry = sp.local("effective_expiry", 0)
            sp.if self.data.permit_expiries.contains(permit_key) & self.data.permit_expiries[permit_key].is_some():
                  effective_expiry.value = self.data.permit_expiries[permit_key].open_some()
            sp.else:
                sp.if self.data.user_expiries.contains(params.from_) & self.data.user_expiries[params.from_].is_some():
                      effective_expiry.value = self.data.user_expiries[params.from_].open_some()
                sp.else:
                    effective_expiry.value = self.data.default_expiry
            #effective_expiry = self.getEffectiveExpiry(sp.pair(params.from_, params_hash))
            #Deleting permit regardless of whether or not its expired
            sp.if sp.as_nat(sp.now - permit_submission_timestamp) >= effective_expiry.value:
                #Expired
                del self.data.permits[sp.pair(params.from_, params_hash)]
                sp.result(sp.bool(False))
            sp.else:
                del self.data.permits[sp.pair(params.from_, params_hash)]
                sp.result(sp.bool(True))
        sp.else:
            sp.result(sp.bool(False))

    @sp.entry_point
    def permit(self, params):
        sp.set_type(params, sp.TList(sp.TPair(sp.TKey, sp.TPair(sp.TSignature, sp.TBytes))))
        sp.verify(~self.data.paused)
        #Local variable initialization (values here don't matter)
        params_hash = sp.local('params_hash', sp.bytes('0x0000'))
        unsigned = sp.local('unsigned', sp.bytes('0x0000'))
        pk_address = sp.local('pk_address', sp.self_address)
        sp.for permit in params:
          params_hash.value = sp.snd(sp.snd(permit))
          unsigned.value = sp.pack(sp.pair(sp.pair(sp.chain_id, sp.self_address), sp.pair(self.data.counter, params_hash.value)))
          pk_address.value = sp.to_address(sp.implicit_account(sp.hash_key(sp.fst(permit))))
          sp.verify(~ self.data.permits.contains(sp.pair(pk_address.value, params_hash.value)), sp.pair("DUP_PERMIT", params_hash.value))
          sp.verify(sp.check_signature(sp.fst(permit), sp.fst(sp.snd(permit)), unsigned.value), sp.pair("MISSIGNED", unsigned.value))
          self.data.permits[sp.pair(pk_address.value, params_hash.value)] = sp.now
          self.data.counter = self.data.counter + 1

    @sp.entry_point
    def setExpiry(self, params):
        sp.set_type(params, sp.TRecord(address = sp.TAddress, seconds = sp.TNat, permit = sp.TOption(sp.TBytes))).layout(("address", ("seconds", "permit")))
        sp.verify_equal(params.address, sp.sender, message = "NOT_AUTHORIZED")
        sp.if params.permit.is_some():
          some_permit = params.permit.open_some()
          sp.verify(self.data.permits.contains(sp.pair(params.address, some_permit)), "PERMIT_NONEXISTENT")
          permit_submission_timestamp = self.data.permits[sp.pair(params.address, some_permit)]
          sp.if self.data.permit_expiries.contains(sp.pair(params.address, some_permit)) & self.data.permit_expiries[sp.pair(params.address, some_permit)].is_some():
                  permit_expiry = self.data.permit_expiries[sp.pair(params.address, some_permit)].open_some()
                  sp.verify(sp.as_nat(sp.now - permit_submission_timestamp) > permit_expiry, "PERMIT_REVOKED")
                  self.data.permit_expiries[sp.pair(params.address, some_permit)] = sp.some(params.seconds)
          sp.else:
                sp.if self.data.user_expiries.contains(params.address) & self.data.user_expiries[params.address].is_some():
                      user_expiry = self.data.user_expiries[params.address].open_some()
                      sp.verify(sp.as_nat(sp.now - permit_submission_timestamp) > user_expiry, "PERMIT_REVOKED")
                      self.data.permit_expiries[sp.pair(params.address, some_permit)] = sp.some(params.seconds)
                sp.else:
                      sp.verify(sp.as_nat(sp.now - permit_submission_timestamp) > self.data.default_expiry, "PERMIT_REVOKED")
                      self.data.permit_expiries[sp.pair(params.address, some_permit)] = sp.some(params.seconds)
        #Caution/Question about tzip-17: there might be a situation in which permit once was revoked now is alive, if we change user-expiry and that was considered the effective_expiry previously, or if default_expiry was effective and it was less than new value for user expiry.
        sp.else:
            self.data.user_expiries[params.address] = sp.some(params.seconds)

    @sp.entry_point
    def approve(self, params):
        sp.set_type(params, sp.TRecord(spender = sp.TAddress, value = sp.TNat).layout(("spender", "value")))
        sp.verify(~self.data.paused)
        alreadyApproved = self.data.balances[sp.sender].approvals.get(params.spender, 0)
        sp.verify((alreadyApproved == 0) | (params.value == 0), "UnsafeAllowanceChange")
        self.data.balances[sp.sender].approvals[params.spender] = params.value

    @sp.entry_point
    def setPause(self, params):
        sp.set_type(params, sp.TBool)
        sp.verify(sp.sender == self.data.administrator)
        self.data.paused = params

    @sp.entry_point
    def setAdministrator(self, params):
        sp.set_type(params, sp.TAddress)
        sp.verify(sp.sender == self.data.administrator)
        self.data.administrator = params

    @sp.entry_point
    def mint(self, params):
        sp.set_type(params, sp.TRecord(address = sp.TAddress, value = sp.TNat))
        sp.verify(sp.sender == self.data.administrator)
        self.addAddressIfNecessary(params.address)
        self.data.balances[params.address].balance += params.value
        self.data.totalSupply += params.value

    @sp.entry_point
    def burn(self, params):
        sp.set_type(params, sp.TRecord(address = sp.TAddress, value = sp.TNat))
        sp.verify(sp.sender == self.data.administrator)
        sp.verify(self.data.balances[params.address].balance >= params.value)
        self.data.balances[params.address].balance = sp.as_nat(self.data.balances[params.address].balance - params.value)
        self.data.totalSupply = sp.as_nat(self.data.totalSupply - params.value)

    def addAddressIfNecessary(self, address):
        sp.if ~ self.data.balances.contains(address):
            self.data.balances[address] = sp.record(balance = 0, approvals = {})

    @sp.entry_point
    def getBalance(self, params):
        sp.transfer(self.data.balances[params.arg.owner].balance, sp.tez(0), sp.contract(sp.TNat, params.target).open_some())

    @sp.entry_point
    def getAllowance(self, params):
        sp.transfer(self.data.balances[params.arg.owner].approvals[params.arg.spender], sp.tez(0), sp.contract(sp.TNat, params.target).open_some())

    @sp.entry_point
    def getTotalSupply(self, params):
        sp.transfer(self.data.totalSupply, sp.tez(0), sp.contract(sp.TNat, params.target).open_some())

    @sp.entry_point
    def getAdministrator(self, params):
        sp.transfer(self.data.administrator, sp.tez(0), sp.contract(sp.TAddress, params.target).open_some())

    @sp.entry_point
    def getCounter(self, params):
        sp.transfer(self.data.counter, sp.tez(0), sp.contract(sp.TNat, params.target).open_some())

    @sp.entry_point
    def getDefaultExpiry(self, params):
        sp.transfer(self.data.default_expiry, sp.tez(0), sp.contract(sp.TNat, params.target).open_some())

class Viewer(sp.Contract):
    def __init__(self, t):
        self.init(last = sp.none)
        self.init_type(sp.TRecord(last = sp.TOption(t)))
    @sp.entry_point
    def target(self, params):
        self.data.last = sp.some(params)

if "templates" not in __name__:
    @sp.add_test(name = "FA12")
    def test():

        scenario = sp.test_scenario()
        scenario.h1("FA1.2 template - Fungible assets")

        scenario.table_of_contents()

        # sp.test_account generates ED25519 key-pairs deterministically:
        admin = sp.test_account("Administrator")
        alice = sp.test_account("Alice")
        bob   = sp.test_account("Robert")
        carlos = sp.test_account("Carlos")

        # Let's display the accounts:
        scenario.h1("Accounts")
        scenario.show([admin, alice, bob, carlos])

        scenario.h1("Contract")
        c1 = FA12(admin.address)

        scenario.h1("Entry points")
        scenario += c1
        scenario.h2("Admin mints a few coins")
        scenario += c1.mint(address = alice.address, value = 12).run(sender = admin)
        scenario += c1.mint(address = alice.address, value = 3).run(sender = admin)
        scenario += c1.mint(address = alice.address, value = 3).run(sender = admin)
        scenario.verify(c1.data.balances[alice.address].balance == 18)
        scenario.h2("Alice transfers to Bob")
        scenario += c1.transfer(from_ = alice.address, to_ = bob.address, value = 4).run(sender = alice)
        scenario.verify(c1.data.balances[alice.address].balance == 14)
        scenario.h2("Bob tries to transfer from Alice but he doesn't have her approval")
        scenario += c1.transfer(from_ = alice.address, to_ = bob.address, value = 4).run(sender = bob, valid = False)
        scenario.h2("Alice approves Bob and Bob transfers")
        scenario += c1.approve(spender = bob.address, value = 5).run(sender = alice)
        scenario += c1.transfer(from_ = alice.address, to_ = bob.address, value = 4).run(sender = bob)
        scenario.h2("Bob tries to over-transfer from Alice")
        scenario += c1.transfer(from_ = alice.address, to_ = bob.address, value = 4).run(sender = bob, valid = False)
        scenario.h2("Admin burns Bob token")
        scenario += c1.burn(address = bob.address, value = 1).run(sender = admin)
        scenario.verify(c1.data.balances[alice.address].balance == 10)
        scenario.h2("Alice tries to burn Bob token")
        scenario += c1.burn(address = bob.address, value = 1).run(sender = alice, valid = False)
        scenario.h2("Admin pauses the contract and Alice cannot transfer anymore")
        scenario += c1.setPause(True).run(sender = admin)
        scenario += c1.transfer(from_ = alice.address, to_ = bob.address, value = 4).run(sender = alice, valid = False)
        scenario.verify(c1.data.balances[alice.address].balance == 10)
        scenario.h2("Admin transfers while on pause")
        scenario += c1.transfer(from_ = alice.address, to_ = bob.address, value = 1).run(sender = admin)
        scenario.h2("Admin unpauses the contract and transfers are allowed")
        scenario += c1.setPause(False).run(sender = admin)
        scenario.verify(c1.data.balances[alice.address].balance == 9)
        scenario += c1.transfer(from_ = alice.address, to_ = bob.address, value = 1).run(sender = alice)

        scenario.verify(c1.data.totalSupply == 17)
        scenario.verify(c1.data.balances[alice.address].balance == 8)
        scenario.verify(c1.data.balances[bob.address].balance == 9)

        scenario.h2("Permit Submission")
        scenario += c1.mint(address = carlos.address, value = 10).run(sender = admin)
        scenario.verify(c1.data.balances[carlos.address].balance == 10)
        #add permit for transfer of 10 from carlos to bob. alice submits with correct info and also calls.
        params_bytes = sp.pack(sp.pair(carlos.address, sp.pair(bob.address, 10)))
        params_hash = sp.blake2b(params_bytes)
        #TODO: Replace c1.data.counter here with get_counter method
        unsigned = sp.pack(sp.pair(sp.pair(sp.chain_id_cst("0x9caecab9"), c1.address), sp.pair(c1.data.counter, params_hash)))
        signature = sp.make_signature(secret_key = carlos.secret_key, message = unsigned, message_format = "Raw")
        scenario += c1.permit([sp.pair(carlos.public_key, sp.pair(signature, params_hash))]).run(sender = alice, now = sp.timestamp(1571761674), chain_id = sp.chain_id_cst("0x9caecab9"))
        scenario.verify(c1.data.counter == 1)
        scenario.verify_equal(c1.data.permits[(sp.pair(carlos.address, params_hash))], sp.timestamp(1571761674))

        scenario.h2("Execute transfer using permit")
        scenario += c1.transfer(from_ = carlos.address, to_ = bob.address, value = 10).run(sender = bob, now = sp.timestamp(1571761674))
        scenario.verify(c1.data.balances[carlos.address].balance == 0)
        scenario.verify(c1.data.balances[bob.address].balance == 19)
        #Permit deleted
        scenario.verify(~ c1.data.permits.contains(sp.pair(carlos.address, unsigned)))

        scenario.h1("Views")
        scenario.h2("Balance")
        view_balance = Viewer(sp.TNat)
        scenario += view_balance
        scenario += c1.getBalance(arg = sp.record(owner = alice.address), target = view_balance.address)
        scenario.verify_equal(view_balance.data.last, sp.some(8))

        scenario.h2("Administrator")
        view_administrator = Viewer(sp.TAddress)
        scenario += view_administrator
        scenario += c1.getAdministrator(target = view_administrator.address)
        scenario.verify_equal(view_administrator.data.last, sp.some(admin.address))

        scenario.h2("Total Supply")
        view_totalSupply = Viewer(sp.TNat)
        scenario += view_totalSupply
        scenario += c1.getTotalSupply(target = view_totalSupply.address)
        scenario.verify_equal(view_totalSupply.data.last, sp.some(27))

        scenario.h2("Allowance")
        view_allowance = Viewer(sp.TNat)
        scenario += view_allowance
        scenario += c1.getAllowance(arg = sp.record(owner = alice.address, spender = bob.address), target = view_allowance.address)
        scenario.verify_equal(view_allowance.data.last, sp.some(1))

        scenario.h2("Counter")
        view_counter = Viewer(sp.TNat)
        scenario += view_counter
        scenario += c1.getCounter(target = view_counter.address)
        scenario.verify_equal(view_counter.data.last, sp.some(1))

        scenario.h2("Default Expiry")
        view_defaultExpiry = Viewer(sp.TNat)
        scenario += view_defaultExpiry
        scenario += c1.getDefaultExpiry(target = view_defaultExpiry.address)
        scenario.verify_equal(view_defaultExpiry.data.last, sp.some(360))
