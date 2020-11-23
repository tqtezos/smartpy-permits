Read about TZIP here https://gitlab.com/tzip/tzip/-/blob/master/proposals/tzip-17/tzip-17.md

This is an implementation of Permits on top of a generic smartpy fa1.2 contract: https://smartpy.io/ide?template=FA1.2.py&source=post_page---------------------------

## Setting Up
### Requirements
#### Tezos-client and Sandboxed mode
To set up the tezos-client and sandboxed mode follow the instructions in https://tezos.gitlab.io/

#### Get Smartpy
https://smartpy.io/cli/

#### (Optionally) Edit and ReCompile and Smartpy code
```
$ ./test_permit.sh
```

## Use

### Initialize bootstrap addresses
```
$ bootstrap1_address="tz1KqTpEZ7Yob7QbPE4Hy4Wo8fHG8LhKxZSx"
$ bootstrap2_address="tz1gjaF81ZRRvdzjobyfVNsAeSC6PScjfQwN"
$ bootstrap3_address="tz1faswCTDciRzE4oJ9jn2Vm2dvjeyA9fUzU"
```
### Hash transfer entrypoint parameter (bootstrap2 transfers 5 to bootstrap3)

```
$ transfer_param="Pair \"$bootstrap2_address\" (Pair \"$bootstrap3_address\" 5)"
$ type="pair address (pair address nat)"
$ tezos-client hash data "$transfer_param" of type "$type"

Warning:

   The node you are connecting to claims to be running in a
                    Tezos TEST SANDBOX.
      Do NOT use your fundraiser keys on this network.
  You should not see this message if you are not a developer.

Raw packed data: 0x0507070a000000160000e7670f32038107a59a2b9cfefae36ea21f5aa63c07070a000000160000dac9f52543da1aed0bc1d6b46bf7c10db7014cd60005
Script-expression-ID-Hash: exprvGb45XzKDNKAhQAuP6viCyv1rWtKNp4rBZ6wLNKz73XNg44TiH
Raw Script-expression-ID-Hash: 0xe6f1aa42d877954d34bbde9ca5bdd2676b139adb52ebc7b943fe8a07f55591e9
Ledger Blake2b hash: GYWW23KERy8iXhQ8bKQyh4cYuipgE2D6r7WBnc3UuaNt
Raw Sha256 hash: 0x767153a2c57beb0f22dd5bbec04ab81f5b894b4afcb76b6319965c07f5ca9586
Raw Sha512 hash: 0x2d551b4be7217ac498aa4d3cab2d1aac403af76553fc5dbb781f9631409fbcad97e9ccdd495fdda03e0e20480f2bfefe39a7191ce2579f40f9f5f7f503cbeffd
Gas remaining: 1039764 units remaining

$TRANSFER_PARAM_PACKED=0x0507070a000000160000e7670f32038107a59a2b9cfefae36ea21f5aa63c07070a000000160000dac9f52543da1aed0bc1d6b46bf7c10db7014cd60005

```
### Change administrator to bootstrap1 in smartpy_generated/token_contract_storage_init.tz

Add bootstrap1's address to administrator address parameter in smartpy_generated/token_contract_storage_init.tz


### Originate permit-fa1.2 contract

```
$ tezos-client originate contract fa1.2-permits transferring 0 from bootstrap1 running "./smartpy_generated/token_contract_compiled.tz" --burn-cap 500000 --init "$(< smartpy_generated/token_contract_storage_init.tz)"
Warning:

   The node you are connecting to claims to be running in a
                    Tezos TEST SANDBOX.
      Do NOT use your fundraiser keys on this network.
  You should not see this message if you are not a developer.

Node is bootstrapped, ready for injecting operations.
Estimated gas: 420217 units (will add 100 for safety)
Estimated storage: 14040 bytes added (will add 20 for safety)
Operation successfully injected in the node.
Operation hash is 'opFYQzzkgctT7Ph2uERbsP3qqQpgm6MNxvBHmJ7NwNnn7cFzPi8'
Waiting for the operation to be included...
Operation found in block: BMPHZyGAGFgwqPYc3eA5pYrAXUCmw6iA1kPnKDDw1XF4Z9S7RLx (pass: 3, offset: 0)
This sequence of operations was run:
  Manager signed operations:
    From: tz1KqTpEZ7Yob7QbPE4Hy4Wo8fHG8LhKxZSx
    Fee to the baker: ꜩ0.055799
    Expected counter: 1
    Gas limit: 420317
    Storage limit: 14060 bytes
    Balance updates:
      tz1KqTpEZ7Yob7QbPE4Hy4Wo8fHG8LhKxZSx ........... -ꜩ0.055799
      fees(tz1b7tUupMgCNw2cCLpKTkSD1NZzB5TkP2sv,0) ... +ꜩ0.055799
    Origination:
      From: tz1KqTpEZ7Yob7QbPE4Hy4Wo8fHG8LhKxZSx
      Credit: ꜩ0
      Script:
        { parameter
            (or (or (or (pair %approve (address %spender) (nat %value))
                        (or (pair %burn (address %address) (nat %value))
                            (list %delete_permits (pair address bytes))))
                    (or (or (address %getAdministrator)
                            (pair %getAllowance
                               (pair %arg (address %owner) (address %spender))
                               (address %target)))
                        (or (pair %getBalance (address %arg) (address %target)) (address %getCounter))))
                (or (or (or (address %getDefaultExpiry) (address %getTotalSupply))
                        (or (pair %mint (address %address) (nat %value))
                            (list %permit (pair key (pair signature bytes)))))
                    (or (or (address %setAdministrator)
                            (pair %setExpiry (address %address) (pair (option %permit bytes) (nat %seconds))))
                        (or (bool %setPause)
                            (pair %transfer (address %from_) (pair (address %to_) (nat %value))))))) ;
          storage
            (pair (pair (pair (address %administrator)
                              (big_map %balances address (pair (map %approvals address nat) (nat %balance))))
                        (pair (nat %counter) (pair (nat %default_expiry) (nat %max_expiry))))
                  (pair (pair (big_map %metadata string bytes)
                              (pair (bool %paused) (big_map %permit_expiries (pair address bytes) (option nat))))
                        (pair (big_map %permits (pair address bytes) timestamp)
                              (pair (nat %totalSupply) (big_map %user_expiries address (option nat)))))) ;
          code { LAMBDA
                   (pair (pair %in_param address bytes)
                         (pair %in_storage
                            (pair (pair (address %administrator)
                                        (big_map %balances address (pair (map %approvals address nat) (nat %balance))))
                                  (pair (nat %counter) (pair (nat %default_expiry) (nat %max_expiry))))
                            (pair (pair (big_map %metadata string bytes)
                                        (pair (bool %paused) (big_map %permit_expiries (pair address bytes) (option nat))))
                                  (pair (big_map %permits (pair address bytes) timestamp)
                                        (pair (nat %totalSupply) (big_map %user_expiries address (option nat)))))))
                   (pair (list %operations operation)
                         (pair (nat %result)
                               (pair %storage
                                  (pair (pair (address %administrator)
                                              (big_map %balances address (pair (map %approvals address nat) (nat %balance))))
                                        (pair (nat %counter) (pair (nat %default_expiry) (nat %max_expiry))))
                                  (pair (pair (big_map %metadata string bytes)
                                              (pair (bool %paused) (big_map %permit_expiries (pair address bytes) (option nat))))
                                        (pair (big_map %permits (pair address bytes) timestamp)
                                              (pair (nat %totalSupply) (big_map %user_expiries address (option nat))))))))
                   { NIL operation ;
                     SWAP ;
                     DUP ;
                     DUG 2 ;
                     CDR ;
                     DUP ;
                     CDADDR ;
                     DIG 3 ;
                     DUP ;
                     DUG 4 ;
                     CAR ;
                     MEM ;
                     IF { DUP ;
                          CDADDR ;
                          DIG 3 ;
                          DUP ;
                          DUG 4 ;
                          CAR ;
                          GET ;
                          IF_SOME {} { PUSH int 114 ; FAILWITH } ;
                          IF_SOME { DROP ; PUSH bool True } { PUSH bool False } }
                        { PUSH bool False } ;
                     IF { DUP ;
                          CDADDR ;
                          DIG 3 ;
                          CAR ;
                          GET ;
                          IF_SOME {} { PUSH int 115 ; FAILWITH } ;
                          IF_SOME {} { PUSH int 115 ; FAILWITH } }
                        { DUP ;
                          CDDDDR ;
                          DIG 3 ;
                          DUP ;
                          DUG 4 ;
                          CAAR ;
                          MEM ;
                          IF { DUP ;
                               CDDDDR ;
                               DIG 3 ;
                               DUP ;
                               DUG 4 ;
                               CAAR ;
                               GET ;
                               IF_SOME {} { PUSH int 118 ; FAILWITH } ;
                               IF_SOME { DROP ; PUSH bool True } { PUSH bool False } }
                             { PUSH bool False } ;
                          IF { DUP ;
                               CDDDDR ;
                               DIG 3 ;
                               CAAR ;
                               GET ;
                               IF_SOME {} { PUSH int 119 ; FAILWITH } ;
                               IF_SOME {} { PUSH int 119 ; FAILWITH } }
                             { DIG 2 ; DROP ; DUP ; CADDAR } } ;
                     PAIR %result %storage ;
                     SWAP ;
                     PAIR %operations } ;
                 SWAP ;
                 LAMBDA
                   (pair (pair %in_param (address %from_) (pair (address %to_) (nat %value)))
                         (pair %in_storage
                            (pair (pair (address %administrator)
                                        (big_map %balances address (pair (map %approvals address nat) (nat %balance))))
                                  (pair (nat %counter) (pair (nat %default_expiry) (nat %max_expiry))))
                            (pair (pair (big_map %metadata string bytes)
                                        (pair (bool %paused) (big_map %permit_expiries (pair address bytes) (option nat))))
                                  (pair (big_map %permits (pair address bytes) timestamp)
                                        (pair (nat %totalSupply) (big_map %user_expiries address (option nat)))))))
                   (pair (list %operations operation)
                         (pair (bool %result)
                               (pair %storage
                                  (pair (pair (address %administrator)
                                              (big_map %balances address (pair (map %approvals address nat) (nat %balance))))
                                        (pair (nat %counter) (pair (nat %default_expiry) (nat %max_expiry))))
                                  (pair (pair (big_map %metadata string bytes)
                                              (pair (bool %paused) (big_map %permit_expiries (pair address bytes) (option nat))))
                                        (pair (big_map %permits (pair address bytes) timestamp)
                                              (pair (nat %totalSupply) (big_map %user_expiries address (option nat))))))))
                   { NIL operation ;
                     SWAP ;
                     DUP ;
                     DUG 2 ;
                     CDR ;
                     DUP ;
                     CDDAR ;
                     DIG 3 ;
                     DUP ;
                     DUG 4 ;
                     CAR ;
                     PACK ;
                     BLAKE2B ;
                     DIG 4 ;
                     DUP ;
                     DUG 5 ;
                     CAAR ;
                     PAIR ;
                     MEM ;
                     IF { DUP ;
                          CDADDR ;
                          DIG 3 ;
                          DUP ;
                          DUG 4 ;
                          CAR ;
                          PACK ;
                          BLAKE2B ;
                          DIG 4 ;
                          DUP ;
                          DUG 5 ;
                          CAAR ;
                          PAIR ;
                          MEM ;
                          IF { DUP ;
                               CDADDR ;
                               DIG 3 ;
                               DUP ;
                               DUG 4 ;
                               CAR ;
                               PACK ;
                               BLAKE2B ;
                               DIG 4 ;
                               DUP ;
                               DUG 5 ;
                               CAAR ;
                               PAIR ;
                               GET ;
                               IF_SOME {} { PUSH int 67 ; FAILWITH } ;
                               IF_SOME { DROP ; PUSH bool True } { PUSH bool False } }
                             { PUSH bool False } ;
                          IF { DUP ;
                               CDADDR ;
                               DIG 3 ;
                               DUP ;
                               DUG 4 ;
                               CAR ;
                               PACK ;
                               BLAKE2B ;
                               DIG 4 ;
                               DUP ;
                               DUG 5 ;
                               CAAR ;
                               PAIR ;
                               GET ;
                               IF_SOME {} { PUSH int 68 ; FAILWITH } ;
                               IF_SOME {} { PUSH int 68 ; FAILWITH } }
                             { DUP ;
                               CDDDDR ;
                               DIG 3 ;
                               DUP ;
                               DUG 4 ;
                               CAAR ;
                               MEM ;
                               IF { DUP ;
                                    CDDDDR ;
                                    DIG 3 ;
                                    DUP ;
                                    DUG 4 ;
                                    CAAR ;
                                    GET ;
                                    IF_SOME {} { PUSH int 70 ; FAILWITH } ;
                                    IF_SOME { DROP ; PUSH bool True } { PUSH bool False } }
                                  { PUSH bool False } ;
                               IF { DUP ;
                                    CDDDDR ;
                                    DIG 3 ;
                                    DUP ;
                                    DUG 4 ;
                                    CAAR ;
                                    GET ;
                                    IF_SOME {} { PUSH int 71 ; FAILWITH } ;
                                    IF_SOME {} { PUSH int 71 ; FAILWITH } }
                                  { DUP ; CADDAR } } ;
                          SWAP ;
                          DUP ;
                          DUG 2 ;
                          CDDAR ;
                          DIG 4 ;
                          DUP ;
                          DUG 5 ;
                          CAR ;
                          PACK ;
                          BLAKE2B ;
                          DIG 5 ;
                          DUP ;
                          DUG 6 ;
                          CAAR ;
                          PAIR ;
                          GET ;
                          IF_SOME {} { PUSH int 66 ; FAILWITH } ;
                          NOW ;
                          SUB ;
                          ISNAT ;
                          IF_SOME {} { PUSH int 76 ; FAILWITH } ;
                          COMPARE ;
                          GE ;
                          IF { DUP ;
                               CDDAR ;
                               DIG 3 ;
                               DUP ;
                               DUG 4 ;
                               CAR ;
                               PACK ;
                               BLAKE2B ;
                               DIG 4 ;
                               DUP ;
                               DUG 5 ;
                               CAAR ;
                               PAIR ;
                               MEM ;
                               IF { DUP ;
                                    CAR ;
                                    SWAP ;
                                    CDR ;
                                    DUP ;
                                    CAR ;
                                    SWAP ;
                                    CDR ;
                                    DUP ;
                                    CDR ;
                                    SWAP ;
                                    CAR ;
                                    NONE timestamp ;
                                    DIG 6 ;
                                    DUP ;
                                    DUG 7 ;
                                    CAR ;
                                    PACK ;
                                    BLAKE2B ;
                                    DIG 7 ;
                                    DUP ;
                                    DUG 8 ;
                                    CAAR ;
                                    PAIR ;
                                    UPDATE ;
                                    PAIR ;
                                    SWAP ;
                                    PAIR ;
                                    SWAP ;
                                    PAIR }
                                  {} ;
                               DUP ;
                               CDADDR ;
                               DIG 3 ;
                               DUP ;
                               DUG 4 ;
                               CAR ;
                               PACK ;
                               BLAKE2B ;
                               DIG 4 ;
                               DUP ;
                               DUG 5 ;
                               CAAR ;
                               PAIR ;
                               MEM ;
                               IF { DUP ;
                                    CAR ;
                                    SWAP ;
                                    CDR ;
                                    DUP ;
                                    CDR ;
                                    SWAP ;
                                    CAR ;
                                    DUP ;
                                    CAR ;
                                    SWAP ;
                                    CDR ;
                                    DUP ;
                                    CAR ;
                                    SWAP ;
                                    CDR ;
                                    NONE (option nat) ;
                                    DIG 7 ;
                                    DUP ;
                                    DUG 8 ;
                                    CAR ;
                                    PACK ;
                                    BLAKE2B ;
                                    DIG 8 ;
                                    CAAR ;
                                    PAIR ;
                                    UPDATE ;
                                    SWAP ;
                                    PAIR ;
                                    SWAP ;
                                    PAIR ;
                                    PAIR ;
                                    SWAP ;
                                    PAIR }
                                  { DIG 2 ; DROP } ;
                               PUSH bool False }
                             { DUP ;
                               CDDAR ;
                               DIG 3 ;
                               DUP ;
                               DUG 4 ;
                               CAR ;
                               PACK ;
                               BLAKE2B ;
                               DIG 4 ;
                               DUP ;
                               DUG 5 ;
                               CAAR ;
                               PAIR ;
                               MEM ;
                               IF { DUP ;
                                    CAR ;
                                    SWAP ;
                                    CDR ;
                                    DUP ;
                                    CAR ;
                                    SWAP ;
                                    CDR ;
                                    DUP ;
                                    CDR ;
                                    SWAP ;
                                    CAR ;
                                    NONE timestamp ;
                                    DIG 6 ;
                                    DUP ;
                                    DUG 7 ;
                                    CAR ;
                                    PACK ;
                                    BLAKE2B ;
                                    DIG 7 ;
                                    DUP ;
                                    DUG 8 ;
                                    CAAR ;
                                    PAIR ;
                                    UPDATE ;
                                    PAIR ;
                                    SWAP ;
                                    PAIR ;
                                    SWAP ;
                                    PAIR }
                                  {} ;
                               DUP ;
                               CDADDR ;
                               DIG 3 ;
                               DUP ;
                               DUG 4 ;
                               CAR ;
                               PACK ;
                               BLAKE2B ;
                               DIG 4 ;
                               DUP ;
                               DUG 5 ;
                               CAAR ;
                               PAIR ;
                               MEM ;
                               IF { DUP ;
                                    CAR ;
                                    SWAP ;
                                    CDR ;
                                    DUP ;
                                    CDR ;
                                    SWAP ;
                                    CAR ;
                                    DUP ;
                                    CAR ;
                                    SWAP ;
                                    CDR ;
                                    DUP ;
                                    CAR ;
                                    SWAP ;
                                    CDR ;
                                    NONE (option nat) ;
                                    DIG 7 ;
                                    DUP ;
                                    DUG 8 ;
                                    CAR ;
                                    PACK ;
                                    BLAKE2B ;
                                    DIG 8 ;
                                    CAAR ;
                                    PAIR ;
                                    UPDATE ;
                                    SWAP ;
                                    PAIR ;
                                    SWAP ;
                                    PAIR ;
                                    PAIR ;
                                    SWAP ;
                                    PAIR }
                                  { DIG 2 ; DROP } ;
                               PUSH bool True } }
                        { DIG 2 ; DROP ; PUSH bool False } ;
                     PAIR %result %storage ;
                     SWAP ;
                     PAIR %operations } ;
                 SWAP ;
                 DUP ;
                 CDR ;
                 SWAP ;
                 CAR ;
                 IF_LEFT
                   { IF_LEFT
                       { IF_LEFT
                           { SWAP ;
                             DUP ;
                             DUG 2 ;
                             CDADAR ;
                             IF { PUSH string "WrongCondition: ~ self.data.paused" ; FAILWITH } {} ;
                             PUSH nat 0 ;
                             DIG 2 ;
                             DUP ;
                             DUG 3 ;
                             CAADR ;
                             SENDER ;
                             GET ;
                             IF_SOME {} { PUSH int 162 ; FAILWITH } ;
                             CAR ;
                             DIG 2 ;
                             DUP ;
                             DUG 3 ;
                             CAR ;
                             GET ;
                             IF_SOME {} { PUSH nat 0 } ;
                             COMPARE ;
                             EQ ;
                             IF { PUSH bool True } { DUP ; CDR ; PUSH nat 0 ; COMPARE ; EQ } ;
                             IF { DIG 2 ; DROP ; DIG 2 ; DROP }
                                { PUSH string "UnsafeAllowanceChange" ; FAILWITH } ;
                             SWAP ;
                             DUP ;
                             CDR ;
                             SWAP ;
                             CAR ;
                             DUP ;
                             CDR ;
                             SWAP ;
                             CAR ;
                             DUP ;
                             CAR ;
                             SWAP ;
                             CDR ;
                             DUP ;
                             SENDER ;
                             DUP ;
                             DUG 2 ;
                             GET ;
                             IF_SOME {} { PUSH int 166 ; FAILWITH } ;
                             DUP ;
                             CDR ;
                             SWAP ;
                             CAR ;
                             DIG 7 ;
                             DUP ;
                             CAR ;
                             SWAP ;
                             CDR ;
                             SOME ;
                             SWAP ;
                             UPDATE ;
                             PAIR ;
                             SOME ;
                             SWAP ;
                             UPDATE ;
                             SWAP ;
                             PAIR ;
                             PAIR ;
                             PAIR ;
                             NIL operation }
                           { IF_LEFT
                               { SWAP ;
                                 DUP ;
                                 DUG 2 ;
                                 CAAAR ;
                                 SENDER ;
                                 COMPARE ;
                                 EQ ;
                                 IF {}
                                    { PUSH string "WrongCondition: sp.sender == self.data.administrator" ;
                                      FAILWITH } ;
                                 DUP ;
                                 CDR ;
                                 DIG 2 ;
                                 DUP ;
                                 DUG 3 ;
                                 CAADR ;
                                 DIG 2 ;
                                 DUP ;
                                 DUG 3 ;
                                 CAR ;
                                 GET ;
                                 IF_SOME {} { PUSH int 192 ; FAILWITH } ;
                                 CDR ;
                                 COMPARE ;
                                 GE ;
                                 IF { DIG 2 ; DROP ; DIG 2 ; DROP }
                                    { PUSH string
                                           "WrongCondition: self.data.balances[params.address].balance >= params.value" ;
                                      FAILWITH } ;
                                 SWAP ;
                                 DUP ;
                                 DUG 2 ;
                                 DUP ;
                                 CDR ;
                                 SWAP ;
                                 CAR ;
                                 DUP ;
                                 CDR ;
                                 SWAP ;
                                 CAR ;
                                 DUP ;
                                 CAR ;
                                 SWAP ;
                                 CDR ;
                                 DUP ;
                                 DIG 5 ;
                                 DUP ;
                                 DUG 6 ;
                                 CAR ;
                                 DUP ;
                                 DUG 2 ;
                                 GET ;
                                 IF_SOME {} { PUSH int 193 ; FAILWITH } ;
                                 CAR ;
                                 DIG 6 ;
                                 DUP ;
                                 DUG 7 ;
                                 CDR ;
                                 DIG 8 ;
                                 CAADR ;
                                 DIG 8 ;
                                 DUP ;
                                 DUG 9 ;
                                 CAR ;
                                 GET ;
                                 IF_SOME {} { PUSH int 194 ; FAILWITH } ;
                                 CDR ;
                                 SUB ;
                                 ISNAT ;
                                 IF_SOME {} { PUSH int 193 ; FAILWITH } ;
                                 SWAP ;
                                 PAIR ;
                                 SOME ;
                                 SWAP ;
                                 UPDATE ;
                                 SWAP ;
                                 PAIR ;
                                 PAIR ;
                                 PAIR ;
                                 DUP ;
                                 DUG 2 ;
                                 DUP ;
                                 CAR ;
                                 SWAP ;
                                 CDR ;
                                 DUP ;
                                 CAR ;
                                 SWAP ;
                                 CDR ;
                                 DUP ;
                                 CAR ;
                                 SWAP ;
                                 CDDR ;
                                 DIG 4 ;
                                 CDR ;
                                 DIG 5 ;
                                 CDDDAR ;
                                 SUB ;
                                 ISNAT ;
                                 IF_SOME {} { PUSH int 195 ; FAILWITH } ;
                                 PAIR ;
                                 SWAP ;
                                 PAIR ;
                                 SWAP ;
                                 PAIR ;
                                 SWAP ;
                                 PAIR ;
                                 NIL operation }
                               { PUSH int 0 ;
                                 NIL operation ;
                                 DIG 2 ;
                                 DUP ;
                                 DUG 3 ;
                                 ITER { DIG 4 ;
                                        DUP ;
                                        DUG 5 ;
                                        CDDAR ;
                                        SWAP ;
                                        DUP ;
                                        DUG 2 ;
                                        MEM ;
                                        IF {} { DUP ; PUSH string "NO_PERMIT_TO_DELETE" ; PAIR ; FAILWITH } ;
                                        DIG 6 ;
                                        DUP ;
                                        DUG 7 ;
                                        DIG 5 ;
                                        DIG 2 ;
                                        DUP ;
                                        DUG 3 ;
                                        PAIR %in_param %in_storage ;
                                        EXEC ;
                                        DUP ;
                                        CDDR ;
                                        DUG 5 ;
                                        DUP ;
                                        CAR ;
                                        ITER { DIG 3 ; SWAP ; CONS ; DUG 2 } ;
                                        DUP ;
                                        CDAR ;
                                        DIG 6 ;
                                        DUP ;
                                        DUG 7 ;
                                        CDDAR ;
                                        DIG 3 ;
                                        DUP ;
                                        DUG 4 ;
                                        GET ;
                                        IF_SOME {} { PUSH int 45 ; FAILWITH } ;
                                        NOW ;
                                        SUB ;
                                        ISNAT ;
                                        IF_SOME {} { PUSH int 46 ; FAILWITH } ;
                                        COMPARE ;
                                        GE ;
                                        IF { DROP }
                                           { SWAP ; DUP ; DUG 2 ; PUSH string "PERMIT_NOT_EXPIRED" ; PAIR ; FAILWITH } ;
                                        DIG 4 ;
                                        DUP ;
                                        DUG 5 ;
                                        CDDAR ;
                                        SWAP ;
                                        DUP ;
                                        DUG 2 ;
                                        MEM ;
                                        IF { DIG 4 ;
                                             DUP ;
                                             CAR ;
                                             SWAP ;
                                             CDR ;
                                             DUP ;
                                             CAR ;
                                             SWAP ;
                                             CDR ;
                                             DUP ;
                                             CDR ;
                                             SWAP ;
                                             CAR ;
                                             NONE timestamp ;
                                             DIG 5 ;
                                             DUP ;
                                             DUG 6 ;
                                             UPDATE ;
                                             PAIR ;
                                             SWAP ;
                                             PAIR ;
                                             SWAP ;
                                             PAIR ;
                                             DUG 4 }
                                           {} ;
                                        DIG 4 ;
                                        DUP ;
                                        DUG 5 ;
                                        CDADDR ;
                                        SWAP ;
                                        DUP ;
                                        DUG 2 ;
                                        MEM ;
                                        IF { DIG 4 ;
                                             DUP ;
                                             CAR ;
                                             SWAP ;
                                             CDR ;
                                             DUP ;
                                             CDR ;
                                             SWAP ;
                                             CAR ;
                                             DUP ;
                                             CAR ;
                                             SWAP ;
                                             CDR ;
                                             DUP ;
                                             CAR ;
                                             SWAP ;
                                             CDR ;
                                             NONE (option nat) ;
                                             DIG 6 ;
                                             UPDATE ;
                                             SWAP ;
                                             PAIR ;
                                             SWAP ;
                                             PAIR ;
                                             PAIR ;
                                             SWAP ;
                                             PAIR ;
                                             DUG 3 }
                                           { DROP } } ;
                                 SWAP ;
                                 DROP ;
                                 SWAP ;
                                 DROP ;
                                 DIG 2 ;
                                 DROP ;
                                 DIG 2 ;
                                 DROP } } }
                       { IF_LEFT
                           { IF_LEFT
                               { DIG 2 ;
                                 DROP ;
                                 DIG 2 ;
                                 DROP ;
                                 CONTRACT address ;
                                 NIL operation ;
                                 SWAP ;
                                 IF_SOME {} { PUSH int 219 ; FAILWITH } ;
                                 PUSH mutez 0 ;
                                 DIG 3 ;
                                 DUP ;
                                 DUG 4 ;
                                 CAAAR ;
                                 TRANSFER_TOKENS ;
                                 CONS }
                               { DIG 2 ;
                                 DROP ;
                                 DIG 2 ;
                                 DROP ;
                                 DUP ;
                                 CDR ;
                                 CONTRACT nat ;
                                 NIL operation ;
                                 SWAP ;
                                 IF_SOME {} { PUSH int 209 ; FAILWITH } ;
                                 PUSH mutez 0 ;
                                 DIG 4 ;
                                 DUP ;
                                 DUG 5 ;
                                 CAADR ;
                                 DIG 4 ;
                                 DUP ;
                                 DUG 5 ;
                                 CAAR ;
                                 GET ;
                                 IF_SOME {} { PUSH int 208 ; FAILWITH } ;
                                 CAR ;
                                 DIG 4 ;
                                 CADR ;
                                 GET ;
                                 IF_SOME {} { PUSH int 208 ; FAILWITH } ;
                                 TRANSFER_TOKENS ;
                                 CONS } }
                           { IF_LEFT
                               { DIG 2 ;
                                 DROP ;
                                 DIG 2 ;
                                 DROP ;
                                 DUP ;
                                 CDR ;
                                 CONTRACT nat ;
                                 NIL operation ;
                                 SWAP ;
                                 IF_SOME {} { PUSH int 204 ; FAILWITH } ;
                                 PUSH mutez 0 ;
                                 DIG 4 ;
                                 DUP ;
                                 DUG 5 ;
                                 CAADR ;
                                 DIG 4 ;
                                 CAR ;
                                 GET ;
                                 IF_SOME {} { PUSH int 203 ; FAILWITH } ;
                                 CDR ;
                                 TRANSFER_TOKENS ;
                                 CONS }
                               { DIG 2 ;
                                 DROP ;
                                 DIG 2 ;
                                 DROP ;
                                 CONTRACT nat ;
                                 NIL operation ;
                                 SWAP ;
                                 IF_SOME {} { PUSH int 223 ; FAILWITH } ;
                                 PUSH mutez 0 ;
                                 DIG 3 ;
                                 DUP ;
                                 DUG 4 ;
                                 CADAR ;
                                 TRANSFER_TOKENS ;
                                 CONS } } } }
                   { IF_LEFT
                       { IF_LEFT
                           { IF_LEFT
                               { DIG 2 ;
                                 DROP ;
                                 DIG 2 ;
                                 DROP ;
                                 CONTRACT nat ;
                                 NIL operation ;
                                 SWAP ;
                                 IF_SOME {} { PUSH int 229 ; FAILWITH } ;
                                 PUSH mutez 0 ;
                                 DIG 3 ;
                                 DUP ;
                                 DUG 4 ;
                                 CADDAR ;
                                 TRANSFER_TOKENS ;
                                 CONS }
                               { DIG 2 ;
                                 DROP ;
                                 DIG 2 ;
                                 DROP ;
                                 CONTRACT nat ;
                                 NIL operation ;
                                 SWAP ;
                                 IF_SOME {} { PUSH int 214 ; FAILWITH } ;
                                 PUSH mutez 0 ;
                                 DIG 3 ;
                                 DUP ;
                                 DUG 4 ;
                                 CDDDAR ;
                                 TRANSFER_TOKENS ;
                                 CONS } }
                           { IF_LEFT
                               { SWAP ;
                                 DUP ;
                                 DUG 2 ;
                                 CAAAR ;
                                 SENDER ;
                                 COMPARE ;
                                 EQ ;
                                 IF {}
                                    { PUSH string "WrongCondition: sp.sender == self.data.administrator" ;
                                      FAILWITH } ;
                                 SWAP ;
                                 DUP ;
                                 DUG 2 ;
                                 CAADR ;
                                 SWAP ;
                                 DUP ;
                                 DUG 2 ;
                                 CAR ;
                                 MEM ;
                                 IF { DIG 2 ; DROP ; DIG 2 ; DROP }
                                    { DIG 2 ;
                                      DROP ;
                                      DIG 2 ;
                                      DROP ;
                                      SWAP ;
                                      DUP ;
                                      CDR ;
                                      SWAP ;
                                      CAR ;
                                      DUP ;
                                      CDR ;
                                      SWAP ;
                                      CAR ;
                                      DUP ;
                                      CAR ;
                                      SWAP ;
                                      CDR ;
                                      DIG 4 ;
                                      DUP ;
                                      DUG 5 ;
                                      CAR ;
                                      PUSH (option (pair (map %approvals address nat) (nat %balance))) (Some (Pair {} 0)) ;
                                      SWAP ;
                                      UPDATE ;
                                      SWAP ;
                                      PAIR ;
                                      PAIR ;
                                      PAIR ;
                                      SWAP } ;
                                 SWAP ;
                                 DUP ;
                                 CDR ;
                                 SWAP ;
                                 CAR ;
                                 DUP ;
                                 CDR ;
                                 SWAP ;
                                 CAR ;
                                 DUP ;
                                 CAR ;
                                 SWAP ;
                                 CDR ;
                                 DUP ;
                                 DIG 5 ;
                                 DUP ;
                                 DUG 6 ;
                                 CAR ;
                                 DUP ;
                                 DUG 2 ;
                                 GET ;
                                 IF_SOME {} { PUSH int 185 ; FAILWITH } ;
                                 DUP ;
                                 CAR ;
                                 SWAP ;
                                 CDR ;
                                 DIG 7 ;
                                 DUP ;
                                 DUG 8 ;
                                 CDR ;
                                 ADD ;
                                 SWAP ;
                                 PAIR ;
                                 SOME ;
                                 SWAP ;
                                 UPDATE ;
                                 SWAP ;
                                 PAIR ;
                                 PAIR ;
                                 PAIR ;
                                 DUP ;
                                 CAR ;
                                 SWAP ;
                                 CDR ;
                                 DUP ;
                                 CAR ;
                                 SWAP ;
                                 CDR ;
                                 DUP ;
                                 CAR ;
                                 SWAP ;
                                 CDR ;
                                 DUP ;
                                 CDR ;
                                 SWAP ;
                                 CAR ;
                                 DIG 5 ;
                                 CDR ;
                                 ADD ;
                                 PAIR ;
                                 SWAP ;
                                 PAIR ;
                                 SWAP ;
                                 PAIR ;
                                 SWAP ;
                                 PAIR ;
                                 NIL operation }
                               { SWAP ;
                                 DUP ;
                                 DUG 2 ;
                                 CDADAR ;
                                 IF { PUSH string "WrongCondition: ~ self.data.paused" ; FAILWITH } {} ;
                                 DUP ;
                                 NIL operation ;
                                 SWAP ;
                                 ITER { DIG 5 ;
                                        DUP ;
                                        DUG 6 ;
                                        DIG 4 ;
                                        DIG 2 ;
                                        DUP ;
                                        CDDR ;
                                        SWAP ;
                                        DUP ;
                                        DUG 4 ;
                                        CAR ;
                                        HASH_KEY ;
                                        IMPLICIT_ACCOUNT ;
                                        ADDRESS ;
                                        PAIR ;
                                        PAIR %in_param %in_storage ;
                                        EXEC ;
                                        DUP ;
                                        CDDR ;
                                        DUG 4 ;
                                        DUP ;
                                        CAR ;
                                        ITER { DIG 3 ; SWAP ; CONS ; DUG 2 } ;
                                        DIG 4 ;
                                        DUP ;
                                        DUG 5 ;
                                        CDDAR ;
                                        DIG 2 ;
                                        DUP ;
                                        CDDR ;
                                        SWAP ;
                                        DUP ;
                                        DUG 4 ;
                                        CAR ;
                                        HASH_KEY ;
                                        IMPLICIT_ACCOUNT ;
                                        ADDRESS ;
                                        PAIR ;
                                        MEM ;
                                        IF { DUP ;
                                             CDAR ;
                                             DIG 5 ;
                                             DUP ;
                                             DUG 6 ;
                                             CDDAR ;
                                             DIG 3 ;
                                             DUP ;
                                             CDDR ;
                                             SWAP ;
                                             DUP ;
                                             DUG 5 ;
                                             CAR ;
                                             HASH_KEY ;
                                             IMPLICIT_ACCOUNT ;
                                             ADDRESS ;
                                             PAIR ;
                                             GET ;
                                             IF_SOME {} { PUSH int 102 ; FAILWITH } ;
                                             NOW ;
                                             SUB ;
                                             ISNAT ;
                                             IF_SOME {} { PUSH int 103 ; FAILWITH } ;
                                             COMPARE ;
                                             LT }
                                           { PUSH bool False } ;
                                        IF { SWAP ; DUP ; DUG 2 ; CDDR ; PUSH string "DUP_PERMIT" ; PAIR ; FAILWITH }
                                           {} ;
                                        SWAP ;
                                        DUP ;
                                        DUG 2 ;
                                        CDDR ;
                                        DIG 5 ;
                                        DUP ;
                                        DUG 6 ;
                                        CADAR ;
                                        PAIR ;
                                        SELF ;
                                        ADDRESS ;
                                        CHAIN_ID ;
                                        PAIR ;
                                        PAIR ;
                                        PACK ;
                                        DIG 2 ;
                                        DUP ;
                                        CDAR ;
                                        SWAP ;
                                        DUP ;
                                        DUG 4 ;
                                        CAR ;
                                        CHECK_SIGNATURE ;
                                        IF { DROP }
                                           { SWAP ;
                                             DUP ;
                                             DUG 2 ;
                                             CDDR ;
                                             DIG 5 ;
                                             DUP ;
                                             DUG 6 ;
                                             CADAR ;
                                             PAIR ;
                                             SELF ;
                                             ADDRESS ;
                                             CHAIN_ID ;
                                             PAIR ;
                                             PAIR ;
                                             PACK ;
                                             PUSH string "MISSIGNED" ;
                                             PAIR ;
                                             FAILWITH } ;
                                        DIG 3 ;
                                        DUP ;
                                        CAR ;
                                        SWAP ;
                                        CDR ;
                                        DUP ;
                                        CAR ;
                                        SWAP ;
                                        CDR ;
                                        DUP ;
                                        CDR ;
                                        SWAP ;
                                        CAR ;
                                        DIG 4 ;
                                        DUP ;
                                        CDDR ;
                                        SWAP ;
                                        CAR ;
                                        HASH_KEY ;
                                        IMPLICIT_ACCOUNT ;
                                        ADDRESS ;
                                        PAIR ;
                                        NOW ;
                                        SOME ;
                                        SWAP ;
                                        UPDATE ;
                                        PAIR ;
                                        SWAP ;
                                        PAIR ;
                                        SWAP ;
                                        PAIR ;
                                        DUP ;
                                        CDR ;
                                        SWAP ;
                                        CAR ;
                                        DUP ;
                                        CAR ;
                                        SWAP ;
                                        CDR ;
                                        DUP ;
                                        CDR ;
                                        SWAP ;
                                        CAR ;
                                        PUSH nat 1 ;
                                        ADD ;
                                        PAIR ;
                                        SWAP ;
                                        PAIR ;
                                        PAIR ;
                                        DUG 2 } ;
                                 SWAP ;
                                 DROP ;
                                 DIG 2 ;
                                 DROP ;
                                 DIG 2 ;
                                 DROP } } }
                       { IF_LEFT
                           { IF_LEFT
                               { SWAP ;
                                 DUP ;
                                 DUG 2 ;
                                 CAAAR ;
                                 SENDER ;
                                 COMPARE ;
                                 EQ ;
                                 IF { DIG 2 ; DROP ; DIG 2 ; DROP }
                                    { PUSH string "WrongCondition: sp.sender == self.data.administrator" ;
                                      FAILWITH } ;
                                 SWAP ;
                                 DUP ;
                                 CDR ;
                                 SWAP ;
                                 CAR ;
                                 DUP ;
                                 CDR ;
                                 SWAP ;
                                 CADR ;
                                 DIG 3 ;
                                 PAIR ;
                                 PAIR ;
                                 PAIR }
                               { SWAP ;
                                 DUP ;
                                 DUG 2 ;
                                 CDADAR ;
                                 IF { PUSH string "WrongCondition: ~ self.data.paused" ; FAILWITH } {} ;
                                 SWAP ;
                                 DUP ;
                                 DUG 2 ;
                                 CADDDR ;
                                 SWAP ;
                                 DUP ;
                                 DUG 2 ;
                                 CDDR ;
                                 COMPARE ;
                                 LE ;
                                 IF {} { PUSH string "MAX_SECONDS_EXCEEDED" ; FAILWITH } ;
                                 SENDER ;
                                 PACK ;
                                 SWAP ;
                                 DUP ;
                                 DUG 2 ;
                                 CAR ;
                                 PACK ;
                                 COMPARE ;
                                 EQ ;
                                 IF {} { PUSH bool False ; FAILWITH } ;
                                 DUP ;
                                 CDAR ;
                                 IF_SOME
                                   { DROP ;
                                     SWAP ;
                                     DUP ;
                                     DUG 2 ;
                                     CDDAR ;
                                     SWAP ;
                                     DUP ;
                                     DUG 2 ;
                                     CDAR ;
                                     IF_SOME {} { PUSH int 132 ; FAILWITH } ;
                                     DIG 2 ;
                                     DUP ;
                                     DUG 3 ;
                                     CAR ;
                                     PAIR ;
                                     MEM ;
                                     IF {} { PUSH string "PERMIT_NONEXISTENT" ; FAILWITH } ;
                                     SWAP ;
                                     DUP ;
                                     DUG 2 ;
                                     CDADDR ;
                                     SWAP ;
                                     DUP ;
                                     DUG 2 ;
                                     CDAR ;
                                     IF_SOME {} { PUSH int 132 ; FAILWITH } ;
                                     DIG 2 ;
                                     DUP ;
                                     DUG 3 ;
                                     CAR ;
                                     PAIR ;
                                     MEM ;
                                     IF { SWAP ;
                                          DUP ;
                                          DUG 2 ;
                                          CDADDR ;
                                          SWAP ;
                                          DUP ;
                                          DUG 2 ;
                                          CDAR ;
                                          IF_SOME {} { PUSH int 132 ; FAILWITH } ;
                                          DIG 2 ;
                                          DUP ;
                                          DUG 3 ;
                                          CAR ;
                                          PAIR ;
                                          GET ;
                                          IF_SOME {} { PUSH int 137 ; FAILWITH } ;
                                          IF_SOME { DROP ; PUSH bool True } { PUSH bool False } }
                                        { PUSH bool False } ;
                                     IF { SWAP ;
                                          DUP ;
                                          DUG 2 ;
                                          CDADDR ;
                                          SWAP ;
                                          DUP ;
                                          DUG 2 ;
                                          CDAR ;
                                          IF_SOME {} { PUSH int 132 ; FAILWITH } ;
                                          DIG 2 ;
                                          DUP ;
                                          DUG 3 ;
                                          CAR ;
                                          PAIR ;
                                          GET ;
                                          IF_SOME {} { PUSH int 138 ; FAILWITH } ;
                                          IF_SOME {} { PUSH int 138 ; FAILWITH } ;
                                          DIG 2 ;
                                          DUP ;
                                          DUG 3 ;
                                          CDDAR ;
                                          DIG 2 ;
                                          DUP ;
                                          DUG 3 ;
                                          CDAR ;
                                          IF_SOME {} { PUSH int 132 ; FAILWITH } ;
                                          DIG 3 ;
                                          DUP ;
                                          DUG 4 ;
                                          CAR ;
                                          PAIR ;
                                          GET ;
                                          IF_SOME {} { PUSH int 135 ; FAILWITH } ;
                                          NOW ;
                                          SUB ;
                                          ISNAT ;
                                          IF_SOME {} { PUSH int 140 ; FAILWITH } ;
                                          COMPARE ;
                                          LT ;
                                          IF { DIG 2 ; DROP ; DIG 2 ; DROP }
                                             { PUSH string "PERMIT_REVOKED" ; FAILWITH } }
                                        { SWAP ;
                                          DUP ;
                                          DUG 2 ;
                                          CDDDDR ;
                                          SWAP ;
                                          DUP ;
                                          DUG 2 ;
                                          CAR ;
                                          MEM ;
                                          IF { SWAP ;
                                               DUP ;
                                               DUG 2 ;
                                               CDDDDR ;
                                               SWAP ;
                                               DUP ;
                                               DUG 2 ;
                                               CAR ;
                                               GET ;
                                               IF_SOME {} { PUSH int 143 ; FAILWITH } ;
                                               IF_SOME { DROP ; PUSH bool True } { PUSH bool False } }
                                             { PUSH bool False } ;
                                          IF { SWAP ;
                                               DUP ;
                                               DUG 2 ;
                                               CDDDDR ;
                                               SWAP ;
                                               DUP ;
                                               DUG 2 ;
                                               CAR ;
                                               GET ;
                                               IF_SOME {} { PUSH int 144 ; FAILWITH } ;
                                               IF_SOME {} { PUSH int 144 ; FAILWITH } ;
                                               DIG 2 ;
                                               DUP ;
                                               DUG 3 ;
                                               CDDAR ;
                                               DIG 2 ;
                                               DUP ;
                                               DUG 3 ;
                                               CDAR ;
                                               IF_SOME {} { PUSH int 132 ; FAILWITH } ;
                                               DIG 3 ;
                                               DUP ;
                                               DUG 4 ;
                                               CAR ;
                                               PAIR ;
                                               GET ;
                                               IF_SOME {} { PUSH int 135 ; FAILWITH } ;
                                               NOW ;
                                               SUB ;
                                               ISNAT ;
                                               IF_SOME {} { PUSH int 146 ; FAILWITH } ;
                                               COMPARE ;
                                               LT ;
                                               IF { DIG 2 ; DROP ; DIG 2 ; DROP }
                                                  { PUSH string "PERMIT_REVOKED" ; FAILWITH } }
                                             { SWAP ;
                                               DUP ;
                                               CADDAR ;
                                               SWAP ;
                                               DUP ;
                                               DUG 3 ;
                                               CDDAR ;
                                               DIG 2 ;
                                               DUP ;
                                               DUG 3 ;
                                               CDAR ;
                                               IF_SOME {} { PUSH int 132 ; FAILWITH } ;
                                               DIG 3 ;
                                               DUP ;
                                               DUG 4 ;
                                               CAR ;
                                               PAIR ;
                                               GET ;
                                               IF_SOME {} { PUSH int 135 ; FAILWITH } ;
                                               NOW ;
                                               SUB ;
                                               ISNAT ;
                                               IF_SOME {} { PUSH int 149 ; FAILWITH } ;
                                               COMPARE ;
                                               LT ;
                                               IF { DIG 2 ; DROP ; DIG 2 ; DROP }
                                                  { PUSH string "PERMIT_REVOKED" ; FAILWITH } } } ;
                                     SWAP ;
                                     DUP ;
                                     CAR ;
                                     SWAP ;
                                     CDR ;
                                     DUP ;
                                     CDR ;
                                     SWAP ;
                                     CAR ;
                                     DUP ;
                                     CAR ;
                                     SWAP ;
                                     CDR ;
                                     DUP ;
                                     CAR ;
                                     SWAP ;
                                     CDR ;
                                     DIG 5 ;
                                     DUP ;
                                     DUG 6 ;
                                     CDAR ;
                                     IF_SOME {} { PUSH int 132 ; FAILWITH } ;
                                     DIG 6 ;
                                     DUP ;
                                     DUG 7 ;
                                     CAR ;
                                     PAIR ;
                                     DIG 6 ;
                                     CDDR ;
                                     SOME ;
                                     SOME ;
                                     SWAP ;
                                     UPDATE ;
                                     SWAP ;
                                     PAIR ;
                                     SWAP ;
                                     PAIR ;
                                     PAIR ;
                                     SWAP ;
                                     PAIR }
                                   { DIG 2 ;
                                     DROP ;
                                     DIG 2 ;
                                     DROP ;
                                     SWAP ;
                                     DUP ;
                                     CAR ;
                                     SWAP ;
                                     CDR ;
                                     DUP ;
                                     CAR ;
                                     SWAP ;
                                     CDR ;
                                     DUP ;
                                     CAR ;
                                     SWAP ;
                                     CDR ;
                                     DUP ;
                                     CAR ;
                                     SWAP ;
                                     CDR ;
                                     DIG 5 ;
                                     DUP ;
                                     CAR ;
                                     SWAP ;
                                     CDDR ;
                                     SOME ;
                                     SOME ;
                                     SWAP ;
                                     UPDATE ;
                                     SWAP ;
                                     PAIR ;
                                     SWAP ;
                                     PAIR ;
                                     SWAP ;
                                     PAIR ;
                                     SWAP ;
                                     PAIR } } ;
                             NIL operation }
                           { IF_LEFT
                               { SWAP ;
                                 DUP ;
                                 DUG 2 ;
                                 CAAAR ;
                                 SENDER ;
                                 COMPARE ;
                                 EQ ;
                                 IF { DIG 2 ; DROP ; DIG 2 ; DROP }
                                    { PUSH string "WrongCondition: sp.sender == self.data.administrator" ;
                                      FAILWITH } ;
                                 SWAP ;
                                 DUP ;
                                 CAR ;
                                 SWAP ;
                                 CDR ;
                                 DUP ;
                                 CDR ;
                                 SWAP ;
                                 CAR ;
                                 DUP ;
                                 CAR ;
                                 SWAP ;
                                 CDDR ;
                                 DIG 4 ;
                                 PAIR ;
                                 SWAP ;
                                 PAIR ;
                                 PAIR ;
                                 SWAP ;
                                 PAIR ;
                                 NIL operation }
                               { SENDER ;
                                 DIG 3 ;
                                 DUP ;
                                 DUG 4 ;
                                 DIG 3 ;
                                 DIG 3 ;
                                 DUP ;
                                 DUG 4 ;
                                 PAIR %in_param %in_storage ;
                                 EXEC ;
                                 DUP ;
                                 CDDR ;
                                 DUG 3 ;
                                 DUP ;
                                 CAR ;
                                 NIL operation ;
                                 SWAP ;
                                 ITER { CONS } ;
                                 SWAP ;
                                 DUP ;
                                 DUG 2 ;
                                 CDAR ;
                                 IF { DIG 2 ; DROP ; DIG 2 ; DUP ; DUG 3 ; CAR ; DUG 2 } {} ;
                                 DIG 4 ;
                                 DUP ;
                                 DUG 5 ;
                                 CAAAR ;
                                 DIG 3 ;
                                 DUP ;
                                 DUG 4 ;
                                 COMPARE ;
                                 EQ ;
                                 IF { PUSH bool True }
                                    { DIG 4 ;
                                      DUP ;
                                      DUG 5 ;
                                      CDADAR ;
                                      IF { PUSH bool False }
                                         { DIG 2 ;
                                           DUP ;
                                           DUG 3 ;
                                           DIG 4 ;
                                           DUP ;
                                           DUG 5 ;
                                           CAR ;
                                           COMPARE ;
                                           EQ ;
                                           IF { PUSH bool True }
                                              { DIG 3 ;
                                                DUP ;
                                                DUG 4 ;
                                                CDDR ;
                                                DIG 5 ;
                                                DUP ;
                                                DUG 6 ;
                                                CAADR ;
                                                DIG 5 ;
                                                DUP ;
                                                DUG 6 ;
                                                CAR ;
                                                GET ;
                                                IF_SOME {} { PUSH int 26 ; FAILWITH } ;
                                                CAR ;
                                                DIG 4 ;
                                                DUP ;
                                                DUG 5 ;
                                                GET ;
                                                IF_SOME {} { PUSH int 26 ; FAILWITH } ;
                                                COMPARE ;
                                                GE } } } ;
                                 IF {}
                                    { PUSH string
                                           "WrongCondition: (sender.value == self.data.administrator) | ((~ self.data.paused) & ((params.from_ == sender.value) | (self.data.balances[params.from_].approvals[sender.value] >= params.value)))" ;
                                      FAILWITH } ;
                                 DIG 4 ;
                                 DUP ;
                                 DUG 5 ;
                                 CAADR ;
                                 DIG 4 ;
                                 DUP ;
                                 DUG 5 ;
                                 CDAR ;
                                 MEM ;
                                 IF {}
                                    { DIG 4 ;
                                      DUP ;
                                      CDR ;
                                      SWAP ;
                                      CAR ;
                                      DUP ;
                                      CDR ;
                                      SWAP ;
                                      CAR ;
                                      DUP ;
                                      CAR ;
                                      SWAP ;
                                      CDR ;
                                      DIG 7 ;
                                      DUP ;
                                      DUG 8 ;
                                      CDAR ;
                                      PUSH (option (pair (map %approvals address nat) (nat %balance))) (Some (Pair {} 0)) ;
                                      SWAP ;
                                      UPDATE ;
                                      SWAP ;
                                      PAIR ;
                                      PAIR ;
                                      PAIR ;
                                      DUG 4 } ;
                                 DIG 3 ;
                                 DUP ;
                                 DUG 4 ;
                                 CDDR ;
                                 DIG 5 ;
                                 DUP ;
                                 DUG 6 ;
                                 CAADR ;
                                 DIG 5 ;
                                 DUP ;
                                 DUG 6 ;
                                 CAR ;
                                 GET ;
                                 IF_SOME {} { PUSH int 28 ; FAILWITH } ;
                                 CDR ;
                                 COMPARE ;
                                 GE ;
                                 IF {}
                                    { PUSH string
                                           "WrongCondition: self.data.balances[params.from_].balance >= params.value" ;
                                      FAILWITH } ;
                                 DIG 4 ;
                                 DUP ;
                                 DUG 5 ;
                                 DUP ;
                                 CDR ;
                                 SWAP ;
                                 CAR ;
                                 DUP ;
                                 CDR ;
                                 SWAP ;
                                 CAR ;
                                 DUP ;
                                 CAR ;
                                 SWAP ;
                                 CDR ;
                                 DUP ;
                                 DIG 8 ;
                                 DUP ;
                                 DUG 9 ;
                                 CAR ;
                                 DUP ;
                                 DUG 2 ;
                                 GET ;
                                 IF_SOME {} { PUSH int 29 ; FAILWITH } ;
                                 CAR ;
                                 DIG 9 ;
                                 DUP ;
                                 DUG 10 ;
                                 CDDR ;
                                 DIG 11 ;
                                 CAADR ;
                                 DIG 11 ;
                                 DUP ;
                                 DUG 12 ;
                                 CAR ;
                                 GET ;
                                 IF_SOME {} { PUSH int 30 ; FAILWITH } ;
                                 CDR ;
                                 SUB ;
                                 ISNAT ;
                                 IF_SOME {} { PUSH int 29 ; FAILWITH } ;
                                 SWAP ;
                                 PAIR ;
                                 SOME ;
                                 SWAP ;
                                 UPDATE ;
                                 SWAP ;
                                 PAIR ;
                                 PAIR ;
                                 PAIR ;
                                 DUP ;
                                 CDR ;
                                 SWAP ;
                                 CAR ;
                                 DUP ;
                                 CDR ;
                                 SWAP ;
                                 CAR ;
                                 DUP ;
                                 CAR ;
                                 SWAP ;
                                 CDR ;
                                 DUP ;
                                 DIG 8 ;
                                 DUP ;
                                 DUG 9 ;
                                 CDAR ;
                                 DUP ;
                                 DUG 2 ;
                                 GET ;
                                 IF_SOME {} { PUSH int 31 ; FAILWITH } ;
                                 DUP ;
                                 CAR ;
                                 SWAP ;
                                 CDR ;
                                 DIG 10 ;
                                 DUP ;
                                 DUG 11 ;
                                 CDDR ;
                                 ADD ;
                                 SWAP ;
                                 PAIR ;
                                 SOME ;
                                 SWAP ;
                                 UPDATE ;
                                 SWAP ;
                                 PAIR ;
                                 PAIR ;
                                 PAIR ;
                                 DUG 4 ;
                                 DIG 2 ;
                                 DUP ;
                                 DUG 3 ;
                                 DIG 4 ;
                                 DUP ;
                                 DUG 5 ;
                                 CAR ;
                                 COMPARE ;
                                 NEQ ;
                                 IF { DIG 2 ; DUP ; DUG 3 ; DIG 5 ; DUP ; DUG 6 ; CAAAR ; COMPARE ; NEQ }
                                    { PUSH bool False } ;
                                 IF { SWAP ;
                                      DROP ;
                                      DIG 4 ;
                                      DROP ;
                                      DIG 4 ;
                                      DROP ;
                                      DIG 3 ;
                                      DUP ;
                                      DUG 4 ;
                                      DUP ;
                                      CDR ;
                                      SWAP ;
                                      CAR ;
                                      DUP ;
                                      CDR ;
                                      SWAP ;
                                      CAR ;
                                      DUP ;
                                      CAR ;
                                      SWAP ;
                                      CDR ;
                                      DUP ;
                                      DIG 7 ;
                                      DUP ;
                                      DUG 8 ;
                                      CAR ;
                                      DUP ;
                                      DUG 2 ;
                                      GET ;
                                      IF_SOME {} { PUSH int 33 ; FAILWITH } ;
                                      DUP ;
                                      CDR ;
                                      SWAP ;
                                      CAR ;
                                      DIG 8 ;
                                      DIG 9 ;
                                      DUP ;
                                      DUG 10 ;
                                      CDDR ;
                                      DIG 11 ;
                                      CAADR ;
                                      DIG 11 ;
                                      CAR ;
                                      GET ;
                                      IF_SOME {} { PUSH int 34 ; FAILWITH } ;
                                      CAR ;
                                      DIG 2 ;
                                      DUP ;
                                      DUG 3 ;
                                      GET ;
                                      IF_SOME {} { PUSH int 34 ; FAILWITH } ;
                                      SUB ;
                                      ISNAT ;
                                      IF_SOME {} { PUSH int 33 ; FAILWITH } ;
                                      SOME ;
                                      SWAP ;
                                      UPDATE ;
                                      PAIR ;
                                      SOME ;
                                      SWAP ;
                                      UPDATE ;
                                      SWAP ;
                                      PAIR ;
                                      PAIR ;
                                      PAIR ;
                                      SWAP }
                                    { SWAP ; DROP ; SWAP ; DROP ; SWAP ; DROP ; DIG 2 ; DROP ; DIG 2 ; DROP } } } } } ;
                 NIL operation ;
                 SWAP ;
                 ITER { CONS } ;
                 PAIR } }
        Initial storage:
          (Pair (Pair (Pair "tz1KqTpEZ7Yob7QbPE4Hy4Wo8fHG8LhKxZSx" {}) (Pair 0 (Pair 50000 2628000)))
                (Pair (Pair { Elt "" 0x74657a6f732d73746f726167653a6d642d6a736f6e ;
                              Elt "md-json"
                                  0x7b226e616d65223a2022736d61727470792d7065726d697473222c20226465736372697074696f6e223a2022496d706c656d656e746174696f6e206f6620547a69702d313720696e20536d6172747079206f6e206261736963204641312e3220636f6e74726163745c6e222c20226c6963656e7365223a207b226e616d65223a20224d4954222c202264657461696c73223a2022546865204d4954204c6963656e7365227d2c2022686f6d6570616765223a202268747470733a2f2f6769746875622e636f6d2f454775656e7a2f736d61727470792d7065726d697473222c2022696e7465726661636573223a205b22545a49502d3136222c2022545a49502d3137225d2c20227669657773223a205b7b226e616d65223a202267657444656661756c74457870697279222c2022696d706c656d656e746174696f6e73223a205b7b226d696368656c736f6e2d73746f726167652d76696577223a207b22706172616d65746572223a207b227072696d223a202261646472657373222c2022616e6e6f7473223a205b222567657444656661756c74457870697279225d7d2c202272657475726e2d74797065223a207b227072696d223a20226e6174227d2c2022636f6465223a205b7b227072696d223a2022444947222c202261726773223a205b7b22696e74223a202232227d5d7d2c207b227072696d223a202244524f50227d2c207b227072696d223a2022444947222c202261726773223a205b7b22696e74223a202232227d5d7d2c207b227072696d223a202244524f50227d2c207b227072696d223a2022434f4e5452414354222c202261726773223a205b7b227072696d223a20226e6174227d5d7d2c207b227072696d223a20224e494c222c202261726773223a205b7b227072696d223a20226f7065726174696f6e227d5d7d2c207b227072696d223a202253574150227d2c207b227072696d223a202249465f4e4f4e45222c202261726773223a205b5b7b227072696d223a202250555348222c202261726773223a205b7b227072696d223a2022696e74227d2c207b22696e74223a2022323239227d5d7d2c207b227072696d223a20224641494c57495448227d5d2c205b5d5d7d2c207b227072696d223a202250555348222c202261726773223a205b7b227072696d223a20226d7574657a227d2c207b22696e74223a202230227d5d7d2c207b227072696d223a2022444947222c202261726773223a205b7b22696e74223a202233227d5d7d2c207b227072696d223a2022445550227d2c207b227072696d223a2022445547222c202261726773223a205b7b22696e74223a202234227d5d7d2c207b227072696d223a2022434152227d2c207b227072696d223a2022434452227d2c207b227072696d223a2022434452227d2c207b227072696d223a2022434152227d2c207b227072696d223a20225452414e534645525f544f4b454e53227d2c207b227072696d223a2022434f4e53227d5d7d7d5d2c202270757265223a20747275657d2c207b226e616d65223a2022676574436f756e746572222c2022696d706c656d656e746174696f6e73223a205b7b226d696368656c736f6e2d73746f726167652d76696577223a207b22706172616d65746572223a207b227072696d223a202261646472657373222c2022616e6e6f7473223a205b2225676574436f756e746572225d7d2c202272657475726e2d74797065223a207b227072696d223a20226e6174227d2c2022636f6465223a205b7b227072696d223a2022444947222c202261726773223a205b7b22696e74223a202232227d5d7d2c207b227072696d223a202244524f50227d2c207b227072696d223a2022444947222c202261726773223a205b7b22696e74223a202232227d5d7d2c207b227072696d223a202244524f50227d2c207b227072696d223a2022434f4e5452414354222c202261726773223a205b7b227072696d223a20226e6174227d5d7d2c207b227072696d223a20224e494c222c202261726773223a205b7b227072696d223a20226f7065726174696f6e227d5d7d2c207b227072696d223a202253574150227d2c207b227072696d223a202249465f4e4f4e45222c202261726773223a205b5b7b227072696d223a202250555348222c202261726773223a205b7b227072696d223a2022696e74227d2c207b22696e74223a2022323233227d5d7d2c207b227072696d223a20224641494c57495448227d5d2c205b5d5d7d2c207b227072696d223a202250555348222c202261726773223a205b7b227072696d223a20226d7574657a227d2c207b22696e74223a202230227d5d7d2c207b227072696d223a2022444947222c202261726773223a205b7b22696e74223a202233227d5d7d2c207b227072696d223a2022445550227d2c207b227072696d223a2022445547222c202261726773223a205b7b22696e74223a202234227d5d7d2c207b227072696d223a2022434152227d2c207b227072696d223a2022434452227d2c207b227072696d223a2022434152227d2c207b227072696d223a20225452414e534645525f544f4b454e53227d2c207b227072696d223a2022434f4e53227d5d7d7d5d2c202270757265223a20747275657d5d7d }
                            (Pair False {}))
                      (Pair {} (Pair 0 {}))))
        No delegate for this contract
        This origination was successfully applied
        Originated contracts:
          KT1H5ELRW3wmVMuZPJwL3DEUkCc5B6gH4M9H
        Storage size: 13783 bytes
        Updated big_maps:
          New map(4) of type (big_map address (option nat))
          New map(3) of type (big_map (pair address bytes) timestamp)
          New map(2) of type (big_map (pair address bytes) (option nat))
          New map(1) of type (big_map string bytes)
          Set map(1)[""] to 0x74657a6f732d73746f726167653a6d642d6a736f6e
          Set map(1)["md-json"] to 0x7b226e616d65223a2022736d61727470792d7065726d697473222c20226465736372697074696f6e223a2022496d706c656d656e746174696f6e206f6620547a69702d313720696e20536d6172747079206f6e206261736963204641312e3220636f6e74726163745c6e222c20226c6963656e7365223a207b226e616d65223a20224d4954222c202264657461696c73223a2022546865204d4954204c6963656e7365227d2c2022686f6d6570616765223a202268747470733a2f2f6769746875622e636f6d2f454775656e7a2f736d61727470792d7065726d697473222c2022696e7465726661636573223a205b22545a49502d3136222c2022545a49502d3137225d2c20227669657773223a205b7b226e616d65223a202267657444656661756c74457870697279222c2022696d706c656d656e746174696f6e73223a205b7b226d696368656c736f6e2d73746f726167652d76696577223a207b22706172616d65746572223a207b227072696d223a202261646472657373222c2022616e6e6f7473223a205b222567657444656661756c74457870697279225d7d2c202272657475726e2d74797065223a207b227072696d223a20226e6174227d2c2022636f6465223a205b7b227072696d223a2022444947222c202261726773223a205b7b22696e74223a202232227d5d7d2c207b227072696d223a202244524f50227d2c207b227072696d223a2022444947222c202261726773223a205b7b22696e74223a202232227d5d7d2c207b227072696d223a202244524f50227d2c207b227072696d223a2022434f4e5452414354222c202261726773223a205b7b227072696d223a20226e6174227d5d7d2c207b227072696d223a20224e494c222c202261726773223a205b7b227072696d223a20226f7065726174696f6e227d5d7d2c207b227072696d223a202253574150227d2c207b227072696d223a202249465f4e4f4e45222c202261726773223a205b5b7b227072696d223a202250555348222c202261726773223a205b7b227072696d223a2022696e74227d2c207b22696e74223a2022323239227d5d7d2c207b227072696d223a20224641494c57495448227d5d2c205b5d5d7d2c207b227072696d223a202250555348222c202261726773223a205b7b227072696d223a20226d7574657a227d2c207b22696e74223a202230227d5d7d2c207b227072696d223a2022444947222c202261726773223a205b7b22696e74223a202233227d5d7d2c207b227072696d223a2022445550227d2c207b227072696d223a2022445547222c202261726773223a205b7b22696e74223a202234227d5d7d2c207b227072696d223a2022434152227d2c207b227072696d223a2022434452227d2c207b227072696d223a2022434452227d2c207b227072696d223a2022434152227d2c207b227072696d223a20225452414e534645525f544f4b454e53227d2c207b227072696d223a2022434f4e53227d5d7d7d5d2c202270757265223a20747275657d2c207b226e616d65223a2022676574436f756e746572222c2022696d706c656d656e746174696f6e73223a205b7b226d696368656c736f6e2d73746f726167652d76696577223a207b22706172616d65746572223a207b227072696d223a202261646472657373222c2022616e6e6f7473223a205b2225676574436f756e746572225d7d2c202272657475726e2d74797065223a207b227072696d223a20226e6174227d2c2022636f6465223a205b7b227072696d223a2022444947222c202261726773223a205b7b22696e74223a202232227d5d7d2c207b227072696d223a202244524f50227d2c207b227072696d223a2022444947222c202261726773223a205b7b22696e74223a202232227d5d7d2c207b227072696d223a202244524f50227d2c207b227072696d223a2022434f4e5452414354222c202261726773223a205b7b227072696d223a20226e6174227d5d7d2c207b227072696d223a20224e494c222c202261726773223a205b7b227072696d223a20226f7065726174696f6e227d5d7d2c207b227072696d223a202253574150227d2c207b227072696d223a202249465f4e4f4e45222c202261726773223a205b5b7b227072696d223a202250555348222c202261726773223a205b7b227072696d223a2022696e74227d2c207b22696e74223a2022323233227d5d7d2c207b227072696d223a20224641494c57495448227d5d2c205b5d5d7d2c207b227072696d223a202250555348222c202261726773223a205b7b227072696d223a20226d7574657a227d2c207b22696e74223a202230227d5d7d2c207b227072696d223a2022444947222c202261726773223a205b7b22696e74223a202233227d5d7d2c207b227072696d223a2022445550227d2c207b227072696d223a2022445547222c202261726773223a205b7b22696e74223a202234227d5d7d2c207b227072696d223a2022434152227d2c207b227072696d223a2022434452227d2c207b227072696d223a2022434152227d2c207b227072696d223a20225452414e534645525f544f4b454e53227d2c207b227072696d223a2022434f4e53227d5d7d7d5d2c202270757265223a20747275657d5d7d
          New map(0) of type (big_map address (pair (map %approvals address nat) (nat %balance)))
        Paid storage size diff: 13783 bytes
        Consumed gas: 420217
        Balance updates:
          tz1KqTpEZ7Yob7QbPE4Hy4Wo8fHG8LhKxZSx ... -ꜩ13.783
          tz1KqTpEZ7Yob7QbPE4Hy4Wo8fHG8LhKxZSx ... -ꜩ0.257

New contract KT1H5ELRW3wmVMuZPJwL3DEUkCc5B6gH4M9H originated.
The operation has only been included 0 blocks ago.
We recommend to wait more.
Use command
  tezos-client wait for opFYQzzkgctT7Ph2uERbsP3qqQpgm6MNxvBHmJ7NwNnn7cFzPi8 to be included --confirmations 30 --branch BKiYCUrr8qU55HbSqiSS2my3LCezy3SvBAG95sb9dg6q2kA6VrA
and/or an external block explorer.
Contract memorized as fa1.2-permits.

```

### Mint 10 tokens to bootstrap 2

```
$ tezos-client transfer 0 from bootstrap1 to fa1.2-permits --burn-cap 50000 --entrypoint "mint" --arg "Pair \"$bootstrap2_address\" 10"
Warning:

   The node you are connecting to claims to be running in a
                    Tezos TEST SANDBOX.
      Do NOT use your fundraiser keys on this network.
  You should not see this message if you are not a developer.

Node is bootstrapped, ready for injecting operations.
Estimated gas: 334072 units (will add 100 for safety)
Estimated storage: 74 bytes added (will add 20 for safety)
Operation successfully injected in the node.
Operation hash is 'ooGBvF8vBuUaodz4mDtfADNwEdpqToj9gym52FZL53vkpqiPFsY'
Waiting for the operation to be included...
Operation found in block: BLJREkkiBr4nUPtinMCaHUPH4uUDppL3gRCfZ4GYFBnpmY6ihrS (pass: 3, offset: 0)
This sequence of operations was run:
  Manager signed operations:
    From: tz1KqTpEZ7Yob7QbPE4Hy4Wo8fHG8LhKxZSx
    Fee to the baker: ꜩ0.033723
    Expected counter: 2
    Gas limit: 334172
    Storage limit: 94 bytes
    Balance updates:
      tz1KqTpEZ7Yob7QbPE4Hy4Wo8fHG8LhKxZSx ........... -ꜩ0.033723
      fees(tz1b7tUupMgCNw2cCLpKTkSD1NZzB5TkP2sv,0) ... +ꜩ0.033723
    Transaction:
      Amount: ꜩ0
      From: tz1KqTpEZ7Yob7QbPE4Hy4Wo8fHG8LhKxZSx
      To: KT1H5ELRW3wmVMuZPJwL3DEUkCc5B6gH4M9H
      Entrypoint: mint
      Parameter: (Pair "tz1gjaF81ZRRvdzjobyfVNsAeSC6PScjfQwN" 10)
      This transaction was successfully applied
      Updated storage:
        (Pair (Pair (Pair 0x000002298c03ed7d454a101eb7022bc95f7e5f41ac78 0)
                    (Pair 0 (Pair 50000 2628000)))
              (Pair (Pair 1 (Pair False 2)) (Pair 3 (Pair 10 4))))
      Updated big_maps:
        Set map(0)[0x0000e7670f32038107a59a2b9cfefae36ea21f5aa63c] to (Pair {} 10)
      Storage size: 13857 bytes
      Paid storage size diff: 74 bytes
      Consumed gas: 334072
      Balance updates:
        tz1KqTpEZ7Yob7QbPE4Hy4Wo8fHG8LhKxZSx ... -ꜩ0.074

The operation has only been included 0 blocks ago.
We recommend to wait more.
Use command
  tezos-client wait for ooGBvF8vBuUaodz4mDtfADNwEdpqToj9gym52FZL53vkpqiPFsY to be included --confirmations 30 --branch BMPHZyGAGFgwqPYc3eA5pYrAXUCmw6iA1kPnKDDw1XF4Z9S7RLx
and/or an external block explorer.
```

### Observe transfer by non bootstrap2 sender fails

```
$ tezos-client transfer 0 from bootstrap4 to fa1.2-permits --burn-cap 50000 --entrypoint "transfer" --arg "$transfer_param"

Warning:

   The node you are connecting to claims to be running in a
                    Tezos TEST SANDBOX.
      Do NOT use your fundraiser keys on this network.
  You should not see this message if you are not a developer.

Node is bootstrapped, ready for injecting operations.
This simulation failed:
  Manager signed operations:
    From: tz1b7tUupMgCNw2cCLpKTkSD1NZzB5TkP2sv
    Fee to the baker: ꜩ0
    Expected counter: 1
    Gas limit: 1040000
    Storage limit: 60000 bytes
    Transaction:
      Amount: ꜩ0
      From: tz1b7tUupMgCNw2cCLpKTkSD1NZzB5TkP2sv
      To: KT1H5ELRW3wmVMuZPJwL3DEUkCc5B6gH4M9H
      Entrypoint: transfer
      Parameter: (Pair "tz1gjaF81ZRRvdzjobyfVNsAeSC6PScjfQwN"
                       (Pair "tz1faswCTDciRzE4oJ9jn2Vm2dvjeyA9fUzU" 5))
      This operation FAILED.

Runtime error in contract KT1H5ELRW3wmVMuZPJwL3DEUkCc5B6gH4M9H:
  0001: { .....}
At line 1553 characters 67 to 75,
script reached FAILWITH instruction
with 26
Fatal error:
  transfer simulation failed

```

### Define a fake permit parameter to get the expected unsigned bytes
1. Get the BLAKE2B of `TRANSFER_PARAM_PACKED` by entering its value into the editor in [TZComet](https://tqtezos.github.io/TZComet/#/editor), pressing show binary info and copying the value BLAKE2B-Hex under "Binary-Michelson-Expression (with watermark)".

```
TRANSFER_PARAM_HASHED=0x877b50b43b81b9d2c5a6c56087fab148a6622741cd0e79557e6b6131b8b5e49b
```

2. Set a random signature
```
RAND_SIG="edsigtfkWys7vyeQy1PnHcBuac1dgj2aJ8Jv3fvoDE5XRtxTMRgJBwVgMTzvhAzBQyjH48ux9KE8jRZBSk4Rv2bfphsfpKP3ggM"
```

3. Get Bootstrap2's public_key and capture it

```
$ tezos-client show address bootstrap2 -S

Warning:

   The node you are connecting to claims to be running in a
                    Tezos TEST SANDBOX.
      Do NOT use your fundraiser keys on this network.
  You should not see this message if you are not a developer.

Hash: tz1gjaF81ZRRvdzjobyfVNsAeSC6PScjfQwN
Public Key: edpktzNbDAUjUk697W7gYg2CRuBQjyPxbEg8dLccYYwKSKvkPvjtV9
Secret Key: unencrypted:edsk39qAm1fiMjgmPkw1EgQYkMzkJezLNewd7PLNHTkr6w9XA2zdfo

$ PUB_KEY="edpktzNbDAUjUk697W7gYg2CRuBQjyPxbEg8dLccYYwKSKvkPvjtV9"
```

4. Set Fake permit param

```
PERMIT_PARAM_FAKE="{Pair \"$PUB_KEY\" (Pair \"$RAND_SIG\" $TRANSFER_PARAM_HASHED)}"

```

5. Call permit entrypoint with fake Parameter

```
$ tezos-client transfer 0 from bootstrap4 to fa1.2-permits --burn-cap 5000 --entrypoint "permit" --arg "$PERMIT_PARAM_FAKE"

Warning:

   The node you are connecting to claims to be running in a
                    Tezos TEST SANDBOX.
      Do NOT use your fundraiser keys on this network.
  You should not see this message if you are not a developer.

Node is bootstrapped, ready for injecting operations.
This simulation failed:
  Manager signed operations:
    From: tz1b7tUupMgCNw2cCLpKTkSD1NZzB5TkP2sv
    Fee to the baker: ꜩ0
    Expected counter: 2
    Gas limit: 1040000
    Storage limit: 60000 bytes
    Transaction:
      Amount: ꜩ0
      From: tz1b7tUupMgCNw2cCLpKTkSD1NZzB5TkP2sv
      To: KT1H5ELRW3wmVMuZPJwL3DEUkCc5B6gH4M9H
      Entrypoint: permit
      Parameter: { Pair "edpktzNbDAUjUk697W7gYg2CRuBQjyPxbEg8dLccYYwKSKvkPvjtV9"
                        (Pair "edsigtfkWys7vyeQy1PnHcBuac1dgj2aJ8Jv3fvoDE5XRtxTMRgJBwVgMTzvhAzBQyjH48ux9KE8jRZBSk4Rv2bfphsfpKP3ggM"
                              0xe6f1aa42d877954d34bbde9ca5bdd2676b139adb52ebc7b943fe8a07f55591e9) }
      This operation FAILED.

Runtime error in contract KT1H5ELRW3wmVMuZPJwL3DEUkCc5B6gH4M9H:
  0001: { ...}
At line 1090 characters 37 to 45,
script reached FAILWITH instruction
with
  (Pair "MISSIGNED"
        0x05070707070a000000047a06a7700a00000016015d22ffe866052e73c7dc6e964601fdbc5913572c00070700010a00000020e6f1aa42d877954d34bbde9ca5bdd2676b139adb52ebc7b943fe8a07f55591e9)
Fatal error:
  transfer simulation failed
```

6. Set MISSIGNED with bytes returned in error message of fake permit submission
```
$ MISSIGNED=0x05070707070a000000047a06a7700a00000016015d22ffe866052e73c7dc6e964601fdbc5913572c00070700010a00000020e6f1aa42d877954d34bbde9ca5bdd2676b139adb52ebc7b943fe8a07f55591e9
```

### Sign MISSIGNED bytes and submit new permit
1. Sign MISSIGNED

```
$ tezos-client sign bytes $MISSIGNED for bootstrap2  
Warning:

   The node you are connecting to claims to be running in a
                    Tezos TEST SANDBOX.
      Do NOT use your fundraiser keys on this network.
  You should not see this message if you are not a developer.

Signature: edsigtmPaqoLGWLYYqNPvDoKgn9aFYEEkKJnSNpUhY14a3kqad4m18NYoZn4twQkvXKEQoigSE7uneqHCgswZYqyZbqqMBwesJr
```

2. Capture signature
```
$ SIGNATURE=edsigtmPaqoLGWLYYqNPvDoKgn9aFYEEkKJnSNpUhY14a3kqad4m18NYoZn4twQkvXKEQoigSE7uneqHCgswZYqyZbqqMBwesJr
```

3. Craft correct permit parameter
```
PERMIT_PARAM="{Pair \"$PUB_KEY\" (Pair \"$SIGNATURE\" $TRANSFER_PARAM_HASHED)}"
```

4. Anyone can submit permit
```
$ tezos-client transfer 0 from bootstrap4 to fa1.2-permits --burn-cap 5000 --entrypoint "permit" --arg "$PERMIT_PARAM"

Warning:

   The node you are connecting to claims to be running in a
                    Tezos TEST SANDBOX.
      Do NOT use your fundraiser keys on this network.
  You should not see this message if you are not a developer.

Node is bootstrapped, ready for injecting operations.
Estimated gas: 337549 units (will add 100 for safety)
Estimated storage: 71 bytes added (will add 20 for safety)
Operation successfully injected in the node.
Operation hash is 'opUaLcMgp8fkir5xWVnvMF2VDvnWJQcQJRi7z3as3wKFYB3r3xt'
Waiting for the operation to be included...
Operation found in block: BMR7g84ZngYqMjKjD56hRGbzMW47ePKAcEVBPXuFeoUv7fRdnxn (pass: 3, offset: 0)
This sequence of operations was run:
  Manager signed operations:
    From: tz1b7tUupMgCNw2cCLpKTkSD1NZzB5TkP2sv
    Fee to the baker: ꜩ0.034236
    Expected counter: 2
    Gas limit: 337649
    Storage limit: 91 bytes
    Balance updates:
      tz1b7tUupMgCNw2cCLpKTkSD1NZzB5TkP2sv ........... -ꜩ0.034236
      fees(tz1b7tUupMgCNw2cCLpKTkSD1NZzB5TkP2sv,0) ... +ꜩ0.034236
    Transaction:
      Amount: ꜩ0
      From: tz1b7tUupMgCNw2cCLpKTkSD1NZzB5TkP2sv
      To: KT1H5ELRW3wmVMuZPJwL3DEUkCc5B6gH4M9H
      Entrypoint: permit
      Parameter: { Pair "edpktzNbDAUjUk697W7gYg2CRuBQjyPxbEg8dLccYYwKSKvkPvjtV9"
                        (Pair "edsigtmPaqoLGWLYYqNPvDoKgn9aFYEEkKJnSNpUhY14a3kqad4m18NYoZn4twQkvXKEQoigSE7uneqHCgswZYqyZbqqMBwesJr"
                              0xe6f1aa42d877954d34bbde9ca5bdd2676b139adb52ebc7b943fe8a07f55591e9) }
      This transaction was successfully applied
      Updated storage:
        (Pair (Pair (Pair 0x000002298c03ed7d454a101eb7022bc95f7e5f41ac78 0)
                    (Pair 2 (Pair 50000 2628000)))
              (Pair (Pair 1 (Pair False 2)) (Pair 3 (Pair 10 4))))
      Updated big_maps:
        Set map(3)[(Pair 0x0000e7670f32038107a59a2b9cfefae36ea21f5aa63c
              0xe6f1aa42d877954d34bbde9ca5bdd2676b139adb52ebc7b943fe8a07f55591e9)] to 1605912691
      Storage size: 13999 bytes
      Paid storage size diff: 71 bytes
      Consumed gas: 337549
      Balance updates:
        tz1b7tUupMgCNw2cCLpKTkSD1NZzB5TkP2sv ... -ꜩ0.071

The operation has only been included 0 blocks ago.
We recommend to wait more.
Use command
  tezos-client wait for opUaLcMgp8fkir5xWVnvMF2VDvnWJQcQJRi7z3as3wKFYB3r3xt to be included --confirmations 30 --branch BM49Tq9TGzam1tyeZYtbR2aUEV4jMvBdu2CsdjWGTJGSz8sNSBA
and/or an external block explorer.
```
### Successfully execute transfer away from bootstrap2 by calling transfer endpoint from any account

```
$ tezos-client transfer 0 from bootstrap4 to fa1.2-permits --burn-cap 50000 --entrypoint "transfer" --arg "$transfer_param"

Warning:

   The node you are connecting to claims to be running in a
                    Tezos TEST SANDBOX.
      Do NOT use your fundraiser keys on this network.
  You should not see this message if you are not a developer.

Node is bootstrapped, ready for injecting operations.
Estimated gas: 344718 units (will add 100 for safety)
Estimated storage: 3 bytes added (will add 20 for safety)
Operation successfully injected in the node.
Operation hash is 'onxpDWvgwrSGiGYq4WAYne25MHtJeCv9NXf3p3T5z9BfsP5c9WG'
Waiting for the operation to be included...
Operation found in block: BKqCiU1aPv9rFEeryqSrMn58SwhyfHevJwkbNEZ8nSS7U4DdSwe (pass: 3, offset: 0)
This sequence of operations was run:
  Manager signed operations:
    From: tz1b7tUupMgCNw2cCLpKTkSD1NZzB5TkP2sv
    Fee to the baker: ꜩ0.034834
    Expected counter: 3
    Gas limit: 344818
    Storage limit: 23 bytes
    Balance updates:
      tz1b7tUupMgCNw2cCLpKTkSD1NZzB5TkP2sv ........... -ꜩ0.034834
      fees(tz1b7tUupMgCNw2cCLpKTkSD1NZzB5TkP2sv,0) ... +ꜩ0.034834
    Transaction:
      Amount: ꜩ0
      From: tz1b7tUupMgCNw2cCLpKTkSD1NZzB5TkP2sv
      To: KT1H5ELRW3wmVMuZPJwL3DEUkCc5B6gH4M9H
      Entrypoint: transfer
      Parameter: (Pair "tz1gjaF81ZRRvdzjobyfVNsAeSC6PScjfQwN"
                       (Pair "tz1faswCTDciRzE4oJ9jn2Vm2dvjeyA9fUzU" 5))
      This transaction was successfully applied
      Updated storage:
        (Pair (Pair (Pair 0x000002298c03ed7d454a101eb7022bc95f7e5f41ac78 0)
                    (Pair 2 (Pair 50000 2628000)))
              (Pair (Pair 1 (Pair False 2)) (Pair 3 (Pair 10 4))))
      Updated big_maps:
        Unset map(3)[(Pair 0x0000e7670f32038107a59a2b9cfefae36ea21f5aa63c
              0xe6f1aa42d877954d34bbde9ca5bdd2676b139adb52ebc7b943fe8a07f55591e9)]
        Set map(0)[0x0000dac9f52543da1aed0bc1d6b46bf7c10db7014cd6] to (Pair {} 5)
        Set map(0)[0x0000e7670f32038107a59a2b9cfefae36ea21f5aa63c] to (Pair {} 5)
      Storage size: 14002 bytes
      Paid storage size diff: 3 bytes
      Consumed gas: 344718
      Balance updates:
        tz1b7tUupMgCNw2cCLpKTkSD1NZzB5TkP2sv ... -ꜩ0.003

The operation has only been included 0 blocks ago.
We recommend to wait more.
Use command
  tezos-client wait for onxpDWvgwrSGiGYq4WAYne25MHtJeCv9NXf3p3T5z9BfsP5c9WG to be included --confirmations 30 --branch BMR7g84ZngYqMjKjD56hRGbzMW47ePKAcEVBPXuFeoUv7fRdnxn
and/or an external block explorer.
```

# Misc notes/TODO

1. Not including all possible views in metadata json because it makes storage too large and max operation size gets exceeded.
2. A lot of code would be cut if I could call one sub_entry_point from another (specifically getEffectiveExpiry)
3. Question about TZIP-17 in general: Is it acceptable that permit can go from expired to unexpired? Namely, if a permit was expired due to user expiry being too low and then we increase user_expiry, functionally the permit's life gets extended? 

# Design choices

1. Batch delete permit entrypoint and permits/expiry info deleted when encountered as expired.
2. max_expiry is a storage variable to avoid contract locking (see tzip.md doc).
