##
# Program Header:
# CIS 117 Python Programming: Lab #3
# Name: Damien Reggio
# Description: Programming with Numbers and Strings, Execution Control,
#   Iterator Structures and User Defined Functions
# Application: Your Supermarket Coupons – The Grocery Bill
# Topics: Imperative Programming
# Development Environment: Windows 7/Ubuntu 14.04
# Version: Python 3.7
# Filename: DamienReggioLab3.py
# Date: 2/5/2020

import re

COUPON_LVL_0 = 0
COUPON_LVL_1 = 8
COUPON_LVL_2 = 10
COUPON_LVL_3 = 12
COUPON_LVL_4 = 14
LVL_1 = 10
LVL_2 = 60
LVL_3 = 150
LVL_4 = 210

NUM_RUNS = 5

def main():
    """
    :input: no input
    ask user how big their grocery bill was and prints out discount amount
    :return:
    """
    grocery_total = get_grocery_bill()

    get_coupon_value(grocery_total)



def get_grocery_bill():
    """
    :input: no input (user is asked within function)
    Obtains grocery bill from users, if input is invalid, ask again
    :return: float of total grocery bill
    """
    total_valid = False  # to enter the while for the first time

    while not total_valid:
        grocery_total = input("Please enter the total amount of your grocery" +
                              " bill in the in #.## format: ")

        # lets allow for 1, 1.00 0.13 but not .13
        #
        if re.match('^\d+(\.\d{2})?$', grocery_total):
            total_valid = True
            try:
                grocery_total = float(grocery_total)
                if grocery_total < 0: # this check is not necessary due to RE
                    total_valid = False
            except ValueError: # this should never fire because of the RE
                total_valid = False
    return grocery_total

def money_format(money):
    """
    :param money: a float or an int representing a dollar and cent amount
    formats money into a pretty format
    :return: money as a string in /d+./d/d format
    """
    return ('{0:.2f}'.format(money))

def get_coupon_value(grocery_total):
    """
    :param gorcery_total: float, $ spent on groceries
    takes in total and outputs coupon discount uses predefined named constants
    prints out dollar value of discount and discount level
    :return: no return
    """
    if grocery_total < LVL_1:
        coupon_amount = COUPON_LVL_0
        discount = COUPON_LVL_0 / 100 * grocery_total
    elif grocery_total < LVL_2:
        coupon_amount = COUPON_LVL_1
        discount = COUPON_LVL_1 / 100 * grocery_total
    elif grocery_total < LVL_3:
        coupon_amount = COUPON_LVL_2
        discount = COUPON_LVL_2 / 100 * grocery_total
    elif grocery_total < LVL_4:
        coupon_amount = COUPON_LVL_3
        discount = COUPON_LVL_3 / 100 * grocery_total
    else:
        coupon_amount = COUPON_LVL_4
        discount = COUPON_LVL_4 / 100 * grocery_total

    print('You win a discount coupon of ${}. ({}% of your purchase)'
          .format(money_format(discount), coupon_amount))


if __name__ == '__main__':
    for i in range(0, NUM_RUNS):
        main()

# output
#
'''
Please enter the total amount of your grocery bill in the in #.## format: aasd
Please enter the total amount of your grocery bill in the in #.## format: 1 2 3
Please enter the total amount of your grocery bill in the in #.## format: -1
Please enter the total amount of your grocery bill in the in #.## format: 
Please enter the total amount of your grocery bill in the in #.## format: 5
You win a discount coupon of $0.00. (0% of your purchase)
Please enter the total amount of your grocery bill in the in #.## format: 30
You win a discount coupon of $2.40. (8% of your purchase)
Please enter the total amount of your grocery bill in the in #.## format: 60
You win a discount coupon of $6.00. (10% of your purchase)
Please enter the total amount of your grocery bill in the in #.## format: 209.99
You win a discount coupon of $25.20. (12% of your purchase)
Please enter the total amount of your grocery bill in the in #.## format: 222
You win a discount coupon of $31.08. (14% of your purchase)

'''
