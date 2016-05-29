"""
Author: Rona Chong
Name of program: taxes_and_tip_calculator.py
Description: This program asks the user for 3 inputs (price before tax, tax rate, and desired tip rate) and returns the total that the user should pay.
"""

print "Welcome to the taxes and tip calculator!"
priceBeforeTax = float(raw_input("What is the price before tax? "))
taxRate = float(raw_input("What are the taxes? (in %) "))
tipRate = float(raw_input("What do you want to tip? (in %) "))

print "The price you need to pay is: $%f." % ((priceBeforeTax*(1 + taxRate/100))*(1 + tipRate/100)) # calculating total by multiplying price before tax by 1 + tax rate and then multiplying that new amount by 1 + tip rate.
