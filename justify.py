def parseFile(inputFileName):
    fileContent = open(inputFileName, "r").read()
    tokenList = fileContent.strip().split()
    for i in range(len(tokenList)):
        tokenList[i] = tokenList[i].strip()
    return tokenList


tokens = parseFile("in.txt")
tokenListLen = len(tokens)
lineLength = 0
resultStr = ""
outputLineList = []
wordCountPerLine = 0
for i in range(tokenListLen):
    tokLen = len(tokens[i])
    if lineLength + tokLen <= 80:
        lineLength += tokLen
        wordCountPerLine += 1
        if lineLength == 80:
            outputLineList.append(tokens[i])
        else:
            outputLineList.append(tokens[i] + ' ')
            lineLength += 1

    else:
        if str(outputLineList[-1]).endswith(' '):
            outputLineList[-1] = outputLineList[-1].strip()
            lineLength -= 1
        numSpaces = 80 - lineLength
        spacePerWord = numSpaces // wordCountPerLine
        for idx in range(len(outputLineList)):
            if spacePerWord == 0:
                if numSpaces > 0:
                    resultStr += outputLineList[idx] + ' '
                    numSpaces -= 1
                else:
                    resultStr += outputLineList[idx]

            else:
                if numSpaces > 0:
                    resultStr += outputLineList[idx] + ' ' * spacePerWord
                    numSpaces -= spacePerWord
                else:
                    resultStr += outputLineList[idx]
        resultStr = resultStr.strip()
        resultStr += '\n'
        outputLineList.clear()
        outputLineList.append(tokens[i] + ' ')
        wordCountPerLine = 1
        lineLength = len(tokens[i]) + 1

if str(outputLineList[-1]).endswith(' '):
    outputLineList[-1] = outputLineList[-1].strip()
    lineLength -= 1
numSpaces = 80 - lineLength
spacePerWord = numSpaces // (wordCountPerLine-1)
for idx in range(len(outputLineList)-1):
    if spacePerWord == 0:
        if numSpaces > 0:
            outputLineList[idx] = outputLineList[idx] + ' '
            numSpaces -= 1
    else:
        if numSpaces > 0:
            outputLineList[idx] = outputLineList[idx] + ' ' * spacePerWord
            numSpaces -= spacePerWord
extraspace = outputLineList[-1].count(' ')
numSpaces += extraspace
outputLineList[-1] = outputLineList[-1].strip()
for a in range(len(outputLineList)):
    if numSpaces > 0:
        outputLineList[a] = outputLineList[a] + ' '
        numSpaces -= 1
    else:
        break
for tok in outputLineList:
    resultStr += tok

resultStr += '\n'

outfile = open("Out.txt", "w");
outfile.write(resultStr);
