import re

# get rid of repetitions n steps away
def shrink(inputStr, nbSteps):
    idx = 0
    output = ""
    while idx < len(inputStr):
        print(idx)

        # get the current letter and append to output
        letter = inputStr[idx:idx+nbSteps]
        print("letter:", letter)

        # get the index of the next character
        innerIdx = idx + nbSteps
        
        # get tokens n steps long and compare with current token
        compLetter = inputStr[innerIdx:innerIdx+nbSteps]
        print("compLetter:", compLetter)
        isSkipped = False
        while compLetter == letter:
            innerIdx += nbSteps
            isSkipped = True
            if innerIdx > len(inputStr):
                break
            compLetter = inputStr[innerIdx:innerIdx+nbSteps]

        # if any character was skipped, add + token
        if isSkipped:
            output += "(" + letter + ")+"
            isSkipped = False
            idx = innerIdx
        # set the index to reflect the skip
        else:
            output += letter[0]
            idx += 1

    return output

# compose a [max strlen] x [# of strings] char matrix given input strings
def composeMatrix(inputStrings):
    inputStringsLen = [len(s) for s in inputStrings]
    maxStrLen = 0
    for s in inputStrings:
        maxStrLen = max(inputStringsLen)
    
    m = [[] for x in range(maxStrLen)]
    for row in range(maxStrLen):
        for s in inputStrings:
            if row < len(s):
                m[row].append(s[row])
            else:
                m[row].append("EOS")
    
    return m        


### Test 1 ###
print("Testing shrink():")

# initial variables
inputStr = "aaaaaaaabcabcabca"
maxChars = len(inputStr) / 2

# tests
output = shrink(inputStr, 1)
output = shrink(output, 2)
output = shrink(output, 3)

# print the resulting shortened regex string
print("Result:", output)


### Test 2 ###
print("Testing composeMatrix():")
inputStrings = ["aabc", "abc"]
print(composeMatrix(inputStrings))