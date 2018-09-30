def taxRateFinder(taxPer,bracket):
    taxRate = []
    for number in range(len(bracket)) :
      taxRate.append((bracket[number] - bracket[number - 1]) * taxPer[number])
      if taxRate[number] != 0 :
        taxRate[number] = taxRate[number] + taxRate[number - 1]
    return taxRate