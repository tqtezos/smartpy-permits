import smartpy as sp
import smartpy_michelson as mi

class FA12(sp.Contract):
    def __init__(self, admin):
        self.init(paused = False, balances = sp.big_map(tvalue = sp.TRecord(approvals = sp.TMap(sp.TAddress, sp.TNat), balance = sp.TNat)), administrator = admin, totalSupply = 0,
        permits = sp.big_map(tkey = sp.TPair(sp.TAddress, sp.TBytes), tvalue = sp.TTimestamp), user_expiries = sp.big_map(tkey = sp.TAddress, tvalue = sp.TOption(sp.TNat)),
        permit_expiries = sp.big_map(tkey = sp.TPair(sp.TAddress, sp.TBytes), tvalue = sp.TOption(sp.TNat)), counter = 0, default_expiry = 360)

    @sp.sub_entry_point
    def transfer_helper(self, params):
        sp.verify((params.sender_ == self.data.administrator) |
            (~self.data.paused &
                ((params.from_ == params.sender_) |
                 (self.data.balances[params.from_].approvals[params.sender_] >= params.value))))
        self.addAddressIfNecessary(params.to_)
        sp.verify(self.data.balances[params.from_].balance >= params.value)
        self.data.balances[params.from_].balance = sp.as_nat(self.data.balances[params.from_].balance - params.value)
        self.data.balances[params.to_].balance += params.value
        sp.if ((params.from_ != params.sender_) & (self.data.administrator != params.sender_)):
            self.data.balances[params.from_].approvals[params.sender_] = sp.as_nat(self.data.balances[params.from_].approvals[params.sender_] - params.value)

    @sp.entry_point
    def transfer(self, params):
        sp.set_type(params, sp.TRecord(from_ = sp.TAddress, to_ = sp.TAddress, value = sp.TNat)).layout(("from_ as from", ("to_ as to", "value")))
        new_params = sp.record(from_ = params.from_, to_ = params.to_, value = params.value, sender_ = sp.sender)
        self.transfer_helper(new_params)

    @sp.entry_point
    def transfer_signed(self, params):
        sp.set_type(params, sp.TRecord(from_ = sp.TAddress, to_ = sp.TAddress, value = sp.TNat, pk = sp.TKey, signed = sp.TSignature))
        sender = sp.local("sender", sp.sender)
        sp.if (params.from_ != sender.value):
            params_bytes = sp.concat([sp.pack(params.from_), sp.pack(params.to_), sp.pack(params.value)])
            params_hash = sp.blake2b(params_bytes)
            unsigned = sp.blake2b(mi.operator("SELF; ADDRESS; CHAIN_ID; PAIR; PAIR; PACK", [sp.TPair(sp.TNat, sp.TBytes)], [sp.TBytes])(sp.pair(self.data.counter, params_hash)))
            pk_address = sp.to_address(sp.implicit_account(sp.hash_key(params.pk)))
            sp.verify(self.data.permits.contains(sp.pair(pk_address, unsigned)),
                      message = sp.pair("NO_PERMIT", sp.pair(pk_address, unsigned)))
            #Setting sender.value to pk_address so call to transfer_helper will be authorized
            sender.value = pk_address
        self.transfer_helper(sp.record(from_ = params.from_, to_ = params.to_, value = params.value, sender_ = sender.value))

    @sp.entry_point
    def add_permits(self, params):
        sp.set_type(params, sp.TList(sp.TPair(sp.TKey, sp.TPair(sp.TSignature, sp.TBytes))))
        #Local variable initialization (values here don't matter)
        pk_address = sp.local('pk_address', sp.self_address)
        sp.for permit in params:
          pk_address.value = sp.to_address(sp.implicit_account(sp.hash_key(sp.fst(permit))))
          sp.if self.data.permits.contains(sp.pair(pk_address.value, sp.snd(sp.snd(permit)))):
            sp.failwith("DUP_PERMIT")
          sp.if sp.check_signature(sp.fst(permit), sp.fst(sp.snd(permit)), sp.snd(sp.snd(permit))):
            self.data.permits[sp.pair(pk_address.value, sp.snd(sp.snd(permit)))] = sp.now
            self.data.counter = self.data.counter + 1
          sp.else:
            sp.failwith(sp.pair("MISSIGNED", sp.snd(sp.snd(permit))))

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

        # Let's display the accounts:
        scenario.h1("Accounts")
        scenario.show([admin, alice, bob])

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
        scenario.h2("Admin unpauses the contract and transferts are allowed")
        scenario += c1.setPause(False).run(sender = admin)
        scenario.verify(c1.data.balances[alice.address].balance == 9)
        scenario += c1.transfer(from_ = alice.address, to_ = bob.address, value = 1).run(sender = alice)

        scenario.verify(c1.data.totalSupply == 17)
        scenario.verify(c1.data.balances[alice.address].balance == 8)
        scenario.verify(c1.data.balances[bob.address].balance == 9)

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
        scenario.verify_equal(view_totalSupply.data.last, sp.some(17))

        scenario.h2("Allowance")
        view_allowance = Viewer(sp.TNat)
        scenario += view_allowance
        scenario += c1.getAllowance(arg = sp.record(owner = alice.address, spender = bob.address), target = view_allowance.address)
        scenario.verify_equal(view_allowance.data.last, sp.some(1))
