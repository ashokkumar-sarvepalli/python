def readFile(path):
    with open(path, "rt") as f:
        return f.read()

    
def buildPercentageChangeTable(contentsRead):
    i=0
    
    previousDay = 0
    currentDay= 0
    percentageChange = {}
    # its read as one massive string
    #print(contentsRead)
    for line in contentsRead.splitlines():
        columns = line.split(",")
        if i>1:
            arr = []
            currentDay= int(columns[2])
            currentDate = columns[0]
            if currentDay>1000:
                currentPercentage = ((currentDay-previousDay)/previousDay)*100
                arr.append(currentDay)
                arr.append(currentPercentage)
                percentageChange[currentDate] = arr
                #print("The percentage increase from ",previousDate,"to ",currentDate, "is : ", currentPercentage, "%")
            previousDay = currentDay
            previousDate = currentDate
        if i==1:
            previousDay= int(columns[2])
            previousDate =columns[0]
        i=i+1

    return percentageChange


contentsRead = readFile("njcovidcases.csv")
percentageChange = buildPercentageChangeTable(contentsRead)
#print(percentageChange)
for key in percentageChange:
    print(key,":",percentageChange[key])

