"""
Program: Basic if-elif Statement
Author: Michael Mack
Last Date Modified:  1-29-23

The purpose of this program is to give an example and display the use of an if-elseif statement.
"""

# Give information on the subscription and levels of subscription
print("Thank you for choosing Programmer's Toolkit Monthly Subscription Box!")
print("Each month we offer something different such as t-shirts, stickers, figurines, and programming books!")
print("There are four levels of subscription available Platinum, Gold, Silver, and Bronze.")
print("We also offer a free trial for those wanting to test the subscription.")

# Ask user for input on which subscription they are interested in and show the cost
level = input("Please enter the subscription level you want: ")

# Create if-elif statement to print prices
if level == 'Platinum':
    print("Price for Platinum is $60 a month. Thanks!")
elif level == 'Gold':
    print("Price for Gold is $50 a month, Thanks!")
elif level == 'Silver':
    print("Price for Silver is $40 a month, Thanks!")
elif level == 'Bronze':
    print("Price for Bronze is $30 a month, Thanks!")
elif level == 'Free Trial':
    print("Free trial selected, Thanks!")
else:
    print("Not a valid subscription.")

# Test cases, expected, and actual results

# Test Input      Expected        Result

# Platinum      Price: $60      Price: $60
# Bronze        Price: $30      Price: $30
# Yellow        Not Valid       Not Valid



