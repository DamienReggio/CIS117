##
# Program Header:
# CIS 117 Python Programming: Lab #4
# Name: Damien Reggio
# Description: Programming with Text Data, Files and Exceptions
# Application: Your Shopping Budget – The Pricelist
# Topics: Working with files and formatting
# Development Environment: Windows 7/ Ubuntu 14.04
# Version: Python 3.7
# Filename: DamienReggioLab4.py
# Date: 2/13/2020

import re

NUM_RUNS = 3

def main():
    """
    :input: no input (asked within function)
    asks user for input and output filenames, collects grocery list then
    writes grocery list to ouput file name
    :return: no return (writes to a file)
    """
    in_file = input("Please enter input file name: ")
    out_file = input("Please enter output file name: ")

    grocery_list_dict = get_grocery_list(in_file)
    if(grocery_list_dict):
        write_grocery_list_pretty(grocery_list_dict, out_file)
    else:
        print("the grocery list was not read from file, something went wrong")

def get_grocery_list(in_file):
    """
    :param filename: String A hopefully valid filename containing a grocery list
    Reads a grocery list from a file and returns that list in the form of
    a dictionary
    :return: dictionary of form item = price
    """
    grocery_list = {}
    try:
        grocery_file = open(in_file, 'r')
    except IOError:
        # lets exit the function the the file does not exist
        #
        print("Input file does not exist? Please check filename.")
        return None

    for line in grocery_file:
        # require at least one digit do not accept 5. accept fraction of cents
        #
        match = re.match('^(.+): (\d*\.?\d+)$', line)
        if match:
            # If item is already on list add the price to existing entry
            #
            item = match.group(1)
            price = float(match.group(2))
            grocery_list[item] = grocery_list.get(item, 0) + price
            # Might as well calculate the total while iterating through all
            # items  key: _Total_ in case they eat a cereal called "Total"
            #
            grocery_list['_Total_'] = grocery_list.get('_Total_', 0) + price
        else:
            line = line.strip('\n')
            print("unreadable format skipping line:", line)

    grocery_file.close()

    return grocery_list

def write_grocery_list_pretty(grocery_list, out_file):
    """
    :param grocery_list: a dictionary with keys as items and values as price
    with a sepcial _Total_ key
    :param out_file: string,  filename to write to
    writes a file with item left aligned and price right aligned with total
    on the bottom
    :return: no return, a file is written
    """
    # The lab makes it look like it wants the file to already be created and to
    # error out if it is not. That means I need to write over the file and
    # fail if it does not exist. This is why I use r+ when I am not going to
    # read the file
    #
    try:
        pretty_list = open(out_file, 'r+') # not 'w' to check if it exist
    except IOError:
        # lets exit the function the the file does not exist
        #
        print("Output file does not exist? Please check filename.")
        return

    pretty_list.truncate(0) # this clears the file out

    for item, price in grocery_list.items():
        if item == '_Total_': # we want total to be last
            pass
        else:
            # this will overflow if names or price are too long
            #
            writing_string = gen_double_aligned_30(item, price)
            pretty_list.write(writing_string + '\n')

    writing_string =  gen_double_aligned_30('Total:', grocery_list['_Total_'])
    pretty_list.write(writing_string)

    pretty_list.close()

def gen_double_aligned_30(string_l, dollar_r):
    """
    :param string_l: string to be left justified
    :param dollar_r: dollar amount to be right justified
    :return: a formated string of form
    stringl              stringR
    with the entire string length totaling 30
    """
    # check if we overflow
    #
    if len('{:.2f}'.format(dollar_r)) <= 10:
        dollar_r_string = '{:.2f}'.format(dollar_r)
    else: # it's too big
        dollar_r_string = '{:.4e}'.format(dollar_r) # exponent takes up 4 chars

    if len(string_l) > 20:
        string_l_return = string_l[:20]
    else:
        string_l_return = string_l

    return '{:<20}{:>10}'.format(string_l_return, dollar_r_string)


if __name__ == '__main__':
    for run in range(0, NUM_RUNS):
        main()



# output
# Include both the program run at the console display as well as a copy of the
# output file in your .py file.
#
'''
Please enter input file name: not_a_file.txt
Please enter output file name: DamieReggioLab4out.txt
Input file does not exist? Please check filename.
the grocery list was not read from file, something went wrong
Please enter input file name: lab4.txt
Please enter output file name: not_a_file.txt
unreadable format skipping line: Price List - Definitely Need
unreadable format skipping line: Wish List
Output file does not exist? Please check filename.
Please enter input file name: lab4.txt
Please enter output file name: DamienReggioLab4out.txt
unreadable format skipping line: Price List - Definitely Need
unreadable format skipping line: Wish List

DamienReggioLab4out.txt
Apples                    0.57
Binder paper              2.29
Cheese                    1.59
Mop                       7.50
Scouring pads             5.00
Shampoo                   2.54
Conditioner               2.79
Ice Cream                 5.89
Total:                   28.17
'''
