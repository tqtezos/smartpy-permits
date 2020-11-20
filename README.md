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
  0001: { parameter
  0002:     (or (or (or (pair %approve (address %spender) (nat %value))
  0003:                 (or (pair %burn (address %address) (nat %value))
  0004:                     (list %delete_permits (pair address bytes))))
  0005:             (or (or (address %getAdministrator)
  0006:                     (pair %getAllowance
  0007:                        (pair %arg (address %owner) (address %spender))
  0008:                        (address %target)))
  0009:                 (or (pair %getBalance (address %arg) (address %target)) (address %getCounter))))
  0010:         (or (or (or (address %getDefaultExpiry) (address %getTotalSupply))
  0011:                 (or (pair %mint (address %address) (nat %value))
  0012:                     (list %permit (pair key (pair signature bytes)))))
  0013:             (or (or (address %setAdministrator)
  0014:                     (pair %setExpiry (address %address) (pair (option %permit bytes) (nat %seconds))))
  0015:                 (or (bool %setPause)
  0016:                     (pair %transfer (address %from_) (pair (address %to_) (nat %value))))))) ;
  0017:   storage
  0018:     (pair (pair (pair (address %administrator)
  0019:                       (big_map %balances address (pair (map %approvals address nat) (nat %balance))))
  0020:                 (pair (nat %counter) (pair (nat %default_expiry) (nat %max_expiry))))
  0021:           (pair (pair (big_map %metadata string bytes)
  0022:                       (pair (bool %paused) (big_map %permit_expiries (pair address bytes) (option nat))))
  0023:                 (pair (big_map %permits (pair address bytes) timestamp)
  0024:                       (pair (nat %totalSupply) (big_map %user_expiries address (option nat)))))) ;
  0025:   code { LAMBDA
  0026:            (pair (pair %in_param address bytes)
  0027:                  (pair %in_storage
  0028:                     (pair (pair (address %administrator)
  0029:                                 (big_map %balances address (pair (map %approvals address nat) (nat %balance))))
  0030:                           (pair (nat %counter) (pair (nat %default_expiry) (nat %max_expiry))))
  0031:                     (pair (pair (big_map %metadata string bytes)
  0032:                                 (pair (bool %paused) (big_map %permit_expiries (pair address bytes) (option nat))))
  0033:                           (pair (big_map %permits (pair address bytes) timestamp)
  0034:                                 (pair (nat %totalSupply) (big_map %user_expiries address (option nat)))))))
  0035:            (pair (list %operations operation)
  0036:                  (pair (nat %result)
  0037:                        (pair %storage
  0038:                           (pair (pair (address %administrator)
  0039:                                       (big_map %balances address (pair (map %approvals address nat) (nat %balance))))
  0040:                                 (pair (nat %counter) (pair (nat %default_expiry) (nat %max_expiry))))
  0041:                           (pair (pair (big_map %metadata string bytes)
  0042:                                       (pair (bool %paused) (big_map %permit_expiries (pair address bytes) (option nat))))
  0043:                                 (pair (big_map %permits (pair address bytes) timestamp)
  0044:                                       (pair (nat %totalSupply) (big_map %user_expiries address (option nat))))))))
  0045:            { NIL operation ;
  0046:              SWAP ;
  0047:              DUP ;
  0048:              DUG 2 ;
  0049:              CDR ;
  0050:              DUP ;
  0051:              CDADDR ;
  0052:              DIG 3 ;
  0053:              DUP ;
  0054:              DUG 4 ;
  0055:              CAR ;
  0056:              MEM ;
  0057:              IF { DUP ;
  0058:                   CDADDR ;
  0059:                   DIG 3 ;
  0060:                   DUP ;
  0061:                   DUG 4 ;
  0062:                   CAR ;
  0063:                   GET ;
  0064:                   IF_SOME {} { PUSH int 114 ; FAILWITH } ;
  0065:                   IF_SOME { DROP ; PUSH bool True } { PUSH bool False } }
  0066:                 { PUSH bool False } ;
  0067:              IF { DUP ;
  0068:                   CDADDR ;
  0069:                   DIG 3 ;
  0070:                   CAR ;
  0071:                   GET ;
  0072:                   IF_SOME {} { PUSH int 115 ; FAILWITH } ;
  0073:                   IF_SOME {} { PUSH int 115 ; FAILWITH } }
  0074:                 { DUP ;
  0075:                   CDDDDR ;
  0076:                   DIG 3 ;
  0077:                   DUP ;
  0078:                   DUG 4 ;
  0079:                   CAAR ;
  0080:                   MEM ;
  0081:                   IF { DUP ;
  0082:                        CDDDDR ;
  0083:                        DIG 3 ;
  0084:                        DUP ;
  0085:                        DUG 4 ;
  0086:                        CAAR ;
  0087:                        GET ;
  0088:                        IF_SOME {} { PUSH int 118 ; FAILWITH } ;
  0089:                        IF_SOME { DROP ; PUSH bool True } { PUSH bool False } }
  0090:                      { PUSH bool False } ;
  0091:                   IF { DUP ;
  0092:                        CDDDDR ;
  0093:                        DIG 3 ;
  0094:                        CAAR ;
  0095:                        GET ;
  0096:                        IF_SOME {} { PUSH int 119 ; FAILWITH } ;
  0097:                        IF_SOME {} { PUSH int 119 ; FAILWITH } }
  0098:                      { DIG 2 ; DROP ; DUP ; CADDAR } } ;
  0099:              PAIR %result %storage ;
  0100:              SWAP ;
  0101:              PAIR %operations } ;
  0102:          SWAP ;
  0103:          LAMBDA
  0104:            (pair (pair %in_param (address %from_) (pair (address %to_) (nat %value)))
  0105:                  (pair %in_storage
  0106:                     (pair (pair (address %administrator)
  0107:                                 (big_map %balances address (pair (map %approvals address nat) (nat %balance))))
  0108:                           (pair (nat %counter) (pair (nat %default_expiry) (nat %max_expiry))))
  0109:                     (pair (pair (big_map %metadata string bytes)
  0110:                                 (pair (bool %paused) (big_map %permit_expiries (pair address bytes) (option nat))))
  0111:                           (pair (big_map %permits (pair address bytes) timestamp)
  0112:                                 (pair (nat %totalSupply) (big_map %user_expiries address (option nat)))))))
  0113:            (pair (list %operations operation)
  0114:                  (pair (bool %result)
  0115:                        (pair %storage
  0116:                           (pair (pair (address %administrator)
  0117:                                       (big_map %balances address (pair (map %approvals address nat) (nat %balance))))
  0118:                                 (pair (nat %counter) (pair (nat %default_expiry) (nat %max_expiry))))
  0119:                           (pair (pair (big_map %metadata string bytes)
  0120:                                       (pair (bool %paused) (big_map %permit_expiries (pair address bytes) (option nat))))
  0121:                                 (pair (big_map %permits (pair address bytes) timestamp)
  0122:                                       (pair (nat %totalSupply) (big_map %user_expiries address (option nat))))))))
  0123:            { NIL operation ;
  0124:              SWAP ;
  0125:              DUP ;
  0126:              DUG 2 ;
  0127:              CDR ;
  0128:              DUP ;
  0129:              CDDAR ;
  0130:              DIG 3 ;
  0131:              DUP ;
  0132:              DUG 4 ;
  0133:              CAR ;
  0134:              PACK ;
  0135:              BLAKE2B ;
  0136:              DIG 4 ;
  0137:              DUP ;
  0138:              DUG 5 ;
  0139:              CAAR ;
  0140:              PAIR ;
  0141:              MEM ;
  0142:              IF { DUP ;
  0143:                   CDADDR ;
  0144:                   DIG 3 ;
  0145:                   DUP ;
  0146:                   DUG 4 ;
  0147:                   CAR ;
  0148:                   PACK ;
  0149:                   BLAKE2B ;
  0150:                   DIG 4 ;
  0151:                   DUP ;
  0152:                   DUG 5 ;
  0153:                   CAAR ;
  0154:                   PAIR ;
  0155:                   MEM ;
  0156:                   IF { DUP ;
  0157:                        CDADDR ;
  0158:                        DIG 3 ;
  0159:                        DUP ;
  0160:                        DUG 4 ;
  0161:                        CAR ;
  0162:                        PACK ;
  0163:                        BLAKE2B ;
  0164:                        DIG 4 ;
  0165:                        DUP ;
  0166:                        DUG 5 ;
  0167:                        CAAR ;
  0168:                        PAIR ;
  0169:                        GET ;
  0170:                        IF_SOME {} { PUSH int 67 ; FAILWITH } ;
  0171:                        IF_SOME { DROP ; PUSH bool True } { PUSH bool False } }
  0172:                      { PUSH bool False } ;
  0173:                   IF { DUP ;
  0174:                        CDADDR ;
  0175:                        DIG 3 ;
  0176:                        DUP ;
  0177:                        DUG 4 ;
  0178:                        CAR ;
  0179:                        PACK ;
  0180:                        BLAKE2B ;
  0181:                        DIG 4 ;
  0182:                        DUP ;
  0183:                        DUG 5 ;
  0184:                        CAAR ;
  0185:                        PAIR ;
  0186:                        GET ;
  0187:                        IF_SOME {} { PUSH int 68 ; FAILWITH } ;
  0188:                        IF_SOME {} { PUSH int 68 ; FAILWITH } }
  0189:                      { DUP ;
  0190:                        CDDDDR ;
  0191:                        DIG 3 ;
  0192:                        DUP ;
  0193:                        DUG 4 ;
  0194:                        CAAR ;
  0195:                        MEM ;
  0196:                        IF { DUP ;
  0197:                             CDDDDR ;
  0198:                             DIG 3 ;
  0199:                             DUP ;
  0200:                             DUG 4 ;
  0201:                             CAAR ;
  0202:                             GET ;
  0203:                             IF_SOME {} { PUSH int 70 ; FAILWITH } ;
  0204:                             IF_SOME { DROP ; PUSH bool True } { PUSH bool False } }
  0205:                           { PUSH bool False } ;
  0206:                        IF { DUP ;
  0207:                             CDDDDR ;
  0208:                             DIG 3 ;
  0209:                             DUP ;
  0210:                             DUG 4 ;
  0211:                             CAAR ;
  0212:                             GET ;
  0213:                             IF_SOME {} { PUSH int 71 ; FAILWITH } ;
  0214:                             IF_SOME {} { PUSH int 71 ; FAILWITH } }
  0215:                           { DUP ; CADDAR } } ;
  0216:                   SWAP ;
  0217:                   DUP ;
  0218:                   DUG 2 ;
  0219:                   CDDAR ;
  0220:                   DIG 4 ;
  0221:                   DUP ;
  0222:                   DUG 5 ;
  0223:                   CAR ;
  0224:                   PACK ;
  0225:                   BLAKE2B ;
  0226:                   DIG 5 ;
  0227:                   DUP ;
  0228:                   DUG 6 ;
  0229:                   CAAR ;
  0230:                   PAIR ;
  0231:                   GET ;
  0232:                   IF_SOME {} { PUSH int 66 ; FAILWITH } ;
  0233:                   NOW ;
  0234:                   SUB ;
  0235:                   ISNAT ;
  0236:                   IF_SOME {} { PUSH int 76 ; FAILWITH } ;
  0237:                   COMPARE ;
  0238:                   GE ;
  0239:                   IF { DUP ;
  0240:                        CDDAR ;
  0241:                        DIG 3 ;
  0242:                        DUP ;
  0243:                        DUG 4 ;
  0244:                        CAR ;
  0245:                        PACK ;
  0246:                        BLAKE2B ;
  0247:                        DIG 4 ;
  0248:                        DUP ;
  0249:                        DUG 5 ;
  0250:                        CAAR ;
  0251:                        PAIR ;
  0252:                        MEM ;
  0253:                        IF { DUP ;
  0254:                             CAR ;
  0255:                             SWAP ;
  0256:                             CDR ;
  0257:                             DUP ;
  0258:                             CAR ;
  0259:                             SWAP ;
  0260:                             CDR ;
  0261:                             DUP ;
  0262:                             CDR ;
  0263:                             SWAP ;
  0264:                             CAR ;
  0265:                             NONE timestamp ;
  0266:                             DIG 6 ;
  0267:                             DUP ;
  0268:                             DUG 7 ;
  0269:                             CAR ;
  0270:                             PACK ;
  0271:                             BLAKE2B ;
  0272:                             DIG 7 ;
  0273:                             DUP ;
  0274:                             DUG 8 ;
  0275:                             CAAR ;
  0276:                             PAIR ;
  0277:                             UPDATE ;
  0278:                             PAIR ;
  0279:                             SWAP ;
  0280:                             PAIR ;
  0281:                             SWAP ;
  0282:                             PAIR }
  0283:                           {} ;
  0284:                        DUP ;
  0285:                        CDADDR ;
  0286:                        DIG 3 ;
  0287:                        DUP ;
  0288:                        DUG 4 ;
  0289:                        CAR ;
  0290:                        PACK ;
  0291:                        BLAKE2B ;
  0292:                        DIG 4 ;
  0293:                        DUP ;
  0294:                        DUG 5 ;
  0295:                        CAAR ;
  0296:                        PAIR ;
  0297:                        MEM ;
  0298:                        IF { DUP ;
  0299:                             CAR ;
  0300:                             SWAP ;
  0301:                             CDR ;
  0302:                             DUP ;
  0303:                             CDR ;
  0304:                             SWAP ;
  0305:                             CAR ;
  0306:                             DUP ;
  0307:                             CAR ;
  0308:                             SWAP ;
  0309:                             CDR ;
  0310:                             DUP ;
  0311:                             CAR ;
  0312:                             SWAP ;
  0313:                             CDR ;
  0314:                             NONE (option nat) ;
  0315:                             DIG 7 ;
  0316:                             DUP ;
  0317:                             DUG 8 ;
  0318:                             CAR ;
  0319:                             PACK ;
  0320:                             BLAKE2B ;
  0321:                             DIG 8 ;
  0322:                             CAAR ;
  0323:                             PAIR ;
  0324:                             UPDATE ;
  0325:                             SWAP ;
  0326:                             PAIR ;
  0327:                             SWAP ;
  0328:                             PAIR ;
  0329:                             PAIR ;
  0330:                             SWAP ;
  0331:                             PAIR }
  0332:                           { DIG 2 ; DROP } ;
  0333:                        PUSH bool False }
  0334:                      { DUP ;
  0335:                        CDDAR ;
  0336:                        DIG 3 ;
  0337:                        DUP ;
  0338:                        DUG 4 ;
  0339:                        CAR ;
  0340:                        PACK ;
  0341:                        BLAKE2B ;
  0342:                        DIG 4 ;
  0343:                        DUP ;
  0344:                        DUG 5 ;
  0345:                        CAAR ;
  0346:                        PAIR ;
  0347:                        MEM ;
  0348:                        IF { DUP ;
  0349:                             CAR ;
  0350:                             SWAP ;
  0351:                             CDR ;
  0352:                             DUP ;
  0353:                             CAR ;
  0354:                             SWAP ;
  0355:                             CDR ;
  0356:                             DUP ;
  0357:                             CDR ;
  0358:                             SWAP ;
  0359:                             CAR ;
  0360:                             NONE timestamp ;
  0361:                             DIG 6 ;
  0362:                             DUP ;
  0363:                             DUG 7 ;
  0364:                             CAR ;
  0365:                             PACK ;
  0366:                             BLAKE2B ;
  0367:                             DIG 7 ;
  0368:                             DUP ;
  0369:                             DUG 8 ;
  0370:                             CAAR ;
  0371:                             PAIR ;
  0372:                             UPDATE ;
  0373:                             PAIR ;
  0374:                             SWAP ;
  0375:                             PAIR ;
  0376:                             SWAP ;
  0377:                             PAIR }
  0378:                           {} ;
  0379:                        DUP ;
  0380:                        CDADDR ;
  0381:                        DIG 3 ;
  0382:                        DUP ;
  0383:                        DUG 4 ;
  0384:                        CAR ;
  0385:                        PACK ;
  0386:                        BLAKE2B ;
  0387:                        DIG 4 ;
  0388:                        DUP ;
  0389:                        DUG 5 ;
  0390:                        CAAR ;
  0391:                        PAIR ;
  0392:                        MEM ;
  0393:                        IF { DUP ;
  0394:                             CAR ;
  0395:                             SWAP ;
  0396:                             CDR ;
  0397:                             DUP ;
  0398:                             CDR ;
  0399:                             SWAP ;
  0400:                             CAR ;
  0401:                             DUP ;
  0402:                             CAR ;
  0403:                             SWAP ;
  0404:                             CDR ;
  0405:                             DUP ;
  0406:                             CAR ;
  0407:                             SWAP ;
  0408:                             CDR ;
  0409:                             NONE (option nat) ;
  0410:                             DIG 7 ;
  0411:                             DUP ;
  0412:                             DUG 8 ;
  0413:                             CAR ;
  0414:                             PACK ;
  0415:                             BLAKE2B ;
  0416:                             DIG 8 ;
  0417:                             CAAR ;
  0418:                             PAIR ;
  0419:                             UPDATE ;
  0420:                             SWAP ;
  0421:                             PAIR ;
  0422:                             SWAP ;
  0423:                             PAIR ;
  0424:                             PAIR ;
  0425:                             SWAP ;
  0426:                             PAIR }
  0427:                           { DIG 2 ; DROP } ;
  0428:                        PUSH bool True } }
  0429:                 { DIG 2 ; DROP ; PUSH bool False } ;
  0430:              PAIR %result %storage ;
  0431:              SWAP ;
  0432:              PAIR %operations } ;
  0433:          SWAP ;
  0434:          DUP ;
  0435:          CDR ;
  0436:          SWAP ;
  0437:          CAR ;
  0438:          IF_LEFT
  0439:            { IF_LEFT
  0440:                { IF_LEFT
  0441:                    { SWAP ;
  0442:                      DUP ;
  0443:                      DUG 2 ;
  0444:                      CDADAR ;
  0445:                      IF { PUSH string "WrongCondition: ~ self.data.paused" ; FAILWITH } {} ;
  0446:                      PUSH nat 0 ;
  0447:                      DIG 2 ;
  0448:                      DUP ;
  0449:                      DUG 3 ;
  0450:                      CAADR ;
  0451:                      SENDER ;
  0452:                      GET ;
  0453:                      IF_SOME {} { PUSH int 162 ; FAILWITH } ;
  0454:                      CAR ;
  0455:                      DIG 2 ;
  0456:                      DUP ;
  0457:                      DUG 3 ;
  0458:                      CAR ;
  0459:                      GET ;
  0460:                      IF_SOME {} { PUSH nat 0 } ;
  0461:                      COMPARE ;
  0462:                      EQ ;
  0463:                      IF { PUSH bool True } { DUP ; CDR ; PUSH nat 0 ; COMPARE ; EQ } ;
  0464:                      IF { DIG 2 ; DROP ; DIG 2 ; DROP }
  0465:                         { PUSH string "UnsafeAllowanceChange" ; FAILWITH } ;
  0466:                      SWAP ;
  0467:                      DUP ;
  0468:                      CDR ;
  0469:                      SWAP ;
  0470:                      CAR ;
  0471:                      DUP ;
  0472:                      CDR ;
  0473:                      SWAP ;
  0474:                      CAR ;
  0475:                      DUP ;
  0476:                      CAR ;
  0477:                      SWAP ;
  0478:                      CDR ;
  0479:                      DUP ;
  0480:                      SENDER ;
  0481:                      DUP ;
  0482:                      DUG 2 ;
  0483:                      GET ;
  0484:                      IF_SOME {} { PUSH int 166 ; FAILWITH } ;
  0485:                      DUP ;
  0486:                      CDR ;
  0487:                      SWAP ;
  0488:                      CAR ;
  0489:                      DIG 7 ;
  0490:                      DUP ;
  0491:                      CAR ;
  0492:                      SWAP ;
  0493:                      CDR ;
  0494:                      SOME ;
  0495:                      SWAP ;
  0496:                      UPDATE ;
  0497:                      PAIR ;
  0498:                      SOME ;
  0499:                      SWAP ;
  0500:                      UPDATE ;
  0501:                      SWAP ;
  0502:                      PAIR ;
  0503:                      PAIR ;
  0504:                      PAIR ;
  0505:                      NIL operation }
  0506:                    { IF_LEFT
  0507:                        { SWAP ;
  0508:                          DUP ;
  0509:                          DUG 2 ;
  0510:                          CAAAR ;
  0511:                          SENDER ;
  0512:                          COMPARE ;
  0513:                          EQ ;
  0514:                          IF {}
  0515:                             { PUSH string "WrongCondition: sp.sender == self.data.administrator" ;
  0516:                               FAILWITH } ;
  0517:                          DUP ;
  0518:                          CDR ;
  0519:                          DIG 2 ;
  0520:                          DUP ;
  0521:                          DUG 3 ;
  0522:                          CAADR ;
  0523:                          DIG 2 ;
  0524:                          DUP ;
  0525:                          DUG 3 ;
  0526:                          CAR ;
  0527:                          GET ;
  0528:                          IF_SOME {} { PUSH int 192 ; FAILWITH } ;
  0529:                          CDR ;
  0530:                          COMPARE ;
  0531:                          GE ;
  0532:                          IF { DIG 2 ; DROP ; DIG 2 ; DROP }
  0533:                             { PUSH string
  0534:                                    "WrongCondition: self.data.balances[params.address].balance >= params.value" ;
  0535:                               FAILWITH } ;
  0536:                          SWAP ;
  0537:                          DUP ;
  0538:                          DUG 2 ;
  0539:                          DUP ;
  0540:                          CDR ;
  0541:                          SWAP ;
  0542:                          CAR ;
  0543:                          DUP ;
  0544:                          CDR ;
  0545:                          SWAP ;
  0546:                          CAR ;
  0547:                          DUP ;
  0548:                          CAR ;
  0549:                          SWAP ;
  0550:                          CDR ;
  0551:                          DUP ;
  0552:                          DIG 5 ;
  0553:                          DUP ;
  0554:                          DUG 6 ;
  0555:                          CAR ;
  0556:                          DUP ;
  0557:                          DUG 2 ;
  0558:                          GET ;
  0559:                          IF_SOME {} { PUSH int 193 ; FAILWITH } ;
  0560:                          CAR ;
  0561:                          DIG 6 ;
  0562:                          DUP ;
  0563:                          DUG 7 ;
  0564:                          CDR ;
  0565:                          DIG 8 ;
  0566:                          CAADR ;
  0567:                          DIG 8 ;
  0568:                          DUP ;
  0569:                          DUG 9 ;
  0570:                          CAR ;
  0571:                          GET ;
  0572:                          IF_SOME {} { PUSH int 194 ; FAILWITH } ;
  0573:                          CDR ;
  0574:                          SUB ;
  0575:                          ISNAT ;
  0576:                          IF_SOME {} { PUSH int 193 ; FAILWITH } ;
  0577:                          SWAP ;
  0578:                          PAIR ;
  0579:                          SOME ;
  0580:                          SWAP ;
  0581:                          UPDATE ;
  0582:                          SWAP ;
  0583:                          PAIR ;
  0584:                          PAIR ;
  0585:                          PAIR ;
  0586:                          DUP ;
  0587:                          DUG 2 ;
  0588:                          DUP ;
  0589:                          CAR ;
  0590:                          SWAP ;
  0591:                          CDR ;
  0592:                          DUP ;
  0593:                          CAR ;
  0594:                          SWAP ;
  0595:                          CDR ;
  0596:                          DUP ;
  0597:                          CAR ;
  0598:                          SWAP ;
  0599:                          CDDR ;
  0600:                          DIG 4 ;
  0601:                          CDR ;
  0602:                          DIG 5 ;
  0603:                          CDDDAR ;
  0604:                          SUB ;
  0605:                          ISNAT ;
  0606:                          IF_SOME {} { PUSH int 195 ; FAILWITH } ;
  0607:                          PAIR ;
  0608:                          SWAP ;
  0609:                          PAIR ;
  0610:                          SWAP ;
  0611:                          PAIR ;
  0612:                          SWAP ;
  0613:                          PAIR ;
  0614:                          NIL operation }
  0615:                        { PUSH int 0 ;
  0616:                          NIL operation ;
  0617:                          DIG 2 ;
  0618:                          DUP ;
  0619:                          DUG 3 ;
  0620:                          ITER { DIG 4 ;
  0621:                                 DUP ;
  0622:                                 DUG 5 ;
  0623:                                 CDDAR ;
  0624:                                 SWAP ;
  0625:                                 DUP ;
  0626:                                 DUG 2 ;
  0627:                                 MEM ;
  0628:                                 IF {} { DUP ; PUSH string "NO_PERMIT_TO_DELETE" ; PAIR ; FAILWITH } ;
  0629:                                 DIG 6 ;
  0630:                                 DUP ;
  0631:                                 DUG 7 ;
  0632:                                 DIG 5 ;
  0633:                                 DIG 2 ;
  0634:                                 DUP ;
  0635:                                 DUG 3 ;
  0636:                                 PAIR %in_param %in_storage ;
  0637:                                 EXEC ;
  0638:                                 DUP ;
  0639:                                 CDDR ;
  0640:                                 DUG 5 ;
  0641:                                 DUP ;
  0642:                                 CAR ;
  0643:                                 ITER { DIG 3 ; SWAP ; CONS ; DUG 2 } ;
  0644:                                 DUP ;
  0645:                                 CDAR ;
  0646:                                 DIG 6 ;
  0647:                                 DUP ;
  0648:                                 DUG 7 ;
  0649:                                 CDDAR ;
  0650:                                 DIG 3 ;
  0651:                                 DUP ;
  0652:                                 DUG 4 ;
  0653:                                 GET ;
  0654:                                 IF_SOME {} { PUSH int 45 ; FAILWITH } ;
  0655:                                 NOW ;
  0656:                                 SUB ;
  0657:                                 ISNAT ;
  0658:                                 IF_SOME {} { PUSH int 46 ; FAILWITH } ;
  0659:                                 COMPARE ;
  0660:                                 GE ;
  0661:                                 IF { DROP }
  0662:                                    { SWAP ; DUP ; DUG 2 ; PUSH string "PERMIT_NOT_EXPIRED" ; PAIR ; FAILWITH } ;
  0663:                                 DIG 4 ;
  0664:                                 DUP ;
  0665:                                 DUG 5 ;
  0666:                                 CDDAR ;
  0667:                                 SWAP ;
  0668:                                 DUP ;
  0669:                                 DUG 2 ;
  0670:                                 MEM ;
  0671:                                 IF { DIG 4 ;
  0672:                                      DUP ;
  0673:                                      CAR ;
  0674:                                      SWAP ;
  0675:                                      CDR ;
  0676:                                      DUP ;
  0677:                                      CAR ;
  0678:                                      SWAP ;
  0679:                                      CDR ;
  0680:                                      DUP ;
  0681:                                      CDR ;
  0682:                                      SWAP ;
  0683:                                      CAR ;
  0684:                                      NONE timestamp ;
  0685:                                      DIG 5 ;
  0686:                                      DUP ;
  0687:                                      DUG 6 ;
  0688:                                      UPDATE ;
  0689:                                      PAIR ;
  0690:                                      SWAP ;
  0691:                                      PAIR ;
  0692:                                      SWAP ;
  0693:                                      PAIR ;
  0694:                                      DUG 4 }
  0695:                                    {} ;
  0696:                                 DIG 4 ;
  0697:                                 DUP ;
  0698:                                 DUG 5 ;
  0699:                                 CDADDR ;
  0700:                                 SWAP ;
  0701:                                 DUP ;
  0702:                                 DUG 2 ;
  0703:                                 MEM ;
  0704:                                 IF { DIG 4 ;
  0705:                                      DUP ;
  0706:                                      CAR ;
  0707:                                      SWAP ;
  0708:                                      CDR ;
  0709:                                      DUP ;
  0710:                                      CDR ;
  0711:                                      SWAP ;
  0712:                                      CAR ;
  0713:                                      DUP ;
  0714:                                      CAR ;
  0715:                                      SWAP ;
  0716:                                      CDR ;
  0717:                                      DUP ;
  0718:                                      CAR ;
  0719:                                      SWAP ;
  0720:                                      CDR ;
  0721:                                      NONE (option nat) ;
  0722:                                      DIG 6 ;
  0723:                                      UPDATE ;
  0724:                                      SWAP ;
  0725:                                      PAIR ;
  0726:                                      SWAP ;
  0727:                                      PAIR ;
  0728:                                      PAIR ;
  0729:                                      SWAP ;
  0730:                                      PAIR ;
  0731:                                      DUG 3 }
  0732:                                    { DROP } } ;
  0733:                          SWAP ;
  0734:                          DROP ;
  0735:                          SWAP ;
  0736:                          DROP ;
  0737:                          DIG 2 ;
  0738:                          DROP ;
  0739:                          DIG 2 ;
  0740:                          DROP } } }
  0741:                { IF_LEFT
  0742:                    { IF_LEFT
  0743:                        { DIG 2 ;
  0744:                          DROP ;
  0745:                          DIG 2 ;
  0746:                          DROP ;
  0747:                          CONTRACT address ;
  0748:                          NIL operation ;
  0749:                          SWAP ;
  0750:                          IF_SOME {} { PUSH int 219 ; FAILWITH } ;
  0751:                          PUSH mutez 0 ;
  0752:                          DIG 3 ;
  0753:                          DUP ;
  0754:                          DUG 4 ;
  0755:                          CAAAR ;
  0756:                          TRANSFER_TOKENS ;
  0757:                          CONS }
  0758:                        { DIG 2 ;
  0759:                          DROP ;
  0760:                          DIG 2 ;
  0761:                          DROP ;
  0762:                          DUP ;
  0763:                          CDR ;
  0764:                          CONTRACT nat ;
  0765:                          NIL operation ;
  0766:                          SWAP ;
  0767:                          IF_SOME {} { PUSH int 209 ; FAILWITH } ;
  0768:                          PUSH mutez 0 ;
  0769:                          DIG 4 ;
  0770:                          DUP ;
  0771:                          DUG 5 ;
  0772:                          CAADR ;
  0773:                          DIG 4 ;
  0774:                          DUP ;
  0775:                          DUG 5 ;
  0776:                          CAAR ;
  0777:                          GET ;
  0778:                          IF_SOME {} { PUSH int 208 ; FAILWITH } ;
  0779:                          CAR ;
  0780:                          DIG 4 ;
  0781:                          CADR ;
  0782:                          GET ;
  0783:                          IF_SOME {} { PUSH int 208 ; FAILWITH } ;
  0784:                          TRANSFER_TOKENS ;
  0785:                          CONS } }
  0786:                    { IF_LEFT
  0787:                        { DIG 2 ;
  0788:                          DROP ;
  0789:                          DIG 2 ;
  0790:                          DROP ;
  0791:                          DUP ;
  0792:                          CDR ;
  0793:                          CONTRACT nat ;
  0794:                          NIL operation ;
  0795:                          SWAP ;
  0796:                          IF_SOME {} { PUSH int 204 ; FAILWITH } ;
  0797:                          PUSH mutez 0 ;
  0798:                          DIG 4 ;
  0799:                          DUP ;
  0800:                          DUG 5 ;
  0801:                          CAADR ;
  0802:                          DIG 4 ;
  0803:                          CAR ;
  0804:                          GET ;
  0805:                          IF_SOME {} { PUSH int 203 ; FAILWITH } ;
  0806:                          CDR ;
  0807:                          TRANSFER_TOKENS ;
  0808:                          CONS }
  0809:                        { DIG 2 ;
  0810:                          DROP ;
  0811:                          DIG 2 ;
  0812:                          DROP ;
  0813:                          CONTRACT nat ;
  0814:                          NIL operation ;
  0815:                          SWAP ;
  0816:                          IF_SOME {} { PUSH int 223 ; FAILWITH } ;
  0817:                          PUSH mutez 0 ;
  0818:                          DIG 3 ;
  0819:                          DUP ;
  0820:                          DUG 4 ;
  0821:                          CADAR ;
  0822:                          TRANSFER_TOKENS ;
  0823:                          CONS } } } }
  0824:            { IF_LEFT
  0825:                { IF_LEFT
  0826:                    { IF_LEFT
  0827:                        { DIG 2 ;
  0828:                          DROP ;
  0829:                          DIG 2 ;
  0830:                          DROP ;
  0831:                          CONTRACT nat ;
  0832:                          NIL operation ;
  0833:                          SWAP ;
  0834:                          IF_SOME {} { PUSH int 229 ; FAILWITH } ;
  0835:                          PUSH mutez 0 ;
  0836:                          DIG 3 ;
  0837:                          DUP ;
  0838:                          DUG 4 ;
  0839:                          CADDAR ;
  0840:                          TRANSFER_TOKENS ;
  0841:                          CONS }
  0842:                        { DIG 2 ;
  0843:                          DROP ;
  0844:                          DIG 2 ;
  0845:                          DROP ;
  0846:                          CONTRACT nat ;
  0847:                          NIL operation ;
  0848:                          SWAP ;
  0849:                          IF_SOME {} { PUSH int 214 ; FAILWITH } ;
  0850:                          PUSH mutez 0 ;
  0851:                          DIG 3 ;
  0852:                          DUP ;
  0853:                          DUG 4 ;
  0854:                          CDDDAR ;
  0855:                          TRANSFER_TOKENS ;
  0856:                          CONS } }
  0857:                    { IF_LEFT
  0858:                        { SWAP ;
  0859:                          DUP ;
  0860:                          DUG 2 ;
  0861:                          CAAAR ;
  0862:                          SENDER ;
  0863:                          COMPARE ;
  0864:                          EQ ;
  0865:                          IF {}
  0866:                             { PUSH string "WrongCondition: sp.sender == self.data.administrator" ;
  0867:                               FAILWITH } ;
  0868:                          SWAP ;
  0869:                          DUP ;
  0870:                          DUG 2 ;
  0871:                          CAADR ;
  0872:                          SWAP ;
  0873:                          DUP ;
  0874:                          DUG 2 ;
  0875:                          CAR ;
  0876:                          MEM ;
  0877:                          IF { DIG 2 ; DROP ; DIG 2 ; DROP }
  0878:                             { DIG 2 ;
  0879:                               DROP ;
  0880:                               DIG 2 ;
  0881:                               DROP ;
  0882:                               SWAP ;
  0883:                               DUP ;
  0884:                               CDR ;
  0885:                               SWAP ;
  0886:                               CAR ;
  0887:                               DUP ;
  0888:                               CDR ;
  0889:                               SWAP ;
  0890:                               CAR ;
  0891:                               DUP ;
  0892:                               CAR ;
  0893:                               SWAP ;
  0894:                               CDR ;
  0895:                               DIG 4 ;
  0896:                               DUP ;
  0897:                               DUG 5 ;
  0898:                               CAR ;
  0899:                               PUSH (option (pair (map %approvals address nat) (nat %balance))) (Some (Pair {} 0)) ;
  0900:                               SWAP ;
  0901:                               UPDATE ;
  0902:                               SWAP ;
  0903:                               PAIR ;
  0904:                               PAIR ;
  0905:                               PAIR ;
  0906:                               SWAP } ;
  0907:                          SWAP ;
  0908:                          DUP ;
  0909:                          CDR ;
  0910:                          SWAP ;
  0911:                          CAR ;
  0912:                          DUP ;
  0913:                          CDR ;
  0914:                          SWAP ;
  0915:                          CAR ;
  0916:                          DUP ;
  0917:                          CAR ;
  0918:                          SWAP ;
  0919:                          CDR ;
  0920:                          DUP ;
  0921:                          DIG 5 ;
  0922:                          DUP ;
  0923:                          DUG 6 ;
  0924:                          CAR ;
  0925:                          DUP ;
  0926:                          DUG 2 ;
  0927:                          GET ;
  0928:                          IF_SOME {} { PUSH int 185 ; FAILWITH } ;
  0929:                          DUP ;
  0930:                          CAR ;
  0931:                          SWAP ;
  0932:                          CDR ;
  0933:                          DIG 7 ;
  0934:                          DUP ;
  0935:                          DUG 8 ;
  0936:                          CDR ;
  0937:                          ADD ;
  0938:                          SWAP ;
  0939:                          PAIR ;
  0940:                          SOME ;
  0941:                          SWAP ;
  0942:                          UPDATE ;
  0943:                          SWAP ;
  0944:                          PAIR ;
  0945:                          PAIR ;
  0946:                          PAIR ;
  0947:                          DUP ;
  0948:                          CAR ;
  0949:                          SWAP ;
  0950:                          CDR ;
  0951:                          DUP ;
  0952:                          CAR ;
  0953:                          SWAP ;
  0954:                          CDR ;
  0955:                          DUP ;
  0956:                          CAR ;
  0957:                          SWAP ;
  0958:                          CDR ;
  0959:                          DUP ;
  0960:                          CDR ;
  0961:                          SWAP ;
  0962:                          CAR ;
  0963:                          DIG 5 ;
  0964:                          CDR ;
  0965:                          ADD ;
  0966:                          PAIR ;
  0967:                          SWAP ;
  0968:                          PAIR ;
  0969:                          SWAP ;
  0970:                          PAIR ;
  0971:                          SWAP ;
  0972:                          PAIR ;
  0973:                          NIL operation }
  0974:                        { SWAP ;
  0975:                          DUP ;
  0976:                          DUG 2 ;
  0977:                          CDADAR ;
  0978:                          IF { PUSH string "WrongCondition: ~ self.data.paused" ; FAILWITH } {} ;
  0979:                          DUP ;
  0980:                          NIL operation ;
  0981:                          SWAP ;
  0982:                          ITER { DIG 5 ;
  0983:                                 DUP ;
  0984:                                 DUG 6 ;
  0985:                                 DIG 4 ;
  0986:                                 DIG 2 ;
  0987:                                 DUP ;
  0988:                                 CDDR ;
  0989:                                 SWAP ;
  0990:                                 DUP ;
  0991:                                 DUG 4 ;
  0992:                                 CAR ;
  0993:                                 HASH_KEY ;
  0994:                                 IMPLICIT_ACCOUNT ;
  0995:                                 ADDRESS ;
  0996:                                 PAIR ;
  0997:                                 PAIR %in_param %in_storage ;
  0998:                                 EXEC ;
  0999:                                 DUP ;
  1000:                                 CDDR ;
  1001:                                 DUG 4 ;
  1002:                                 DUP ;
  1003:                                 CAR ;
  1004:                                 ITER { DIG 3 ; SWAP ; CONS ; DUG 2 } ;
  1005:                                 DIG 4 ;
  1006:                                 DUP ;
  1007:                                 DUG 5 ;
  1008:                                 CDDAR ;
  1009:                                 DIG 2 ;
  1010:                                 DUP ;
  1011:                                 CDDR ;
  1012:                                 SWAP ;
  1013:                                 DUP ;
  1014:                                 DUG 4 ;
  1015:                                 CAR ;
  1016:                                 HASH_KEY ;
  1017:                                 IMPLICIT_ACCOUNT ;
  1018:                                 ADDRESS ;
  1019:                                 PAIR ;
  1020:                                 MEM ;
  1021:                                 IF { DUP ;
  1022:                                      CDAR ;
  1023:                                      DIG 5 ;
  1024:                                      DUP ;
  1025:                                      DUG 6 ;
  1026:                                      CDDAR ;
  1027:                                      DIG 3 ;
  1028:                                      DUP ;
  1029:                                      CDDR ;
  1030:                                      SWAP ;
  1031:                                      DUP ;
  1032:                                      DUG 5 ;
  1033:                                      CAR ;
  1034:                                      HASH_KEY ;
  1035:                                      IMPLICIT_ACCOUNT ;
  1036:                                      ADDRESS ;
  1037:                                      PAIR ;
  1038:                                      GET ;
  1039:                                      IF_SOME {} { PUSH int 102 ; FAILWITH } ;
  1040:                                      NOW ;
  1041:                                      SUB ;
  1042:                                      ISNAT ;
  1043:                                      IF_SOME {} { PUSH int 103 ; FAILWITH } ;
  1044:                                      COMPARE ;
  1045:                                      LT }
  1046:                                    { PUSH bool False } ;
  1047:                                 IF { SWAP ; DUP ; DUG 2 ; CDDR ; PUSH string "DUP_PERMIT" ; PAIR ; FAILWITH }
  1048:                                    {} ;
  1049:                                 SWAP ;
  1050:                                 DUP ;
  1051:                                 DUG 2 ;
  1052:                                 CDDR ;
  1053:                                 DIG 5 ;
  1054:                                 DUP ;
  1055:                                 DUG 6 ;
  1056:                                 CADAR ;
  1057:                                 PAIR ;
  1058:                                 SELF ;
  1059:                                 ADDRESS ;
  1060:                                 CHAIN_ID ;
  1061:                                 PAIR ;
  1062:                                 PAIR ;
  1063:                                 PACK ;
  1064:                                 DIG 2 ;
  1065:                                 DUP ;
  1066:                                 CDAR ;
  1067:                                 SWAP ;
  1068:                                 DUP ;
  1069:                                 DUG 4 ;
  1070:                                 CAR ;
  1071:                                 CHECK_SIGNATURE ;
  1072:                                 IF { DROP }
  1073:                                    { SWAP ;
  1074:                                      DUP ;
  1075:                                      DUG 2 ;
  1076:                                      CDDR ;
  1077:                                      DIG 5 ;
  1078:                                      DUP ;
  1079:                                      DUG 6 ;
  1080:                                      CADAR ;
  1081:                                      PAIR ;
  1082:                                      SELF ;
  1083:                                      ADDRESS ;
  1084:                                      CHAIN_ID ;
  1085:                                      PAIR ;
  1086:                                      PAIR ;
  1087:                                      PACK ;
  1088:                                      PUSH string "MISSIGNED" ;
  1089:                                      PAIR ;
  1090:                                      FAILWITH } ;
  1091:                                 DIG 3 ;
  1092:                                 DUP ;
  1093:                                 CAR ;
  1094:                                 SWAP ;
  1095:                                 CDR ;
  1096:                                 DUP ;
  1097:                                 CAR ;
  1098:                                 SWAP ;
  1099:                                 CDR ;
  1100:                                 DUP ;
  1101:                                 CDR ;
  1102:                                 SWAP ;
  1103:                                 CAR ;
  1104:                                 DIG 4 ;
  1105:                                 DUP ;
  1106:                                 CDDR ;
  1107:                                 SWAP ;
  1108:                                 CAR ;
  1109:                                 HASH_KEY ;
  1110:                                 IMPLICIT_ACCOUNT ;
  1111:                                 ADDRESS ;
  1112:                                 PAIR ;
  1113:                                 NOW ;
  1114:                                 SOME ;
  1115:                                 SWAP ;
  1116:                                 UPDATE ;
  1117:                                 PAIR ;
  1118:                                 SWAP ;
  1119:                                 PAIR ;
  1120:                                 SWAP ;
  1121:                                 PAIR ;
  1122:                                 DUP ;
  1123:                                 CDR ;
  1124:                                 SWAP ;
  1125:                                 CAR ;
  1126:                                 DUP ;
  1127:                                 CAR ;
  1128:                                 SWAP ;
  1129:                                 CDR ;
  1130:                                 DUP ;
  1131:                                 CDR ;
  1132:                                 SWAP ;
  1133:                                 CAR ;
  1134:                                 PUSH nat 1 ;
  1135:                                 ADD ;
  1136:                                 PAIR ;
  1137:                                 SWAP ;
  1138:                                 PAIR ;
  1139:                                 PAIR ;
  1140:                                 DUG 2 } ;
  1141:                          SWAP ;
  1142:                          DROP ;
  1143:                          DIG 2 ;
  1144:                          DROP ;
  1145:                          DIG 2 ;
  1146:                          DROP } } }
  1147:                { IF_LEFT
  1148:                    { IF_LEFT
  1149:                        { SWAP ;
  1150:                          DUP ;
  1151:                          DUG 2 ;
  1152:                          CAAAR ;
  1153:                          SENDER ;
  1154:                          COMPARE ;
  1155:                          EQ ;
  1156:                          IF { DIG 2 ; DROP ; DIG 2 ; DROP }
  1157:                             { PUSH string "WrongCondition: sp.sender == self.data.administrator" ;
  1158:                               FAILWITH } ;
  1159:                          SWAP ;
  1160:                          DUP ;
  1161:                          CDR ;
  1162:                          SWAP ;
  1163:                          CAR ;
  1164:                          DUP ;
  1165:                          CDR ;
  1166:                          SWAP ;
  1167:                          CADR ;
  1168:                          DIG 3 ;
  1169:                          PAIR ;
  1170:                          PAIR ;
  1171:                          PAIR }
  1172:                        { SWAP ;
  1173:                          DUP ;
  1174:                          DUG 2 ;
  1175:                          CDADAR ;
  1176:                          IF { PUSH string "WrongCondition: ~ self.data.paused" ; FAILWITH } {} ;
  1177:                          SWAP ;
  1178:                          DUP ;
  1179:                          DUG 2 ;
  1180:                          CADDDR ;
  1181:                          SWAP ;
  1182:                          DUP ;
  1183:                          DUG 2 ;
  1184:                          CDDR ;
  1185:                          COMPARE ;
  1186:                          LE ;
  1187:                          IF {} { PUSH string "MAX_SECONDS_EXCEEDED" ; FAILWITH } ;
  1188:                          SENDER ;
  1189:                          PACK ;
  1190:                          SWAP ;
  1191:                          DUP ;
  1192:                          DUG 2 ;
  1193:                          CAR ;
  1194:                          PACK ;
  1195:                          COMPARE ;
  1196:                          EQ ;
  1197:                          IF {} { PUSH bool False ; FAILWITH } ;
  1198:                          DUP ;
  1199:                          CDAR ;
  1200:                          IF_SOME
  1201:                            { DROP ;
  1202:                              SWAP ;
  1203:                              DUP ;
  1204:                              DUG 2 ;
  1205:                              CDDAR ;
  1206:                              SWAP ;
  1207:                              DUP ;
  1208:                              DUG 2 ;
  1209:                              CDAR ;
  1210:                              IF_SOME {} { PUSH int 132 ; FAILWITH } ;
  1211:                              DIG 2 ;
  1212:                              DUP ;
  1213:                              DUG 3 ;
  1214:                              CAR ;
  1215:                              PAIR ;
  1216:                              MEM ;
  1217:                              IF {} { PUSH string "PERMIT_NONEXISTENT" ; FAILWITH } ;
  1218:                              SWAP ;
  1219:                              DUP ;
  1220:                              DUG 2 ;
  1221:                              CDADDR ;
  1222:                              SWAP ;
  1223:                              DUP ;
  1224:                              DUG 2 ;
  1225:                              CDAR ;
  1226:                              IF_SOME {} { PUSH int 132 ; FAILWITH } ;
  1227:                              DIG 2 ;
  1228:                              DUP ;
  1229:                              DUG 3 ;
  1230:                              CAR ;
  1231:                              PAIR ;
  1232:                              MEM ;
  1233:                              IF { SWAP ;
  1234:                                   DUP ;
  1235:                                   DUG 2 ;
  1236:                                   CDADDR ;
  1237:                                   SWAP ;
  1238:                                   DUP ;
  1239:                                   DUG 2 ;
  1240:                                   CDAR ;
  1241:                                   IF_SOME {} { PUSH int 132 ; FAILWITH } ;
  1242:                                   DIG 2 ;
  1243:                                   DUP ;
  1244:                                   DUG 3 ;
  1245:                                   CAR ;
  1246:                                   PAIR ;
  1247:                                   GET ;
  1248:                                   IF_SOME {} { PUSH int 137 ; FAILWITH } ;
  1249:                                   IF_SOME { DROP ; PUSH bool True } { PUSH bool False } }
  1250:                                 { PUSH bool False } ;
  1251:                              IF { SWAP ;
  1252:                                   DUP ;
  1253:                                   DUG 2 ;
  1254:                                   CDADDR ;
  1255:                                   SWAP ;
  1256:                                   DUP ;
  1257:                                   DUG 2 ;
  1258:                                   CDAR ;
  1259:                                   IF_SOME {} { PUSH int 132 ; FAILWITH } ;
  1260:                                   DIG 2 ;
  1261:                                   DUP ;
  1262:                                   DUG 3 ;
  1263:                                   CAR ;
  1264:                                   PAIR ;
  1265:                                   GET ;
  1266:                                   IF_SOME {} { PUSH int 138 ; FAILWITH } ;
  1267:                                   IF_SOME {} { PUSH int 138 ; FAILWITH } ;
  1268:                                   DIG 2 ;
  1269:                                   DUP ;
  1270:                                   DUG 3 ;
  1271:                                   CDDAR ;
  1272:                                   DIG 2 ;
  1273:                                   DUP ;
  1274:                                   DUG 3 ;
  1275:                                   CDAR ;
  1276:                                   IF_SOME {} { PUSH int 132 ; FAILWITH } ;
  1277:                                   DIG 3 ;
  1278:                                   DUP ;
  1279:                                   DUG 4 ;
  1280:                                   CAR ;
  1281:                                   PAIR ;
  1282:                                   GET ;
  1283:                                   IF_SOME {} { PUSH int 135 ; FAILWITH } ;
  1284:                                   NOW ;
  1285:                                   SUB ;
  1286:                                   ISNAT ;
  1287:                                   IF_SOME {} { PUSH int 140 ; FAILWITH } ;
  1288:                                   COMPARE ;
  1289:                                   LT ;
  1290:                                   IF { DIG 2 ; DROP ; DIG 2 ; DROP }
  1291:                                      { PUSH string "PERMIT_REVOKED" ; FAILWITH } }
  1292:                                 { SWAP ;
  1293:                                   DUP ;
  1294:                                   DUG 2 ;
  1295:                                   CDDDDR ;
  1296:                                   SWAP ;
  1297:                                   DUP ;
  1298:                                   DUG 2 ;
  1299:                                   CAR ;
  1300:                                   MEM ;
  1301:                                   IF { SWAP ;
  1302:                                        DUP ;
  1303:                                        DUG 2 ;
  1304:                                        CDDDDR ;
  1305:                                        SWAP ;
  1306:                                        DUP ;
  1307:                                        DUG 2 ;
  1308:                                        CAR ;
  1309:                                        GET ;
  1310:                                        IF_SOME {} { PUSH int 143 ; FAILWITH } ;
  1311:                                        IF_SOME { DROP ; PUSH bool True } { PUSH bool False } }
  1312:                                      { PUSH bool False } ;
  1313:                                   IF { SWAP ;
  1314:                                        DUP ;
  1315:                                        DUG 2 ;
  1316:                                        CDDDDR ;
  1317:                                        SWAP ;
  1318:                                        DUP ;
  1319:                                        DUG 2 ;
  1320:                                        CAR ;
  1321:                                        GET ;
  1322:                                        IF_SOME {} { PUSH int 144 ; FAILWITH } ;
  1323:                                        IF_SOME {} { PUSH int 144 ; FAILWITH } ;
  1324:                                        DIG 2 ;
  1325:                                        DUP ;
  1326:                                        DUG 3 ;
  1327:                                        CDDAR ;
  1328:                                        DIG 2 ;
  1329:                                        DUP ;
  1330:                                        DUG 3 ;
  1331:                                        CDAR ;
  1332:                                        IF_SOME {} { PUSH int 132 ; FAILWITH } ;
  1333:                                        DIG 3 ;
  1334:                                        DUP ;
  1335:                                        DUG 4 ;
  1336:                                        CAR ;
  1337:                                        PAIR ;
  1338:                                        GET ;
  1339:                                        IF_SOME {} { PUSH int 135 ; FAILWITH } ;
  1340:                                        NOW ;
  1341:                                        SUB ;
  1342:                                        ISNAT ;
  1343:                                        IF_SOME {} { PUSH int 146 ; FAILWITH } ;
  1344:                                        COMPARE ;
  1345:                                        LT ;
  1346:                                        IF { DIG 2 ; DROP ; DIG 2 ; DROP }
  1347:                                           { PUSH string "PERMIT_REVOKED" ; FAILWITH } }
  1348:                                      { SWAP ;
  1349:                                        DUP ;
  1350:                                        CADDAR ;
  1351:                                        SWAP ;
  1352:                                        DUP ;
  1353:                                        DUG 3 ;
  1354:                                        CDDAR ;
  1355:                                        DIG 2 ;
  1356:                                        DUP ;
  1357:                                        DUG 3 ;
  1358:                                        CDAR ;
  1359:                                        IF_SOME {} { PUSH int 132 ; FAILWITH } ;
  1360:                                        DIG 3 ;
  1361:                                        DUP ;
  1362:                                        DUG 4 ;
  1363:                                        CAR ;
  1364:                                        PAIR ;
  1365:                                        GET ;
  1366:                                        IF_SOME {} { PUSH int 135 ; FAILWITH } ;
  1367:                                        NOW ;
  1368:                                        SUB ;
  1369:                                        ISNAT ;
  1370:                                        IF_SOME {} { PUSH int 149 ; FAILWITH } ;
  1371:                                        COMPARE ;
  1372:                                        LT ;
  1373:                                        IF { DIG 2 ; DROP ; DIG 2 ; DROP }
  1374:                                           { PUSH string "PERMIT_REVOKED" ; FAILWITH } } } ;
  1375:                              SWAP ;
  1376:                              DUP ;
  1377:                              CAR ;
  1378:                              SWAP ;
  1379:                              CDR ;
  1380:                              DUP ;
  1381:                              CDR ;
  1382:                              SWAP ;
  1383:                              CAR ;
  1384:                              DUP ;
  1385:                              CAR ;
  1386:                              SWAP ;
  1387:                              CDR ;
  1388:                              DUP ;
  1389:                              CAR ;
  1390:                              SWAP ;
  1391:                              CDR ;
  1392:                              DIG 5 ;
  1393:                              DUP ;
  1394:                              DUG 6 ;
  1395:                              CDAR ;
  1396:                              IF_SOME {} { PUSH int 132 ; FAILWITH } ;
  1397:                              DIG 6 ;
  1398:                              DUP ;
  1399:                              DUG 7 ;
  1400:                              CAR ;
  1401:                              PAIR ;
  1402:                              DIG 6 ;
  1403:                              CDDR ;
  1404:                              SOME ;
  1405:                              SOME ;
  1406:                              SWAP ;
  1407:                              UPDATE ;
  1408:                              SWAP ;
  1409:                              PAIR ;
  1410:                              SWAP ;
  1411:                              PAIR ;
  1412:                              PAIR ;
  1413:                              SWAP ;
  1414:                              PAIR }
  1415:                            { DIG 2 ;
  1416:                              DROP ;
  1417:                              DIG 2 ;
  1418:                              DROP ;
  1419:                              SWAP ;
  1420:                              DUP ;
  1421:                              CAR ;
  1422:                              SWAP ;
  1423:                              CDR ;
  1424:                              DUP ;
  1425:                              CAR ;
  1426:                              SWAP ;
  1427:                              CDR ;
  1428:                              DUP ;
  1429:                              CAR ;
  1430:                              SWAP ;
  1431:                              CDR ;
  1432:                              DUP ;
  1433:                              CAR ;
  1434:                              SWAP ;
  1435:                              CDR ;
  1436:                              DIG 5 ;
  1437:                              DUP ;
  1438:                              CAR ;
  1439:                              SWAP ;
  1440:                              CDDR ;
  1441:                              SOME ;
  1442:                              SOME ;
  1443:                              SWAP ;
  1444:                              UPDATE ;
  1445:                              SWAP ;
  1446:                              PAIR ;
  1447:                              SWAP ;
  1448:                              PAIR ;
  1449:                              SWAP ;
  1450:                              PAIR ;
  1451:                              SWAP ;
  1452:                              PAIR } } ;
  1453:                      NIL operation }
  1454:                    { IF_LEFT
  1455:                        { SWAP ;
  1456:                          DUP ;
  1457:                          DUG 2 ;
  1458:                          CAAAR ;
  1459:                          SENDER ;
  1460:                          COMPARE ;
  1461:                          EQ ;
  1462:                          IF { DIG 2 ; DROP ; DIG 2 ; DROP }
  1463:                             { PUSH string "WrongCondition: sp.sender == self.data.administrator" ;
  1464:                               FAILWITH } ;
  1465:                          SWAP ;
  1466:                          DUP ;
  1467:                          CAR ;
  1468:                          SWAP ;
  1469:                          CDR ;
  1470:                          DUP ;
  1471:                          CDR ;
  1472:                          SWAP ;
  1473:                          CAR ;
  1474:                          DUP ;
  1475:                          CAR ;
  1476:                          SWAP ;
  1477:                          CDDR ;
  1478:                          DIG 4 ;
  1479:                          PAIR ;
  1480:                          SWAP ;
  1481:                          PAIR ;
  1482:                          PAIR ;
  1483:                          SWAP ;
  1484:                          PAIR ;
  1485:                          NIL operation }
  1486:                        { SENDER ;
  1487:                          DIG 3 ;
  1488:                          DUP ;
  1489:                          DUG 4 ;
  1490:                          DIG 3 ;
  1491:                          DIG 3 ;
  1492:                          DUP ;
  1493:                          DUG 4 ;
  1494:                          PAIR %in_param %in_storage ;
  1495:                          EXEC ;
  1496:                          DUP ;
  1497:                          CDDR ;
  1498:                          DUG 3 ;
  1499:                          DUP ;
  1500:                          CAR ;
  1501:                          NIL operation ;
  1502:                          SWAP ;
  1503:                          ITER { CONS } ;
  1504:                          SWAP ;
  1505:                          DUP ;
  1506:                          DUG 2 ;
  1507:                          CDAR ;
  1508:                          IF { DIG 2 ; DROP ; DIG 2 ; DUP ; DUG 3 ; CAR ; DUG 2 } {} ;
  1509:                          DIG 4 ;
  1510:                          DUP ;
  1511:                          DUG 5 ;
  1512:                          CAAAR ;
  1513:                          DIG 3 ;
  1514:                          DUP ;
  1515:                          DUG 4 ;
  1516:                          COMPARE ;
  1517:                          EQ ;
  1518:                          IF { PUSH bool True }
  1519:                             { DIG 4 ;
  1520:                               DUP ;
  1521:                               DUG 5 ;
  1522:                               CDADAR ;
  1523:                               IF { PUSH bool False }
  1524:                                  { DIG 2 ;
  1525:                                    DUP ;
  1526:                                    DUG 3 ;
  1527:                                    DIG 4 ;
  1528:                                    DUP ;
  1529:                                    DUG 5 ;
  1530:                                    CAR ;
  1531:                                    COMPARE ;
  1532:                                    EQ ;
  1533:                                    IF { PUSH bool True }
  1534:                                       { DIG 3 ;
  1535:                                         DUP ;
  1536:                                         DUG 4 ;
  1537:                                         CDDR ;
  1538:                                         DIG 5 ;
  1539:                                         DUP ;
  1540:                                         DUG 6 ;
  1541:                                         CAADR ;
  1542:                                         DIG 5 ;
  1543:                                         DUP ;
  1544:                                         DUG 6 ;
  1545:                                         CAR ;
  1546:                                         GET ;
  1547:                                         IF_SOME {} { PUSH int 26 ; FAILWITH } ;
  1548:                                         CAR ;
  1549:                                         DIG 4 ;
  1550:                                         DUP ;
  1551:                                         DUG 5 ;
  1552:                                         GET ;
  1553:                                         IF_SOME {} { PUSH int 26 ; FAILWITH } ;
  1554:                                         COMPARE ;
  1555:                                         GE } } } ;
  1556:                          IF {}
  1557:                             { PUSH string
  1558:                                    "WrongCondition: (sender.value == self.data.administrator) | ((~ self.data.paused) & ((params.from_ == sender.value) | (self.data.balances[params.from_].approvals[sender.value] >= params.value)))" ;
  1559:                               FAILWITH } ;
  1560:                          DIG 4 ;
  1561:                          DUP ;
  1562:                          DUG 5 ;
  1563:                          CAADR ;
  1564:                          DIG 4 ;
  1565:                          DUP ;
  1566:                          DUG 5 ;
  1567:                          CDAR ;
  1568:                          MEM ;
  1569:                          IF {}
  1570:                             { DIG 4 ;
  1571:                               DUP ;
  1572:                               CDR ;
  1573:                               SWAP ;
  1574:                               CAR ;
  1575:                               DUP ;
  1576:                               CDR ;
  1577:                               SWAP ;
  1578:                               CAR ;
  1579:                               DUP ;
  1580:                               CAR ;
  1581:                               SWAP ;
  1582:                               CDR ;
  1583:                               DIG 7 ;
  1584:                               DUP ;
  1585:                               DUG 8 ;
  1586:                               CDAR ;
  1587:                               PUSH (option (pair (map %approvals address nat) (nat %balance))) (Some (Pair {} 0)) ;
  1588:                               SWAP ;
  1589:                               UPDATE ;
  1590:                               SWAP ;
  1591:                               PAIR ;
  1592:                               PAIR ;
  1593:                               PAIR ;
  1594:                               DUG 4 } ;
  1595:                          DIG 3 ;
  1596:                          DUP ;
  1597:                          DUG 4 ;
  1598:                          CDDR ;
  1599:                          DIG 5 ;
  1600:                          DUP ;
  1601:                          DUG 6 ;
  1602:                          CAADR ;
  1603:                          DIG 5 ;
  1604:                          DUP ;
  1605:                          DUG 6 ;
  1606:                          CAR ;
  1607:                          GET ;
  1608:                          IF_SOME {} { PUSH int 28 ; FAILWITH } ;
  1609:                          CDR ;
  1610:                          COMPARE ;
  1611:                          GE ;
  1612:                          IF {}
  1613:                             { PUSH string
  1614:                                    "WrongCondition: self.data.balances[params.from_].balance >= params.value" ;
  1615:                               FAILWITH } ;
  1616:                          DIG 4 ;
  1617:                          DUP ;
  1618:                          DUG 5 ;
  1619:                          DUP ;
  1620:                          CDR ;
  1621:                          SWAP ;
  1622:                          CAR ;
  1623:                          DUP ;
  1624:                          CDR ;
  1625:                          SWAP ;
  1626:                          CAR ;
  1627:                          DUP ;
  1628:                          CAR ;
  1629:                          SWAP ;
  1630:                          CDR ;
  1631:                          DUP ;
  1632:                          DIG 8 ;
  1633:                          DUP ;
  1634:                          DUG 9 ;
  1635:                          CAR ;
  1636:                          DUP ;
  1637:                          DUG 2 ;
  1638:                          GET ;
  1639:                          IF_SOME {} { PUSH int 29 ; FAILWITH } ;
  1640:                          CAR ;
  1641:                          DIG 9 ;
  1642:                          DUP ;
  1643:                          DUG 10 ;
  1644:                          CDDR ;
  1645:                          DIG 11 ;
  1646:                          CAADR ;
  1647:                          DIG 11 ;
  1648:                          DUP ;
  1649:                          DUG 12 ;
  1650:                          CAR ;
  1651:                          GET ;
  1652:                          IF_SOME {} { PUSH int 30 ; FAILWITH } ;
  1653:                          CDR ;
  1654:                          SUB ;
  1655:                          ISNAT ;
  1656:                          IF_SOME {} { PUSH int 29 ; FAILWITH } ;
  1657:                          SWAP ;
  1658:                          PAIR ;
  1659:                          SOME ;
  1660:                          SWAP ;
  1661:                          UPDATE ;
  1662:                          SWAP ;
  1663:                          PAIR ;
  1664:                          PAIR ;
  1665:                          PAIR ;
  1666:                          DUP ;
  1667:                          CDR ;
  1668:                          SWAP ;
  1669:                          CAR ;
  1670:                          DUP ;
  1671:                          CDR ;
  1672:                          SWAP ;
  1673:                          CAR ;
  1674:                          DUP ;
  1675:                          CAR ;
  1676:                          SWAP ;
  1677:                          CDR ;
  1678:                          DUP ;
  1679:                          DIG 8 ;
  1680:                          DUP ;
  1681:                          DUG 9 ;
  1682:                          CDAR ;
  1683:                          DUP ;
  1684:                          DUG 2 ;
  1685:                          GET ;
  1686:                          IF_SOME {} { PUSH int 31 ; FAILWITH } ;
  1687:                          DUP ;
  1688:                          CAR ;
  1689:                          SWAP ;
  1690:                          CDR ;
  1691:                          DIG 10 ;
  1692:                          DUP ;
  1693:                          DUG 11 ;
  1694:                          CDDR ;
  1695:                          ADD ;
  1696:                          SWAP ;
  1697:                          PAIR ;
  1698:                          SOME ;
  1699:                          SWAP ;
  1700:                          UPDATE ;
  1701:                          SWAP ;
  1702:                          PAIR ;
  1703:                          PAIR ;
  1704:                          PAIR ;
  1705:                          DUG 4 ;
  1706:                          DIG 2 ;
  1707:                          DUP ;
  1708:                          DUG 3 ;
  1709:                          DIG 4 ;
  1710:                          DUP ;
  1711:                          DUG 5 ;
  1712:                          CAR ;
  1713:                          COMPARE ;
  1714:                          NEQ ;
  1715:                          IF { DIG 2 ; DUP ; DUG 3 ; DIG 5 ; DUP ; DUG 6 ; CAAAR ; COMPARE ; NEQ }
  1716:                             { PUSH bool False } ;
  1717:                          IF { SWAP ;
  1718:                               DROP ;
  1719:                               DIG 4 ;
  1720:                               DROP ;
  1721:                               DIG 4 ;
  1722:                               DROP ;
  1723:                               DIG 3 ;
  1724:                               DUP ;
  1725:                               DUG 4 ;
  1726:                               DUP ;
  1727:                               CDR ;
  1728:                               SWAP ;
  1729:                               CAR ;
  1730:                               DUP ;
  1731:                               CDR ;
  1732:                               SWAP ;
  1733:                               CAR ;
  1734:                               DUP ;
  1735:                               CAR ;
  1736:                               SWAP ;
  1737:                               CDR ;
  1738:                               DUP ;
  1739:                               DIG 7 ;
  1740:                               DUP ;
  1741:                               DUG 8 ;
  1742:                               CAR ;
  1743:                               DUP ;
  1744:                               DUG 2 ;
  1745:                               GET ;
  1746:                               IF_SOME {} { PUSH int 33 ; FAILWITH } ;
  1747:                               DUP ;
  1748:                               CDR ;
  1749:                               SWAP ;
  1750:                               CAR ;
  1751:                               DIG 8 ;
  1752:                               DIG 9 ;
  1753:                               DUP ;
  1754:                               DUG 10 ;
  1755:                               CDDR ;
  1756:                               DIG 11 ;
  1757:                               CAADR ;
  1758:                               DIG 11 ;
  1759:                               CAR ;
  1760:                               GET ;
  1761:                               IF_SOME {} { PUSH int 34 ; FAILWITH } ;
  1762:                               CAR ;
  1763:                               DIG 2 ;
  1764:                               DUP ;
  1765:                               DUG 3 ;
  1766:                               GET ;
  1767:                               IF_SOME {} { PUSH int 34 ; FAILWITH } ;
  1768:                               SUB ;
  1769:                               ISNAT ;
  1770:                               IF_SOME {} { PUSH int 33 ; FAILWITH } ;
  1771:                               SOME ;
  1772:                               SWAP ;
  1773:                               UPDATE ;
  1774:                               PAIR ;
  1775:                               SOME ;
  1776:                               SWAP ;
  1777:                               UPDATE ;
  1778:                               SWAP ;
  1779:                               PAIR ;
  1780:                               PAIR ;
  1781:                               PAIR ;
  1782:                               SWAP }
  1783:                             { SWAP ; DROP ; SWAP ; DROP ; SWAP ; DROP ; DIG 2 ; DROP ; DIG 2 ; DROP } } } } } ;
  1784:          NIL operation ;
  1785:          SWAP ;
  1786:          ITER { CONS } ;
  1787:          PAIR } }
At line 1553 characters 67 to 75,
script reached FAILWITH instruction
with 26
Fatal error:
  transfer simulation failed
Warning:
  
   The node you are connecting to claims to be running in a
                    Tezos TEST SANDBOX.
      Do NOT use your fundraiser keys on this network.
  You should not see this message if you are not a developer.

Hash: tz1gjaF81ZRRvdzjobyfVNsAeSC6PScjfQwN
Public Key: edpktzNbDAUjUk697W7gYg2CRuBQjyPxbEg8dLccYYwKSKvkPvjtV9
Secret Key: unencrypted:edsk39qAm1fiMjgmPkw1EgQYkMzkJezLNewd7PLNHTkr6w9XA2zdfo
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
      Entrypoint: permit
      Parameter: { Pair "edpktzNbDAUjUk697W7gYg2CRuBQjyPxbEg8dLccYYwKSKvkPvjtV9"
                        (Pair "edsigtfkWys7vyeQy1PnHcBuac1dgj2aJ8Jv3fvoDE5XRtxTMRgJBwVgMTzvhAzBQyjH48ux9KE8jRZBSk4Rv2bfphsfpKP3ggM") }
      This operation FAILED.

Invalid argument passed to contract KT1H5ELRW3wmVMuZPJwL3DEUkCc5B6gH4M9H.
At (unshown) location 0, value
  (Right
     (Left (Right
              (Right
                 { Pair "edpktzNbDAUjUk697W7gYg2CRuBQjyPxbEg8dLccYYwKSKvkPvjtV9"
                        (Pair "edsigtfkWys7vyeQy1PnHcBuac1dgj2aJ8Jv3fvoDE5XRtxTMRgJBwVgMTzvhAzBQyjH48ux9KE8jRZBSk4Rv2bfphsfpKP3ggM") }))))
is invalid for type
  or (or (or (pair %approve (address %spender) (nat %value))
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
                 (pair %transfer (address %from_) (pair (address %to_) (nat %value)))))).
At (unshown) location 0, value
  (Left (Right
           (Right
              { Pair "edpktzNbDAUjUk697W7gYg2CRuBQjyPxbEg8dLccYYwKSKvkPvjtV9"
                     (Pair "edsigtfkWys7vyeQy1PnHcBuac1dgj2aJ8Jv3fvoDE5XRtxTMRgJBwVgMTzvhAzBQyjH48ux9KE8jRZBSk4Rv2bfphsfpKP3ggM") })))
is invalid for type
  or (or (or (address %getDefaultExpiry) (address %getTotalSupply))
         (or (pair %mint (address %address) (nat %value))
             (list %permit (pair key (pair signature bytes)))))
     (or (or (address %setAdministrator)
             (pair %setExpiry (address %address) (pair (option %permit bytes) (nat %seconds))))
         (or (bool %setPause)
             (pair %transfer (address %from_) (pair (address %to_) (nat %value))))).
At (unshown) location 0, value
  (Right
     (Right
        { Pair "edpktzNbDAUjUk697W7gYg2CRuBQjyPxbEg8dLccYYwKSKvkPvjtV9"
               (Pair "edsigtfkWys7vyeQy1PnHcBuac1dgj2aJ8Jv3fvoDE5XRtxTMRgJBwVgMTzvhAzBQyjH48ux9KE8jRZBSk4Rv2bfphsfpKP3ggM") }))
is invalid for type
  or (or (address %getDefaultExpiry) (address %getTotalSupply))
     (or (pair %mint (address %address) (nat %value))
         (list %permit (pair key (pair signature bytes)))).
At (unshown) location 0, value
  (Right
     { Pair "edpktzNbDAUjUk697W7gYg2CRuBQjyPxbEg8dLccYYwKSKvkPvjtV9"
            (Pair "edsigtfkWys7vyeQy1PnHcBuac1dgj2aJ8Jv3fvoDE5XRtxTMRgJBwVgMTzvhAzBQyjH48ux9KE8jRZBSk4Rv2bfphsfpKP3ggM") })
is invalid for type
  or (pair %mint (address %address) (nat %value))
     (list %permit (pair key (pair signature bytes))).
At (unshown) location 0, value
  { Pair "edpktzNbDAUjUk697W7gYg2CRuBQjyPxbEg8dLccYYwKSKvkPvjtV9"
         (Pair "edsigtfkWys7vyeQy1PnHcBuac1dgj2aJ8Jv3fvoDE5XRtxTMRgJBwVgMTzvhAzBQyjH48ux9KE8jRZBSk4Rv2bfphsfpKP3ggM") }
is invalid for type list (pair key (pair signature bytes)).
At (unshown) location 3, primitive Pair expects 2 arguments but is given 1.
Fatal error:
  transfer simulation failed
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
      Entrypoint: permit
      Parameter: { Pair "edpktzNbDAUjUk697W7gYg2CRuBQjyPxbEg8dLccYYwKSKvkPvjtV9"
                        (Pair "edsigtfkWys7vyeQy1PnHcBuac1dgj2aJ8Jv3fvoDE5XRtxTMRgJBwVgMTzvhAzBQyjH48ux9KE8jRZBSk4Rv2bfphsfpKP3ggM"
                              0x877b50b43b81b9d2c5a6c56087fab148a6622741cd0e79557e6b6131b8b5e49b) }
      This operation FAILED.

Runtime error in contract KT1H5ELRW3wmVMuZPJwL3DEUkCc5B6gH4M9H:
  0001: { parameter
  0002:     (or (or (or (pair %approve (address %spender) (nat %value))
  0003:                 (or (pair %burn (address %address) (nat %value))
  0004:                     (list %delete_permits (pair address bytes))))
  0005:             (or (or (address %getAdministrator)
  0006:                     (pair %getAllowance
  0007:                        (pair %arg (address %owner) (address %spender))
  0008:                        (address %target)))
  0009:                 (or (pair %getBalance (address %arg) (address %target)) (address %getCounter))))
  0010:         (or (or (or (address %getDefaultExpiry) (address %getTotalSupply))
  0011:                 (or (pair %mint (address %address) (nat %value))
  0012:                     (list %permit (pair key (pair signature bytes)))))
  0013:             (or (or (address %setAdministrator)
  0014:                     (pair %setExpiry (address %address) (pair (option %permit bytes) (nat %seconds))))
  0015:                 (or (bool %setPause)
  0016:                     (pair %transfer (address %from_) (pair (address %to_) (nat %value))))))) ;
  0017:   storage
  0018:     (pair (pair (pair (address %administrator)
  0019:                       (big_map %balances address (pair (map %approvals address nat) (nat %balance))))
  0020:                 (pair (nat %counter) (pair (nat %default_expiry) (nat %max_expiry))))
  0021:           (pair (pair (big_map %metadata string bytes)
  0022:                       (pair (bool %paused) (big_map %permit_expiries (pair address bytes) (option nat))))
  0023:                 (pair (big_map %permits (pair address bytes) timestamp)
  0024:                       (pair (nat %totalSupply) (big_map %user_expiries address (option nat)))))) ;
  0025:   code { LAMBDA
  0026:            (pair (pair %in_param address bytes)
  0027:                  (pair %in_storage
  0028:                     (pair (pair (address %administrator)
  0029:                                 (big_map %balances address (pair (map %approvals address nat) (nat %balance))))
  0030:                           (pair (nat %counter) (pair (nat %default_expiry) (nat %max_expiry))))
  0031:                     (pair (pair (big_map %metadata string bytes)
  0032:                                 (pair (bool %paused) (big_map %permit_expiries (pair address bytes) (option nat))))
  0033:                           (pair (big_map %permits (pair address bytes) timestamp)
  0034:                                 (pair (nat %totalSupply) (big_map %user_expiries address (option nat)))))))
  0035:            (pair (list %operations operation)
  0036:                  (pair (nat %result)
  0037:                        (pair %storage
  0038:                           (pair (pair (address %administrator)
  0039:                                       (big_map %balances address (pair (map %approvals address nat) (nat %balance))))
  0040:                                 (pair (nat %counter) (pair (nat %default_expiry) (nat %max_expiry))))
  0041:                           (pair (pair (big_map %metadata string bytes)
  0042:                                       (pair (bool %paused) (big_map %permit_expiries (pair address bytes) (option nat))))
  0043:                                 (pair (big_map %permits (pair address bytes) timestamp)
  0044:                                       (pair (nat %totalSupply) (big_map %user_expiries address (option nat))))))))
  0045:            { NIL operation ;
  0046:              SWAP ;
  0047:              DUP ;
  0048:              DUG 2 ;
  0049:              CDR ;
  0050:              DUP ;
  0051:              CDADDR ;
  0052:              DIG 3 ;
  0053:              DUP ;
  0054:              DUG 4 ;
  0055:              CAR ;
  0056:              MEM ;
  0057:              IF { DUP ;
  0058:                   CDADDR ;
  0059:                   DIG 3 ;
  0060:                   DUP ;
  0061:                   DUG 4 ;
  0062:                   CAR ;
  0063:                   GET ;
  0064:                   IF_SOME {} { PUSH int 114 ; FAILWITH } ;
  0065:                   IF_SOME { DROP ; PUSH bool True } { PUSH bool False } }
  0066:                 { PUSH bool False } ;
  0067:              IF { DUP ;
  0068:                   CDADDR ;
  0069:                   DIG 3 ;
  0070:                   CAR ;
  0071:                   GET ;
  0072:                   IF_SOME {} { PUSH int 115 ; FAILWITH } ;
  0073:                   IF_SOME {} { PUSH int 115 ; FAILWITH } }
  0074:                 { DUP ;
  0075:                   CDDDDR ;
  0076:                   DIG 3 ;
  0077:                   DUP ;
  0078:                   DUG 4 ;
  0079:                   CAAR ;
  0080:                   MEM ;
  0081:                   IF { DUP ;
  0082:                        CDDDDR ;
  0083:                        DIG 3 ;
  0084:                        DUP ;
  0085:                        DUG 4 ;
  0086:                        CAAR ;
  0087:                        GET ;
  0088:                        IF_SOME {} { PUSH int 118 ; FAILWITH } ;
  0089:                        IF_SOME { DROP ; PUSH bool True } { PUSH bool False } }
  0090:                      { PUSH bool False } ;
  0091:                   IF { DUP ;
  0092:                        CDDDDR ;
  0093:                        DIG 3 ;
  0094:                        CAAR ;
  0095:                        GET ;
  0096:                        IF_SOME {} { PUSH int 119 ; FAILWITH } ;
  0097:                        IF_SOME {} { PUSH int 119 ; FAILWITH } }
  0098:                      { DIG 2 ; DROP ; DUP ; CADDAR } } ;
  0099:              PAIR %result %storage ;
  0100:              SWAP ;
  0101:              PAIR %operations } ;
  0102:          SWAP ;
  0103:          LAMBDA
  0104:            (pair (pair %in_param (address %from_) (pair (address %to_) (nat %value)))
  0105:                  (pair %in_storage
  0106:                     (pair (pair (address %administrator)
  0107:                                 (big_map %balances address (pair (map %approvals address nat) (nat %balance))))
  0108:                           (pair (nat %counter) (pair (nat %default_expiry) (nat %max_expiry))))
  0109:                     (pair (pair (big_map %metadata string bytes)
  0110:                                 (pair (bool %paused) (big_map %permit_expiries (pair address bytes) (option nat))))
  0111:                           (pair (big_map %permits (pair address bytes) timestamp)
  0112:                                 (pair (nat %totalSupply) (big_map %user_expiries address (option nat)))))))
  0113:            (pair (list %operations operation)
  0114:                  (pair (bool %result)
  0115:                        (pair %storage
  0116:                           (pair (pair (address %administrator)
  0117:                                       (big_map %balances address (pair (map %approvals address nat) (nat %balance))))
  0118:                                 (pair (nat %counter) (pair (nat %default_expiry) (nat %max_expiry))))
  0119:                           (pair (pair (big_map %metadata string bytes)
  0120:                                       (pair (bool %paused) (big_map %permit_expiries (pair address bytes) (option nat))))
  0121:                                 (pair (big_map %permits (pair address bytes) timestamp)
  0122:                                       (pair (nat %totalSupply) (big_map %user_expiries address (option nat))))))))
  0123:            { NIL operation ;
  0124:              SWAP ;
  0125:              DUP ;
  0126:              DUG 2 ;
  0127:              CDR ;
  0128:              DUP ;
  0129:              CDDAR ;
  0130:              DIG 3 ;
  0131:              DUP ;
  0132:              DUG 4 ;
  0133:              CAR ;
  0134:              PACK ;
  0135:              BLAKE2B ;
  0136:              DIG 4 ;
  0137:              DUP ;
  0138:              DUG 5 ;
  0139:              CAAR ;
  0140:              PAIR ;
  0141:              MEM ;
  0142:              IF { DUP ;
  0143:                   CDADDR ;
  0144:                   DIG 3 ;
  0145:                   DUP ;
  0146:                   DUG 4 ;
  0147:                   CAR ;
  0148:                   PACK ;
  0149:                   BLAKE2B ;
  0150:                   DIG 4 ;
  0151:                   DUP ;
  0152:                   DUG 5 ;
  0153:                   CAAR ;
  0154:                   PAIR ;
  0155:                   MEM ;
  0156:                   IF { DUP ;
  0157:                        CDADDR ;
  0158:                        DIG 3 ;
  0159:                        DUP ;
  0160:                        DUG 4 ;
  0161:                        CAR ;
  0162:                        PACK ;
  0163:                        BLAKE2B ;
  0164:                        DIG 4 ;
  0165:                        DUP ;
  0166:                        DUG 5 ;
  0167:                        CAAR ;
  0168:                        PAIR ;
  0169:                        GET ;
  0170:                        IF_SOME {} { PUSH int 67 ; FAILWITH } ;
  0171:                        IF_SOME { DROP ; PUSH bool True } { PUSH bool False } }
  0172:                      { PUSH bool False } ;
  0173:                   IF { DUP ;
  0174:                        CDADDR ;
  0175:                        DIG 3 ;
  0176:                        DUP ;
  0177:                        DUG 4 ;
  0178:                        CAR ;
  0179:                        PACK ;
  0180:                        BLAKE2B ;
  0181:                        DIG 4 ;
  0182:                        DUP ;
  0183:                        DUG 5 ;
  0184:                        CAAR ;
  0185:                        PAIR ;
  0186:                        GET ;
  0187:                        IF_SOME {} { PUSH int 68 ; FAILWITH } ;
  0188:                        IF_SOME {} { PUSH int 68 ; FAILWITH } }
  0189:                      { DUP ;
  0190:                        CDDDDR ;
  0191:                        DIG 3 ;
  0192:                        DUP ;
  0193:                        DUG 4 ;
  0194:                        CAAR ;
  0195:                        MEM ;
  0196:                        IF { DUP ;
  0197:                             CDDDDR ;
  0198:                             DIG 3 ;
  0199:                             DUP ;
  0200:                             DUG 4 ;
  0201:                             CAAR ;
  0202:                             GET ;
  0203:                             IF_SOME {} { PUSH int 70 ; FAILWITH } ;
  0204:                             IF_SOME { DROP ; PUSH bool True } { PUSH bool False } }
  0205:                           { PUSH bool False } ;
  0206:                        IF { DUP ;
  0207:                             CDDDDR ;
  0208:                             DIG 3 ;
  0209:                             DUP ;
  0210:                             DUG 4 ;
  0211:                             CAAR ;
  0212:                             GET ;
  0213:                             IF_SOME {} { PUSH int 71 ; FAILWITH } ;
  0214:                             IF_SOME {} { PUSH int 71 ; FAILWITH } }
  0215:                           { DUP ; CADDAR } } ;
  0216:                   SWAP ;
  0217:                   DUP ;
  0218:                   DUG 2 ;
  0219:                   CDDAR ;
  0220:                   DIG 4 ;
  0221:                   DUP ;
  0222:                   DUG 5 ;
  0223:                   CAR ;
  0224:                   PACK ;
  0225:                   BLAKE2B ;
  0226:                   DIG 5 ;
  0227:                   DUP ;
  0228:                   DUG 6 ;
  0229:                   CAAR ;
  0230:                   PAIR ;
  0231:                   GET ;
  0232:                   IF_SOME {} { PUSH int 66 ; FAILWITH } ;
  0233:                   NOW ;
  0234:                   SUB ;
  0235:                   ISNAT ;
  0236:                   IF_SOME {} { PUSH int 76 ; FAILWITH } ;
  0237:                   COMPARE ;
  0238:                   GE ;
  0239:                   IF { DUP ;
  0240:                        CDDAR ;
  0241:                        DIG 3 ;
  0242:                        DUP ;
  0243:                        DUG 4 ;
  0244:                        CAR ;
  0245:                        PACK ;
  0246:                        BLAKE2B ;
  0247:                        DIG 4 ;
  0248:                        DUP ;
  0249:                        DUG 5 ;
  0250:                        CAAR ;
  0251:                        PAIR ;
  0252:                        MEM ;
  0253:                        IF { DUP ;
  0254:                             CAR ;
  0255:                             SWAP ;
  0256:                             CDR ;
  0257:                             DUP ;
  0258:                             CAR ;
  0259:                             SWAP ;
  0260:                             CDR ;
  0261:                             DUP ;
  0262:                             CDR ;
  0263:                             SWAP ;
  0264:                             CAR ;
  0265:                             NONE timestamp ;
  0266:                             DIG 6 ;
  0267:                             DUP ;
  0268:                             DUG 7 ;
  0269:                             CAR ;
  0270:                             PACK ;
  0271:                             BLAKE2B ;
  0272:                             DIG 7 ;
  0273:                             DUP ;
  0274:                             DUG 8 ;
  0275:                             CAAR ;
  0276:                             PAIR ;
  0277:                             UPDATE ;
  0278:                             PAIR ;
  0279:                             SWAP ;
  0280:                             PAIR ;
  0281:                             SWAP ;
  0282:                             PAIR }
  0283:                           {} ;
  0284:                        DUP ;
  0285:                        CDADDR ;
  0286:                        DIG 3 ;
  0287:                        DUP ;
  0288:                        DUG 4 ;
  0289:                        CAR ;
  0290:                        PACK ;
  0291:                        BLAKE2B ;
  0292:                        DIG 4 ;
  0293:                        DUP ;
  0294:                        DUG 5 ;
  0295:                        CAAR ;
  0296:                        PAIR ;
  0297:                        MEM ;
  0298:                        IF { DUP ;
  0299:                             CAR ;
  0300:                             SWAP ;
  0301:                             CDR ;
  0302:                             DUP ;
  0303:                             CDR ;
  0304:                             SWAP ;
  0305:                             CAR ;
  0306:                             DUP ;
  0307:                             CAR ;
  0308:                             SWAP ;
  0309:                             CDR ;
  0310:                             DUP ;
  0311:                             CAR ;
  0312:                             SWAP ;
  0313:                             CDR ;
  0314:                             NONE (option nat) ;
  0315:                             DIG 7 ;
  0316:                             DUP ;
  0317:                             DUG 8 ;
  0318:                             CAR ;
  0319:                             PACK ;
  0320:                             BLAKE2B ;
  0321:                             DIG 8 ;
  0322:                             CAAR ;
  0323:                             PAIR ;
  0324:                             UPDATE ;
  0325:                             SWAP ;
  0326:                             PAIR ;
  0327:                             SWAP ;
  0328:                             PAIR ;
  0329:                             PAIR ;
  0330:                             SWAP ;
  0331:                             PAIR }
  0332:                           { DIG 2 ; DROP } ;
  0333:                        PUSH bool False }
  0334:                      { DUP ;
  0335:                        CDDAR ;
  0336:                        DIG 3 ;
  0337:                        DUP ;
  0338:                        DUG 4 ;
  0339:                        CAR ;
  0340:                        PACK ;
  0341:                        BLAKE2B ;
  0342:                        DIG 4 ;
  0343:                        DUP ;
  0344:                        DUG 5 ;
  0345:                        CAAR ;
  0346:                        PAIR ;
  0347:                        MEM ;
  0348:                        IF { DUP ;
  0349:                             CAR ;
  0350:                             SWAP ;
  0351:                             CDR ;
  0352:                             DUP ;
  0353:                             CAR ;
  0354:                             SWAP ;
  0355:                             CDR ;
  0356:                             DUP ;
  0357:                             CDR ;
  0358:                             SWAP ;
  0359:                             CAR ;
  0360:                             NONE timestamp ;
  0361:                             DIG 6 ;
  0362:                             DUP ;
  0363:                             DUG 7 ;
  0364:                             CAR ;
  0365:                             PACK ;
  0366:                             BLAKE2B ;
  0367:                             DIG 7 ;
  0368:                             DUP ;
  0369:                             DUG 8 ;
  0370:                             CAAR ;
  0371:                             PAIR ;
  0372:                             UPDATE ;
  0373:                             PAIR ;
  0374:                             SWAP ;
  0375:                             PAIR ;
  0376:                             SWAP ;
  0377:                             PAIR }
  0378:                           {} ;
  0379:                        DUP ;
  0380:                        CDADDR ;
  0381:                        DIG 3 ;
  0382:                        DUP ;
  0383:                        DUG 4 ;
  0384:                        CAR ;
  0385:                        PACK ;
  0386:                        BLAKE2B ;
  0387:                        DIG 4 ;
  0388:                        DUP ;
  0389:                        DUG 5 ;
  0390:                        CAAR ;
  0391:                        PAIR ;
  0392:                        MEM ;
  0393:                        IF { DUP ;
  0394:                             CAR ;
  0395:                             SWAP ;
  0396:                             CDR ;
  0397:                             DUP ;
  0398:                             CDR ;
  0399:                             SWAP ;
  0400:                             CAR ;
  0401:                             DUP ;
  0402:                             CAR ;
  0403:                             SWAP ;
  0404:                             CDR ;
  0405:                             DUP ;
  0406:                             CAR ;
  0407:                             SWAP ;
  0408:                             CDR ;
  0409:                             NONE (option nat) ;
  0410:                             DIG 7 ;
  0411:                             DUP ;
  0412:                             DUG 8 ;
  0413:                             CAR ;
  0414:                             PACK ;
  0415:                             BLAKE2B ;
  0416:                             DIG 8 ;
  0417:                             CAAR ;
  0418:                             PAIR ;
  0419:                             UPDATE ;
  0420:                             SWAP ;
  0421:                             PAIR ;
  0422:                             SWAP ;
  0423:                             PAIR ;
  0424:                             PAIR ;
  0425:                             SWAP ;
  0426:                             PAIR }
  0427:                           { DIG 2 ; DROP } ;
  0428:                        PUSH bool True } }
  0429:                 { DIG 2 ; DROP ; PUSH bool False } ;
  0430:              PAIR %result %storage ;
  0431:              SWAP ;
  0432:              PAIR %operations } ;
  0433:          SWAP ;
  0434:          DUP ;
  0435:          CDR ;
  0436:          SWAP ;
  0437:          CAR ;
  0438:          IF_LEFT
  0439:            { IF_LEFT
  0440:                { IF_LEFT
  0441:                    { SWAP ;
  0442:                      DUP ;
  0443:                      DUG 2 ;
  0444:                      CDADAR ;
  0445:                      IF { PUSH string "WrongCondition: ~ self.data.paused" ; FAILWITH } {} ;
  0446:                      PUSH nat 0 ;
  0447:                      DIG 2 ;
  0448:                      DUP ;
  0449:                      DUG 3 ;
  0450:                      CAADR ;
  0451:                      SENDER ;
  0452:                      GET ;
  0453:                      IF_SOME {} { PUSH int 162 ; FAILWITH } ;
  0454:                      CAR ;
  0455:                      DIG 2 ;
  0456:                      DUP ;
  0457:                      DUG 3 ;
  0458:                      CAR ;
  0459:                      GET ;
  0460:                      IF_SOME {} { PUSH nat 0 } ;
  0461:                      COMPARE ;
  0462:                      EQ ;
  0463:                      IF { PUSH bool True } { DUP ; CDR ; PUSH nat 0 ; COMPARE ; EQ } ;
  0464:                      IF { DIG 2 ; DROP ; DIG 2 ; DROP }
  0465:                         { PUSH string "UnsafeAllowanceChange" ; FAILWITH } ;
  0466:                      SWAP ;
  0467:                      DUP ;
  0468:                      CDR ;
  0469:                      SWAP ;
  0470:                      CAR ;
  0471:                      DUP ;
  0472:                      CDR ;
  0473:                      SWAP ;
  0474:                      CAR ;
  0475:                      DUP ;
  0476:                      CAR ;
  0477:                      SWAP ;
  0478:                      CDR ;
  0479:                      DUP ;
  0480:                      SENDER ;
  0481:                      DUP ;
  0482:                      DUG 2 ;
  0483:                      GET ;
  0484:                      IF_SOME {} { PUSH int 166 ; FAILWITH } ;
  0485:                      DUP ;
  0486:                      CDR ;
  0487:                      SWAP ;
  0488:                      CAR ;
  0489:                      DIG 7 ;
  0490:                      DUP ;
  0491:                      CAR ;
  0492:                      SWAP ;
  0493:                      CDR ;
  0494:                      SOME ;
  0495:                      SWAP ;
  0496:                      UPDATE ;
  0497:                      PAIR ;
  0498:                      SOME ;
  0499:                      SWAP ;
  0500:                      UPDATE ;
  0501:                      SWAP ;
  0502:                      PAIR ;
  0503:                      PAIR ;
  0504:                      PAIR ;
  0505:                      NIL operation }
  0506:                    { IF_LEFT
  0507:                        { SWAP ;
  0508:                          DUP ;
  0509:                          DUG 2 ;
  0510:                          CAAAR ;
  0511:                          SENDER ;
  0512:                          COMPARE ;
  0513:                          EQ ;
  0514:                          IF {}
  0515:                             { PUSH string "WrongCondition: sp.sender == self.data.administrator" ;
  0516:                               FAILWITH } ;
  0517:                          DUP ;
  0518:                          CDR ;
  0519:                          DIG 2 ;
  0520:                          DUP ;
  0521:                          DUG 3 ;
  0522:                          CAADR ;
  0523:                          DIG 2 ;
  0524:                          DUP ;
  0525:                          DUG 3 ;
  0526:                          CAR ;
  0527:                          GET ;
  0528:                          IF_SOME {} { PUSH int 192 ; FAILWITH } ;
  0529:                          CDR ;
  0530:                          COMPARE ;
  0531:                          GE ;
  0532:                          IF { DIG 2 ; DROP ; DIG 2 ; DROP }
  0533:                             { PUSH string
  0534:                                    "WrongCondition: self.data.balances[params.address].balance >= params.value" ;
  0535:                               FAILWITH } ;
  0536:                          SWAP ;
  0537:                          DUP ;
  0538:                          DUG 2 ;
  0539:                          DUP ;
  0540:                          CDR ;
  0541:                          SWAP ;
  0542:                          CAR ;
  0543:                          DUP ;
  0544:                          CDR ;
  0545:                          SWAP ;
  0546:                          CAR ;
  0547:                          DUP ;
  0548:                          CAR ;
  0549:                          SWAP ;
  0550:                          CDR ;
  0551:                          DUP ;
  0552:                          DIG 5 ;
  0553:                          DUP ;
  0554:                          DUG 6 ;
  0555:                          CAR ;
  0556:                          DUP ;
  0557:                          DUG 2 ;
  0558:                          GET ;
  0559:                          IF_SOME {} { PUSH int 193 ; FAILWITH } ;
  0560:                          CAR ;
  0561:                          DIG 6 ;
  0562:                          DUP ;
  0563:                          DUG 7 ;
  0564:                          CDR ;
  0565:                          DIG 8 ;
  0566:                          CAADR ;
  0567:                          DIG 8 ;
  0568:                          DUP ;
  0569:                          DUG 9 ;
  0570:                          CAR ;
  0571:                          GET ;
  0572:                          IF_SOME {} { PUSH int 194 ; FAILWITH } ;
  0573:                          CDR ;
  0574:                          SUB ;
  0575:                          ISNAT ;
  0576:                          IF_SOME {} { PUSH int 193 ; FAILWITH } ;
  0577:                          SWAP ;
  0578:                          PAIR ;
  0579:                          SOME ;
  0580:                          SWAP ;
  0581:                          UPDATE ;
  0582:                          SWAP ;
  0583:                          PAIR ;
  0584:                          PAIR ;
  0585:                          PAIR ;
  0586:                          DUP ;
  0587:                          DUG 2 ;
  0588:                          DUP ;
  0589:                          CAR ;
  0590:                          SWAP ;
  0591:                          CDR ;
  0592:                          DUP ;
  0593:                          CAR ;
  0594:                          SWAP ;
  0595:                          CDR ;
  0596:                          DUP ;
  0597:                          CAR ;
  0598:                          SWAP ;
  0599:                          CDDR ;
  0600:                          DIG 4 ;
  0601:                          CDR ;
  0602:                          DIG 5 ;
  0603:                          CDDDAR ;
  0604:                          SUB ;
  0605:                          ISNAT ;
  0606:                          IF_SOME {} { PUSH int 195 ; FAILWITH } ;
  0607:                          PAIR ;
  0608:                          SWAP ;
  0609:                          PAIR ;
  0610:                          SWAP ;
  0611:                          PAIR ;
  0612:                          SWAP ;
  0613:                          PAIR ;
  0614:                          NIL operation }
  0615:                        { PUSH int 0 ;
  0616:                          NIL operation ;
  0617:                          DIG 2 ;
  0618:                          DUP ;
  0619:                          DUG 3 ;
  0620:                          ITER { DIG 4 ;
  0621:                                 DUP ;
  0622:                                 DUG 5 ;
  0623:                                 CDDAR ;
  0624:                                 SWAP ;
  0625:                                 DUP ;
  0626:                                 DUG 2 ;
  0627:                                 MEM ;
  0628:                                 IF {} { DUP ; PUSH string "NO_PERMIT_TO_DELETE" ; PAIR ; FAILWITH } ;
  0629:                                 DIG 6 ;
  0630:                                 DUP ;
  0631:                                 DUG 7 ;
  0632:                                 DIG 5 ;
  0633:                                 DIG 2 ;
  0634:                                 DUP ;
  0635:                                 DUG 3 ;
  0636:                                 PAIR %in_param %in_storage ;
  0637:                                 EXEC ;
  0638:                                 DUP ;
  0639:                                 CDDR ;
  0640:                                 DUG 5 ;
  0641:                                 DUP ;
  0642:                                 CAR ;
  0643:                                 ITER { DIG 3 ; SWAP ; CONS ; DUG 2 } ;
  0644:                                 DUP ;
  0645:                                 CDAR ;
  0646:                                 DIG 6 ;
  0647:                                 DUP ;
  0648:                                 DUG 7 ;
  0649:                                 CDDAR ;
  0650:                                 DIG 3 ;
  0651:                                 DUP ;
  0652:                                 DUG 4 ;
  0653:                                 GET ;
  0654:                                 IF_SOME {} { PUSH int 45 ; FAILWITH } ;
  0655:                                 NOW ;
  0656:                                 SUB ;
  0657:                                 ISNAT ;
  0658:                                 IF_SOME {} { PUSH int 46 ; FAILWITH } ;
  0659:                                 COMPARE ;
  0660:                                 GE ;
  0661:                                 IF { DROP }
  0662:                                    { SWAP ; DUP ; DUG 2 ; PUSH string "PERMIT_NOT_EXPIRED" ; PAIR ; FAILWITH } ;
  0663:                                 DIG 4 ;
  0664:                                 DUP ;
  0665:                                 DUG 5 ;
  0666:                                 CDDAR ;
  0667:                                 SWAP ;
  0668:                                 DUP ;
  0669:                                 DUG 2 ;
  0670:                                 MEM ;
  0671:                                 IF { DIG 4 ;
  0672:                                      DUP ;
  0673:                                      CAR ;
  0674:                                      SWAP ;
  0675:                                      CDR ;
  0676:                                      DUP ;
  0677:                                      CAR ;
  0678:                                      SWAP ;
  0679:                                      CDR ;
  0680:                                      DUP ;
  0681:                                      CDR ;
  0682:                                      SWAP ;
  0683:                                      CAR ;
  0684:                                      NONE timestamp ;
  0685:                                      DIG 5 ;
  0686:                                      DUP ;
  0687:                                      DUG 6 ;
  0688:                                      UPDATE ;
  0689:                                      PAIR ;
  0690:                                      SWAP ;
  0691:                                      PAIR ;
  0692:                                      SWAP ;
  0693:                                      PAIR ;
  0694:                                      DUG 4 }
  0695:                                    {} ;
  0696:                                 DIG 4 ;
  0697:                                 DUP ;
  0698:                                 DUG 5 ;
  0699:                                 CDADDR ;
  0700:                                 SWAP ;
  0701:                                 DUP ;
  0702:                                 DUG 2 ;
  0703:                                 MEM ;
  0704:                                 IF { DIG 4 ;
  0705:                                      DUP ;
  0706:                                      CAR ;
  0707:                                      SWAP ;
  0708:                                      CDR ;
  0709:                                      DUP ;
  0710:                                      CDR ;
  0711:                                      SWAP ;
  0712:                                      CAR ;
  0713:                                      DUP ;
  0714:                                      CAR ;
  0715:                                      SWAP ;
  0716:                                      CDR ;
  0717:                                      DUP ;
  0718:                                      CAR ;
  0719:                                      SWAP ;
  0720:                                      CDR ;
  0721:                                      NONE (option nat) ;
  0722:                                      DIG 6 ;
  0723:                                      UPDATE ;
  0724:                                      SWAP ;
  0725:                                      PAIR ;
  0726:                                      SWAP ;
  0727:                                      PAIR ;
  0728:                                      PAIR ;
  0729:                                      SWAP ;
  0730:                                      PAIR ;
  0731:                                      DUG 3 }
  0732:                                    { DROP } } ;
  0733:                          SWAP ;
  0734:                          DROP ;
  0735:                          SWAP ;
  0736:                          DROP ;
  0737:                          DIG 2 ;
  0738:                          DROP ;
  0739:                          DIG 2 ;
  0740:                          DROP } } }
  0741:                { IF_LEFT
  0742:                    { IF_LEFT
  0743:                        { DIG 2 ;
  0744:                          DROP ;
  0745:                          DIG 2 ;
  0746:                          DROP ;
  0747:                          CONTRACT address ;
  0748:                          NIL operation ;
  0749:                          SWAP ;
  0750:                          IF_SOME {} { PUSH int 219 ; FAILWITH } ;
  0751:                          PUSH mutez 0 ;
  0752:                          DIG 3 ;
  0753:                          DUP ;
  0754:                          DUG 4 ;
  0755:                          CAAAR ;
  0756:                          TRANSFER_TOKENS ;
  0757:                          CONS }
  0758:                        { DIG 2 ;
  0759:                          DROP ;
  0760:                          DIG 2 ;
  0761:                          DROP ;
  0762:                          DUP ;
  0763:                          CDR ;
  0764:                          CONTRACT nat ;
  0765:                          NIL operation ;
  0766:                          SWAP ;
  0767:                          IF_SOME {} { PUSH int 209 ; FAILWITH } ;
  0768:                          PUSH mutez 0 ;
  0769:                          DIG 4 ;
  0770:                          DUP ;
  0771:                          DUG 5 ;
  0772:                          CAADR ;
  0773:                          DIG 4 ;
  0774:                          DUP ;
  0775:                          DUG 5 ;
  0776:                          CAAR ;
  0777:                          GET ;
  0778:                          IF_SOME {} { PUSH int 208 ; FAILWITH } ;
  0779:                          CAR ;
  0780:                          DIG 4 ;
  0781:                          CADR ;
  0782:                          GET ;
  0783:                          IF_SOME {} { PUSH int 208 ; FAILWITH } ;
  0784:                          TRANSFER_TOKENS ;
  0785:                          CONS } }
  0786:                    { IF_LEFT
  0787:                        { DIG 2 ;
  0788:                          DROP ;
  0789:                          DIG 2 ;
  0790:                          DROP ;
  0791:                          DUP ;
  0792:                          CDR ;
  0793:                          CONTRACT nat ;
  0794:                          NIL operation ;
  0795:                          SWAP ;
  0796:                          IF_SOME {} { PUSH int 204 ; FAILWITH } ;
  0797:                          PUSH mutez 0 ;
  0798:                          DIG 4 ;
  0799:                          DUP ;
  0800:                          DUG 5 ;
  0801:                          CAADR ;
  0802:                          DIG 4 ;
  0803:                          CAR ;
  0804:                          GET ;
  0805:                          IF_SOME {} { PUSH int 203 ; FAILWITH } ;
  0806:                          CDR ;
  0807:                          TRANSFER_TOKENS ;
  0808:                          CONS }
  0809:                        { DIG 2 ;
  0810:                          DROP ;
  0811:                          DIG 2 ;
  0812:                          DROP ;
  0813:                          CONTRACT nat ;
  0814:                          NIL operation ;
  0815:                          SWAP ;
  0816:                          IF_SOME {} { PUSH int 223 ; FAILWITH } ;
  0817:                          PUSH mutez 0 ;
  0818:                          DIG 3 ;
  0819:                          DUP ;
  0820:                          DUG 4 ;
  0821:                          CADAR ;
  0822:                          TRANSFER_TOKENS ;
  0823:                          CONS } } } }
  0824:            { IF_LEFT
  0825:                { IF_LEFT
  0826:                    { IF_LEFT
  0827:                        { DIG 2 ;
  0828:                          DROP ;
  0829:                          DIG 2 ;
  0830:                          DROP ;
  0831:                          CONTRACT nat ;
  0832:                          NIL operation ;
  0833:                          SWAP ;
  0834:                          IF_SOME {} { PUSH int 229 ; FAILWITH } ;
  0835:                          PUSH mutez 0 ;
  0836:                          DIG 3 ;
  0837:                          DUP ;
  0838:                          DUG 4 ;
  0839:                          CADDAR ;
  0840:                          TRANSFER_TOKENS ;
  0841:                          CONS }
  0842:                        { DIG 2 ;
  0843:                          DROP ;
  0844:                          DIG 2 ;
  0845:                          DROP ;
  0846:                          CONTRACT nat ;
  0847:                          NIL operation ;
  0848:                          SWAP ;
  0849:                          IF_SOME {} { PUSH int 214 ; FAILWITH } ;
  0850:                          PUSH mutez 0 ;
  0851:                          DIG 3 ;
  0852:                          DUP ;
  0853:                          DUG 4 ;
  0854:                          CDDDAR ;
  0855:                          TRANSFER_TOKENS ;
  0856:                          CONS } }
  0857:                    { IF_LEFT
  0858:                        { SWAP ;
  0859:                          DUP ;
  0860:                          DUG 2 ;
  0861:                          CAAAR ;
  0862:                          SENDER ;
  0863:                          COMPARE ;
  0864:                          EQ ;
  0865:                          IF {}
  0866:                             { PUSH string "WrongCondition: sp.sender == self.data.administrator" ;
  0867:                               FAILWITH } ;
  0868:                          SWAP ;
  0869:                          DUP ;
  0870:                          DUG 2 ;
  0871:                          CAADR ;
  0872:                          SWAP ;
  0873:                          DUP ;
  0874:                          DUG 2 ;
  0875:                          CAR ;
  0876:                          MEM ;
  0877:                          IF { DIG 2 ; DROP ; DIG 2 ; DROP }
  0878:                             { DIG 2 ;
  0879:                               DROP ;
  0880:                               DIG 2 ;
  0881:                               DROP ;
  0882:                               SWAP ;
  0883:                               DUP ;
  0884:                               CDR ;
  0885:                               SWAP ;
  0886:                               CAR ;
  0887:                               DUP ;
  0888:                               CDR ;
  0889:                               SWAP ;
  0890:                               CAR ;
  0891:                               DUP ;
  0892:                               CAR ;
  0893:                               SWAP ;
  0894:                               CDR ;
  0895:                               DIG 4 ;
  0896:                               DUP ;
  0897:                               DUG 5 ;
  0898:                               CAR ;
  0899:                               PUSH (option (pair (map %approvals address nat) (nat %balance))) (Some (Pair {} 0)) ;
  0900:                               SWAP ;
  0901:                               UPDATE ;
  0902:                               SWAP ;
  0903:                               PAIR ;
  0904:                               PAIR ;
  0905:                               PAIR ;
  0906:                               SWAP } ;
  0907:                          SWAP ;
  0908:                          DUP ;
  0909:                          CDR ;
  0910:                          SWAP ;
  0911:                          CAR ;
  0912:                          DUP ;
  0913:                          CDR ;
  0914:                          SWAP ;
  0915:                          CAR ;
  0916:                          DUP ;
  0917:                          CAR ;
  0918:                          SWAP ;
  0919:                          CDR ;
  0920:                          DUP ;
  0921:                          DIG 5 ;
  0922:                          DUP ;
  0923:                          DUG 6 ;
  0924:                          CAR ;
  0925:                          DUP ;
  0926:                          DUG 2 ;
  0927:                          GET ;
  0928:                          IF_SOME {} { PUSH int 185 ; FAILWITH } ;
  0929:                          DUP ;
  0930:                          CAR ;
  0931:                          SWAP ;
  0932:                          CDR ;
  0933:                          DIG 7 ;
  0934:                          DUP ;
  0935:                          DUG 8 ;
  0936:                          CDR ;
  0937:                          ADD ;
  0938:                          SWAP ;
  0939:                          PAIR ;
  0940:                          SOME ;
  0941:                          SWAP ;
  0942:                          UPDATE ;
  0943:                          SWAP ;
  0944:                          PAIR ;
  0945:                          PAIR ;
  0946:                          PAIR ;
  0947:                          DUP ;
  0948:                          CAR ;
  0949:                          SWAP ;
  0950:                          CDR ;
  0951:                          DUP ;
  0952:                          CAR ;
  0953:                          SWAP ;
  0954:                          CDR ;
  0955:                          DUP ;
  0956:                          CAR ;
  0957:                          SWAP ;
  0958:                          CDR ;
  0959:                          DUP ;
  0960:                          CDR ;
  0961:                          SWAP ;
  0962:                          CAR ;
  0963:                          DIG 5 ;
  0964:                          CDR ;
  0965:                          ADD ;
  0966:                          PAIR ;
  0967:                          SWAP ;
  0968:                          PAIR ;
  0969:                          SWAP ;
  0970:                          PAIR ;
  0971:                          SWAP ;
  0972:                          PAIR ;
  0973:                          NIL operation }
  0974:                        { SWAP ;
  0975:                          DUP ;
  0976:                          DUG 2 ;
  0977:                          CDADAR ;
  0978:                          IF { PUSH string "WrongCondition: ~ self.data.paused" ; FAILWITH } {} ;
  0979:                          DUP ;
  0980:                          NIL operation ;
  0981:                          SWAP ;
  0982:                          ITER { DIG 5 ;
  0983:                                 DUP ;
  0984:                                 DUG 6 ;
  0985:                                 DIG 4 ;
  0986:                                 DIG 2 ;
  0987:                                 DUP ;
  0988:                                 CDDR ;
  0989:                                 SWAP ;
  0990:                                 DUP ;
  0991:                                 DUG 4 ;
  0992:                                 CAR ;
  0993:                                 HASH_KEY ;
  0994:                                 IMPLICIT_ACCOUNT ;
  0995:                                 ADDRESS ;
  0996:                                 PAIR ;
  0997:                                 PAIR %in_param %in_storage ;
  0998:                                 EXEC ;
  0999:                                 DUP ;
  1000:                                 CDDR ;
  1001:                                 DUG 4 ;
  1002:                                 DUP ;
  1003:                                 CAR ;
  1004:                                 ITER { DIG 3 ; SWAP ; CONS ; DUG 2 } ;
  1005:                                 DIG 4 ;
  1006:                                 DUP ;
  1007:                                 DUG 5 ;
  1008:                                 CDDAR ;
  1009:                                 DIG 2 ;
  1010:                                 DUP ;
  1011:                                 CDDR ;
  1012:                                 SWAP ;
  1013:                                 DUP ;
  1014:                                 DUG 4 ;
  1015:                                 CAR ;
  1016:                                 HASH_KEY ;
  1017:                                 IMPLICIT_ACCOUNT ;
  1018:                                 ADDRESS ;
  1019:                                 PAIR ;
  1020:                                 MEM ;
  1021:                                 IF { DUP ;
  1022:                                      CDAR ;
  1023:                                      DIG 5 ;
  1024:                                      DUP ;
  1025:                                      DUG 6 ;
  1026:                                      CDDAR ;
  1027:                                      DIG 3 ;
  1028:                                      DUP ;
  1029:                                      CDDR ;
  1030:                                      SWAP ;
  1031:                                      DUP ;
  1032:                                      DUG 5 ;
  1033:                                      CAR ;
  1034:                                      HASH_KEY ;
  1035:                                      IMPLICIT_ACCOUNT ;
  1036:                                      ADDRESS ;
  1037:                                      PAIR ;
  1038:                                      GET ;
  1039:                                      IF_SOME {} { PUSH int 102 ; FAILWITH } ;
  1040:                                      NOW ;
  1041:                                      SUB ;
  1042:                                      ISNAT ;
  1043:                                      IF_SOME {} { PUSH int 103 ; FAILWITH } ;
  1044:                                      COMPARE ;
  1045:                                      LT }
  1046:                                    { PUSH bool False } ;
  1047:                                 IF { SWAP ; DUP ; DUG 2 ; CDDR ; PUSH string "DUP_PERMIT" ; PAIR ; FAILWITH }
  1048:                                    {} ;
  1049:                                 SWAP ;
  1050:                                 DUP ;
  1051:                                 DUG 2 ;
  1052:                                 CDDR ;
  1053:                                 DIG 5 ;
  1054:                                 DUP ;
  1055:                                 DUG 6 ;
  1056:                                 CADAR ;
  1057:                                 PAIR ;
  1058:                                 SELF ;
  1059:                                 ADDRESS ;
  1060:                                 CHAIN_ID ;
  1061:                                 PAIR ;
  1062:                                 PAIR ;
  1063:                                 PACK ;
  1064:                                 DIG 2 ;
  1065:                                 DUP ;
  1066:                                 CDAR ;
  1067:                                 SWAP ;
  1068:                                 DUP ;
  1069:                                 DUG 4 ;
  1070:                                 CAR ;
  1071:                                 CHECK_SIGNATURE ;
  1072:                                 IF { DROP }
  1073:                                    { SWAP ;
  1074:                                      DUP ;
  1075:                                      DUG 2 ;
  1076:                                      CDDR ;
  1077:                                      DIG 5 ;
  1078:                                      DUP ;
  1079:                                      DUG 6 ;
  1080:                                      CADAR ;
  1081:                                      PAIR ;
  1082:                                      SELF ;
  1083:                                      ADDRESS ;
  1084:                                      CHAIN_ID ;
  1085:                                      PAIR ;
  1086:                                      PAIR ;
  1087:                                      PACK ;
  1088:                                      PUSH string "MISSIGNED" ;
  1089:                                      PAIR ;
  1090:                                      FAILWITH } ;
  1091:                                 DIG 3 ;
  1092:                                 DUP ;
  1093:                                 CAR ;
  1094:                                 SWAP ;
  1095:                                 CDR ;
  1096:                                 DUP ;
  1097:                                 CAR ;
  1098:                                 SWAP ;
  1099:                                 CDR ;
  1100:                                 DUP ;
  1101:                                 CDR ;
  1102:                                 SWAP ;
  1103:                                 CAR ;
  1104:                                 DIG 4 ;
  1105:                                 DUP ;
  1106:                                 CDDR ;
  1107:                                 SWAP ;
  1108:                                 CAR ;
  1109:                                 HASH_KEY ;
  1110:                                 IMPLICIT_ACCOUNT ;
  1111:                                 ADDRESS ;
  1112:                                 PAIR ;
  1113:                                 NOW ;
  1114:                                 SOME ;
  1115:                                 SWAP ;
  1116:                                 UPDATE ;
  1117:                                 PAIR ;
  1118:                                 SWAP ;
  1119:                                 PAIR ;
  1120:                                 SWAP ;
  1121:                                 PAIR ;
  1122:                                 DUP ;
  1123:                                 CDR ;
  1124:                                 SWAP ;
  1125:                                 CAR ;
  1126:                                 DUP ;
  1127:                                 CAR ;
  1128:                                 SWAP ;
  1129:                                 CDR ;
  1130:                                 DUP ;
  1131:                                 CDR ;
  1132:                                 SWAP ;
  1133:                                 CAR ;
  1134:                                 PUSH nat 1 ;
  1135:                                 ADD ;
  1136:                                 PAIR ;
  1137:                                 SWAP ;
  1138:                                 PAIR ;
  1139:                                 PAIR ;
  1140:                                 DUG 2 } ;
  1141:                          SWAP ;
  1142:                          DROP ;
  1143:                          DIG 2 ;
  1144:                          DROP ;
  1145:                          DIG 2 ;
  1146:                          DROP } } }
  1147:                { IF_LEFT
  1148:                    { IF_LEFT
  1149:                        { SWAP ;
  1150:                          DUP ;
  1151:                          DUG 2 ;
  1152:                          CAAAR ;
  1153:                          SENDER ;
  1154:                          COMPARE ;
  1155:                          EQ ;
  1156:                          IF { DIG 2 ; DROP ; DIG 2 ; DROP }
  1157:                             { PUSH string "WrongCondition: sp.sender == self.data.administrator" ;
  1158:                               FAILWITH } ;
  1159:                          SWAP ;
  1160:                          DUP ;
  1161:                          CDR ;
  1162:                          SWAP ;
  1163:                          CAR ;
  1164:                          DUP ;
  1165:                          CDR ;
  1166:                          SWAP ;
  1167:                          CADR ;
  1168:                          DIG 3 ;
  1169:                          PAIR ;
  1170:                          PAIR ;
  1171:                          PAIR }
  1172:                        { SWAP ;
  1173:                          DUP ;
  1174:                          DUG 2 ;
  1175:                          CDADAR ;
  1176:                          IF { PUSH string "WrongCondition: ~ self.data.paused" ; FAILWITH } {} ;
  1177:                          SWAP ;
  1178:                          DUP ;
  1179:                          DUG 2 ;
  1180:                          CADDDR ;
  1181:                          SWAP ;
  1182:                          DUP ;
  1183:                          DUG 2 ;
  1184:                          CDDR ;
  1185:                          COMPARE ;
  1186:                          LE ;
  1187:                          IF {} { PUSH string "MAX_SECONDS_EXCEEDED" ; FAILWITH } ;
  1188:                          SENDER ;
  1189:                          PACK ;
  1190:                          SWAP ;
  1191:                          DUP ;
  1192:                          DUG 2 ;
  1193:                          CAR ;
  1194:                          PACK ;
  1195:                          COMPARE ;
  1196:                          EQ ;
  1197:                          IF {} { PUSH bool False ; FAILWITH } ;
  1198:                          DUP ;
  1199:                          CDAR ;
  1200:                          IF_SOME
  1201:                            { DROP ;
  1202:                              SWAP ;
  1203:                              DUP ;
  1204:                              DUG 2 ;
  1205:                              CDDAR ;
  1206:                              SWAP ;
  1207:                              DUP ;
  1208:                              DUG 2 ;
  1209:                              CDAR ;
  1210:                              IF_SOME {} { PUSH int 132 ; FAILWITH } ;
  1211:                              DIG 2 ;
  1212:                              DUP ;
  1213:                              DUG 3 ;
  1214:                              CAR ;
  1215:                              PAIR ;
  1216:                              MEM ;
  1217:                              IF {} { PUSH string "PERMIT_NONEXISTENT" ; FAILWITH } ;
  1218:                              SWAP ;
  1219:                              DUP ;
  1220:                              DUG 2 ;
  1221:                              CDADDR ;
  1222:                              SWAP ;
  1223:                              DUP ;
  1224:                              DUG 2 ;
  1225:                              CDAR ;
  1226:                              IF_SOME {} { PUSH int 132 ; FAILWITH } ;
  1227:                              DIG 2 ;
  1228:                              DUP ;
  1229:                              DUG 3 ;
  1230:                              CAR ;
  1231:                              PAIR ;
  1232:                              MEM ;
  1233:                              IF { SWAP ;
  1234:                                   DUP ;
  1235:                                   DUG 2 ;
  1236:                                   CDADDR ;
  1237:                                   SWAP ;
  1238:                                   DUP ;
  1239:                                   DUG 2 ;
  1240:                                   CDAR ;
  1241:                                   IF_SOME {} { PUSH int 132 ; FAILWITH } ;
  1242:                                   DIG 2 ;
  1243:                                   DUP ;
  1244:                                   DUG 3 ;
  1245:                                   CAR ;
  1246:                                   PAIR ;
  1247:                                   GET ;
  1248:                                   IF_SOME {} { PUSH int 137 ; FAILWITH } ;
  1249:                                   IF_SOME { DROP ; PUSH bool True } { PUSH bool False } }
  1250:                                 { PUSH bool False } ;
  1251:                              IF { SWAP ;
  1252:                                   DUP ;
  1253:                                   DUG 2 ;
  1254:                                   CDADDR ;
  1255:                                   SWAP ;
  1256:                                   DUP ;
  1257:                                   DUG 2 ;
  1258:                                   CDAR ;
  1259:                                   IF_SOME {} { PUSH int 132 ; FAILWITH } ;
  1260:                                   DIG 2 ;
  1261:                                   DUP ;
  1262:                                   DUG 3 ;
  1263:                                   CAR ;
  1264:                                   PAIR ;
  1265:                                   GET ;
  1266:                                   IF_SOME {} { PUSH int 138 ; FAILWITH } ;
  1267:                                   IF_SOME {} { PUSH int 138 ; FAILWITH } ;
  1268:                                   DIG 2 ;
  1269:                                   DUP ;
  1270:                                   DUG 3 ;
  1271:                                   CDDAR ;
  1272:                                   DIG 2 ;
  1273:                                   DUP ;
  1274:                                   DUG 3 ;
  1275:                                   CDAR ;
  1276:                                   IF_SOME {} { PUSH int 132 ; FAILWITH } ;
  1277:                                   DIG 3 ;
  1278:                                   DUP ;
  1279:                                   DUG 4 ;
  1280:                                   CAR ;
  1281:                                   PAIR ;
  1282:                                   GET ;
  1283:                                   IF_SOME {} { PUSH int 135 ; FAILWITH } ;
  1284:                                   NOW ;
  1285:                                   SUB ;
  1286:                                   ISNAT ;
  1287:                                   IF_SOME {} { PUSH int 140 ; FAILWITH } ;
  1288:                                   COMPARE ;
  1289:                                   LT ;
  1290:                                   IF { DIG 2 ; DROP ; DIG 2 ; DROP }
  1291:                                      { PUSH string "PERMIT_REVOKED" ; FAILWITH } }
  1292:                                 { SWAP ;
  1293:                                   DUP ;
  1294:                                   DUG 2 ;
  1295:                                   CDDDDR ;
  1296:                                   SWAP ;
  1297:                                   DUP ;
  1298:                                   DUG 2 ;
  1299:                                   CAR ;
  1300:                                   MEM ;
  1301:                                   IF { SWAP ;
  1302:                                        DUP ;
  1303:                                        DUG 2 ;
  1304:                                        CDDDDR ;
  1305:                                        SWAP ;
  1306:                                        DUP ;
  1307:                                        DUG 2 ;
  1308:                                        CAR ;
  1309:                                        GET ;
  1310:                                        IF_SOME {} { PUSH int 143 ; FAILWITH } ;
  1311:                                        IF_SOME { DROP ; PUSH bool True } { PUSH bool False } }
  1312:                                      { PUSH bool False } ;
  1313:                                   IF { SWAP ;
  1314:                                        DUP ;
  1315:                                        DUG 2 ;
  1316:                                        CDDDDR ;
  1317:                                        SWAP ;
  1318:                                        DUP ;
  1319:                                        DUG 2 ;
  1320:                                        CAR ;
  1321:                                        GET ;
  1322:                                        IF_SOME {} { PUSH int 144 ; FAILWITH } ;
  1323:                                        IF_SOME {} { PUSH int 144 ; FAILWITH } ;
  1324:                                        DIG 2 ;
  1325:                                        DUP ;
  1326:                                        DUG 3 ;
  1327:                                        CDDAR ;
  1328:                                        DIG 2 ;
  1329:                                        DUP ;
  1330:                                        DUG 3 ;
  1331:                                        CDAR ;
  1332:                                        IF_SOME {} { PUSH int 132 ; FAILWITH } ;
  1333:                                        DIG 3 ;
  1334:                                        DUP ;
  1335:                                        DUG 4 ;
  1336:                                        CAR ;
  1337:                                        PAIR ;
  1338:                                        GET ;
  1339:                                        IF_SOME {} { PUSH int 135 ; FAILWITH } ;
  1340:                                        NOW ;
  1341:                                        SUB ;
  1342:                                        ISNAT ;
  1343:                                        IF_SOME {} { PUSH int 146 ; FAILWITH } ;
  1344:                                        COMPARE ;
  1345:                                        LT ;
  1346:                                        IF { DIG 2 ; DROP ; DIG 2 ; DROP }
  1347:                                           { PUSH string "PERMIT_REVOKED" ; FAILWITH } }
  1348:                                      { SWAP ;
  1349:                                        DUP ;
  1350:                                        CADDAR ;
  1351:                                        SWAP ;
  1352:                                        DUP ;
  1353:                                        DUG 3 ;
  1354:                                        CDDAR ;
  1355:                                        DIG 2 ;
  1356:                                        DUP ;
  1357:                                        DUG 3 ;
  1358:                                        CDAR ;
  1359:                                        IF_SOME {} { PUSH int 132 ; FAILWITH } ;
  1360:                                        DIG 3 ;
  1361:                                        DUP ;
  1362:                                        DUG 4 ;
  1363:                                        CAR ;
  1364:                                        PAIR ;
  1365:                                        GET ;
  1366:                                        IF_SOME {} { PUSH int 135 ; FAILWITH } ;
  1367:                                        NOW ;
  1368:                                        SUB ;
  1369:                                        ISNAT ;
  1370:                                        IF_SOME {} { PUSH int 149 ; FAILWITH } ;
  1371:                                        COMPARE ;
  1372:                                        LT ;
  1373:                                        IF { DIG 2 ; DROP ; DIG 2 ; DROP }
  1374:                                           { PUSH string "PERMIT_REVOKED" ; FAILWITH } } } ;
  1375:                              SWAP ;
  1376:                              DUP ;
  1377:                              CAR ;
  1378:                              SWAP ;
  1379:                              CDR ;
  1380:                              DUP ;
  1381:                              CDR ;
  1382:                              SWAP ;
  1383:                              CAR ;
  1384:                              DUP ;
  1385:                              CAR ;
  1386:                              SWAP ;
  1387:                              CDR ;
  1388:                              DUP ;
  1389:                              CAR ;
  1390:                              SWAP ;
  1391:                              CDR ;
  1392:                              DIG 5 ;
  1393:                              DUP ;
  1394:                              DUG 6 ;
  1395:                              CDAR ;
  1396:                              IF_SOME {} { PUSH int 132 ; FAILWITH } ;
  1397:                              DIG 6 ;
  1398:                              DUP ;
  1399:                              DUG 7 ;
  1400:                              CAR ;
  1401:                              PAIR ;
  1402:                              DIG 6 ;
  1403:                              CDDR ;
  1404:                              SOME ;
  1405:                              SOME ;
  1406:                              SWAP ;
  1407:                              UPDATE ;
  1408:                              SWAP ;
  1409:                              PAIR ;
  1410:                              SWAP ;
  1411:                              PAIR ;
  1412:                              PAIR ;
  1413:                              SWAP ;
  1414:                              PAIR }
  1415:                            { DIG 2 ;
  1416:                              DROP ;
  1417:                              DIG 2 ;
  1418:                              DROP ;
  1419:                              SWAP ;
  1420:                              DUP ;
  1421:                              CAR ;
  1422:                              SWAP ;
  1423:                              CDR ;
  1424:                              DUP ;
  1425:                              CAR ;
  1426:                              SWAP ;
  1427:                              CDR ;
  1428:                              DUP ;
  1429:                              CAR ;
  1430:                              SWAP ;
  1431:                              CDR ;
  1432:                              DUP ;
  1433:                              CAR ;
  1434:                              SWAP ;
  1435:                              CDR ;
  1436:                              DIG 5 ;
  1437:                              DUP ;
  1438:                              CAR ;
  1439:                              SWAP ;
  1440:                              CDDR ;
  1441:                              SOME ;
  1442:                              SOME ;
  1443:                              SWAP ;
  1444:                              UPDATE ;
  1445:                              SWAP ;
  1446:                              PAIR ;
  1447:                              SWAP ;
  1448:                              PAIR ;
  1449:                              SWAP ;
  1450:                              PAIR ;
  1451:                              SWAP ;
  1452:                              PAIR } } ;
  1453:                      NIL operation }
  1454:                    { IF_LEFT
  1455:                        { SWAP ;
  1456:                          DUP ;
  1457:                          DUG 2 ;
  1458:                          CAAAR ;
  1459:                          SENDER ;
  1460:                          COMPARE ;
  1461:                          EQ ;
  1462:                          IF { DIG 2 ; DROP ; DIG 2 ; DROP }
  1463:                             { PUSH string "WrongCondition: sp.sender == self.data.administrator" ;
  1464:                               FAILWITH } ;
  1465:                          SWAP ;
  1466:                          DUP ;
  1467:                          CAR ;
  1468:                          SWAP ;
  1469:                          CDR ;
  1470:                          DUP ;
  1471:                          CDR ;
  1472:                          SWAP ;
  1473:                          CAR ;
  1474:                          DUP ;
  1475:                          CAR ;
  1476:                          SWAP ;
  1477:                          CDDR ;
  1478:                          DIG 4 ;
  1479:                          PAIR ;
  1480:                          SWAP ;
  1481:                          PAIR ;
  1482:                          PAIR ;
  1483:                          SWAP ;
  1484:                          PAIR ;
  1485:                          NIL operation }
  1486:                        { SENDER ;
  1487:                          DIG 3 ;
  1488:                          DUP ;
  1489:                          DUG 4 ;
  1490:                          DIG 3 ;
  1491:                          DIG 3 ;
  1492:                          DUP ;
  1493:                          DUG 4 ;
  1494:                          PAIR %in_param %in_storage ;
  1495:                          EXEC ;
  1496:                          DUP ;
  1497:                          CDDR ;
  1498:                          DUG 3 ;
  1499:                          DUP ;
  1500:                          CAR ;
  1501:                          NIL operation ;
  1502:                          SWAP ;
  1503:                          ITER { CONS } ;
  1504:                          SWAP ;
  1505:                          DUP ;
  1506:                          DUG 2 ;
  1507:                          CDAR ;
  1508:                          IF { DIG 2 ; DROP ; DIG 2 ; DUP ; DUG 3 ; CAR ; DUG 2 } {} ;
  1509:                          DIG 4 ;
  1510:                          DUP ;
  1511:                          DUG 5 ;
  1512:                          CAAAR ;
  1513:                          DIG 3 ;
  1514:                          DUP ;
  1515:                          DUG 4 ;
  1516:                          COMPARE ;
  1517:                          EQ ;
  1518:                          IF { PUSH bool True }
  1519:                             { DIG 4 ;
  1520:                               DUP ;
  1521:                               DUG 5 ;
  1522:                               CDADAR ;
  1523:                               IF { PUSH bool False }
  1524:                                  { DIG 2 ;
  1525:                                    DUP ;
  1526:                                    DUG 3 ;
  1527:                                    DIG 4 ;
  1528:                                    DUP ;
  1529:                                    DUG 5 ;
  1530:                                    CAR ;
  1531:                                    COMPARE ;
  1532:                                    EQ ;
  1533:                                    IF { PUSH bool True }
  1534:                                       { DIG 3 ;
  1535:                                         DUP ;
  1536:                                         DUG 4 ;
  1537:                                         CDDR ;
  1538:                                         DIG 5 ;
  1539:                                         DUP ;
  1540:                                         DUG 6 ;
  1541:                                         CAADR ;
  1542:                                         DIG 5 ;
  1543:                                         DUP ;
  1544:                                         DUG 6 ;
  1545:                                         CAR ;
  1546:                                         GET ;
  1547:                                         IF_SOME {} { PUSH int 26 ; FAILWITH } ;
  1548:                                         CAR ;
  1549:                                         DIG 4 ;
  1550:                                         DUP ;
  1551:                                         DUG 5 ;
  1552:                                         GET ;
  1553:                                         IF_SOME {} { PUSH int 26 ; FAILWITH } ;
  1554:                                         COMPARE ;
  1555:                                         GE } } } ;
  1556:                          IF {}
  1557:                             { PUSH string
  1558:                                    "WrongCondition: (sender.value == self.data.administrator) | ((~ self.data.paused) & ((params.from_ == sender.value) | (self.data.balances[params.from_].approvals[sender.value] >= params.value)))" ;
  1559:                               FAILWITH } ;
  1560:                          DIG 4 ;
  1561:                          DUP ;
  1562:                          DUG 5 ;
  1563:                          CAADR ;
  1564:                          DIG 4 ;
  1565:                          DUP ;
  1566:                          DUG 5 ;
  1567:                          CDAR ;
  1568:                          MEM ;
  1569:                          IF {}
  1570:                             { DIG 4 ;
  1571:                               DUP ;
  1572:                               CDR ;
  1573:                               SWAP ;
  1574:                               CAR ;
  1575:                               DUP ;
  1576:                               CDR ;
  1577:                               SWAP ;
  1578:                               CAR ;
  1579:                               DUP ;
  1580:                               CAR ;
  1581:                               SWAP ;
  1582:                               CDR ;
  1583:                               DIG 7 ;
  1584:                               DUP ;
  1585:                               DUG 8 ;
  1586:                               CDAR ;
  1587:                               PUSH (option (pair (map %approvals address nat) (nat %balance))) (Some (Pair {} 0)) ;
  1588:                               SWAP ;
  1589:                               UPDATE ;
  1590:                               SWAP ;
  1591:                               PAIR ;
  1592:                               PAIR ;
  1593:                               PAIR ;
  1594:                               DUG 4 } ;
  1595:                          DIG 3 ;
  1596:                          DUP ;
  1597:                          DUG 4 ;
  1598:                          CDDR ;
  1599:                          DIG 5 ;
  1600:                          DUP ;
  1601:                          DUG 6 ;
  1602:                          CAADR ;
  1603:                          DIG 5 ;
  1604:                          DUP ;
  1605:                          DUG 6 ;
  1606:                          CAR ;
  1607:                          GET ;
  1608:                          IF_SOME {} { PUSH int 28 ; FAILWITH } ;
  1609:                          CDR ;
  1610:                          COMPARE ;
  1611:                          GE ;
  1612:                          IF {}
  1613:                             { PUSH string
  1614:                                    "WrongCondition: self.data.balances[params.from_].balance >= params.value" ;
  1615:                               FAILWITH } ;
  1616:                          DIG 4 ;
  1617:                          DUP ;
  1618:                          DUG 5 ;
  1619:                          DUP ;
  1620:                          CDR ;
  1621:                          SWAP ;
  1622:                          CAR ;
  1623:                          DUP ;
  1624:                          CDR ;
  1625:                          SWAP ;
  1626:                          CAR ;
  1627:                          DUP ;
  1628:                          CAR ;
  1629:                          SWAP ;
  1630:                          CDR ;
  1631:                          DUP ;
  1632:                          DIG 8 ;
  1633:                          DUP ;
  1634:                          DUG 9 ;
  1635:                          CAR ;
  1636:                          DUP ;
  1637:                          DUG 2 ;
  1638:                          GET ;
  1639:                          IF_SOME {} { PUSH int 29 ; FAILWITH } ;
  1640:                          CAR ;
  1641:                          DIG 9 ;
  1642:                          DUP ;
  1643:                          DUG 10 ;
  1644:                          CDDR ;
  1645:                          DIG 11 ;
  1646:                          CAADR ;
  1647:                          DIG 11 ;
  1648:                          DUP ;
  1649:                          DUG 12 ;
  1650:                          CAR ;
  1651:                          GET ;
  1652:                          IF_SOME {} { PUSH int 30 ; FAILWITH } ;
  1653:                          CDR ;
  1654:                          SUB ;
  1655:                          ISNAT ;
  1656:                          IF_SOME {} { PUSH int 29 ; FAILWITH } ;
  1657:                          SWAP ;
  1658:                          PAIR ;
  1659:                          SOME ;
  1660:                          SWAP ;
  1661:                          UPDATE ;
  1662:                          SWAP ;
  1663:                          PAIR ;
  1664:                          PAIR ;
  1665:                          PAIR ;
  1666:                          DUP ;
  1667:                          CDR ;
  1668:                          SWAP ;
  1669:                          CAR ;
  1670:                          DUP ;
  1671:                          CDR ;
  1672:                          SWAP ;
  1673:                          CAR ;
  1674:                          DUP ;
  1675:                          CAR ;
  1676:                          SWAP ;
  1677:                          CDR ;
  1678:                          DUP ;
  1679:                          DIG 8 ;
  1680:                          DUP ;
  1681:                          DUG 9 ;
  1682:                          CDAR ;
  1683:                          DUP ;
  1684:                          DUG 2 ;
  1685:                          GET ;
  1686:                          IF_SOME {} { PUSH int 31 ; FAILWITH } ;
  1687:                          DUP ;
  1688:                          CAR ;
  1689:                          SWAP ;
  1690:                          CDR ;
  1691:                          DIG 10 ;
  1692:                          DUP ;
  1693:                          DUG 11 ;
  1694:                          CDDR ;
  1695:                          ADD ;
  1696:                          SWAP ;
  1697:                          PAIR ;
  1698:                          SOME ;
  1699:                          SWAP ;
  1700:                          UPDATE ;
  1701:                          SWAP ;
  1702:                          PAIR ;
  1703:                          PAIR ;
  1704:                          PAIR ;
  1705:                          DUG 4 ;
  1706:                          DIG 2 ;
  1707:                          DUP ;
  1708:                          DUG 3 ;
  1709:                          DIG 4 ;
  1710:                          DUP ;
  1711:                          DUG 5 ;
  1712:                          CAR ;
  1713:                          COMPARE ;
  1714:                          NEQ ;
  1715:                          IF { DIG 2 ; DUP ; DUG 3 ; DIG 5 ; DUP ; DUG 6 ; CAAAR ; COMPARE ; NEQ }
  1716:                             { PUSH bool False } ;
  1717:                          IF { SWAP ;
  1718:                               DROP ;
  1719:                               DIG 4 ;
  1720:                               DROP ;
  1721:                               DIG 4 ;
  1722:                               DROP ;
  1723:                               DIG 3 ;
  1724:                               DUP ;
  1725:                               DUG 4 ;
  1726:                               DUP ;
  1727:                               CDR ;
  1728:                               SWAP ;
  1729:                               CAR ;
  1730:                               DUP ;
  1731:                               CDR ;
  1732:                               SWAP ;
  1733:                               CAR ;
  1734:                               DUP ;
  1735:                               CAR ;
  1736:                               SWAP ;
  1737:                               CDR ;
  1738:                               DUP ;
  1739:                               DIG 7 ;
  1740:                               DUP ;
  1741:                               DUG 8 ;
  1742:                               CAR ;
  1743:                               DUP ;
  1744:                               DUG 2 ;
  1745:                               GET ;
  1746:                               IF_SOME {} { PUSH int 33 ; FAILWITH } ;
  1747:                               DUP ;
  1748:                               CDR ;
  1749:                               SWAP ;
  1750:                               CAR ;
  1751:                               DIG 8 ;
  1752:                               DIG 9 ;
  1753:                               DUP ;
  1754:                               DUG 10 ;
  1755:                               CDDR ;
  1756:                               DIG 11 ;
  1757:                               CAADR ;
  1758:                               DIG 11 ;
  1759:                               CAR ;
  1760:                               GET ;
  1761:                               IF_SOME {} { PUSH int 34 ; FAILWITH } ;
  1762:                               CAR ;
  1763:                               DIG 2 ;
  1764:                               DUP ;
  1765:                               DUG 3 ;
  1766:                               GET ;
  1767:                               IF_SOME {} { PUSH int 34 ; FAILWITH } ;
  1768:                               SUB ;
  1769:                               ISNAT ;
  1770:                               IF_SOME {} { PUSH int 33 ; FAILWITH } ;
  1771:                               SOME ;
  1772:                               SWAP ;
  1773:                               UPDATE ;
  1774:                               PAIR ;
  1775:                               SOME ;
  1776:                               SWAP ;
  1777:                               UPDATE ;
  1778:                               SWAP ;
  1779:                               PAIR ;
  1780:                               PAIR ;
  1781:                               PAIR ;
  1782:                               SWAP }
  1783:                             { SWAP ; DROP ; SWAP ; DROP ; SWAP ; DROP ; DIG 2 ; DROP ; DIG 2 ; DROP } } } } } ;
  1784:          NIL operation ;
  1785:          SWAP ;
  1786:          ITER { CONS } ;
  1787:          PAIR } }
At line 1090 characters 37 to 45,
script reached FAILWITH instruction
with
  (Pair "MISSIGNED"
        0x05070707070a000000047a06a7700a00000016015d22ffe866052e73c7dc6e964601fdbc5913572c00070700000a00000020877b50b43b81b9d2c5a6c56087fab148a6622741cd0e79557e6b6131b8b5e49b)
Fatal error:
  transfer simulation failed
Warning:
  
   The node you are connecting to claims to be running in a
                    Tezos TEST SANDBOX.
      Do NOT use your fundraiser keys on this network.
  You should not see this message if you are not a developer.

Signature: edsigtz1zkDTMU7E6GUTFgJzfNyuPqxPLt7SDZf5yZS3YuTdSepcMpDPeNYMUQ1FQ7T3gXjv2NMoqzHKrZrdCNtSRxMhWMJA86X
Warning:
  
   The node you are connecting to claims to be running in a
                    Tezos TEST SANDBOX.
      Do NOT use your fundraiser keys on this network.
  You should not see this message if you are not a developer.

Node is bootstrapped, ready for injecting operations.
Estimated gas: 337543 units (will add 100 for safety)
Estimated storage: 71 bytes added (will add 20 for safety)
Operation successfully injected in the node.
Operation hash is 'ooRA7EbFJ3d7YniFcFe844rGzmoKEvxscSAccqYeZqfDFRLow7v'
Waiting for the operation to be included...
Operation found in block: BM49Tq9TGzam1tyeZYtbR2aUEV4jMvBdu2CsdjWGTJGSz8sNSBA (pass: 3, offset: 0)
This sequence of operations was run:
  Manager signed operations:
    From: tz1b7tUupMgCNw2cCLpKTkSD1NZzB5TkP2sv
    Fee to the baker: ꜩ0.034236
    Expected counter: 1
    Gas limit: 337643
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
                        (Pair "edsigtz1zkDTMU7E6GUTFgJzfNyuPqxPLt7SDZf5yZS3YuTdSepcMpDPeNYMUQ1FQ7T3gXjv2NMoqzHKrZrdCNtSRxMhWMJA86X"
                              0x877b50b43b81b9d2c5a6c56087fab148a6622741cd0e79557e6b6131b8b5e49b) }
      This transaction was successfully applied
      Updated storage:
        (Pair (Pair (Pair 0x000002298c03ed7d454a101eb7022bc95f7e5f41ac78 0)
                    (Pair 1 (Pair 50000 2628000)))
              (Pair (Pair 1 (Pair False 2)) (Pair 3 (Pair 10 4))))
      Updated big_maps:
        Set map(3)[(Pair 0x0000e7670f32038107a59a2b9cfefae36ea21f5aa63c
              0x877b50b43b81b9d2c5a6c56087fab148a6622741cd0e79557e6b6131b8b5e49b)] to 1605912176
      Storage size: 13928 bytes
      Paid storage size diff: 71 bytes
      Consumed gas: 337543
      Balance updates:
        tz1b7tUupMgCNw2cCLpKTkSD1NZzB5TkP2sv ... -ꜩ0.071

The operation has only been included 0 blocks ago.
We recommend to wait more.
Use command
  tezos-client wait for ooRA7EbFJ3d7YniFcFe844rGzmoKEvxscSAccqYeZqfDFRLow7v to be included --confirmations 30 --branch BLJREkkiBr4nUPtinMCaHUPH4uUDppL3gRCfZ4GYFBnpmY6ihrS
and/or an external block explorer.
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
      Entrypoint: transfer
      Parameter: (Pair "tz1gjaF81ZRRvdzjobyfVNsAeSC6PScjfQwN"
                       (Pair "tz1faswCTDciRzE4oJ9jn2Vm2dvjeyA9fUzU" 5))
      This operation FAILED.

Runtime error in contract KT1H5ELRW3wmVMuZPJwL3DEUkCc5B6gH4M9H:
  0001: { parameter
  0002:     (or (or (or (pair %approve (address %spender) (nat %value))
  0003:                 (or (pair %burn (address %address) (nat %value))
  0004:                     (list %delete_permits (pair address bytes))))
  0005:             (or (or (address %getAdministrator)
  0006:                     (pair %getAllowance
  0007:                        (pair %arg (address %owner) (address %spender))
  0008:                        (address %target)))
  0009:                 (or (pair %getBalance (address %arg) (address %target)) (address %getCounter))))
  0010:         (or (or (or (address %getDefaultExpiry) (address %getTotalSupply))
  0011:                 (or (pair %mint (address %address) (nat %value))
  0012:                     (list %permit (pair key (pair signature bytes)))))
  0013:             (or (or (address %setAdministrator)
  0014:                     (pair %setExpiry (address %address) (pair (option %permit bytes) (nat %seconds))))
  0015:                 (or (bool %setPause)
  0016:                     (pair %transfer (address %from_) (pair (address %to_) (nat %value))))))) ;
  0017:   storage
  0018:     (pair (pair (pair (address %administrator)
  0019:                       (big_map %balances address (pair (map %approvals address nat) (nat %balance))))
  0020:                 (pair (nat %counter) (pair (nat %default_expiry) (nat %max_expiry))))
  0021:           (pair (pair (big_map %metadata string bytes)
  0022:                       (pair (bool %paused) (big_map %permit_expiries (pair address bytes) (option nat))))
  0023:                 (pair (big_map %permits (pair address bytes) timestamp)
  0024:                       (pair (nat %totalSupply) (big_map %user_expiries address (option nat)))))) ;
  0025:   code { LAMBDA
  0026:            (pair (pair %in_param address bytes)
  0027:                  (pair %in_storage
  0028:                     (pair (pair (address %administrator)
  0029:                                 (big_map %balances address (pair (map %approvals address nat) (nat %balance))))
  0030:                           (pair (nat %counter) (pair (nat %default_expiry) (nat %max_expiry))))
  0031:                     (pair (pair (big_map %metadata string bytes)
  0032:                                 (pair (bool %paused) (big_map %permit_expiries (pair address bytes) (option nat))))
  0033:                           (pair (big_map %permits (pair address bytes) timestamp)
  0034:                                 (pair (nat %totalSupply) (big_map %user_expiries address (option nat)))))))
  0035:            (pair (list %operations operation)
  0036:                  (pair (nat %result)
  0037:                        (pair %storage
  0038:                           (pair (pair (address %administrator)
  0039:                                       (big_map %balances address (pair (map %approvals address nat) (nat %balance))))
  0040:                                 (pair (nat %counter) (pair (nat %default_expiry) (nat %max_expiry))))
  0041:                           (pair (pair (big_map %metadata string bytes)
  0042:                                       (pair (bool %paused) (big_map %permit_expiries (pair address bytes) (option nat))))
  0043:                                 (pair (big_map %permits (pair address bytes) timestamp)
  0044:                                       (pair (nat %totalSupply) (big_map %user_expiries address (option nat))))))))
  0045:            { NIL operation ;
  0046:              SWAP ;
  0047:              DUP ;
  0048:              DUG 2 ;
  0049:              CDR ;
  0050:              DUP ;
  0051:              CDADDR ;
  0052:              DIG 3 ;
  0053:              DUP ;
  0054:              DUG 4 ;
  0055:              CAR ;
  0056:              MEM ;
  0057:              IF { DUP ;
  0058:                   CDADDR ;
  0059:                   DIG 3 ;
  0060:                   DUP ;
  0061:                   DUG 4 ;
  0062:                   CAR ;
  0063:                   GET ;
  0064:                   IF_SOME {} { PUSH int 114 ; FAILWITH } ;
  0065:                   IF_SOME { DROP ; PUSH bool True } { PUSH bool False } }
  0066:                 { PUSH bool False } ;
  0067:              IF { DUP ;
  0068:                   CDADDR ;
  0069:                   DIG 3 ;
  0070:                   CAR ;
  0071:                   GET ;
  0072:                   IF_SOME {} { PUSH int 115 ; FAILWITH } ;
  0073:                   IF_SOME {} { PUSH int 115 ; FAILWITH } }
  0074:                 { DUP ;
  0075:                   CDDDDR ;
  0076:                   DIG 3 ;
  0077:                   DUP ;
  0078:                   DUG 4 ;
  0079:                   CAAR ;
  0080:                   MEM ;
  0081:                   IF { DUP ;
  0082:                        CDDDDR ;
  0083:                        DIG 3 ;
  0084:                        DUP ;
  0085:                        DUG 4 ;
  0086:                        CAAR ;
  0087:                        GET ;
  0088:                        IF_SOME {} { PUSH int 118 ; FAILWITH } ;
  0089:                        IF_SOME { DROP ; PUSH bool True } { PUSH bool False } }
  0090:                      { PUSH bool False } ;
  0091:                   IF { DUP ;
  0092:                        CDDDDR ;
  0093:                        DIG 3 ;
  0094:                        CAAR ;
  0095:                        GET ;
  0096:                        IF_SOME {} { PUSH int 119 ; FAILWITH } ;
  0097:                        IF_SOME {} { PUSH int 119 ; FAILWITH } }
  0098:                      { DIG 2 ; DROP ; DUP ; CADDAR } } ;
  0099:              PAIR %result %storage ;
  0100:              SWAP ;
  0101:              PAIR %operations } ;
  0102:          SWAP ;
  0103:          LAMBDA
  0104:            (pair (pair %in_param (address %from_) (pair (address %to_) (nat %value)))
  0105:                  (pair %in_storage
  0106:                     (pair (pair (address %administrator)
  0107:                                 (big_map %balances address (pair (map %approvals address nat) (nat %balance))))
  0108:                           (pair (nat %counter) (pair (nat %default_expiry) (nat %max_expiry))))
  0109:                     (pair (pair (big_map %metadata string bytes)
  0110:                                 (pair (bool %paused) (big_map %permit_expiries (pair address bytes) (option nat))))
  0111:                           (pair (big_map %permits (pair address bytes) timestamp)
  0112:                                 (pair (nat %totalSupply) (big_map %user_expiries address (option nat)))))))
  0113:            (pair (list %operations operation)
  0114:                  (pair (bool %result)
  0115:                        (pair %storage
  0116:                           (pair (pair (address %administrator)
  0117:                                       (big_map %balances address (pair (map %approvals address nat) (nat %balance))))
  0118:                                 (pair (nat %counter) (pair (nat %default_expiry) (nat %max_expiry))))
  0119:                           (pair (pair (big_map %metadata string bytes)
  0120:                                       (pair (bool %paused) (big_map %permit_expiries (pair address bytes) (option nat))))
  0121:                                 (pair (big_map %permits (pair address bytes) timestamp)
  0122:                                       (pair (nat %totalSupply) (big_map %user_expiries address (option nat))))))))
  0123:            { NIL operation ;
  0124:              SWAP ;
  0125:              DUP ;
  0126:              DUG 2 ;
  0127:              CDR ;
  0128:              DUP ;
  0129:              CDDAR ;
  0130:              DIG 3 ;
  0131:              DUP ;
  0132:              DUG 4 ;
  0133:              CAR ;
  0134:              PACK ;
  0135:              BLAKE2B ;
  0136:              DIG 4 ;
  0137:              DUP ;
  0138:              DUG 5 ;
  0139:              CAAR ;
  0140:              PAIR ;
  0141:              MEM ;
  0142:              IF { DUP ;
  0143:                   CDADDR ;
  0144:                   DIG 3 ;
  0145:                   DUP ;
  0146:                   DUG 4 ;
  0147:                   CAR ;
  0148:                   PACK ;
  0149:                   BLAKE2B ;
  0150:                   DIG 4 ;
  0151:                   DUP ;
  0152:                   DUG 5 ;
  0153:                   CAAR ;
  0154:                   PAIR ;
  0155:                   MEM ;
  0156:                   IF { DUP ;
  0157:                        CDADDR ;
  0158:                        DIG 3 ;
  0159:                        DUP ;
  0160:                        DUG 4 ;
  0161:                        CAR ;
  0162:                        PACK ;
  0163:                        BLAKE2B ;
  0164:                        DIG 4 ;
  0165:                        DUP ;
  0166:                        DUG 5 ;
  0167:                        CAAR ;
  0168:                        PAIR ;
  0169:                        GET ;
  0170:                        IF_SOME {} { PUSH int 67 ; FAILWITH } ;
  0171:                        IF_SOME { DROP ; PUSH bool True } { PUSH bool False } }
  0172:                      { PUSH bool False } ;
  0173:                   IF { DUP ;
  0174:                        CDADDR ;
  0175:                        DIG 3 ;
  0176:                        DUP ;
  0177:                        DUG 4 ;
  0178:                        CAR ;
  0179:                        PACK ;
  0180:                        BLAKE2B ;
  0181:                        DIG 4 ;
  0182:                        DUP ;
  0183:                        DUG 5 ;
  0184:                        CAAR ;
  0185:                        PAIR ;
  0186:                        GET ;
  0187:                        IF_SOME {} { PUSH int 68 ; FAILWITH } ;
  0188:                        IF_SOME {} { PUSH int 68 ; FAILWITH } }
  0189:                      { DUP ;
  0190:                        CDDDDR ;
  0191:                        DIG 3 ;
  0192:                        DUP ;
  0193:                        DUG 4 ;
  0194:                        CAAR ;
  0195:                        MEM ;
  0196:                        IF { DUP ;
  0197:                             CDDDDR ;
  0198:                             DIG 3 ;
  0199:                             DUP ;
  0200:                             DUG 4 ;
  0201:                             CAAR ;
  0202:                             GET ;
  0203:                             IF_SOME {} { PUSH int 70 ; FAILWITH } ;
  0204:                             IF_SOME { DROP ; PUSH bool True } { PUSH bool False } }
  0205:                           { PUSH bool False } ;
  0206:                        IF { DUP ;
  0207:                             CDDDDR ;
  0208:                             DIG 3 ;
  0209:                             DUP ;
  0210:                             DUG 4 ;
  0211:                             CAAR ;
  0212:                             GET ;
  0213:                             IF_SOME {} { PUSH int 71 ; FAILWITH } ;
  0214:                             IF_SOME {} { PUSH int 71 ; FAILWITH } }
  0215:                           { DUP ; CADDAR } } ;
  0216:                   SWAP ;
  0217:                   DUP ;
  0218:                   DUG 2 ;
  0219:                   CDDAR ;
  0220:                   DIG 4 ;
  0221:                   DUP ;
  0222:                   DUG 5 ;
  0223:                   CAR ;
  0224:                   PACK ;
  0225:                   BLAKE2B ;
  0226:                   DIG 5 ;
  0227:                   DUP ;
  0228:                   DUG 6 ;
  0229:                   CAAR ;
  0230:                   PAIR ;
  0231:                   GET ;
  0232:                   IF_SOME {} { PUSH int 66 ; FAILWITH } ;
  0233:                   NOW ;
  0234:                   SUB ;
  0235:                   ISNAT ;
  0236:                   IF_SOME {} { PUSH int 76 ; FAILWITH } ;
  0237:                   COMPARE ;
  0238:                   GE ;
  0239:                   IF { DUP ;
  0240:                        CDDAR ;
  0241:                        DIG 3 ;
  0242:                        DUP ;
  0243:                        DUG 4 ;
  0244:                        CAR ;
  0245:                        PACK ;
  0246:                        BLAKE2B ;
  0247:                        DIG 4 ;
  0248:                        DUP ;
  0249:                        DUG 5 ;
  0250:                        CAAR ;
  0251:                        PAIR ;
  0252:                        MEM ;
  0253:                        IF { DUP ;
  0254:                             CAR ;
  0255:                             SWAP ;
  0256:                             CDR ;
  0257:                             DUP ;
  0258:                             CAR ;
  0259:                             SWAP ;
  0260:                             CDR ;
  0261:                             DUP ;
  0262:                             CDR ;
  0263:                             SWAP ;
  0264:                             CAR ;
  0265:                             NONE timestamp ;
  0266:                             DIG 6 ;
  0267:                             DUP ;
  0268:                             DUG 7 ;
  0269:                             CAR ;
  0270:                             PACK ;
  0271:                             BLAKE2B ;
  0272:                             DIG 7 ;
  0273:                             DUP ;
  0274:                             DUG 8 ;
  0275:                             CAAR ;
  0276:                             PAIR ;
  0277:                             UPDATE ;
  0278:                             PAIR ;
  0279:                             SWAP ;
  0280:                             PAIR ;
  0281:                             SWAP ;
  0282:                             PAIR }
  0283:                           {} ;
  0284:                        DUP ;
  0285:                        CDADDR ;
  0286:                        DIG 3 ;
  0287:                        DUP ;
  0288:                        DUG 4 ;
  0289:                        CAR ;
  0290:                        PACK ;
  0291:                        BLAKE2B ;
  0292:                        DIG 4 ;
  0293:                        DUP ;
  0294:                        DUG 5 ;
  0295:                        CAAR ;
  0296:                        PAIR ;
  0297:                        MEM ;
  0298:                        IF { DUP ;
  0299:                             CAR ;
  0300:                             SWAP ;
  0301:                             CDR ;
  0302:                             DUP ;
  0303:                             CDR ;
  0304:                             SWAP ;
  0305:                             CAR ;
  0306:                             DUP ;
  0307:                             CAR ;
  0308:                             SWAP ;
  0309:                             CDR ;
  0310:                             DUP ;
  0311:                             CAR ;
  0312:                             SWAP ;
  0313:                             CDR ;
  0314:                             NONE (option nat) ;
  0315:                             DIG 7 ;
  0316:                             DUP ;
  0317:                             DUG 8 ;
  0318:                             CAR ;
  0319:                             PACK ;
  0320:                             BLAKE2B ;
  0321:                             DIG 8 ;
  0322:                             CAAR ;
  0323:                             PAIR ;
  0324:                             UPDATE ;
  0325:                             SWAP ;
  0326:                             PAIR ;
  0327:                             SWAP ;
  0328:                             PAIR ;
  0329:                             PAIR ;
  0330:                             SWAP ;
  0331:                             PAIR }
  0332:                           { DIG 2 ; DROP } ;
  0333:                        PUSH bool False }
  0334:                      { DUP ;
  0335:                        CDDAR ;
  0336:                        DIG 3 ;
  0337:                        DUP ;
  0338:                        DUG 4 ;
  0339:                        CAR ;
  0340:                        PACK ;
  0341:                        BLAKE2B ;
  0342:                        DIG 4 ;
  0343:                        DUP ;
  0344:                        DUG 5 ;
  0345:                        CAAR ;
  0346:                        PAIR ;
  0347:                        MEM ;
  0348:                        IF { DUP ;
  0349:                             CAR ;
  0350:                             SWAP ;
  0351:                             CDR ;
  0352:                             DUP ;
  0353:                             CAR ;
  0354:                             SWAP ;
  0355:                             CDR ;
  0356:                             DUP ;
  0357:                             CDR ;
  0358:                             SWAP ;
  0359:                             CAR ;
  0360:                             NONE timestamp ;
  0361:                             DIG 6 ;
  0362:                             DUP ;
  0363:                             DUG 7 ;
  0364:                             CAR ;
  0365:                             PACK ;
  0366:                             BLAKE2B ;
  0367:                             DIG 7 ;
  0368:                             DUP ;
  0369:                             DUG 8 ;
  0370:                             CAAR ;
  0371:                             PAIR ;
  0372:                             UPDATE ;
  0373:                             PAIR ;
  0374:                             SWAP ;
  0375:                             PAIR ;
  0376:                             SWAP ;
  0377:                             PAIR }
  0378:                           {} ;
  0379:                        DUP ;
  0380:                        CDADDR ;
  0381:                        DIG 3 ;
  0382:                        DUP ;
  0383:                        DUG 4 ;
  0384:                        CAR ;
  0385:                        PACK ;
  0386:                        BLAKE2B ;
  0387:                        DIG 4 ;
  0388:                        DUP ;
  0389:                        DUG 5 ;
  0390:                        CAAR ;
  0391:                        PAIR ;
  0392:                        MEM ;
  0393:                        IF { DUP ;
  0394:                             CAR ;
  0395:                             SWAP ;
  0396:                             CDR ;
  0397:                             DUP ;
  0398:                             CDR ;
  0399:                             SWAP ;
  0400:                             CAR ;
  0401:                             DUP ;
  0402:                             CAR ;
  0403:                             SWAP ;
  0404:                             CDR ;
  0405:                             DUP ;
  0406:                             CAR ;
  0407:                             SWAP ;
  0408:                             CDR ;
  0409:                             NONE (option nat) ;
  0410:                             DIG 7 ;
  0411:                             DUP ;
  0412:                             DUG 8 ;
  0413:                             CAR ;
  0414:                             PACK ;
  0415:                             BLAKE2B ;
  0416:                             DIG 8 ;
  0417:                             CAAR ;
  0418:                             PAIR ;
  0419:                             UPDATE ;
  0420:                             SWAP ;
  0421:                             PAIR ;
  0422:                             SWAP ;
  0423:                             PAIR ;
  0424:                             PAIR ;
  0425:                             SWAP ;
  0426:                             PAIR }
  0427:                           { DIG 2 ; DROP } ;
  0428:                        PUSH bool True } }
  0429:                 { DIG 2 ; DROP ; PUSH bool False } ;
  0430:              PAIR %result %storage ;
  0431:              SWAP ;
  0432:              PAIR %operations } ;
  0433:          SWAP ;
  0434:          DUP ;
  0435:          CDR ;
  0436:          SWAP ;
  0437:          CAR ;
  0438:          IF_LEFT
  0439:            { IF_LEFT
  0440:                { IF_LEFT
  0441:                    { SWAP ;
  0442:                      DUP ;
  0443:                      DUG 2 ;
  0444:                      CDADAR ;
  0445:                      IF { PUSH string "WrongCondition: ~ self.data.paused" ; FAILWITH } {} ;
  0446:                      PUSH nat 0 ;
  0447:                      DIG 2 ;
  0448:                      DUP ;
  0449:                      DUG 3 ;
  0450:                      CAADR ;
  0451:                      SENDER ;
  0452:                      GET ;
  0453:                      IF_SOME {} { PUSH int 162 ; FAILWITH } ;
  0454:                      CAR ;
  0455:                      DIG 2 ;
  0456:                      DUP ;
  0457:                      DUG 3 ;
  0458:                      CAR ;
  0459:                      GET ;
  0460:                      IF_SOME {} { PUSH nat 0 } ;
  0461:                      COMPARE ;
  0462:                      EQ ;
  0463:                      IF { PUSH bool True } { DUP ; CDR ; PUSH nat 0 ; COMPARE ; EQ } ;
  0464:                      IF { DIG 2 ; DROP ; DIG 2 ; DROP }
  0465:                         { PUSH string "UnsafeAllowanceChange" ; FAILWITH } ;
  0466:                      SWAP ;
  0467:                      DUP ;
  0468:                      CDR ;
  0469:                      SWAP ;
  0470:                      CAR ;
  0471:                      DUP ;
  0472:                      CDR ;
  0473:                      SWAP ;
  0474:                      CAR ;
  0475:                      DUP ;
  0476:                      CAR ;
  0477:                      SWAP ;
  0478:                      CDR ;
  0479:                      DUP ;
  0480:                      SENDER ;
  0481:                      DUP ;
  0482:                      DUG 2 ;
  0483:                      GET ;
  0484:                      IF_SOME {} { PUSH int 166 ; FAILWITH } ;
  0485:                      DUP ;
  0486:                      CDR ;
  0487:                      SWAP ;
  0488:                      CAR ;
  0489:                      DIG 7 ;
  0490:                      DUP ;
  0491:                      CAR ;
  0492:                      SWAP ;
  0493:                      CDR ;
  0494:                      SOME ;
  0495:                      SWAP ;
  0496:                      UPDATE ;
  0497:                      PAIR ;
  0498:                      SOME ;
  0499:                      SWAP ;
  0500:                      UPDATE ;
  0501:                      SWAP ;
  0502:                      PAIR ;
  0503:                      PAIR ;
  0504:                      PAIR ;
  0505:                      NIL operation }
  0506:                    { IF_LEFT
  0507:                        { SWAP ;
  0508:                          DUP ;
  0509:                          DUG 2 ;
  0510:                          CAAAR ;
  0511:                          SENDER ;
  0512:                          COMPARE ;
  0513:                          EQ ;
  0514:                          IF {}
  0515:                             { PUSH string "WrongCondition: sp.sender == self.data.administrator" ;
  0516:                               FAILWITH } ;
  0517:                          DUP ;
  0518:                          CDR ;
  0519:                          DIG 2 ;
  0520:                          DUP ;
  0521:                          DUG 3 ;
  0522:                          CAADR ;
  0523:                          DIG 2 ;
  0524:                          DUP ;
  0525:                          DUG 3 ;
  0526:                          CAR ;
  0527:                          GET ;
  0528:                          IF_SOME {} { PUSH int 192 ; FAILWITH } ;
  0529:                          CDR ;
  0530:                          COMPARE ;
  0531:                          GE ;
  0532:                          IF { DIG 2 ; DROP ; DIG 2 ; DROP }
  0533:                             { PUSH string
  0534:                                    "WrongCondition: self.data.balances[params.address].balance >= params.value" ;
  0535:                               FAILWITH } ;
  0536:                          SWAP ;
  0537:                          DUP ;
  0538:                          DUG 2 ;
  0539:                          DUP ;
  0540:                          CDR ;
  0541:                          SWAP ;
  0542:                          CAR ;
  0543:                          DUP ;
  0544:                          CDR ;
  0545:                          SWAP ;
  0546:                          CAR ;
  0547:                          DUP ;
  0548:                          CAR ;
  0549:                          SWAP ;
  0550:                          CDR ;
  0551:                          DUP ;
  0552:                          DIG 5 ;
  0553:                          DUP ;
  0554:                          DUG 6 ;
  0555:                          CAR ;
  0556:                          DUP ;
  0557:                          DUG 2 ;
  0558:                          GET ;
  0559:                          IF_SOME {} { PUSH int 193 ; FAILWITH } ;
  0560:                          CAR ;
  0561:                          DIG 6 ;
  0562:                          DUP ;
  0563:                          DUG 7 ;
  0564:                          CDR ;
  0565:                          DIG 8 ;
  0566:                          CAADR ;
  0567:                          DIG 8 ;
  0568:                          DUP ;
  0569:                          DUG 9 ;
  0570:                          CAR ;
  0571:                          GET ;
  0572:                          IF_SOME {} { PUSH int 194 ; FAILWITH } ;
  0573:                          CDR ;
  0574:                          SUB ;
  0575:                          ISNAT ;
  0576:                          IF_SOME {} { PUSH int 193 ; FAILWITH } ;
  0577:                          SWAP ;
  0578:                          PAIR ;
  0579:                          SOME ;
  0580:                          SWAP ;
  0581:                          UPDATE ;
  0582:                          SWAP ;
  0583:                          PAIR ;
  0584:                          PAIR ;
  0585:                          PAIR ;
  0586:                          DUP ;
  0587:                          DUG 2 ;
  0588:                          DUP ;
  0589:                          CAR ;
  0590:                          SWAP ;
  0591:                          CDR ;
  0592:                          DUP ;
  0593:                          CAR ;
  0594:                          SWAP ;
  0595:                          CDR ;
  0596:                          DUP ;
  0597:                          CAR ;
  0598:                          SWAP ;
  0599:                          CDDR ;
  0600:                          DIG 4 ;
  0601:                          CDR ;
  0602:                          DIG 5 ;
  0603:                          CDDDAR ;
  0604:                          SUB ;
  0605:                          ISNAT ;
  0606:                          IF_SOME {} { PUSH int 195 ; FAILWITH } ;
  0607:                          PAIR ;
  0608:                          SWAP ;
  0609:                          PAIR ;
  0610:                          SWAP ;
  0611:                          PAIR ;
  0612:                          SWAP ;
  0613:                          PAIR ;
  0614:                          NIL operation }
  0615:                        { PUSH int 0 ;
  0616:                          NIL operation ;
  0617:                          DIG 2 ;
  0618:                          DUP ;
  0619:                          DUG 3 ;
  0620:                          ITER { DIG 4 ;
  0621:                                 DUP ;
  0622:                                 DUG 5 ;
  0623:                                 CDDAR ;
  0624:                                 SWAP ;
  0625:                                 DUP ;
  0626:                                 DUG 2 ;
  0627:                                 MEM ;
  0628:                                 IF {} { DUP ; PUSH string "NO_PERMIT_TO_DELETE" ; PAIR ; FAILWITH } ;
  0629:                                 DIG 6 ;
  0630:                                 DUP ;
  0631:                                 DUG 7 ;
  0632:                                 DIG 5 ;
  0633:                                 DIG 2 ;
  0634:                                 DUP ;
  0635:                                 DUG 3 ;
  0636:                                 PAIR %in_param %in_storage ;
  0637:                                 EXEC ;
  0638:                                 DUP ;
  0639:                                 CDDR ;
  0640:                                 DUG 5 ;
  0641:                                 DUP ;
  0642:                                 CAR ;
  0643:                                 ITER { DIG 3 ; SWAP ; CONS ; DUG 2 } ;
  0644:                                 DUP ;
  0645:                                 CDAR ;
  0646:                                 DIG 6 ;
  0647:                                 DUP ;
  0648:                                 DUG 7 ;
  0649:                                 CDDAR ;
  0650:                                 DIG 3 ;
  0651:                                 DUP ;
  0652:                                 DUG 4 ;
  0653:                                 GET ;
  0654:                                 IF_SOME {} { PUSH int 45 ; FAILWITH } ;
  0655:                                 NOW ;
  0656:                                 SUB ;
  0657:                                 ISNAT ;
  0658:                                 IF_SOME {} { PUSH int 46 ; FAILWITH } ;
  0659:                                 COMPARE ;
  0660:                                 GE ;
  0661:                                 IF { DROP }
  0662:                                    { SWAP ; DUP ; DUG 2 ; PUSH string "PERMIT_NOT_EXPIRED" ; PAIR ; FAILWITH } ;
  0663:                                 DIG 4 ;
  0664:                                 DUP ;
  0665:                                 DUG 5 ;
  0666:                                 CDDAR ;
  0667:                                 SWAP ;
  0668:                                 DUP ;
  0669:                                 DUG 2 ;
  0670:                                 MEM ;
  0671:                                 IF { DIG 4 ;
  0672:                                      DUP ;
  0673:                                      CAR ;
  0674:                                      SWAP ;
  0675:                                      CDR ;
  0676:                                      DUP ;
  0677:                                      CAR ;
  0678:                                      SWAP ;
  0679:                                      CDR ;
  0680:                                      DUP ;
  0681:                                      CDR ;
  0682:                                      SWAP ;
  0683:                                      CAR ;
  0684:                                      NONE timestamp ;
  0685:                                      DIG 5 ;
  0686:                                      DUP ;
  0687:                                      DUG 6 ;
  0688:                                      UPDATE ;
  0689:                                      PAIR ;
  0690:                                      SWAP ;
  0691:                                      PAIR ;
  0692:                                      SWAP ;
  0693:                                      PAIR ;
  0694:                                      DUG 4 }
  0695:                                    {} ;
  0696:                                 DIG 4 ;
  0697:                                 DUP ;
  0698:                                 DUG 5 ;
  0699:                                 CDADDR ;
  0700:                                 SWAP ;
  0701:                                 DUP ;
  0702:                                 DUG 2 ;
  0703:                                 MEM ;
  0704:                                 IF { DIG 4 ;
  0705:                                      DUP ;
  0706:                                      CAR ;
  0707:                                      SWAP ;
  0708:                                      CDR ;
  0709:                                      DUP ;
  0710:                                      CDR ;
  0711:                                      SWAP ;
  0712:                                      CAR ;
  0713:                                      DUP ;
  0714:                                      CAR ;
  0715:                                      SWAP ;
  0716:                                      CDR ;
  0717:                                      DUP ;
  0718:                                      CAR ;
  0719:                                      SWAP ;
  0720:                                      CDR ;
  0721:                                      NONE (option nat) ;
  0722:                                      DIG 6 ;
  0723:                                      UPDATE ;
  0724:                                      SWAP ;
  0725:                                      PAIR ;
  0726:                                      SWAP ;
  0727:                                      PAIR ;
  0728:                                      PAIR ;
  0729:                                      SWAP ;
  0730:                                      PAIR ;
  0731:                                      DUG 3 }
  0732:                                    { DROP } } ;
  0733:                          SWAP ;
  0734:                          DROP ;
  0735:                          SWAP ;
  0736:                          DROP ;
  0737:                          DIG 2 ;
  0738:                          DROP ;
  0739:                          DIG 2 ;
  0740:                          DROP } } }
  0741:                { IF_LEFT
  0742:                    { IF_LEFT
  0743:                        { DIG 2 ;
  0744:                          DROP ;
  0745:                          DIG 2 ;
  0746:                          DROP ;
  0747:                          CONTRACT address ;
  0748:                          NIL operation ;
  0749:                          SWAP ;
  0750:                          IF_SOME {} { PUSH int 219 ; FAILWITH } ;
  0751:                          PUSH mutez 0 ;
  0752:                          DIG 3 ;
  0753:                          DUP ;
  0754:                          DUG 4 ;
  0755:                          CAAAR ;
  0756:                          TRANSFER_TOKENS ;
  0757:                          CONS }
  0758:                        { DIG 2 ;
  0759:                          DROP ;
  0760:                          DIG 2 ;
  0761:                          DROP ;
  0762:                          DUP ;
  0763:                          CDR ;
  0764:                          CONTRACT nat ;
  0765:                          NIL operation ;
  0766:                          SWAP ;
  0767:                          IF_SOME {} { PUSH int 209 ; FAILWITH } ;
  0768:                          PUSH mutez 0 ;
  0769:                          DIG 4 ;
  0770:                          DUP ;
  0771:                          DUG 5 ;
  0772:                          CAADR ;
  0773:                          DIG 4 ;
  0774:                          DUP ;
  0775:                          DUG 5 ;
  0776:                          CAAR ;
  0777:                          GET ;
  0778:                          IF_SOME {} { PUSH int 208 ; FAILWITH } ;
  0779:                          CAR ;
  0780:                          DIG 4 ;
  0781:                          CADR ;
  0782:                          GET ;
  0783:                          IF_SOME {} { PUSH int 208 ; FAILWITH } ;
  0784:                          TRANSFER_TOKENS ;
  0785:                          CONS } }
  0786:                    { IF_LEFT
  0787:                        { DIG 2 ;
  0788:                          DROP ;
  0789:                          DIG 2 ;
  0790:                          DROP ;
  0791:                          DUP ;
  0792:                          CDR ;
  0793:                          CONTRACT nat ;
  0794:                          NIL operation ;
  0795:                          SWAP ;
  0796:                          IF_SOME {} { PUSH int 204 ; FAILWITH } ;
  0797:                          PUSH mutez 0 ;
  0798:                          DIG 4 ;
  0799:                          DUP ;
  0800:                          DUG 5 ;
  0801:                          CAADR ;
  0802:                          DIG 4 ;
  0803:                          CAR ;
  0804:                          GET ;
  0805:                          IF_SOME {} { PUSH int 203 ; FAILWITH } ;
  0806:                          CDR ;
  0807:                          TRANSFER_TOKENS ;
  0808:                          CONS }
  0809:                        { DIG 2 ;
  0810:                          DROP ;
  0811:                          DIG 2 ;
  0812:                          DROP ;
  0813:                          CONTRACT nat ;
  0814:                          NIL operation ;
  0815:                          SWAP ;
  0816:                          IF_SOME {} { PUSH int 223 ; FAILWITH } ;
  0817:                          PUSH mutez 0 ;
  0818:                          DIG 3 ;
  0819:                          DUP ;
  0820:                          DUG 4 ;
  0821:                          CADAR ;
  0822:                          TRANSFER_TOKENS ;
  0823:                          CONS } } } }
  0824:            { IF_LEFT
  0825:                { IF_LEFT
  0826:                    { IF_LEFT
  0827:                        { DIG 2 ;
  0828:                          DROP ;
  0829:                          DIG 2 ;
  0830:                          DROP ;
  0831:                          CONTRACT nat ;
  0832:                          NIL operation ;
  0833:                          SWAP ;
  0834:                          IF_SOME {} { PUSH int 229 ; FAILWITH } ;
  0835:                          PUSH mutez 0 ;
  0836:                          DIG 3 ;
  0837:                          DUP ;
  0838:                          DUG 4 ;
  0839:                          CADDAR ;
  0840:                          TRANSFER_TOKENS ;
  0841:                          CONS }
  0842:                        { DIG 2 ;
  0843:                          DROP ;
  0844:                          DIG 2 ;
  0845:                          DROP ;
  0846:                          CONTRACT nat ;
  0847:                          NIL operation ;
  0848:                          SWAP ;
  0849:                          IF_SOME {} { PUSH int 214 ; FAILWITH } ;
  0850:                          PUSH mutez 0 ;
  0851:                          DIG 3 ;
  0852:                          DUP ;
  0853:                          DUG 4 ;
  0854:                          CDDDAR ;
  0855:                          TRANSFER_TOKENS ;
  0856:                          CONS } }
  0857:                    { IF_LEFT
  0858:                        { SWAP ;
  0859:                          DUP ;
  0860:                          DUG 2 ;
  0861:                          CAAAR ;
  0862:                          SENDER ;
  0863:                          COMPARE ;
  0864:                          EQ ;
  0865:                          IF {}
  0866:                             { PUSH string "WrongCondition: sp.sender == self.data.administrator" ;
  0867:                               FAILWITH } ;
  0868:                          SWAP ;
  0869:                          DUP ;
  0870:                          DUG 2 ;
  0871:                          CAADR ;
  0872:                          SWAP ;
  0873:                          DUP ;
  0874:                          DUG 2 ;
  0875:                          CAR ;
  0876:                          MEM ;
  0877:                          IF { DIG 2 ; DROP ; DIG 2 ; DROP }
  0878:                             { DIG 2 ;
  0879:                               DROP ;
  0880:                               DIG 2 ;
  0881:                               DROP ;
  0882:                               SWAP ;
  0883:                               DUP ;
  0884:                               CDR ;
  0885:                               SWAP ;
  0886:                               CAR ;
  0887:                               DUP ;
  0888:                               CDR ;
  0889:                               SWAP ;
  0890:                               CAR ;
  0891:                               DUP ;
  0892:                               CAR ;
  0893:                               SWAP ;
  0894:                               CDR ;
  0895:                               DIG 4 ;
  0896:                               DUP ;
  0897:                               DUG 5 ;
  0898:                               CAR ;
  0899:                               PUSH (option (pair (map %approvals address nat) (nat %balance))) (Some (Pair {} 0)) ;
  0900:                               SWAP ;
  0901:                               UPDATE ;
  0902:                               SWAP ;
  0903:                               PAIR ;
  0904:                               PAIR ;
  0905:                               PAIR ;
  0906:                               SWAP } ;
  0907:                          SWAP ;
  0908:                          DUP ;
  0909:                          CDR ;
  0910:                          SWAP ;
  0911:                          CAR ;
  0912:                          DUP ;
  0913:                          CDR ;
  0914:                          SWAP ;
  0915:                          CAR ;
  0916:                          DUP ;
  0917:                          CAR ;
  0918:                          SWAP ;
  0919:                          CDR ;
  0920:                          DUP ;
  0921:                          DIG 5 ;
  0922:                          DUP ;
  0923:                          DUG 6 ;
  0924:                          CAR ;
  0925:                          DUP ;
  0926:                          DUG 2 ;
  0927:                          GET ;
  0928:                          IF_SOME {} { PUSH int 185 ; FAILWITH } ;
  0929:                          DUP ;
  0930:                          CAR ;
  0931:                          SWAP ;
  0932:                          CDR ;
  0933:                          DIG 7 ;
  0934:                          DUP ;
  0935:                          DUG 8 ;
  0936:                          CDR ;
  0937:                          ADD ;
  0938:                          SWAP ;
  0939:                          PAIR ;
  0940:                          SOME ;
  0941:                          SWAP ;
  0942:                          UPDATE ;
  0943:                          SWAP ;
  0944:                          PAIR ;
  0945:                          PAIR ;
  0946:                          PAIR ;
  0947:                          DUP ;
  0948:                          CAR ;
  0949:                          SWAP ;
  0950:                          CDR ;
  0951:                          DUP ;
  0952:                          CAR ;
  0953:                          SWAP ;
  0954:                          CDR ;
  0955:                          DUP ;
  0956:                          CAR ;
  0957:                          SWAP ;
  0958:                          CDR ;
  0959:                          DUP ;
  0960:                          CDR ;
  0961:                          SWAP ;
  0962:                          CAR ;
  0963:                          DIG 5 ;
  0964:                          CDR ;
  0965:                          ADD ;
  0966:                          PAIR ;
  0967:                          SWAP ;
  0968:                          PAIR ;
  0969:                          SWAP ;
  0970:                          PAIR ;
  0971:                          SWAP ;
  0972:                          PAIR ;
  0973:                          NIL operation }
  0974:                        { SWAP ;
  0975:                          DUP ;
  0976:                          DUG 2 ;
  0977:                          CDADAR ;
  0978:                          IF { PUSH string "WrongCondition: ~ self.data.paused" ; FAILWITH } {} ;
  0979:                          DUP ;
  0980:                          NIL operation ;
  0981:                          SWAP ;
  0982:                          ITER { DIG 5 ;
  0983:                                 DUP ;
  0984:                                 DUG 6 ;
  0985:                                 DIG 4 ;
  0986:                                 DIG 2 ;
  0987:                                 DUP ;
  0988:                                 CDDR ;
  0989:                                 SWAP ;
  0990:                                 DUP ;
  0991:                                 DUG 4 ;
  0992:                                 CAR ;
  0993:                                 HASH_KEY ;
  0994:                                 IMPLICIT_ACCOUNT ;
  0995:                                 ADDRESS ;
  0996:                                 PAIR ;
  0997:                                 PAIR %in_param %in_storage ;
  0998:                                 EXEC ;
  0999:                                 DUP ;
  1000:                                 CDDR ;
  1001:                                 DUG 4 ;
  1002:                                 DUP ;
  1003:                                 CAR ;
  1004:                                 ITER { DIG 3 ; SWAP ; CONS ; DUG 2 } ;
  1005:                                 DIG 4 ;
  1006:                                 DUP ;
  1007:                                 DUG 5 ;
  1008:                                 CDDAR ;
  1009:                                 DIG 2 ;
  1010:                                 DUP ;
  1011:                                 CDDR ;
  1012:                                 SWAP ;
  1013:                                 DUP ;
  1014:                                 DUG 4 ;
  1015:                                 CAR ;
  1016:                                 HASH_KEY ;
  1017:                                 IMPLICIT_ACCOUNT ;
  1018:                                 ADDRESS ;
  1019:                                 PAIR ;
  1020:                                 MEM ;
  1021:                                 IF { DUP ;
  1022:                                      CDAR ;
  1023:                                      DIG 5 ;
  1024:                                      DUP ;
  1025:                                      DUG 6 ;
  1026:                                      CDDAR ;
  1027:                                      DIG 3 ;
  1028:                                      DUP ;
  1029:                                      CDDR ;
  1030:                                      SWAP ;
  1031:                                      DUP ;
  1032:                                      DUG 5 ;
  1033:                                      CAR ;
  1034:                                      HASH_KEY ;
  1035:                                      IMPLICIT_ACCOUNT ;
  1036:                                      ADDRESS ;
  1037:                                      PAIR ;
  1038:                                      GET ;
  1039:                                      IF_SOME {} { PUSH int 102 ; FAILWITH } ;
  1040:                                      NOW ;
  1041:                                      SUB ;
  1042:                                      ISNAT ;
  1043:                                      IF_SOME {} { PUSH int 103 ; FAILWITH } ;
  1044:                                      COMPARE ;
  1045:                                      LT }
  1046:                                    { PUSH bool False } ;
  1047:                                 IF { SWAP ; DUP ; DUG 2 ; CDDR ; PUSH string "DUP_PERMIT" ; PAIR ; FAILWITH }
  1048:                                    {} ;
  1049:                                 SWAP ;
  1050:                                 DUP ;
  1051:                                 DUG 2 ;
  1052:                                 CDDR ;
  1053:                                 DIG 5 ;
  1054:                                 DUP ;
  1055:                                 DUG 6 ;
  1056:                                 CADAR ;
  1057:                                 PAIR ;
  1058:                                 SELF ;
  1059:                                 ADDRESS ;
  1060:                                 CHAIN_ID ;
  1061:                                 PAIR ;
  1062:                                 PAIR ;
  1063:                                 PACK ;
  1064:                                 DIG 2 ;
  1065:                                 DUP ;
  1066:                                 CDAR ;
  1067:                                 SWAP ;
  1068:                                 DUP ;
  1069:                                 DUG 4 ;
  1070:                                 CAR ;
  1071:                                 CHECK_SIGNATURE ;
  1072:                                 IF { DROP }
  1073:                                    { SWAP ;
  1074:                                      DUP ;
  1075:                                      DUG 2 ;
  1076:                                      CDDR ;
  1077:                                      DIG 5 ;
  1078:                                      DUP ;
  1079:                                      DUG 6 ;
  1080:                                      CADAR ;
  1081:                                      PAIR ;
  1082:                                      SELF ;
  1083:                                      ADDRESS ;
  1084:                                      CHAIN_ID ;
  1085:                                      PAIR ;
  1086:                                      PAIR ;
  1087:                                      PACK ;
  1088:                                      PUSH string "MISSIGNED" ;
  1089:                                      PAIR ;
  1090:                                      FAILWITH } ;
  1091:                                 DIG 3 ;
  1092:                                 DUP ;
  1093:                                 CAR ;
  1094:                                 SWAP ;
  1095:                                 CDR ;
  1096:                                 DUP ;
  1097:                                 CAR ;
  1098:                                 SWAP ;
  1099:                                 CDR ;
  1100:                                 DUP ;
  1101:                                 CDR ;
  1102:                                 SWAP ;
  1103:                                 CAR ;
  1104:                                 DIG 4 ;
  1105:                                 DUP ;
  1106:                                 CDDR ;
  1107:                                 SWAP ;
  1108:                                 CAR ;
  1109:                                 HASH_KEY ;
  1110:                                 IMPLICIT_ACCOUNT ;
  1111:                                 ADDRESS ;
  1112:                                 PAIR ;
  1113:                                 NOW ;
  1114:                                 SOME ;
  1115:                                 SWAP ;
  1116:                                 UPDATE ;
  1117:                                 PAIR ;
  1118:                                 SWAP ;
  1119:                                 PAIR ;
  1120:                                 SWAP ;
  1121:                                 PAIR ;
  1122:                                 DUP ;
  1123:                                 CDR ;
  1124:                                 SWAP ;
  1125:                                 CAR ;
  1126:                                 DUP ;
  1127:                                 CAR ;
  1128:                                 SWAP ;
  1129:                                 CDR ;
  1130:                                 DUP ;
  1131:                                 CDR ;
  1132:                                 SWAP ;
  1133:                                 CAR ;
  1134:                                 PUSH nat 1 ;
  1135:                                 ADD ;
  1136:                                 PAIR ;
  1137:                                 SWAP ;
  1138:                                 PAIR ;
  1139:                                 PAIR ;
  1140:                                 DUG 2 } ;
  1141:                          SWAP ;
  1142:                          DROP ;
  1143:                          DIG 2 ;
  1144:                          DROP ;
  1145:                          DIG 2 ;
  1146:                          DROP } } }
  1147:                { IF_LEFT
  1148:                    { IF_LEFT
  1149:                        { SWAP ;
  1150:                          DUP ;
  1151:                          DUG 2 ;
  1152:                          CAAAR ;
  1153:                          SENDER ;
  1154:                          COMPARE ;
  1155:                          EQ ;
  1156:                          IF { DIG 2 ; DROP ; DIG 2 ; DROP }
  1157:                             { PUSH string "WrongCondition: sp.sender == self.data.administrator" ;
  1158:                               FAILWITH } ;
  1159:                          SWAP ;
  1160:                          DUP ;
  1161:                          CDR ;
  1162:                          SWAP ;
  1163:                          CAR ;
  1164:                          DUP ;
  1165:                          CDR ;
  1166:                          SWAP ;
  1167:                          CADR ;
  1168:                          DIG 3 ;
  1169:                          PAIR ;
  1170:                          PAIR ;
  1171:                          PAIR }
  1172:                        { SWAP ;
  1173:                          DUP ;
  1174:                          DUG 2 ;
  1175:                          CDADAR ;
  1176:                          IF { PUSH string "WrongCondition: ~ self.data.paused" ; FAILWITH } {} ;
  1177:                          SWAP ;
  1178:                          DUP ;
  1179:                          DUG 2 ;
  1180:                          CADDDR ;
  1181:                          SWAP ;
  1182:                          DUP ;
  1183:                          DUG 2 ;
  1184:                          CDDR ;
  1185:                          COMPARE ;
  1186:                          LE ;
  1187:                          IF {} { PUSH string "MAX_SECONDS_EXCEEDED" ; FAILWITH } ;
  1188:                          SENDER ;
  1189:                          PACK ;
  1190:                          SWAP ;
  1191:                          DUP ;
  1192:                          DUG 2 ;
  1193:                          CAR ;
  1194:                          PACK ;
  1195:                          COMPARE ;
  1196:                          EQ ;
  1197:                          IF {} { PUSH bool False ; FAILWITH } ;
  1198:                          DUP ;
  1199:                          CDAR ;
  1200:                          IF_SOME
  1201:                            { DROP ;
  1202:                              SWAP ;
  1203:                              DUP ;
  1204:                              DUG 2 ;
  1205:                              CDDAR ;
  1206:                              SWAP ;
  1207:                              DUP ;
  1208:                              DUG 2 ;
  1209:                              CDAR ;
  1210:                              IF_SOME {} { PUSH int 132 ; FAILWITH } ;
  1211:                              DIG 2 ;
  1212:                              DUP ;
  1213:                              DUG 3 ;
  1214:                              CAR ;
  1215:                              PAIR ;
  1216:                              MEM ;
  1217:                              IF {} { PUSH string "PERMIT_NONEXISTENT" ; FAILWITH } ;
  1218:                              SWAP ;
  1219:                              DUP ;
  1220:                              DUG 2 ;
  1221:                              CDADDR ;
  1222:                              SWAP ;
  1223:                              DUP ;
  1224:                              DUG 2 ;
  1225:                              CDAR ;
  1226:                              IF_SOME {} { PUSH int 132 ; FAILWITH } ;
  1227:                              DIG 2 ;
  1228:                              DUP ;
  1229:                              DUG 3 ;
  1230:                              CAR ;
  1231:                              PAIR ;
  1232:                              MEM ;
  1233:                              IF { SWAP ;
  1234:                                   DUP ;
  1235:                                   DUG 2 ;
  1236:                                   CDADDR ;
  1237:                                   SWAP ;
  1238:                                   DUP ;
  1239:                                   DUG 2 ;
  1240:                                   CDAR ;
  1241:                                   IF_SOME {} { PUSH int 132 ; FAILWITH } ;
  1242:                                   DIG 2 ;
  1243:                                   DUP ;
  1244:                                   DUG 3 ;
  1245:                                   CAR ;
  1246:                                   PAIR ;
  1247:                                   GET ;
  1248:                                   IF_SOME {} { PUSH int 137 ; FAILWITH } ;
  1249:                                   IF_SOME { DROP ; PUSH bool True } { PUSH bool False } }
  1250:                                 { PUSH bool False } ;
  1251:                              IF { SWAP ;
  1252:                                   DUP ;
  1253:                                   DUG 2 ;
  1254:                                   CDADDR ;
  1255:                                   SWAP ;
  1256:                                   DUP ;
  1257:                                   DUG 2 ;
  1258:                                   CDAR ;
  1259:                                   IF_SOME {} { PUSH int 132 ; FAILWITH } ;
  1260:                                   DIG 2 ;
  1261:                                   DUP ;
  1262:                                   DUG 3 ;
  1263:                                   CAR ;
  1264:                                   PAIR ;
  1265:                                   GET ;
  1266:                                   IF_SOME {} { PUSH int 138 ; FAILWITH } ;
  1267:                                   IF_SOME {} { PUSH int 138 ; FAILWITH } ;
  1268:                                   DIG 2 ;
  1269:                                   DUP ;
  1270:                                   DUG 3 ;
  1271:                                   CDDAR ;
  1272:                                   DIG 2 ;
  1273:                                   DUP ;
  1274:                                   DUG 3 ;
  1275:                                   CDAR ;
  1276:                                   IF_SOME {} { PUSH int 132 ; FAILWITH } ;
  1277:                                   DIG 3 ;
  1278:                                   DUP ;
  1279:                                   DUG 4 ;
  1280:                                   CAR ;
  1281:                                   PAIR ;
  1282:                                   GET ;
  1283:                                   IF_SOME {} { PUSH int 135 ; FAILWITH } ;
  1284:                                   NOW ;
  1285:                                   SUB ;
  1286:                                   ISNAT ;
  1287:                                   IF_SOME {} { PUSH int 140 ; FAILWITH } ;
  1288:                                   COMPARE ;
  1289:                                   LT ;
  1290:                                   IF { DIG 2 ; DROP ; DIG 2 ; DROP }
  1291:                                      { PUSH string "PERMIT_REVOKED" ; FAILWITH } }
  1292:                                 { SWAP ;
  1293:                                   DUP ;
  1294:                                   DUG 2 ;
  1295:                                   CDDDDR ;
  1296:                                   SWAP ;
  1297:                                   DUP ;
  1298:                                   DUG 2 ;
  1299:                                   CAR ;
  1300:                                   MEM ;
  1301:                                   IF { SWAP ;
  1302:                                        DUP ;
  1303:                                        DUG 2 ;
  1304:                                        CDDDDR ;
  1305:                                        SWAP ;
  1306:                                        DUP ;
  1307:                                        DUG 2 ;
  1308:                                        CAR ;
  1309:                                        GET ;
  1310:                                        IF_SOME {} { PUSH int 143 ; FAILWITH } ;
  1311:                                        IF_SOME { DROP ; PUSH bool True } { PUSH bool False } }
  1312:                                      { PUSH bool False } ;
  1313:                                   IF { SWAP ;
  1314:                                        DUP ;
  1315:                                        DUG 2 ;
  1316:                                        CDDDDR ;
  1317:                                        SWAP ;
  1318:                                        DUP ;
  1319:                                        DUG 2 ;
  1320:                                        CAR ;
  1321:                                        GET ;
  1322:                                        IF_SOME {} { PUSH int 144 ; FAILWITH } ;
  1323:                                        IF_SOME {} { PUSH int 144 ; FAILWITH } ;
  1324:                                        DIG 2 ;
  1325:                                        DUP ;
  1326:                                        DUG 3 ;
  1327:                                        CDDAR ;
  1328:                                        DIG 2 ;
  1329:                                        DUP ;
  1330:                                        DUG 3 ;
  1331:                                        CDAR ;
  1332:                                        IF_SOME {} { PUSH int 132 ; FAILWITH } ;
  1333:                                        DIG 3 ;
  1334:                                        DUP ;
  1335:                                        DUG 4 ;
  1336:                                        CAR ;
  1337:                                        PAIR ;
  1338:                                        GET ;
  1339:                                        IF_SOME {} { PUSH int 135 ; FAILWITH } ;
  1340:                                        NOW ;
  1341:                                        SUB ;
  1342:                                        ISNAT ;
  1343:                                        IF_SOME {} { PUSH int 146 ; FAILWITH } ;
  1344:                                        COMPARE ;
  1345:                                        LT ;
  1346:                                        IF { DIG 2 ; DROP ; DIG 2 ; DROP }
  1347:                                           { PUSH string "PERMIT_REVOKED" ; FAILWITH } }
  1348:                                      { SWAP ;
  1349:                                        DUP ;
  1350:                                        CADDAR ;
  1351:                                        SWAP ;
  1352:                                        DUP ;
  1353:                                        DUG 3 ;
  1354:                                        CDDAR ;
  1355:                                        DIG 2 ;
  1356:                                        DUP ;
  1357:                                        DUG 3 ;
  1358:                                        CDAR ;
  1359:                                        IF_SOME {} { PUSH int 132 ; FAILWITH } ;
  1360:                                        DIG 3 ;
  1361:                                        DUP ;
  1362:                                        DUG 4 ;
  1363:                                        CAR ;
  1364:                                        PAIR ;
  1365:                                        GET ;
  1366:                                        IF_SOME {} { PUSH int 135 ; FAILWITH } ;
  1367:                                        NOW ;
  1368:                                        SUB ;
  1369:                                        ISNAT ;
  1370:                                        IF_SOME {} { PUSH int 149 ; FAILWITH } ;
  1371:                                        COMPARE ;
  1372:                                        LT ;
  1373:                                        IF { DIG 2 ; DROP ; DIG 2 ; DROP }
  1374:                                           { PUSH string "PERMIT_REVOKED" ; FAILWITH } } } ;
  1375:                              SWAP ;
  1376:                              DUP ;
  1377:                              CAR ;
  1378:                              SWAP ;
  1379:                              CDR ;
  1380:                              DUP ;
  1381:                              CDR ;
  1382:                              SWAP ;
  1383:                              CAR ;
  1384:                              DUP ;
  1385:                              CAR ;
  1386:                              SWAP ;
  1387:                              CDR ;
  1388:                              DUP ;
  1389:                              CAR ;
  1390:                              SWAP ;
  1391:                              CDR ;
  1392:                              DIG 5 ;
  1393:                              DUP ;
  1394:                              DUG 6 ;
  1395:                              CDAR ;
  1396:                              IF_SOME {} { PUSH int 132 ; FAILWITH } ;
  1397:                              DIG 6 ;
  1398:                              DUP ;
  1399:                              DUG 7 ;
  1400:                              CAR ;
  1401:                              PAIR ;
  1402:                              DIG 6 ;
  1403:                              CDDR ;
  1404:                              SOME ;
  1405:                              SOME ;
  1406:                              SWAP ;
  1407:                              UPDATE ;
  1408:                              SWAP ;
  1409:                              PAIR ;
  1410:                              SWAP ;
  1411:                              PAIR ;
  1412:                              PAIR ;
  1413:                              SWAP ;
  1414:                              PAIR }
  1415:                            { DIG 2 ;
  1416:                              DROP ;
  1417:                              DIG 2 ;
  1418:                              DROP ;
  1419:                              SWAP ;
  1420:                              DUP ;
  1421:                              CAR ;
  1422:                              SWAP ;
  1423:                              CDR ;
  1424:                              DUP ;
  1425:                              CAR ;
  1426:                              SWAP ;
  1427:                              CDR ;
  1428:                              DUP ;
  1429:                              CAR ;
  1430:                              SWAP ;
  1431:                              CDR ;
  1432:                              DUP ;
  1433:                              CAR ;
  1434:                              SWAP ;
  1435:                              CDR ;
  1436:                              DIG 5 ;
  1437:                              DUP ;
  1438:                              CAR ;
  1439:                              SWAP ;
  1440:                              CDDR ;
  1441:                              SOME ;
  1442:                              SOME ;
  1443:                              SWAP ;
  1444:                              UPDATE ;
  1445:                              SWAP ;
  1446:                              PAIR ;
  1447:                              SWAP ;
  1448:                              PAIR ;
  1449:                              SWAP ;
  1450:                              PAIR ;
  1451:                              SWAP ;
  1452:                              PAIR } } ;
  1453:                      NIL operation }
  1454:                    { IF_LEFT
  1455:                        { SWAP ;
  1456:                          DUP ;
  1457:                          DUG 2 ;
  1458:                          CAAAR ;
  1459:                          SENDER ;
  1460:                          COMPARE ;
  1461:                          EQ ;
  1462:                          IF { DIG 2 ; DROP ; DIG 2 ; DROP }
  1463:                             { PUSH string "WrongCondition: sp.sender == self.data.administrator" ;
  1464:                               FAILWITH } ;
  1465:                          SWAP ;
  1466:                          DUP ;
  1467:                          CAR ;
  1468:                          SWAP ;
  1469:                          CDR ;
  1470:                          DUP ;
  1471:                          CDR ;
  1472:                          SWAP ;
  1473:                          CAR ;
  1474:                          DUP ;
  1475:                          CAR ;
  1476:                          SWAP ;
  1477:                          CDDR ;
  1478:                          DIG 4 ;
  1479:                          PAIR ;
  1480:                          SWAP ;
  1481:                          PAIR ;
  1482:                          PAIR ;
  1483:                          SWAP ;
  1484:                          PAIR ;
  1485:                          NIL operation }
  1486:                        { SENDER ;
  1487:                          DIG 3 ;
  1488:                          DUP ;
  1489:                          DUG 4 ;
  1490:                          DIG 3 ;
  1491:                          DIG 3 ;
  1492:                          DUP ;
  1493:                          DUG 4 ;
  1494:                          PAIR %in_param %in_storage ;
  1495:                          EXEC ;
  1496:                          DUP ;
  1497:                          CDDR ;
  1498:                          DUG 3 ;
  1499:                          DUP ;
  1500:                          CAR ;
  1501:                          NIL operation ;
  1502:                          SWAP ;
  1503:                          ITER { CONS } ;
  1504:                          SWAP ;
  1505:                          DUP ;
  1506:                          DUG 2 ;
  1507:                          CDAR ;
  1508:                          IF { DIG 2 ; DROP ; DIG 2 ; DUP ; DUG 3 ; CAR ; DUG 2 } {} ;
  1509:                          DIG 4 ;
  1510:                          DUP ;
  1511:                          DUG 5 ;
  1512:                          CAAAR ;
  1513:                          DIG 3 ;
  1514:                          DUP ;
  1515:                          DUG 4 ;
  1516:                          COMPARE ;
  1517:                          EQ ;
  1518:                          IF { PUSH bool True }
  1519:                             { DIG 4 ;
  1520:                               DUP ;
  1521:                               DUG 5 ;
  1522:                               CDADAR ;
  1523:                               IF { PUSH bool False }
  1524:                                  { DIG 2 ;
  1525:                                    DUP ;
  1526:                                    DUG 3 ;
  1527:                                    DIG 4 ;
  1528:                                    DUP ;
  1529:                                    DUG 5 ;
  1530:                                    CAR ;
  1531:                                    COMPARE ;
  1532:                                    EQ ;
  1533:                                    IF { PUSH bool True }
  1534:                                       { DIG 3 ;
  1535:                                         DUP ;
  1536:                                         DUG 4 ;
  1537:                                         CDDR ;
  1538:                                         DIG 5 ;
  1539:                                         DUP ;
  1540:                                         DUG 6 ;
  1541:                                         CAADR ;
  1542:                                         DIG 5 ;
  1543:                                         DUP ;
  1544:                                         DUG 6 ;
  1545:                                         CAR ;
  1546:                                         GET ;
  1547:                                         IF_SOME {} { PUSH int 26 ; FAILWITH } ;
  1548:                                         CAR ;
  1549:                                         DIG 4 ;
  1550:                                         DUP ;
  1551:                                         DUG 5 ;
  1552:                                         GET ;
  1553:                                         IF_SOME {} { PUSH int 26 ; FAILWITH } ;
  1554:                                         COMPARE ;
  1555:                                         GE } } } ;
  1556:                          IF {}
  1557:                             { PUSH string
  1558:                                    "WrongCondition: (sender.value == self.data.administrator) | ((~ self.data.paused) & ((params.from_ == sender.value) | (self.data.balances[params.from_].approvals[sender.value] >= params.value)))" ;
  1559:                               FAILWITH } ;
  1560:                          DIG 4 ;
  1561:                          DUP ;
  1562:                          DUG 5 ;
  1563:                          CAADR ;
  1564:                          DIG 4 ;
  1565:                          DUP ;
  1566:                          DUG 5 ;
  1567:                          CDAR ;
  1568:                          MEM ;
  1569:                          IF {}
  1570:                             { DIG 4 ;
  1571:                               DUP ;
  1572:                               CDR ;
  1573:                               SWAP ;
  1574:                               CAR ;
  1575:                               DUP ;
  1576:                               CDR ;
  1577:                               SWAP ;
  1578:                               CAR ;
  1579:                               DUP ;
  1580:                               CAR ;
  1581:                               SWAP ;
  1582:                               CDR ;
  1583:                               DIG 7 ;
  1584:                               DUP ;
  1585:                               DUG 8 ;
  1586:                               CDAR ;
  1587:                               PUSH (option (pair (map %approvals address nat) (nat %balance))) (Some (Pair {} 0)) ;
  1588:                               SWAP ;
  1589:                               UPDATE ;
  1590:                               SWAP ;
  1591:                               PAIR ;
  1592:                               PAIR ;
  1593:                               PAIR ;
  1594:                               DUG 4 } ;
  1595:                          DIG 3 ;
  1596:                          DUP ;
  1597:                          DUG 4 ;
  1598:                          CDDR ;
  1599:                          DIG 5 ;
  1600:                          DUP ;
  1601:                          DUG 6 ;
  1602:                          CAADR ;
  1603:                          DIG 5 ;
  1604:                          DUP ;
  1605:                          DUG 6 ;
  1606:                          CAR ;
  1607:                          GET ;
  1608:                          IF_SOME {} { PUSH int 28 ; FAILWITH } ;
  1609:                          CDR ;
  1610:                          COMPARE ;
  1611:                          GE ;
  1612:                          IF {}
  1613:                             { PUSH string
  1614:                                    "WrongCondition: self.data.balances[params.from_].balance >= params.value" ;
  1615:                               FAILWITH } ;
  1616:                          DIG 4 ;
  1617:                          DUP ;
  1618:                          DUG 5 ;
  1619:                          DUP ;
  1620:                          CDR ;
  1621:                          SWAP ;
  1622:                          CAR ;
  1623:                          DUP ;
  1624:                          CDR ;
  1625:                          SWAP ;
  1626:                          CAR ;
  1627:                          DUP ;
  1628:                          CAR ;
  1629:                          SWAP ;
  1630:                          CDR ;
  1631:                          DUP ;
  1632:                          DIG 8 ;
  1633:                          DUP ;
  1634:                          DUG 9 ;
  1635:                          CAR ;
  1636:                          DUP ;
  1637:                          DUG 2 ;
  1638:                          GET ;
  1639:                          IF_SOME {} { PUSH int 29 ; FAILWITH } ;
  1640:                          CAR ;
  1641:                          DIG 9 ;
  1642:                          DUP ;
  1643:                          DUG 10 ;
  1644:                          CDDR ;
  1645:                          DIG 11 ;
  1646:                          CAADR ;
  1647:                          DIG 11 ;
  1648:                          DUP ;
  1649:                          DUG 12 ;
  1650:                          CAR ;
  1651:                          GET ;
  1652:                          IF_SOME {} { PUSH int 30 ; FAILWITH } ;
  1653:                          CDR ;
  1654:                          SUB ;
  1655:                          ISNAT ;
  1656:                          IF_SOME {} { PUSH int 29 ; FAILWITH } ;
  1657:                          SWAP ;
  1658:                          PAIR ;
  1659:                          SOME ;
  1660:                          SWAP ;
  1661:                          UPDATE ;
  1662:                          SWAP ;
  1663:                          PAIR ;
  1664:                          PAIR ;
  1665:                          PAIR ;
  1666:                          DUP ;
  1667:                          CDR ;
  1668:                          SWAP ;
  1669:                          CAR ;
  1670:                          DUP ;
  1671:                          CDR ;
  1672:                          SWAP ;
  1673:                          CAR ;
  1674:                          DUP ;
  1675:                          CAR ;
  1676:                          SWAP ;
  1677:                          CDR ;
  1678:                          DUP ;
  1679:                          DIG 8 ;
  1680:                          DUP ;
  1681:                          DUG 9 ;
  1682:                          CDAR ;
  1683:                          DUP ;
  1684:                          DUG 2 ;
  1685:                          GET ;
  1686:                          IF_SOME {} { PUSH int 31 ; FAILWITH } ;
  1687:                          DUP ;
  1688:                          CAR ;
  1689:                          SWAP ;
  1690:                          CDR ;
  1691:                          DIG 10 ;
  1692:                          DUP ;
  1693:                          DUG 11 ;
  1694:                          CDDR ;
  1695:                          ADD ;
  1696:                          SWAP ;
  1697:                          PAIR ;
  1698:                          SOME ;
  1699:                          SWAP ;
  1700:                          UPDATE ;
  1701:                          SWAP ;
  1702:                          PAIR ;
  1703:                          PAIR ;
  1704:                          PAIR ;
  1705:                          DUG 4 ;
  1706:                          DIG 2 ;
  1707:                          DUP ;
  1708:                          DUG 3 ;
  1709:                          DIG 4 ;
  1710:                          DUP ;
  1711:                          DUG 5 ;
  1712:                          CAR ;
  1713:                          COMPARE ;
  1714:                          NEQ ;
  1715:                          IF { DIG 2 ; DUP ; DUG 3 ; DIG 5 ; DUP ; DUG 6 ; CAAAR ; COMPARE ; NEQ }
  1716:                             { PUSH bool False } ;
  1717:                          IF { SWAP ;
  1718:                               DROP ;
  1719:                               DIG 4 ;
  1720:                               DROP ;
  1721:                               DIG 4 ;
  1722:                               DROP ;
  1723:                               DIG 3 ;
  1724:                               DUP ;
  1725:                               DUG 4 ;
  1726:                               DUP ;
  1727:                               CDR ;
  1728:                               SWAP ;
  1729:                               CAR ;
  1730:                               DUP ;
  1731:                               CDR ;
  1732:                               SWAP ;
  1733:                               CAR ;
  1734:                               DUP ;
  1735:                               CAR ;
  1736:                               SWAP ;
  1737:                               CDR ;
  1738:                               DUP ;
  1739:                               DIG 7 ;
  1740:                               DUP ;
  1741:                               DUG 8 ;
  1742:                               CAR ;
  1743:                               DUP ;
  1744:                               DUG 2 ;
  1745:                               GET ;
  1746:                               IF_SOME {} { PUSH int 33 ; FAILWITH } ;
  1747:                               DUP ;
  1748:                               CDR ;
  1749:                               SWAP ;
  1750:                               CAR ;
  1751:                               DIG 8 ;
  1752:                               DIG 9 ;
  1753:                               DUP ;
  1754:                               DUG 10 ;
  1755:                               CDDR ;
  1756:                               DIG 11 ;
  1757:                               CAADR ;
  1758:                               DIG 11 ;
  1759:                               CAR ;
  1760:                               GET ;
  1761:                               IF_SOME {} { PUSH int 34 ; FAILWITH } ;
  1762:                               CAR ;
  1763:                               DIG 2 ;
  1764:                               DUP ;
  1765:                               DUG 3 ;
  1766:                               GET ;
  1767:                               IF_SOME {} { PUSH int 34 ; FAILWITH } ;
  1768:                               SUB ;
  1769:                               ISNAT ;
  1770:                               IF_SOME {} { PUSH int 33 ; FAILWITH } ;
  1771:                               SOME ;
  1772:                               SWAP ;
  1773:                               UPDATE ;
  1774:                               PAIR ;
  1775:                               SOME ;
  1776:                               SWAP ;
  1777:                               UPDATE ;
  1778:                               SWAP ;
  1779:                               PAIR ;
  1780:                               PAIR ;
  1781:                               PAIR ;
  1782:                               SWAP }
  1783:                             { SWAP ; DROP ; SWAP ; DROP ; SWAP ; DROP ; DIG 2 ; DROP ; DIG 2 ; DROP } } } } } ;
  1784:          NIL operation ;
  1785:          SWAP ;
  1786:          ITER { CONS } ;
  1787:          PAIR } }
At line 1553 characters 67 to 75,
script reached FAILWITH instruction
with 26
Fatal error:
  transfer simulation failed
Warning:
  
   The node you are connecting to claims to be running in a
                    Tezos TEST SANDBOX.
      Do NOT use your fundraiser keys on this network.
  You should not see this message if you are not a developer.

Invalid primitive:
  1: { Pair "edpktzNbDAUjUk697W7gYg2CRuBQjyPxbEg8dLccYYwKSKvkPvjtV9"
  2:        (Pair "edsigtfkWys7vyeQy1PnHcBuac1dgj2aJ8Jv3fvoDE5XRtxTMRgJBwVgMTzvhAzBQyjH48ux9KE8jRZBSk4Rv2bfphsfpKP3ggM"
  3:              e6f1aa42d877954d34bbde9ca5bdd2676b139adb52ebc7b943fe8a07f55591e9) }
Primitive e6f1aa42d877954d34bbde9ca5bdd2676b139adb52ebc7b943fe8a07f55591e9 has invalid case.
Fatal error:
  transfer simulation failed
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
  0001: { parameter
  0002:     (or (or (or (pair %approve (address %spender) (nat %value))
  0003:                 (or (pair %burn (address %address) (nat %value))
  0004:                     (list %delete_permits (pair address bytes))))
  0005:             (or (or (address %getAdministrator)
  0006:                     (pair %getAllowance
  0007:                        (pair %arg (address %owner) (address %spender))
  0008:                        (address %target)))
  0009:                 (or (pair %getBalance (address %arg) (address %target)) (address %getCounter))))
  0010:         (or (or (or (address %getDefaultExpiry) (address %getTotalSupply))
  0011:                 (or (pair %mint (address %address) (nat %value))
  0012:                     (list %permit (pair key (pair signature bytes)))))
  0013:             (or (or (address %setAdministrator)
  0014:                     (pair %setExpiry (address %address) (pair (option %permit bytes) (nat %seconds))))
  0015:                 (or (bool %setPause)
  0016:                     (pair %transfer (address %from_) (pair (address %to_) (nat %value))))))) ;
  0017:   storage
  0018:     (pair (pair (pair (address %administrator)
  0019:                       (big_map %balances address (pair (map %approvals address nat) (nat %balance))))
  0020:                 (pair (nat %counter) (pair (nat %default_expiry) (nat %max_expiry))))
  0021:           (pair (pair (big_map %metadata string bytes)
  0022:                       (pair (bool %paused) (big_map %permit_expiries (pair address bytes) (option nat))))
  0023:                 (pair (big_map %permits (pair address bytes) timestamp)
  0024:                       (pair (nat %totalSupply) (big_map %user_expiries address (option nat)))))) ;
  0025:   code { LAMBDA
  0026:            (pair (pair %in_param address bytes)
  0027:                  (pair %in_storage
  0028:                     (pair (pair (address %administrator)
  0029:                                 (big_map %balances address (pair (map %approvals address nat) (nat %balance))))
  0030:                           (pair (nat %counter) (pair (nat %default_expiry) (nat %max_expiry))))
  0031:                     (pair (pair (big_map %metadata string bytes)
  0032:                                 (pair (bool %paused) (big_map %permit_expiries (pair address bytes) (option nat))))
  0033:                           (pair (big_map %permits (pair address bytes) timestamp)
  0034:                                 (pair (nat %totalSupply) (big_map %user_expiries address (option nat)))))))
  0035:            (pair (list %operations operation)
  0036:                  (pair (nat %result)
  0037:                        (pair %storage
  0038:                           (pair (pair (address %administrator)
  0039:                                       (big_map %balances address (pair (map %approvals address nat) (nat %balance))))
  0040:                                 (pair (nat %counter) (pair (nat %default_expiry) (nat %max_expiry))))
  0041:                           (pair (pair (big_map %metadata string bytes)
  0042:                                       (pair (bool %paused) (big_map %permit_expiries (pair address bytes) (option nat))))
  0043:                                 (pair (big_map %permits (pair address bytes) timestamp)
  0044:                                       (pair (nat %totalSupply) (big_map %user_expiries address (option nat))))))))
  0045:            { NIL operation ;
  0046:              SWAP ;
  0047:              DUP ;
  0048:              DUG 2 ;
  0049:              CDR ;
  0050:              DUP ;
  0051:              CDADDR ;
  0052:              DIG 3 ;
  0053:              DUP ;
  0054:              DUG 4 ;
  0055:              CAR ;
  0056:              MEM ;
  0057:              IF { DUP ;
  0058:                   CDADDR ;
  0059:                   DIG 3 ;
  0060:                   DUP ;
  0061:                   DUG 4 ;
  0062:                   CAR ;
  0063:                   GET ;
  0064:                   IF_SOME {} { PUSH int 114 ; FAILWITH } ;
  0065:                   IF_SOME { DROP ; PUSH bool True } { PUSH bool False } }
  0066:                 { PUSH bool False } ;
  0067:              IF { DUP ;
  0068:                   CDADDR ;
  0069:                   DIG 3 ;
  0070:                   CAR ;
  0071:                   GET ;
  0072:                   IF_SOME {} { PUSH int 115 ; FAILWITH } ;
  0073:                   IF_SOME {} { PUSH int 115 ; FAILWITH } }
  0074:                 { DUP ;
  0075:                   CDDDDR ;
  0076:                   DIG 3 ;
  0077:                   DUP ;
  0078:                   DUG 4 ;
  0079:                   CAAR ;
  0080:                   MEM ;
  0081:                   IF { DUP ;
  0082:                        CDDDDR ;
  0083:                        DIG 3 ;
  0084:                        DUP ;
  0085:                        DUG 4 ;
  0086:                        CAAR ;
  0087:                        GET ;
  0088:                        IF_SOME {} { PUSH int 118 ; FAILWITH } ;
  0089:                        IF_SOME { DROP ; PUSH bool True } { PUSH bool False } }
  0090:                      { PUSH bool False } ;
  0091:                   IF { DUP ;
  0092:                        CDDDDR ;
  0093:                        DIG 3 ;
  0094:                        CAAR ;
  0095:                        GET ;
  0096:                        IF_SOME {} { PUSH int 119 ; FAILWITH } ;
  0097:                        IF_SOME {} { PUSH int 119 ; FAILWITH } }
  0098:                      { DIG 2 ; DROP ; DUP ; CADDAR } } ;
  0099:              PAIR %result %storage ;
  0100:              SWAP ;
  0101:              PAIR %operations } ;
  0102:          SWAP ;
  0103:          LAMBDA
  0104:            (pair (pair %in_param (address %from_) (pair (address %to_) (nat %value)))
  0105:                  (pair %in_storage
  0106:                     (pair (pair (address %administrator)
  0107:                                 (big_map %balances address (pair (map %approvals address nat) (nat %balance))))
  0108:                           (pair (nat %counter) (pair (nat %default_expiry) (nat %max_expiry))))
  0109:                     (pair (pair (big_map %metadata string bytes)
  0110:                                 (pair (bool %paused) (big_map %permit_expiries (pair address bytes) (option nat))))
  0111:                           (pair (big_map %permits (pair address bytes) timestamp)
  0112:                                 (pair (nat %totalSupply) (big_map %user_expiries address (option nat)))))))
  0113:            (pair (list %operations operation)
  0114:                  (pair (bool %result)
  0115:                        (pair %storage
  0116:                           (pair (pair (address %administrator)
  0117:                                       (big_map %balances address (pair (map %approvals address nat) (nat %balance))))
  0118:                                 (pair (nat %counter) (pair (nat %default_expiry) (nat %max_expiry))))
  0119:                           (pair (pair (big_map %metadata string bytes)
  0120:                                       (pair (bool %paused) (big_map %permit_expiries (pair address bytes) (option nat))))
  0121:                                 (pair (big_map %permits (pair address bytes) timestamp)
  0122:                                       (pair (nat %totalSupply) (big_map %user_expiries address (option nat))))))))
  0123:            { NIL operation ;
  0124:              SWAP ;
  0125:              DUP ;
  0126:              DUG 2 ;
  0127:              CDR ;
  0128:              DUP ;
  0129:              CDDAR ;
  0130:              DIG 3 ;
  0131:              DUP ;
  0132:              DUG 4 ;
  0133:              CAR ;
  0134:              PACK ;
  0135:              BLAKE2B ;
  0136:              DIG 4 ;
  0137:              DUP ;
  0138:              DUG 5 ;
  0139:              CAAR ;
  0140:              PAIR ;
  0141:              MEM ;
  0142:              IF { DUP ;
  0143:                   CDADDR ;
  0144:                   DIG 3 ;
  0145:                   DUP ;
  0146:                   DUG 4 ;
  0147:                   CAR ;
  0148:                   PACK ;
  0149:                   BLAKE2B ;
  0150:                   DIG 4 ;
  0151:                   DUP ;
  0152:                   DUG 5 ;
  0153:                   CAAR ;
  0154:                   PAIR ;
  0155:                   MEM ;
  0156:                   IF { DUP ;
  0157:                        CDADDR ;
  0158:                        DIG 3 ;
  0159:                        DUP ;
  0160:                        DUG 4 ;
  0161:                        CAR ;
  0162:                        PACK ;
  0163:                        BLAKE2B ;
  0164:                        DIG 4 ;
  0165:                        DUP ;
  0166:                        DUG 5 ;
  0167:                        CAAR ;
  0168:                        PAIR ;
  0169:                        GET ;
  0170:                        IF_SOME {} { PUSH int 67 ; FAILWITH } ;
  0171:                        IF_SOME { DROP ; PUSH bool True } { PUSH bool False } }
  0172:                      { PUSH bool False } ;
  0173:                   IF { DUP ;
  0174:                        CDADDR ;
  0175:                        DIG 3 ;
  0176:                        DUP ;
  0177:                        DUG 4 ;
  0178:                        CAR ;
  0179:                        PACK ;
  0180:                        BLAKE2B ;
  0181:                        DIG 4 ;
  0182:                        DUP ;
  0183:                        DUG 5 ;
  0184:                        CAAR ;
  0185:                        PAIR ;
  0186:                        GET ;
  0187:                        IF_SOME {} { PUSH int 68 ; FAILWITH } ;
  0188:                        IF_SOME {} { PUSH int 68 ; FAILWITH } }
  0189:                      { DUP ;
  0190:                        CDDDDR ;
  0191:                        DIG 3 ;
  0192:                        DUP ;
  0193:                        DUG 4 ;
  0194:                        CAAR ;
  0195:                        MEM ;
  0196:                        IF { DUP ;
  0197:                             CDDDDR ;
  0198:                             DIG 3 ;
  0199:                             DUP ;
  0200:                             DUG 4 ;
  0201:                             CAAR ;
  0202:                             GET ;
  0203:                             IF_SOME {} { PUSH int 70 ; FAILWITH } ;
  0204:                             IF_SOME { DROP ; PUSH bool True } { PUSH bool False } }
  0205:                           { PUSH bool False } ;
  0206:                        IF { DUP ;
  0207:                             CDDDDR ;
  0208:                             DIG 3 ;
  0209:                             DUP ;
  0210:                             DUG 4 ;
  0211:                             CAAR ;
  0212:                             GET ;
  0213:                             IF_SOME {} { PUSH int 71 ; FAILWITH } ;
  0214:                             IF_SOME {} { PUSH int 71 ; FAILWITH } }
  0215:                           { DUP ; CADDAR } } ;
  0216:                   SWAP ;
  0217:                   DUP ;
  0218:                   DUG 2 ;
  0219:                   CDDAR ;
  0220:                   DIG 4 ;
  0221:                   DUP ;
  0222:                   DUG 5 ;
  0223:                   CAR ;
  0224:                   PACK ;
  0225:                   BLAKE2B ;
  0226:                   DIG 5 ;
  0227:                   DUP ;
  0228:                   DUG 6 ;
  0229:                   CAAR ;
  0230:                   PAIR ;
  0231:                   GET ;
  0232:                   IF_SOME {} { PUSH int 66 ; FAILWITH } ;
  0233:                   NOW ;
  0234:                   SUB ;
  0235:                   ISNAT ;
  0236:                   IF_SOME {} { PUSH int 76 ; FAILWITH } ;
  0237:                   COMPARE ;
  0238:                   GE ;
  0239:                   IF { DUP ;
  0240:                        CDDAR ;
  0241:                        DIG 3 ;
  0242:                        DUP ;
  0243:                        DUG 4 ;
  0244:                        CAR ;
  0245:                        PACK ;
  0246:                        BLAKE2B ;
  0247:                        DIG 4 ;
  0248:                        DUP ;
  0249:                        DUG 5 ;
  0250:                        CAAR ;
  0251:                        PAIR ;
  0252:                        MEM ;
  0253:                        IF { DUP ;
  0254:                             CAR ;
  0255:                             SWAP ;
  0256:                             CDR ;
  0257:                             DUP ;
  0258:                             CAR ;
  0259:                             SWAP ;
  0260:                             CDR ;
  0261:                             DUP ;
  0262:                             CDR ;
  0263:                             SWAP ;
  0264:                             CAR ;
  0265:                             NONE timestamp ;
  0266:                             DIG 6 ;
  0267:                             DUP ;
  0268:                             DUG 7 ;
  0269:                             CAR ;
  0270:                             PACK ;
  0271:                             BLAKE2B ;
  0272:                             DIG 7 ;
  0273:                             DUP ;
  0274:                             DUG 8 ;
  0275:                             CAAR ;
  0276:                             PAIR ;
  0277:                             UPDATE ;
  0278:                             PAIR ;
  0279:                             SWAP ;
  0280:                             PAIR ;
  0281:                             SWAP ;
  0282:                             PAIR }
  0283:                           {} ;
  0284:                        DUP ;
  0285:                        CDADDR ;
  0286:                        DIG 3 ;
  0287:                        DUP ;
  0288:                        DUG 4 ;
  0289:                        CAR ;
  0290:                        PACK ;
  0291:                        BLAKE2B ;
  0292:                        DIG 4 ;
  0293:                        DUP ;
  0294:                        DUG 5 ;
  0295:                        CAAR ;
  0296:                        PAIR ;
  0297:                        MEM ;
  0298:                        IF { DUP ;
  0299:                             CAR ;
  0300:                             SWAP ;
  0301:                             CDR ;
  0302:                             DUP ;
  0303:                             CDR ;
  0304:                             SWAP ;
  0305:                             CAR ;
  0306:                             DUP ;
  0307:                             CAR ;
  0308:                             SWAP ;
  0309:                             CDR ;
  0310:                             DUP ;
  0311:                             CAR ;
  0312:                             SWAP ;
  0313:                             CDR ;
  0314:                             NONE (option nat) ;
  0315:                             DIG 7 ;
  0316:                             DUP ;
  0317:                             DUG 8 ;
  0318:                             CAR ;
  0319:                             PACK ;
  0320:                             BLAKE2B ;
  0321:                             DIG 8 ;
  0322:                             CAAR ;
  0323:                             PAIR ;
  0324:                             UPDATE ;
  0325:                             SWAP ;
  0326:                             PAIR ;
  0327:                             SWAP ;
  0328:                             PAIR ;
  0329:                             PAIR ;
  0330:                             SWAP ;
  0331:                             PAIR }
  0332:                           { DIG 2 ; DROP } ;
  0333:                        PUSH bool False }
  0334:                      { DUP ;
  0335:                        CDDAR ;
  0336:                        DIG 3 ;
  0337:                        DUP ;
  0338:                        DUG 4 ;
  0339:                        CAR ;
  0340:                        PACK ;
  0341:                        BLAKE2B ;
  0342:                        DIG 4 ;
  0343:                        DUP ;
  0344:                        DUG 5 ;
  0345:                        CAAR ;
  0346:                        PAIR ;
  0347:                        MEM ;
  0348:                        IF { DUP ;
  0349:                             CAR ;
  0350:                             SWAP ;
  0351:                             CDR ;
  0352:                             DUP ;
  0353:                             CAR ;
  0354:                             SWAP ;
  0355:                             CDR ;
  0356:                             DUP ;
  0357:                             CDR ;
  0358:                             SWAP ;
  0359:                             CAR ;
  0360:                             NONE timestamp ;
  0361:                             DIG 6 ;
  0362:                             DUP ;
  0363:                             DUG 7 ;
  0364:                             CAR ;
  0365:                             PACK ;
  0366:                             BLAKE2B ;
  0367:                             DIG 7 ;
  0368:                             DUP ;
  0369:                             DUG 8 ;
  0370:                             CAAR ;
  0371:                             PAIR ;
  0372:                             UPDATE ;
  0373:                             PAIR ;
  0374:                             SWAP ;
  0375:                             PAIR ;
  0376:                             SWAP ;
  0377:                             PAIR }
  0378:                           {} ;
  0379:                        DUP ;
  0380:                        CDADDR ;
  0381:                        DIG 3 ;
  0382:                        DUP ;
  0383:                        DUG 4 ;
  0384:                        CAR ;
  0385:                        PACK ;
  0386:                        BLAKE2B ;
  0387:                        DIG 4 ;
  0388:                        DUP ;
  0389:                        DUG 5 ;
  0390:                        CAAR ;
  0391:                        PAIR ;
  0392:                        MEM ;
  0393:                        IF { DUP ;
  0394:                             CAR ;
  0395:                             SWAP ;
  0396:                             CDR ;
  0397:                             DUP ;
  0398:                             CDR ;
  0399:                             SWAP ;
  0400:                             CAR ;
  0401:                             DUP ;
  0402:                             CAR ;
  0403:                             SWAP ;
  0404:                             CDR ;
  0405:                             DUP ;
  0406:                             CAR ;
  0407:                             SWAP ;
  0408:                             CDR ;
  0409:                             NONE (option nat) ;
  0410:                             DIG 7 ;
  0411:                             DUP ;
  0412:                             DUG 8 ;
  0413:                             CAR ;
  0414:                             PACK ;
  0415:                             BLAKE2B ;
  0416:                             DIG 8 ;
  0417:                             CAAR ;
  0418:                             PAIR ;
  0419:                             UPDATE ;
  0420:                             SWAP ;
  0421:                             PAIR ;
  0422:                             SWAP ;
  0423:                             PAIR ;
  0424:                             PAIR ;
  0425:                             SWAP ;
  0426:                             PAIR }
  0427:                           { DIG 2 ; DROP } ;
  0428:                        PUSH bool True } }
  0429:                 { DIG 2 ; DROP ; PUSH bool False } ;
  0430:              PAIR %result %storage ;
  0431:              SWAP ;
  0432:              PAIR %operations } ;
  0433:          SWAP ;
  0434:          DUP ;
  0435:          CDR ;
  0436:          SWAP ;
  0437:          CAR ;
  0438:          IF_LEFT
  0439:            { IF_LEFT
  0440:                { IF_LEFT
  0441:                    { SWAP ;
  0442:                      DUP ;
  0443:                      DUG 2 ;
  0444:                      CDADAR ;
  0445:                      IF { PUSH string "WrongCondition: ~ self.data.paused" ; FAILWITH } {} ;
  0446:                      PUSH nat 0 ;
  0447:                      DIG 2 ;
  0448:                      DUP ;
  0449:                      DUG 3 ;
  0450:                      CAADR ;
  0451:                      SENDER ;
  0452:                      GET ;
  0453:                      IF_SOME {} { PUSH int 162 ; FAILWITH } ;
  0454:                      CAR ;
  0455:                      DIG 2 ;
  0456:                      DUP ;
  0457:                      DUG 3 ;
  0458:                      CAR ;
  0459:                      GET ;
  0460:                      IF_SOME {} { PUSH nat 0 } ;
  0461:                      COMPARE ;
  0462:                      EQ ;
  0463:                      IF { PUSH bool True } { DUP ; CDR ; PUSH nat 0 ; COMPARE ; EQ } ;
  0464:                      IF { DIG 2 ; DROP ; DIG 2 ; DROP }
  0465:                         { PUSH string "UnsafeAllowanceChange" ; FAILWITH } ;
  0466:                      SWAP ;
  0467:                      DUP ;
  0468:                      CDR ;
  0469:                      SWAP ;
  0470:                      CAR ;
  0471:                      DUP ;
  0472:                      CDR ;
  0473:                      SWAP ;
  0474:                      CAR ;
  0475:                      DUP ;
  0476:                      CAR ;
  0477:                      SWAP ;
  0478:                      CDR ;
  0479:                      DUP ;
  0480:                      SENDER ;
  0481:                      DUP ;
  0482:                      DUG 2 ;
  0483:                      GET ;
  0484:                      IF_SOME {} { PUSH int 166 ; FAILWITH } ;
  0485:                      DUP ;
  0486:                      CDR ;
  0487:                      SWAP ;
  0488:                      CAR ;
  0489:                      DIG 7 ;
  0490:                      DUP ;
  0491:                      CAR ;
  0492:                      SWAP ;
  0493:                      CDR ;
  0494:                      SOME ;
  0495:                      SWAP ;
  0496:                      UPDATE ;
  0497:                      PAIR ;
  0498:                      SOME ;
  0499:                      SWAP ;
  0500:                      UPDATE ;
  0501:                      SWAP ;
  0502:                      PAIR ;
  0503:                      PAIR ;
  0504:                      PAIR ;
  0505:                      NIL operation }
  0506:                    { IF_LEFT
  0507:                        { SWAP ;
  0508:                          DUP ;
  0509:                          DUG 2 ;
  0510:                          CAAAR ;
  0511:                          SENDER ;
  0512:                          COMPARE ;
  0513:                          EQ ;
  0514:                          IF {}
  0515:                             { PUSH string "WrongCondition: sp.sender == self.data.administrator" ;
  0516:                               FAILWITH } ;
  0517:                          DUP ;
  0518:                          CDR ;
  0519:                          DIG 2 ;
  0520:                          DUP ;
  0521:                          DUG 3 ;
  0522:                          CAADR ;
  0523:                          DIG 2 ;
  0524:                          DUP ;
  0525:                          DUG 3 ;
  0526:                          CAR ;
  0527:                          GET ;
  0528:                          IF_SOME {} { PUSH int 192 ; FAILWITH } ;
  0529:                          CDR ;
  0530:                          COMPARE ;
  0531:                          GE ;
  0532:                          IF { DIG 2 ; DROP ; DIG 2 ; DROP }
  0533:                             { PUSH string
  0534:                                    "WrongCondition: self.data.balances[params.address].balance >= params.value" ;
  0535:                               FAILWITH } ;
  0536:                          SWAP ;
  0537:                          DUP ;
  0538:                          DUG 2 ;
  0539:                          DUP ;
  0540:                          CDR ;
  0541:                          SWAP ;
  0542:                          CAR ;
  0543:                          DUP ;
  0544:                          CDR ;
  0545:                          SWAP ;
  0546:                          CAR ;
  0547:                          DUP ;
  0548:                          CAR ;
  0549:                          SWAP ;
  0550:                          CDR ;
  0551:                          DUP ;
  0552:                          DIG 5 ;
  0553:                          DUP ;
  0554:                          DUG 6 ;
  0555:                          CAR ;
  0556:                          DUP ;
  0557:                          DUG 2 ;
  0558:                          GET ;
  0559:                          IF_SOME {} { PUSH int 193 ; FAILWITH } ;
  0560:                          CAR ;
  0561:                          DIG 6 ;
  0562:                          DUP ;
  0563:                          DUG 7 ;
  0564:                          CDR ;
  0565:                          DIG 8 ;
  0566:                          CAADR ;
  0567:                          DIG 8 ;
  0568:                          DUP ;
  0569:                          DUG 9 ;
  0570:                          CAR ;
  0571:                          GET ;
  0572:                          IF_SOME {} { PUSH int 194 ; FAILWITH } ;
  0573:                          CDR ;
  0574:                          SUB ;
  0575:                          ISNAT ;
  0576:                          IF_SOME {} { PUSH int 193 ; FAILWITH } ;
  0577:                          SWAP ;
  0578:                          PAIR ;
  0579:                          SOME ;
  0580:                          SWAP ;
  0581:                          UPDATE ;
  0582:                          SWAP ;
  0583:                          PAIR ;
  0584:                          PAIR ;
  0585:                          PAIR ;
  0586:                          DUP ;
  0587:                          DUG 2 ;
  0588:                          DUP ;
  0589:                          CAR ;
  0590:                          SWAP ;
  0591:                          CDR ;
  0592:                          DUP ;
  0593:                          CAR ;
  0594:                          SWAP ;
  0595:                          CDR ;
  0596:                          DUP ;
  0597:                          CAR ;
  0598:                          SWAP ;
  0599:                          CDDR ;
  0600:                          DIG 4 ;
  0601:                          CDR ;
  0602:                          DIG 5 ;
  0603:                          CDDDAR ;
  0604:                          SUB ;
  0605:                          ISNAT ;
  0606:                          IF_SOME {} { PUSH int 195 ; FAILWITH } ;
  0607:                          PAIR ;
  0608:                          SWAP ;
  0609:                          PAIR ;
  0610:                          SWAP ;
  0611:                          PAIR ;
  0612:                          SWAP ;
  0613:                          PAIR ;
  0614:                          NIL operation }
  0615:                        { PUSH int 0 ;
  0616:                          NIL operation ;
  0617:                          DIG 2 ;
  0618:                          DUP ;
  0619:                          DUG 3 ;
  0620:                          ITER { DIG 4 ;
  0621:                                 DUP ;
  0622:                                 DUG 5 ;
  0623:                                 CDDAR ;
  0624:                                 SWAP ;
  0625:                                 DUP ;
  0626:                                 DUG 2 ;
  0627:                                 MEM ;
  0628:                                 IF {} { DUP ; PUSH string "NO_PERMIT_TO_DELETE" ; PAIR ; FAILWITH } ;
  0629:                                 DIG 6 ;
  0630:                                 DUP ;
  0631:                                 DUG 7 ;
  0632:                                 DIG 5 ;
  0633:                                 DIG 2 ;
  0634:                                 DUP ;
  0635:                                 DUG 3 ;
  0636:                                 PAIR %in_param %in_storage ;
  0637:                                 EXEC ;
  0638:                                 DUP ;
  0639:                                 CDDR ;
  0640:                                 DUG 5 ;
  0641:                                 DUP ;
  0642:                                 CAR ;
  0643:                                 ITER { DIG 3 ; SWAP ; CONS ; DUG 2 } ;
  0644:                                 DUP ;
  0645:                                 CDAR ;
  0646:                                 DIG 6 ;
  0647:                                 DUP ;
  0648:                                 DUG 7 ;
  0649:                                 CDDAR ;
  0650:                                 DIG 3 ;
  0651:                                 DUP ;
  0652:                                 DUG 4 ;
  0653:                                 GET ;
  0654:                                 IF_SOME {} { PUSH int 45 ; FAILWITH } ;
  0655:                                 NOW ;
  0656:                                 SUB ;
  0657:                                 ISNAT ;
  0658:                                 IF_SOME {} { PUSH int 46 ; FAILWITH } ;
  0659:                                 COMPARE ;
  0660:                                 GE ;
  0661:                                 IF { DROP }
  0662:                                    { SWAP ; DUP ; DUG 2 ; PUSH string "PERMIT_NOT_EXPIRED" ; PAIR ; FAILWITH } ;
  0663:                                 DIG 4 ;
  0664:                                 DUP ;
  0665:                                 DUG 5 ;
  0666:                                 CDDAR ;
  0667:                                 SWAP ;
  0668:                                 DUP ;
  0669:                                 DUG 2 ;
  0670:                                 MEM ;
  0671:                                 IF { DIG 4 ;
  0672:                                      DUP ;
  0673:                                      CAR ;
  0674:                                      SWAP ;
  0675:                                      CDR ;
  0676:                                      DUP ;
  0677:                                      CAR ;
  0678:                                      SWAP ;
  0679:                                      CDR ;
  0680:                                      DUP ;
  0681:                                      CDR ;
  0682:                                      SWAP ;
  0683:                                      CAR ;
  0684:                                      NONE timestamp ;
  0685:                                      DIG 5 ;
  0686:                                      DUP ;
  0687:                                      DUG 6 ;
  0688:                                      UPDATE ;
  0689:                                      PAIR ;
  0690:                                      SWAP ;
  0691:                                      PAIR ;
  0692:                                      SWAP ;
  0693:                                      PAIR ;
  0694:                                      DUG 4 }
  0695:                                    {} ;
  0696:                                 DIG 4 ;
  0697:                                 DUP ;
  0698:                                 DUG 5 ;
  0699:                                 CDADDR ;
  0700:                                 SWAP ;
  0701:                                 DUP ;
  0702:                                 DUG 2 ;
  0703:                                 MEM ;
  0704:                                 IF { DIG 4 ;
  0705:                                      DUP ;
  0706:                                      CAR ;
  0707:                                      SWAP ;
  0708:                                      CDR ;
  0709:                                      DUP ;
  0710:                                      CDR ;
  0711:                                      SWAP ;
  0712:                                      CAR ;
  0713:                                      DUP ;
  0714:                                      CAR ;
  0715:                                      SWAP ;
  0716:                                      CDR ;
  0717:                                      DUP ;
  0718:                                      CAR ;
  0719:                                      SWAP ;
  0720:                                      CDR ;
  0721:                                      NONE (option nat) ;
  0722:                                      DIG 6 ;
  0723:                                      UPDATE ;
  0724:                                      SWAP ;
  0725:                                      PAIR ;
  0726:                                      SWAP ;
  0727:                                      PAIR ;
  0728:                                      PAIR ;
  0729:                                      SWAP ;
  0730:                                      PAIR ;
  0731:                                      DUG 3 }
  0732:                                    { DROP } } ;
  0733:                          SWAP ;
  0734:                          DROP ;
  0735:                          SWAP ;
  0736:                          DROP ;
  0737:                          DIG 2 ;
  0738:                          DROP ;
  0739:                          DIG 2 ;
  0740:                          DROP } } }
  0741:                { IF_LEFT
  0742:                    { IF_LEFT
  0743:                        { DIG 2 ;
  0744:                          DROP ;
  0745:                          DIG 2 ;
  0746:                          DROP ;
  0747:                          CONTRACT address ;
  0748:                          NIL operation ;
  0749:                          SWAP ;
  0750:                          IF_SOME {} { PUSH int 219 ; FAILWITH } ;
  0751:                          PUSH mutez 0 ;
  0752:                          DIG 3 ;
  0753:                          DUP ;
  0754:                          DUG 4 ;
  0755:                          CAAAR ;
  0756:                          TRANSFER_TOKENS ;
  0757:                          CONS }
  0758:                        { DIG 2 ;
  0759:                          DROP ;
  0760:                          DIG 2 ;
  0761:                          DROP ;
  0762:                          DUP ;
  0763:                          CDR ;
  0764:                          CONTRACT nat ;
  0765:                          NIL operation ;
  0766:                          SWAP ;
  0767:                          IF_SOME {} { PUSH int 209 ; FAILWITH } ;
  0768:                          PUSH mutez 0 ;
  0769:                          DIG 4 ;
  0770:                          DUP ;
  0771:                          DUG 5 ;
  0772:                          CAADR ;
  0773:                          DIG 4 ;
  0774:                          DUP ;
  0775:                          DUG 5 ;
  0776:                          CAAR ;
  0777:                          GET ;
  0778:                          IF_SOME {} { PUSH int 208 ; FAILWITH } ;
  0779:                          CAR ;
  0780:                          DIG 4 ;
  0781:                          CADR ;
  0782:                          GET ;
  0783:                          IF_SOME {} { PUSH int 208 ; FAILWITH } ;
  0784:                          TRANSFER_TOKENS ;
  0785:                          CONS } }
  0786:                    { IF_LEFT
  0787:                        { DIG 2 ;
  0788:                          DROP ;
  0789:                          DIG 2 ;
  0790:                          DROP ;
  0791:                          DUP ;
  0792:                          CDR ;
  0793:                          CONTRACT nat ;
  0794:                          NIL operation ;
  0795:                          SWAP ;
  0796:                          IF_SOME {} { PUSH int 204 ; FAILWITH } ;
  0797:                          PUSH mutez 0 ;
  0798:                          DIG 4 ;
  0799:                          DUP ;
  0800:                          DUG 5 ;
  0801:                          CAADR ;
  0802:                          DIG 4 ;
  0803:                          CAR ;
  0804:                          GET ;
  0805:                          IF_SOME {} { PUSH int 203 ; FAILWITH } ;
  0806:                          CDR ;
  0807:                          TRANSFER_TOKENS ;
  0808:                          CONS }
  0809:                        { DIG 2 ;
  0810:                          DROP ;
  0811:                          DIG 2 ;
  0812:                          DROP ;
  0813:                          CONTRACT nat ;
  0814:                          NIL operation ;
  0815:                          SWAP ;
  0816:                          IF_SOME {} { PUSH int 223 ; FAILWITH } ;
  0817:                          PUSH mutez 0 ;
  0818:                          DIG 3 ;
  0819:                          DUP ;
  0820:                          DUG 4 ;
  0821:                          CADAR ;
  0822:                          TRANSFER_TOKENS ;
  0823:                          CONS } } } }
  0824:            { IF_LEFT
  0825:                { IF_LEFT
  0826:                    { IF_LEFT
  0827:                        { DIG 2 ;
  0828:                          DROP ;
  0829:                          DIG 2 ;
  0830:                          DROP ;
  0831:                          CONTRACT nat ;
  0832:                          NIL operation ;
  0833:                          SWAP ;
  0834:                          IF_SOME {} { PUSH int 229 ; FAILWITH } ;
  0835:                          PUSH mutez 0 ;
  0836:                          DIG 3 ;
  0837:                          DUP ;
  0838:                          DUG 4 ;
  0839:                          CADDAR ;
  0840:                          TRANSFER_TOKENS ;
  0841:                          CONS }
  0842:                        { DIG 2 ;
  0843:                          DROP ;
  0844:                          DIG 2 ;
  0845:                          DROP ;
  0846:                          CONTRACT nat ;
  0847:                          NIL operation ;
  0848:                          SWAP ;
  0849:                          IF_SOME {} { PUSH int 214 ; FAILWITH } ;
  0850:                          PUSH mutez 0 ;
  0851:                          DIG 3 ;
  0852:                          DUP ;
  0853:                          DUG 4 ;
  0854:                          CDDDAR ;
  0855:                          TRANSFER_TOKENS ;
  0856:                          CONS } }
  0857:                    { IF_LEFT
  0858:                        { SWAP ;
  0859:                          DUP ;
  0860:                          DUG 2 ;
  0861:                          CAAAR ;
  0862:                          SENDER ;
  0863:                          COMPARE ;
  0864:                          EQ ;
  0865:                          IF {}
  0866:                             { PUSH string "WrongCondition: sp.sender == self.data.administrator" ;
  0867:                               FAILWITH } ;
  0868:                          SWAP ;
  0869:                          DUP ;
  0870:                          DUG 2 ;
  0871:                          CAADR ;
  0872:                          SWAP ;
  0873:                          DUP ;
  0874:                          DUG 2 ;
  0875:                          CAR ;
  0876:                          MEM ;
  0877:                          IF { DIG 2 ; DROP ; DIG 2 ; DROP }
  0878:                             { DIG 2 ;
  0879:                               DROP ;
  0880:                               DIG 2 ;
  0881:                               DROP ;
  0882:                               SWAP ;
  0883:                               DUP ;
  0884:                               CDR ;
  0885:                               SWAP ;
  0886:                               CAR ;
  0887:                               DUP ;
  0888:                               CDR ;
  0889:                               SWAP ;
  0890:                               CAR ;
  0891:                               DUP ;
  0892:                               CAR ;
  0893:                               SWAP ;
  0894:                               CDR ;
  0895:                               DIG 4 ;
  0896:                               DUP ;
  0897:                               DUG 5 ;
  0898:                               CAR ;
  0899:                               PUSH (option (pair (map %approvals address nat) (nat %balance))) (Some (Pair {} 0)) ;
  0900:                               SWAP ;
  0901:                               UPDATE ;
  0902:                               SWAP ;
  0903:                               PAIR ;
  0904:                               PAIR ;
  0905:                               PAIR ;
  0906:                               SWAP } ;
  0907:                          SWAP ;
  0908:                          DUP ;
  0909:                          CDR ;
  0910:                          SWAP ;
  0911:                          CAR ;
  0912:                          DUP ;
  0913:                          CDR ;
  0914:                          SWAP ;
  0915:                          CAR ;
  0916:                          DUP ;
  0917:                          CAR ;
  0918:                          SWAP ;
  0919:                          CDR ;
  0920:                          DUP ;
  0921:                          DIG 5 ;
  0922:                          DUP ;
  0923:                          DUG 6 ;
  0924:                          CAR ;
  0925:                          DUP ;
  0926:                          DUG 2 ;
  0927:                          GET ;
  0928:                          IF_SOME {} { PUSH int 185 ; FAILWITH } ;
  0929:                          DUP ;
  0930:                          CAR ;
  0931:                          SWAP ;
  0932:                          CDR ;
  0933:                          DIG 7 ;
  0934:                          DUP ;
  0935:                          DUG 8 ;
  0936:                          CDR ;
  0937:                          ADD ;
  0938:                          SWAP ;
  0939:                          PAIR ;
  0940:                          SOME ;
  0941:                          SWAP ;
  0942:                          UPDATE ;
  0943:                          SWAP ;
  0944:                          PAIR ;
  0945:                          PAIR ;
  0946:                          PAIR ;
  0947:                          DUP ;
  0948:                          CAR ;
  0949:                          SWAP ;
  0950:                          CDR ;
  0951:                          DUP ;
  0952:                          CAR ;
  0953:                          SWAP ;
  0954:                          CDR ;
  0955:                          DUP ;
  0956:                          CAR ;
  0957:                          SWAP ;
  0958:                          CDR ;
  0959:                          DUP ;
  0960:                          CDR ;
  0961:                          SWAP ;
  0962:                          CAR ;
  0963:                          DIG 5 ;
  0964:                          CDR ;
  0965:                          ADD ;
  0966:                          PAIR ;
  0967:                          SWAP ;
  0968:                          PAIR ;
  0969:                          SWAP ;
  0970:                          PAIR ;
  0971:                          SWAP ;
  0972:                          PAIR ;
  0973:                          NIL operation }
  0974:                        { SWAP ;
  0975:                          DUP ;
  0976:                          DUG 2 ;
  0977:                          CDADAR ;
  0978:                          IF { PUSH string "WrongCondition: ~ self.data.paused" ; FAILWITH } {} ;
  0979:                          DUP ;
  0980:                          NIL operation ;
  0981:                          SWAP ;
  0982:                          ITER { DIG 5 ;
  0983:                                 DUP ;
  0984:                                 DUG 6 ;
  0985:                                 DIG 4 ;
  0986:                                 DIG 2 ;
  0987:                                 DUP ;
  0988:                                 CDDR ;
  0989:                                 SWAP ;
  0990:                                 DUP ;
  0991:                                 DUG 4 ;
  0992:                                 CAR ;
  0993:                                 HASH_KEY ;
  0994:                                 IMPLICIT_ACCOUNT ;
  0995:                                 ADDRESS ;
  0996:                                 PAIR ;
  0997:                                 PAIR %in_param %in_storage ;
  0998:                                 EXEC ;
  0999:                                 DUP ;
  1000:                                 CDDR ;
  1001:                                 DUG 4 ;
  1002:                                 DUP ;
  1003:                                 CAR ;
  1004:                                 ITER { DIG 3 ; SWAP ; CONS ; DUG 2 } ;
  1005:                                 DIG 4 ;
  1006:                                 DUP ;
  1007:                                 DUG 5 ;
  1008:                                 CDDAR ;
  1009:                                 DIG 2 ;
  1010:                                 DUP ;
  1011:                                 CDDR ;
  1012:                                 SWAP ;
  1013:                                 DUP ;
  1014:                                 DUG 4 ;
  1015:                                 CAR ;
  1016:                                 HASH_KEY ;
  1017:                                 IMPLICIT_ACCOUNT ;
  1018:                                 ADDRESS ;
  1019:                                 PAIR ;
  1020:                                 MEM ;
  1021:                                 IF { DUP ;
  1022:                                      CDAR ;
  1023:                                      DIG 5 ;
  1024:                                      DUP ;
  1025:                                      DUG 6 ;
  1026:                                      CDDAR ;
  1027:                                      DIG 3 ;
  1028:                                      DUP ;
  1029:                                      CDDR ;
  1030:                                      SWAP ;
  1031:                                      DUP ;
  1032:                                      DUG 5 ;
  1033:                                      CAR ;
  1034:                                      HASH_KEY ;
  1035:                                      IMPLICIT_ACCOUNT ;
  1036:                                      ADDRESS ;
  1037:                                      PAIR ;
  1038:                                      GET ;
  1039:                                      IF_SOME {} { PUSH int 102 ; FAILWITH } ;
  1040:                                      NOW ;
  1041:                                      SUB ;
  1042:                                      ISNAT ;
  1043:                                      IF_SOME {} { PUSH int 103 ; FAILWITH } ;
  1044:                                      COMPARE ;
  1045:                                      LT }
  1046:                                    { PUSH bool False } ;
  1047:                                 IF { SWAP ; DUP ; DUG 2 ; CDDR ; PUSH string "DUP_PERMIT" ; PAIR ; FAILWITH }
  1048:                                    {} ;
  1049:                                 SWAP ;
  1050:                                 DUP ;
  1051:                                 DUG 2 ;
  1052:                                 CDDR ;
  1053:                                 DIG 5 ;
  1054:                                 DUP ;
  1055:                                 DUG 6 ;
  1056:                                 CADAR ;
  1057:                                 PAIR ;
  1058:                                 SELF ;
  1059:                                 ADDRESS ;
  1060:                                 CHAIN_ID ;
  1061:                                 PAIR ;
  1062:                                 PAIR ;
  1063:                                 PACK ;
  1064:                                 DIG 2 ;
  1065:                                 DUP ;
  1066:                                 CDAR ;
  1067:                                 SWAP ;
  1068:                                 DUP ;
  1069:                                 DUG 4 ;
  1070:                                 CAR ;
  1071:                                 CHECK_SIGNATURE ;
  1072:                                 IF { DROP }
  1073:                                    { SWAP ;
  1074:                                      DUP ;
  1075:                                      DUG 2 ;
  1076:                                      CDDR ;
  1077:                                      DIG 5 ;
  1078:                                      DUP ;
  1079:                                      DUG 6 ;
  1080:                                      CADAR ;
  1081:                                      PAIR ;
  1082:                                      SELF ;
  1083:                                      ADDRESS ;
  1084:                                      CHAIN_ID ;
  1085:                                      PAIR ;
  1086:                                      PAIR ;
  1087:                                      PACK ;
  1088:                                      PUSH string "MISSIGNED" ;
  1089:                                      PAIR ;
  1090:                                      FAILWITH } ;
  1091:                                 DIG 3 ;
  1092:                                 DUP ;
  1093:                                 CAR ;
  1094:                                 SWAP ;
  1095:                                 CDR ;
  1096:                                 DUP ;
  1097:                                 CAR ;
  1098:                                 SWAP ;
  1099:                                 CDR ;
  1100:                                 DUP ;
  1101:                                 CDR ;
  1102:                                 SWAP ;
  1103:                                 CAR ;
  1104:                                 DIG 4 ;
  1105:                                 DUP ;
  1106:                                 CDDR ;
  1107:                                 SWAP ;
  1108:                                 CAR ;
  1109:                                 HASH_KEY ;
  1110:                                 IMPLICIT_ACCOUNT ;
  1111:                                 ADDRESS ;
  1112:                                 PAIR ;
  1113:                                 NOW ;
  1114:                                 SOME ;
  1115:                                 SWAP ;
  1116:                                 UPDATE ;
  1117:                                 PAIR ;
  1118:                                 SWAP ;
  1119:                                 PAIR ;
  1120:                                 SWAP ;
  1121:                                 PAIR ;
  1122:                                 DUP ;
  1123:                                 CDR ;
  1124:                                 SWAP ;
  1125:                                 CAR ;
  1126:                                 DUP ;
  1127:                                 CAR ;
  1128:                                 SWAP ;
  1129:                                 CDR ;
  1130:                                 DUP ;
  1131:                                 CDR ;
  1132:                                 SWAP ;
  1133:                                 CAR ;
  1134:                                 PUSH nat 1 ;
  1135:                                 ADD ;
  1136:                                 PAIR ;
  1137:                                 SWAP ;
  1138:                                 PAIR ;
  1139:                                 PAIR ;
  1140:                                 DUG 2 } ;
  1141:                          SWAP ;
  1142:                          DROP ;
  1143:                          DIG 2 ;
  1144:                          DROP ;
  1145:                          DIG 2 ;
  1146:                          DROP } } }
  1147:                { IF_LEFT
  1148:                    { IF_LEFT
  1149:                        { SWAP ;
  1150:                          DUP ;
  1151:                          DUG 2 ;
  1152:                          CAAAR ;
  1153:                          SENDER ;
  1154:                          COMPARE ;
  1155:                          EQ ;
  1156:                          IF { DIG 2 ; DROP ; DIG 2 ; DROP }
  1157:                             { PUSH string "WrongCondition: sp.sender == self.data.administrator" ;
  1158:                               FAILWITH } ;
  1159:                          SWAP ;
  1160:                          DUP ;
  1161:                          CDR ;
  1162:                          SWAP ;
  1163:                          CAR ;
  1164:                          DUP ;
  1165:                          CDR ;
  1166:                          SWAP ;
  1167:                          CADR ;
  1168:                          DIG 3 ;
  1169:                          PAIR ;
  1170:                          PAIR ;
  1171:                          PAIR }
  1172:                        { SWAP ;
  1173:                          DUP ;
  1174:                          DUG 2 ;
  1175:                          CDADAR ;
  1176:                          IF { PUSH string "WrongCondition: ~ self.data.paused" ; FAILWITH } {} ;
  1177:                          SWAP ;
  1178:                          DUP ;
  1179:                          DUG 2 ;
  1180:                          CADDDR ;
  1181:                          SWAP ;
  1182:                          DUP ;
  1183:                          DUG 2 ;
  1184:                          CDDR ;
  1185:                          COMPARE ;
  1186:                          LE ;
  1187:                          IF {} { PUSH string "MAX_SECONDS_EXCEEDED" ; FAILWITH } ;
  1188:                          SENDER ;
  1189:                          PACK ;
  1190:                          SWAP ;
  1191:                          DUP ;
  1192:                          DUG 2 ;
  1193:                          CAR ;
  1194:                          PACK ;
  1195:                          COMPARE ;
  1196:                          EQ ;
  1197:                          IF {} { PUSH bool False ; FAILWITH } ;
  1198:                          DUP ;
  1199:                          CDAR ;
  1200:                          IF_SOME
  1201:                            { DROP ;
  1202:                              SWAP ;
  1203:                              DUP ;
  1204:                              DUG 2 ;
  1205:                              CDDAR ;
  1206:                              SWAP ;
  1207:                              DUP ;
  1208:                              DUG 2 ;
  1209:                              CDAR ;
  1210:                              IF_SOME {} { PUSH int 132 ; FAILWITH } ;
  1211:                              DIG 2 ;
  1212:                              DUP ;
  1213:                              DUG 3 ;
  1214:                              CAR ;
  1215:                              PAIR ;
  1216:                              MEM ;
  1217:                              IF {} { PUSH string "PERMIT_NONEXISTENT" ; FAILWITH } ;
  1218:                              SWAP ;
  1219:                              DUP ;
  1220:                              DUG 2 ;
  1221:                              CDADDR ;
  1222:                              SWAP ;
  1223:                              DUP ;
  1224:                              DUG 2 ;
  1225:                              CDAR ;
  1226:                              IF_SOME {} { PUSH int 132 ; FAILWITH } ;
  1227:                              DIG 2 ;
  1228:                              DUP ;
  1229:                              DUG 3 ;
  1230:                              CAR ;
  1231:                              PAIR ;
  1232:                              MEM ;
  1233:                              IF { SWAP ;
  1234:                                   DUP ;
  1235:                                   DUG 2 ;
  1236:                                   CDADDR ;
  1237:                                   SWAP ;
  1238:                                   DUP ;
  1239:                                   DUG 2 ;
  1240:                                   CDAR ;
  1241:                                   IF_SOME {} { PUSH int 132 ; FAILWITH } ;
  1242:                                   DIG 2 ;
  1243:                                   DUP ;
  1244:                                   DUG 3 ;
  1245:                                   CAR ;
  1246:                                   PAIR ;
  1247:                                   GET ;
  1248:                                   IF_SOME {} { PUSH int 137 ; FAILWITH } ;
  1249:                                   IF_SOME { DROP ; PUSH bool True } { PUSH bool False } }
  1250:                                 { PUSH bool False } ;
  1251:                              IF { SWAP ;
  1252:                                   DUP ;
  1253:                                   DUG 2 ;
  1254:                                   CDADDR ;
  1255:                                   SWAP ;
  1256:                                   DUP ;
  1257:                                   DUG 2 ;
  1258:                                   CDAR ;
  1259:                                   IF_SOME {} { PUSH int 132 ; FAILWITH } ;
  1260:                                   DIG 2 ;
  1261:                                   DUP ;
  1262:                                   DUG 3 ;
  1263:                                   CAR ;
  1264:                                   PAIR ;
  1265:                                   GET ;
  1266:                                   IF_SOME {} { PUSH int 138 ; FAILWITH } ;
  1267:                                   IF_SOME {} { PUSH int 138 ; FAILWITH } ;
  1268:                                   DIG 2 ;
  1269:                                   DUP ;
  1270:                                   DUG 3 ;
  1271:                                   CDDAR ;
  1272:                                   DIG 2 ;
  1273:                                   DUP ;
  1274:                                   DUG 3 ;
  1275:                                   CDAR ;
  1276:                                   IF_SOME {} { PUSH int 132 ; FAILWITH } ;
  1277:                                   DIG 3 ;
  1278:                                   DUP ;
  1279:                                   DUG 4 ;
  1280:                                   CAR ;
  1281:                                   PAIR ;
  1282:                                   GET ;
  1283:                                   IF_SOME {} { PUSH int 135 ; FAILWITH } ;
  1284:                                   NOW ;
  1285:                                   SUB ;
  1286:                                   ISNAT ;
  1287:                                   IF_SOME {} { PUSH int 140 ; FAILWITH } ;
  1288:                                   COMPARE ;
  1289:                                   LT ;
  1290:                                   IF { DIG 2 ; DROP ; DIG 2 ; DROP }
  1291:                                      { PUSH string "PERMIT_REVOKED" ; FAILWITH } }
  1292:                                 { SWAP ;
  1293:                                   DUP ;
  1294:                                   DUG 2 ;
  1295:                                   CDDDDR ;
  1296:                                   SWAP ;
  1297:                                   DUP ;
  1298:                                   DUG 2 ;
  1299:                                   CAR ;
  1300:                                   MEM ;
  1301:                                   IF { SWAP ;
  1302:                                        DUP ;
  1303:                                        DUG 2 ;
  1304:                                        CDDDDR ;
  1305:                                        SWAP ;
  1306:                                        DUP ;
  1307:                                        DUG 2 ;
  1308:                                        CAR ;
  1309:                                        GET ;
  1310:                                        IF_SOME {} { PUSH int 143 ; FAILWITH } ;
  1311:                                        IF_SOME { DROP ; PUSH bool True } { PUSH bool False } }
  1312:                                      { PUSH bool False } ;
  1313:                                   IF { SWAP ;
  1314:                                        DUP ;
  1315:                                        DUG 2 ;
  1316:                                        CDDDDR ;
  1317:                                        SWAP ;
  1318:                                        DUP ;
  1319:                                        DUG 2 ;
  1320:                                        CAR ;
  1321:                                        GET ;
  1322:                                        IF_SOME {} { PUSH int 144 ; FAILWITH } ;
  1323:                                        IF_SOME {} { PUSH int 144 ; FAILWITH } ;
  1324:                                        DIG 2 ;
  1325:                                        DUP ;
  1326:                                        DUG 3 ;
  1327:                                        CDDAR ;
  1328:                                        DIG 2 ;
  1329:                                        DUP ;
  1330:                                        DUG 3 ;
  1331:                                        CDAR ;
  1332:                                        IF_SOME {} { PUSH int 132 ; FAILWITH } ;
  1333:                                        DIG 3 ;
  1334:                                        DUP ;
  1335:                                        DUG 4 ;
  1336:                                        CAR ;
  1337:                                        PAIR ;
  1338:                                        GET ;
  1339:                                        IF_SOME {} { PUSH int 135 ; FAILWITH } ;
  1340:                                        NOW ;
  1341:                                        SUB ;
  1342:                                        ISNAT ;
  1343:                                        IF_SOME {} { PUSH int 146 ; FAILWITH } ;
  1344:                                        COMPARE ;
  1345:                                        LT ;
  1346:                                        IF { DIG 2 ; DROP ; DIG 2 ; DROP }
  1347:                                           { PUSH string "PERMIT_REVOKED" ; FAILWITH } }
  1348:                                      { SWAP ;
  1349:                                        DUP ;
  1350:                                        CADDAR ;
  1351:                                        SWAP ;
  1352:                                        DUP ;
  1353:                                        DUG 3 ;
  1354:                                        CDDAR ;
  1355:                                        DIG 2 ;
  1356:                                        DUP ;
  1357:                                        DUG 3 ;
  1358:                                        CDAR ;
  1359:                                        IF_SOME {} { PUSH int 132 ; FAILWITH } ;
  1360:                                        DIG 3 ;
  1361:                                        DUP ;
  1362:                                        DUG 4 ;
  1363:                                        CAR ;
  1364:                                        PAIR ;
  1365:                                        GET ;
  1366:                                        IF_SOME {} { PUSH int 135 ; FAILWITH } ;
  1367:                                        NOW ;
  1368:                                        SUB ;
  1369:                                        ISNAT ;
  1370:                                        IF_SOME {} { PUSH int 149 ; FAILWITH } ;
  1371:                                        COMPARE ;
  1372:                                        LT ;
  1373:                                        IF { DIG 2 ; DROP ; DIG 2 ; DROP }
  1374:                                           { PUSH string "PERMIT_REVOKED" ; FAILWITH } } } ;
  1375:                              SWAP ;
  1376:                              DUP ;
  1377:                              CAR ;
  1378:                              SWAP ;
  1379:                              CDR ;
  1380:                              DUP ;
  1381:                              CDR ;
  1382:                              SWAP ;
  1383:                              CAR ;
  1384:                              DUP ;
  1385:                              CAR ;
  1386:                              SWAP ;
  1387:                              CDR ;
  1388:                              DUP ;
  1389:                              CAR ;
  1390:                              SWAP ;
  1391:                              CDR ;
  1392:                              DIG 5 ;
  1393:                              DUP ;
  1394:                              DUG 6 ;
  1395:                              CDAR ;
  1396:                              IF_SOME {} { PUSH int 132 ; FAILWITH } ;
  1397:                              DIG 6 ;
  1398:                              DUP ;
  1399:                              DUG 7 ;
  1400:                              CAR ;
  1401:                              PAIR ;
  1402:                              DIG 6 ;
  1403:                              CDDR ;
  1404:                              SOME ;
  1405:                              SOME ;
  1406:                              SWAP ;
  1407:                              UPDATE ;
  1408:                              SWAP ;
  1409:                              PAIR ;
  1410:                              SWAP ;
  1411:                              PAIR ;
  1412:                              PAIR ;
  1413:                              SWAP ;
  1414:                              PAIR }
  1415:                            { DIG 2 ;
  1416:                              DROP ;
  1417:                              DIG 2 ;
  1418:                              DROP ;
  1419:                              SWAP ;
  1420:                              DUP ;
  1421:                              CAR ;
  1422:                              SWAP ;
  1423:                              CDR ;
  1424:                              DUP ;
  1425:                              CAR ;
  1426:                              SWAP ;
  1427:                              CDR ;
  1428:                              DUP ;
  1429:                              CAR ;
  1430:                              SWAP ;
  1431:                              CDR ;
  1432:                              DUP ;
  1433:                              CAR ;
  1434:                              SWAP ;
  1435:                              CDR ;
  1436:                              DIG 5 ;
  1437:                              DUP ;
  1438:                              CAR ;
  1439:                              SWAP ;
  1440:                              CDDR ;
  1441:                              SOME ;
  1442:                              SOME ;
  1443:                              SWAP ;
  1444:                              UPDATE ;
  1445:                              SWAP ;
  1446:                              PAIR ;
  1447:                              SWAP ;
  1448:                              PAIR ;
  1449:                              SWAP ;
  1450:                              PAIR ;
  1451:                              SWAP ;
  1452:                              PAIR } } ;
  1453:                      NIL operation }
  1454:                    { IF_LEFT
  1455:                        { SWAP ;
  1456:                          DUP ;
  1457:                          DUG 2 ;
  1458:                          CAAAR ;
  1459:                          SENDER ;
  1460:                          COMPARE ;
  1461:                          EQ ;
  1462:                          IF { DIG 2 ; DROP ; DIG 2 ; DROP }
  1463:                             { PUSH string "WrongCondition: sp.sender == self.data.administrator" ;
  1464:                               FAILWITH } ;
  1465:                          SWAP ;
  1466:                          DUP ;
  1467:                          CAR ;
  1468:                          SWAP ;
  1469:                          CDR ;
  1470:                          DUP ;
  1471:                          CDR ;
  1472:                          SWAP ;
  1473:                          CAR ;
  1474:                          DUP ;
  1475:                          CAR ;
  1476:                          SWAP ;
  1477:                          CDDR ;
  1478:                          DIG 4 ;
  1479:                          PAIR ;
  1480:                          SWAP ;
  1481:                          PAIR ;
  1482:                          PAIR ;
  1483:                          SWAP ;
  1484:                          PAIR ;
  1485:                          NIL operation }
  1486:                        { SENDER ;
  1487:                          DIG 3 ;
  1488:                          DUP ;
  1489:                          DUG 4 ;
  1490:                          DIG 3 ;
  1491:                          DIG 3 ;
  1492:                          DUP ;
  1493:                          DUG 4 ;
  1494:                          PAIR %in_param %in_storage ;
  1495:                          EXEC ;
  1496:                          DUP ;
  1497:                          CDDR ;
  1498:                          DUG 3 ;
  1499:                          DUP ;
  1500:                          CAR ;
  1501:                          NIL operation ;
  1502:                          SWAP ;
  1503:                          ITER { CONS } ;
  1504:                          SWAP ;
  1505:                          DUP ;
  1506:                          DUG 2 ;
  1507:                          CDAR ;
  1508:                          IF { DIG 2 ; DROP ; DIG 2 ; DUP ; DUG 3 ; CAR ; DUG 2 } {} ;
  1509:                          DIG 4 ;
  1510:                          DUP ;
  1511:                          DUG 5 ;
  1512:                          CAAAR ;
  1513:                          DIG 3 ;
  1514:                          DUP ;
  1515:                          DUG 4 ;
  1516:                          COMPARE ;
  1517:                          EQ ;
  1518:                          IF { PUSH bool True }
  1519:                             { DIG 4 ;
  1520:                               DUP ;
  1521:                               DUG 5 ;
  1522:                               CDADAR ;
  1523:                               IF { PUSH bool False }
  1524:                                  { DIG 2 ;
  1525:                                    DUP ;
  1526:                                    DUG 3 ;
  1527:                                    DIG 4 ;
  1528:                                    DUP ;
  1529:                                    DUG 5 ;
  1530:                                    CAR ;
  1531:                                    COMPARE ;
  1532:                                    EQ ;
  1533:                                    IF { PUSH bool True }
  1534:                                       { DIG 3 ;
  1535:                                         DUP ;
  1536:                                         DUG 4 ;
  1537:                                         CDDR ;
  1538:                                         DIG 5 ;
  1539:                                         DUP ;
  1540:                                         DUG 6 ;
  1541:                                         CAADR ;
  1542:                                         DIG 5 ;
  1543:                                         DUP ;
  1544:                                         DUG 6 ;
  1545:                                         CAR ;
  1546:                                         GET ;
  1547:                                         IF_SOME {} { PUSH int 26 ; FAILWITH } ;
  1548:                                         CAR ;
  1549:                                         DIG 4 ;
  1550:                                         DUP ;
  1551:                                         DUG 5 ;
  1552:                                         GET ;
  1553:                                         IF_SOME {} { PUSH int 26 ; FAILWITH } ;
  1554:                                         COMPARE ;
  1555:                                         GE } } } ;
  1556:                          IF {}
  1557:                             { PUSH string
  1558:                                    "WrongCondition: (sender.value == self.data.administrator) | ((~ self.data.paused) & ((params.from_ == sender.value) | (self.data.balances[params.from_].approvals[sender.value] >= params.value)))" ;
  1559:                               FAILWITH } ;
  1560:                          DIG 4 ;
  1561:                          DUP ;
  1562:                          DUG 5 ;
  1563:                          CAADR ;
  1564:                          DIG 4 ;
  1565:                          DUP ;
  1566:                          DUG 5 ;
  1567:                          CDAR ;
  1568:                          MEM ;
  1569:                          IF {}
  1570:                             { DIG 4 ;
  1571:                               DUP ;
  1572:                               CDR ;
  1573:                               SWAP ;
  1574:                               CAR ;
  1575:                               DUP ;
  1576:                               CDR ;
  1577:                               SWAP ;
  1578:                               CAR ;
  1579:                               DUP ;
  1580:                               CAR ;
  1581:                               SWAP ;
  1582:                               CDR ;
  1583:                               DIG 7 ;
  1584:                               DUP ;
  1585:                               DUG 8 ;
  1586:                               CDAR ;
  1587:                               PUSH (option (pair (map %approvals address nat) (nat %balance))) (Some (Pair {} 0)) ;
  1588:                               SWAP ;
  1589:                               UPDATE ;
  1590:                               SWAP ;
  1591:                               PAIR ;
  1592:                               PAIR ;
  1593:                               PAIR ;
  1594:                               DUG 4 } ;
  1595:                          DIG 3 ;
  1596:                          DUP ;
  1597:                          DUG 4 ;
  1598:                          CDDR ;
  1599:                          DIG 5 ;
  1600:                          DUP ;
  1601:                          DUG 6 ;
  1602:                          CAADR ;
  1603:                          DIG 5 ;
  1604:                          DUP ;
  1605:                          DUG 6 ;
  1606:                          CAR ;
  1607:                          GET ;
  1608:                          IF_SOME {} { PUSH int 28 ; FAILWITH } ;
  1609:                          CDR ;
  1610:                          COMPARE ;
  1611:                          GE ;
  1612:                          IF {}
  1613:                             { PUSH string
  1614:                                    "WrongCondition: self.data.balances[params.from_].balance >= params.value" ;
  1615:                               FAILWITH } ;
  1616:                          DIG 4 ;
  1617:                          DUP ;
  1618:                          DUG 5 ;
  1619:                          DUP ;
  1620:                          CDR ;
  1621:                          SWAP ;
  1622:                          CAR ;
  1623:                          DUP ;
  1624:                          CDR ;
  1625:                          SWAP ;
  1626:                          CAR ;
  1627:                          DUP ;
  1628:                          CAR ;
  1629:                          SWAP ;
  1630:                          CDR ;
  1631:                          DUP ;
  1632:                          DIG 8 ;
  1633:                          DUP ;
  1634:                          DUG 9 ;
  1635:                          CAR ;
  1636:                          DUP ;
  1637:                          DUG 2 ;
  1638:                          GET ;
  1639:                          IF_SOME {} { PUSH int 29 ; FAILWITH } ;
  1640:                          CAR ;
  1641:                          DIG 9 ;
  1642:                          DUP ;
  1643:                          DUG 10 ;
  1644:                          CDDR ;
  1645:                          DIG 11 ;
  1646:                          CAADR ;
  1647:                          DIG 11 ;
  1648:                          DUP ;
  1649:                          DUG 12 ;
  1650:                          CAR ;
  1651:                          GET ;
  1652:                          IF_SOME {} { PUSH int 30 ; FAILWITH } ;
  1653:                          CDR ;
  1654:                          SUB ;
  1655:                          ISNAT ;
  1656:                          IF_SOME {} { PUSH int 29 ; FAILWITH } ;
  1657:                          SWAP ;
  1658:                          PAIR ;
  1659:                          SOME ;
  1660:                          SWAP ;
  1661:                          UPDATE ;
  1662:                          SWAP ;
  1663:                          PAIR ;
  1664:                          PAIR ;
  1665:                          PAIR ;
  1666:                          DUP ;
  1667:                          CDR ;
  1668:                          SWAP ;
  1669:                          CAR ;
  1670:                          DUP ;
  1671:                          CDR ;
  1672:                          SWAP ;
  1673:                          CAR ;
  1674:                          DUP ;
  1675:                          CAR ;
  1676:                          SWAP ;
  1677:                          CDR ;
  1678:                          DUP ;
  1679:                          DIG 8 ;
  1680:                          DUP ;
  1681:                          DUG 9 ;
  1682:                          CDAR ;
  1683:                          DUP ;
  1684:                          DUG 2 ;
  1685:                          GET ;
  1686:                          IF_SOME {} { PUSH int 31 ; FAILWITH } ;
  1687:                          DUP ;
  1688:                          CAR ;
  1689:                          SWAP ;
  1690:                          CDR ;
  1691:                          DIG 10 ;
  1692:                          DUP ;
  1693:                          DUG 11 ;
  1694:                          CDDR ;
  1695:                          ADD ;
  1696:                          SWAP ;
  1697:                          PAIR ;
  1698:                          SOME ;
  1699:                          SWAP ;
  1700:                          UPDATE ;
  1701:                          SWAP ;
  1702:                          PAIR ;
  1703:                          PAIR ;
  1704:                          PAIR ;
  1705:                          DUG 4 ;
  1706:                          DIG 2 ;
  1707:                          DUP ;
  1708:                          DUG 3 ;
  1709:                          DIG 4 ;
  1710:                          DUP ;
  1711:                          DUG 5 ;
  1712:                          CAR ;
  1713:                          COMPARE ;
  1714:                          NEQ ;
  1715:                          IF { DIG 2 ; DUP ; DUG 3 ; DIG 5 ; DUP ; DUG 6 ; CAAAR ; COMPARE ; NEQ }
  1716:                             { PUSH bool False } ;
  1717:                          IF { SWAP ;
  1718:                               DROP ;
  1719:                               DIG 4 ;
  1720:                               DROP ;
  1721:                               DIG 4 ;
  1722:                               DROP ;
  1723:                               DIG 3 ;
  1724:                               DUP ;
  1725:                               DUG 4 ;
  1726:                               DUP ;
  1727:                               CDR ;
  1728:                               SWAP ;
  1729:                               CAR ;
  1730:                               DUP ;
  1731:                               CDR ;
  1732:                               SWAP ;
  1733:                               CAR ;
  1734:                               DUP ;
  1735:                               CAR ;
  1736:                               SWAP ;
  1737:                               CDR ;
  1738:                               DUP ;
  1739:                               DIG 7 ;
  1740:                               DUP ;
  1741:                               DUG 8 ;
  1742:                               CAR ;
  1743:                               DUP ;
  1744:                               DUG 2 ;
  1745:                               GET ;
  1746:                               IF_SOME {} { PUSH int 33 ; FAILWITH } ;
  1747:                               DUP ;
  1748:                               CDR ;
  1749:                               SWAP ;
  1750:                               CAR ;
  1751:                               DIG 8 ;
  1752:                               DIG 9 ;
  1753:                               DUP ;
  1754:                               DUG 10 ;
  1755:                               CDDR ;
  1756:                               DIG 11 ;
  1757:                               CAADR ;
  1758:                               DIG 11 ;
  1759:                               CAR ;
  1760:                               GET ;
  1761:                               IF_SOME {} { PUSH int 34 ; FAILWITH } ;
  1762:                               CAR ;
  1763:                               DIG 2 ;
  1764:                               DUP ;
  1765:                               DUG 3 ;
  1766:                               GET ;
  1767:                               IF_SOME {} { PUSH int 34 ; FAILWITH } ;
  1768:                               SUB ;
  1769:                               ISNAT ;
  1770:                               IF_SOME {} { PUSH int 33 ; FAILWITH } ;
  1771:                               SOME ;
  1772:                               SWAP ;
  1773:                               UPDATE ;
  1774:                               PAIR ;
  1775:                               SOME ;
  1776:                               SWAP ;
  1777:                               UPDATE ;
  1778:                               SWAP ;
  1779:                               PAIR ;
  1780:                               PAIR ;
  1781:                               PAIR ;
  1782:                               SWAP }
  1783:                             { SWAP ; DROP ; SWAP ; DROP ; SWAP ; DROP ; DIG 2 ; DROP ; DIG 2 ; DROP } } } } } ;
  1784:          NIL operation ;
  1785:          SWAP ;
  1786:          ITER { CONS } ;
  1787:          PAIR } }
At line 1090 characters 37 to 45,
script reached FAILWITH instruction
with
  (Pair "MISSIGNED"
        0x05070707070a000000047a06a7700a00000016015d22ffe866052e73c7dc6e964601fdbc5913572c00070700010a00000020e6f1aa42d877954d34bbde9ca5bdd2676b139adb52ebc7b943fe8a07f55591e9)
Fatal error:
  transfer simulation failed
Warning:
  
   The node you are connecting to claims to be running in a
                    Tezos TEST SANDBOX.
      Do NOT use your fundraiser keys on this network.
  You should not see this message if you are not a developer.

Signature: edsigtmPaqoLGWLYYqNPvDoKgn9aFYEEkKJnSNpUhY14a3kqad4m18NYoZn4twQkvXKEQoigSE7uneqHCgswZYqyZbqqMBwesJr
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
