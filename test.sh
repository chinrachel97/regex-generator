#!/bin/bash

# pre-defined testcases and answers
tests=(""               #0
        "ab"            #1
        "aab"           #2
        "aaab"          #3
        "abab"          #4
        "aabab"         #5
        "aababa"        #6
        "aababababa"    #7
        "<a><a>"        #8
)

answers=(""             #0
        "ab"            #1
        "(a)+b"         #2
        "(a)+b"         #3
        "(ab)+"         #4
        "(a)+bab"       #5
        "(a)+(ba)+"     #6
        "(a)+(ba)+"     #7
        "(<a>)+"        #8
)

len=${#tests[@]}
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

# check each case for pass/fail
for ((i=0; i<$len; i++))
do
    echo "Test $i: ${tests[$i]}"
    test=${tests[$i]}
    output="$(python generate.py $test)"
    echo "Result: $output"
    if [ "$output" = "${answers[$i]}" ]; then
        printf "${GREEN}pass${NC}"; else
        printf "${RED}fail${NC}"
    fi 
    printf "\n"
done