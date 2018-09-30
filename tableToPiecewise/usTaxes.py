import taxengine from *
print("What is your income?")
income = float(input(":"))
bracket = [0,9525,38700,82500,157500,200000,500000]
taxPer = [0,.10,.12,.22,.24,.32,.35,.37]
taxRate = []
taxRate = taxRateFinder(taxPer,bracket)
tax = 0
counter = 0
while tax == 0 :
  if counter <= 5 :
    if income >= bracket[counter] and income <= bracket[counter+1]:
      tax = (taxPer[counter + 1] * (income - bracket[counter])) + taxRate[counter]
  else:
    tax = (.37 * (income - 500000) + 150689.5)
  counter = counter + 1
print("Tax:",tax)
print((tax/income)*100,"%")
