#!/bin/bash

echo "COMPILING"
~/smartpy-cli/SmartPy.sh compile ./contract/token_contract.py 'FA12(sp.address("tz1h3rQ8wBxFd8L9B3d7Jhaawu6Z568XU3xY"))' ./smartpy_generated/
echo "TESTING"
~/smartpy-cli/SmartPy.sh test ./contract/token_contract.py 'FA12(sp.address("tz1h3rQ8wBxFd8L9B3d7Jhaawu6Z568XU3xY"))' 
