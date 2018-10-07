def linTable (inputList,outputList) :
    outputList.append(inputList[:len(inputList)//2])
    if len(inputList)% 2 == 0 :
        outputList.append(inputList[len(inputList)//2:])
    else :
        outputList.append(inputList[(len(inputList)//2)+1:])
print("============")
print("Enter X list")
xList = [float(x) for x in input(":").split(",")]
print("Enter Y list")
yList = [float(x) for x in input(":").split(",")]
print("============")
xList1 = []
yList1 = []
linTable(xList,xList1)
linTable(yList,yList1)
xAvgLow = sum(xList1[0])/float(len(xList1[0]))
xAvgHigh = sum(xList1[1])/float(len(xList1[1]))
yAvgLow = sum(yList1[0])/float(len(yList1[0]))
yAvgHigh = sum(yList1[1])/float(len(yList1[1]))
xAvg = (xAvgLow + xAvgHigh) / 2
yAvg = (yAvgLow + yAvgHigh) / 2
slope = float(yAvg/xAvg)
x = 1
yAvg = 0 - yAvg
b = yAvg/(slope * (0 - xAvg))
