import re

# initial variables
input = "aaabccccdeef"
output = ""
maxChars = len(input) / 2
idx = 0

# get rid of repetitions 1 step away
while idx < len(input):
    # get the current letter and append to output
    letter = input[idx]
    output += letter
    print(letter)

    # get the index of the next character
    innerIdx = idx + 1
    if innerIdx >= len(input):
        break

    # skip repeating letters 1 step away
    compLetter = input[innerIdx]
    isSkipped = False
    while compLetter == letter:
        innerIdx += 1
        if innerIdx >= len(input):
            break
        compLetter = input[innerIdx]
        isSkipped = True

    # if any character was skipped, add + token
    if isSkipped:
        output += "+"
        isSkipped = False
    
    # set the index to reflect the skip
    idx = innerIdx

# print the resulting shortened regex string
print("Result:", output)

# modify the above to remove repetitions n steps away