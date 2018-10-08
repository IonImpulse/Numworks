import math
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
slope = float((yAvgHigh-yAvgLow)/(xAvgHigh-xAvgLow))
b = yAvgLow - (xAvgLow * slope)
print("Linear:")
print("y =",slope,"x +",b)
print("============")
yQuadList = [x+(0-yList[0]) for x in yList]
xQuadList = [x+(0-xList[0]) for x in xList]
yQuadList1 = []
xQuadList1 = []
linTable(yQuadList,yQuadList1)
linTable(xQuadList,xQuadList1)
if len(yQuadList)% 2 == 0 :
    tMiddle = int(len(yQuadList) / 2)
    yMiddle = float((yQuadList[tMiddle]) + .5)
else :
    tMiddle = int((len(yQuadList) + 1) / 2)
    yMiddle = float(yQuadList[tMiddle])
xMiddle = math.sqrt(xQuadList1[1][len(xQuadList1[1])-1])
print(xQuadList1)
print(xMiddle)
