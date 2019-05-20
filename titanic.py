import csv

def openAndParse(filePath):

    with open(filePath,newline='') as csvToParse:
        
        csvRead = csv.reader(csvToParse,delimiter=',')
        csvLines = list()
        
        for readRow in csvRead:
            csvLines.append(readRow)
            
    return csvLines
            

def rearrangeList(inputList,desiredSort):
    
    listHeaders = inputList[0]
    targetSort = list()
    sortedList = list()
    
    for i in range(len(desiredSort)):
        try:
            targetSort.append(listHeaders.index(desiredSort[i]))
        except:
            print('WARNING: Could not locate column \'{}\'. Proceeding anyway.'.format(desiredSort[i]))
        
    for line in inputList:
        
        sortedLine = list()
        
        for j in range(len(targetSort)):
            sortedLine.append(line[targetSort[j]])
        
        sortedList.append(sortedLine)
        
    return sortedList


def writeFile(csvList,fileName):
    
    with open(fileName,'w',newline='') as csvTarget:
    
        fileWriter = csv.writer(csvTarget, delimiter = ',', quotechar = '"')
        
        for i in range(len(csvList)):
            fileWriter.writerow(csvList[i])


def reverseList(listOfNames):
    
    lenOfList = len(listOfNames)
    outputList = list()
    
    for i in range(lenOfList-1, -1, -1):
        
        outputList.append(listOfNames[i])
    
    return outputList


def everyOther(listOfNames):
    
    outputList = list()
    
    for i in range(len(listOfNames)):
        
        if (i % 2) == 1:
            outputList.append(listOfNames[i])
            
    return outputList


# Test functions

# rawDat = openAndParse('train.csv')
#  
#   
# revList = reverseList(rawDat[0])
# alternateList = everyOther(rawDat[0])
#  
#   
# reversedCols = rearrangeList(rawDat,revList)
# everyOtherCol = rearrangeList(rawDat, alternateList)
#   
# writeFile(reversedCols,'output/reversed.csv')
# writeFile(everyOtherCol,'output/alternating.csv')


