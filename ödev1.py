#a 

cost = 79
tax = cost * 0.08
tip = cost * 0.1
total = cost + tax + tip



print("The tax is " + str(tax) + " Eur and the tip is " + str(tip) + " Eur, making the total " + format(total, ".4f") + " Eur.")


print("The tax is " + format(tax, ".2f") + " Eur and the tip is " + format(tip, ".2f") + " Eur, making the total " + format(total, ".2f") + " Eur")


#b
cost = float(input("Please enter the cost of your meal: "))
tax = cost * 0.08
tip = cost * 0.1
total = cost + tax + tip


print("The tax is " + str(tax) + " Eur and the tip is " + str(tip) + " Eur, making the total " + format(total, ".2f") + " Eur")