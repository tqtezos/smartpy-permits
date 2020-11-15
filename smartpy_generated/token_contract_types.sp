Storage: sp.TRecord(administrator = sp.TAddress, balances = sp.TBigMap(sp.TAddress, sp.TRecord(approvals = sp.TMap(sp.TAddress, sp.TNat), balance = sp.TNat).layout(("approvals", "balance"))), counter = sp.TIntOrNat, default_expiry = sp.TIntOrNat, paused = sp.TBool, permit_expiries = sp.TBigMap(sp.TPair(sp.TAddress, sp.TBytes), sp.TOption(sp.TNat)), permits = sp.TBigMap(sp.TPair(sp.TAddress, sp.TBytes), sp.TTimestamp), totalSupply = sp.TNat, user_expiries = sp.TBigMap(sp.TAddress, sp.TOption(sp.TNat))).layout(((("administrator", "balances"), ("counter", "default_expiry")), (("paused", "permit_expiries"), ("permits", ("totalSupply", "user_expiries")))))
Params: sp.TVariant(add_permits = sp.TList(sp.TPair(sp.TKey, sp.TPair(sp.TSignature, sp.TBytes))), approve = sp.TRecord(spender = sp.TAddress, value = sp.TNat).layout(("spender", "value")), burn = sp.TRecord(address = sp.TAddress, value = sp.TNat).layout(("address", "value")), getAdministrator = sp.TRecord(target = sp.TAddress).layout("target"), getAllowance = sp.TRecord(arg = sp.TRecord(owner = sp.TAddress, spender = sp.TAddress).layout(("owner", "spender")), target = sp.TAddress).layout(("arg", "target")), getBalance = sp.TRecord(arg = sp.TRecord(owner = sp.TAddress).layout("owner"), target = sp.TAddress).layout(("arg", "target")), getTotalSupply = sp.TRecord(target = sp.TAddress).layout("target"), mint = sp.TRecord(address = sp.TAddress, value = sp.TNat).layout(("address", "value")), setAdministrator = sp.TAddress, setPause = sp.TBool, transfer = sp.TRecord(from_ = sp.TAddress, to_ = sp.TAddress, value = sp.TNat).layout(("from_", ("to_", "value"))), transfer_signed = sp.TRecord(counter = sp.TNat, from_ = sp.TAddress, to_ = sp.TAddress, value = sp.TNat).layout((("counter", "from_"), ("to_", "value")))).layout(((("add_permits", ("approve", "burn")), ("getAdministrator", ("getAllowance", "getBalance"))), (("getTotalSupply", ("mint", "setAdministrator")), ("setPause", ("transfer", "transfer_signed")))))