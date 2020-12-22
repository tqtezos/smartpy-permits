#!/bin/bash
admin="tz1KqTpEZ7Yob7QbPE4Hy4Wo8fHG8LhKxZSx"
echo "COMPILING"
~/smartpy-cli/SmartPy.sh compile ./contract/FA1.2_Permit.py "FA12_Permit(sp.address(\"$admin\"))" ./smartpy_generated/
echo "TESTING"
~/smartpy-cli/SmartPy.sh test ./contract/FA1.2_Permit.py ./smartpy_generated
