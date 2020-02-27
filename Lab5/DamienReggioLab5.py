##
# Program Header:
# CIS 117 Python Programming: Lab #5
# Name: Damien Reggio
# Description: Sherlock Homes
# Application: File Validation
# Topics: Execution Control Structures, File Encoding, Using Containers
# Creating a Dictionary of Identifiers
# Development Environment: Windows 7/Ubuntu 14.04
# Version: Python 3.7
# Filename: DamienReggioLab5.py
# Date: 2/26/2020

import re

def main():
    """
    :input: no input (asked within function)
    prints out the acquired dictionary
    :return: no return
    """
    valid_entry = False

    while not valid_entry:
        file_name = get_file_name()
        valid_entry = is_file_valid(file_name)

    infile = open(file_name, "r", encoding="utf-8")
    file_dict = load_to_dict(infile)

    for key, value in file_dict.items():
        print('{}: {}'.format(key, value))


def load_to_dict(file_object):
    """
    returns a dictionary with information about the file
    :param file_object: a file object
    :return: a dictionary with items as keys and a list of lines where they
    occured as values
    """
    file_dict = {}
    for line_num, line in enumerate(file_object):
        line = line.rstrip() # remove newline
        # A valid identifier must be a string consisting of only letters,
        # numbers or underscores.
        #
        if re.match('^[\w\d]+$', line):
            if line in file_dict:
                # line number started at 1 in example
                #
                file_dict[line].append(line_num + 1)
            else:
                file_dict[line] = [line_num + 1]
    # I don't need to return a copy because file_dict will be remade next call
    #
    return file_dict


def is_file_valid(file_name):
    """
    checks if file is valid and returns True if it is and False if not
    :param file_name: the name of a file
    :return:bool True if valid file, False if not
    """
    try:
        test_file = open(file_name, "r", encoding="utf-8")
        test_file.close()
        return True
    except OSError:
        print("Oops... An error occurred - Try again")
        return False


def get_file_name():
    """
    asks user to input a filename and outputs it if it is valid
    :return: str returns a file name
    """
    file_name = input("Enter the name of an input file:")
    return file_name


if __name__ == '__main__':
    # Don't need to run this multiple times because it will ask again if
    # invalid input is given
    #
    main()



# output
#
'''
Enter the name of an input file:fake_file.txt
Oops... An error occurred - Try again
Enter the name of an input file:t5
Oops... An error occurred - Try again
Enter the name of an input file:t5.dat
apple: [1, 11]
1: [2, 3]
ball: [4, 19]
art: [5]
dog: [6]
pen: [8, 21]
rat: [9]
4: [10]
carrot: [13]
orange: [15]
ant: [16, 17, 18]
stick: [20]
_: [22]
goodbye: [25]
'''
