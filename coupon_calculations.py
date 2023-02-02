"""
Program: coupon_calculations
Author: Michael Mack
Last Date Modified: 2-1-23

"""
# import constant
import const

# variables
cash_off_subtotal = 0
percent_off_subtotal = 0
shipping_cost = 0

# print thanks and ask for purchase price
print("Thanks for shopping with us! Follow the next steps to calculate your total after discounts, tax, and shipping.")

# ask for purchase price
price = float(input("Please enter your purchase price: $"))

# ask for cash off coupons
cash_coupon = input("Do you have a cash off coupon? Enter y or n: ")

# cash coupon if statement
if cash_coupon == "y":
    cash_off = float(int(input("Please enter which Cash Off coupon you have: ")))
    if cash_off == 5:
        cash_off_subtotal = price - 5
    elif cash_off == 10:
        cash_off_subtotal = price - 10
else:
    cash_off_subtotal = price

type(price)

# ask for percent coupons
percent_coupon = input("Do you have a percent off coupon? Enter y or n: ")

# percent coupon if statement
if percent_coupon == "y":
    percent_off = float(int(input("Please enter which Percent Off coupon you have: ")))
    if percent_off == 10:
        percent_off_subtotal = float(cash_off_subtotal - (cash_off_subtotal*.1))
    elif percent_off == 15:
        percent_off_subtotal = float(cash_off_subtotal - (cash_off_subtotal*.15))
    elif percent_off == 20:
        percent_off_subtotal = float(cash_off_subtotal - (cash_off_subtotal*.2))
else:
    percent_off_subtotal = cash_off_subtotal

# Add shipping
if percent_off_subtotal <= 9.99:
    shipping_cost = 5.95
elif 9.99 < percent_off_subtotal <= 29.99:
    shipping_cost = 7.95
elif 29.99 < percent_off_subtotal <= 49.99:
    shipping_cost = 11.95
elif percent_off_subtotal > 49.99:
    shipping_cost = 0.00

# Add Tax
total_after_tax = percent_off_subtotal * float(const.TAX)

# Total
total = total_after_tax + shipping_cost

# Print Total
print(f"Thanks for your purchase, your total after discounts, tax, and shipping is: ${total: 5.2f}")

# test cases
# price     cash_off        percent_off     total expected      total
# 36.92     10              20              30.78               30.78
# 3.67      5               0               5.95                5.95
# 125.64    10              15              104.19              104.19
# 65.92     0               10              62.89               62.89


