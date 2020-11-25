#!/bin/bash
admin="tz1KqTpEZ7Yob7QbPE4Hy4Wo8fHG8LhKxZSx"
echo "COMPILING"
~/smartpy-cli/SmartPy.sh compile ./contract/token_contract.py "FA12(sp.address(\"$admin\"))" ./smartpy_generated/
echo "TESTING"
~/smartpy-cli/SmartPy.sh test ./contract/token_contract.py "FA12(sp.address(\"$admin\"))"
