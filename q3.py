def wordCount(t):
    """wordCount, counts the number of instances of each word in a text file"""
    file = open(t, 'r');
    lines = file.readlines();

    #removing newlines from end;
    count = 0;
    for line in lines:
        if (line[-1] == '\n'):
            lines[count] = line[:-1];
        count += 1;
    
    #splits strings into lists and counts
    lineNum = 0;
    wordsDict = {}
    for line in lines:
        lineNum = lineNum + 1;
        lineList = line.split();
        for word in lineList:
            if word not in wordsDict:
                wordsDict[word] = [lineNum];
            else:
                wordsDict[word].append(lineNum);
    #return statement
    return wordsDict;
mainDict = wordCount("corvor.txt");
print(mainDict);