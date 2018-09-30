from taxEngine import *
print("a * (x - b) + c")
print("Multiplier? *a*")
taxPer = [float(x) for x in input(":").split(",")]
print("Bracket? *b*")
bracket = [float(x) for x in input(":").split(",")]
taxRate = taxRateFinder(taxPer,bracket)
print(taxPer[1],"x   ", "0 < x <",bracket[1])
bracket.append("Infinity")
for number in range(len(taxPer)-2) :
    print(taxPer[number+2],"* (x -",bracket[number+1],"+",taxRate[number+1],"|",bracket[number + 1],"< x <",bracket[number + 2])
