import re

# initial variables
inputStr = "aabcaa"
output = ""
maxChars = len(inputStr) / 2
idx = 0

# get rid of repetitions 1 step away
while idx < len(inputStr):
    print(idx)
    # get the current letter and append to output
    letter = inputStr[idx]
    output += letter
    print(letter)

    # get the index of the next character
    innerIdx = idx + 1
    if innerIdx >= len(inputStr):
        break

    # skip repeating letters 1 step away
    compLetter = inputStr[innerIdx]
    isSkipped = False
    while compLetter == letter:
        innerIdx += 1
        isSkipped = True
        if innerIdx >= len(inputStr):
            break
        compLetter = inputStr[innerIdx]

    # if any character was skipped, add + token
    if isSkipped:
        output += "+"
        isSkipped = False
    
    # set the index to reflect the skip
    idx = innerIdx

# print the resulting shortened regex string
print("Result:", output)

# modify the above to remove repetitions n steps away