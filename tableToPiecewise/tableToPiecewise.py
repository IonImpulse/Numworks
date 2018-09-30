print("a * (x - b) + c")
print("Multiplier? *a*")
taxPer = input(":")
print("Bracket? *b*")
bracket = input(":")
taxRate = []
for number in range(len(bracket)) :
  taxRate.append((bracket[number] - bracket[number - 1]) * taxPer[number])
  if taxRate[number] != 0 :
    taxRate[number] = taxRate[number] + taxRate[number - 1]
print(taxPer[0],"x   ", "0 < x <",bracket[1])
bracket.append("Infinity")
for number in range(len(taxPer)-1) :
    print(taxPer[number+1],"(x -",bracket[number+1],"+",taxRate[number] "0 < x <",bracket[number + 2])
