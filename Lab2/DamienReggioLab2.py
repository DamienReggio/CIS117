##
# Program Header:
# CIS 117 Python Programming: Lab #2
# Name: Damien Reggio
# Description: Arithmetic, Data Types, User Input, Importing Modules
# Filename: DamienReggioLab2.py
# Date: 1/29/2020

import re
import datetime

# Let's ask for their last name
#
last_name = input("Please enter your family (last) name: ")
# last_name = "Reggio" # for testing

# I'm actually OK with special characters or numbers in a last name but let's
# just make make sure they entered something between 2 and 15 characters
#
while (len(last_name) < 3 or len(last_name) > 15):
    last_name = input("Please enter a last name between 2 and 15 characters: ")
if not re.match('^[a-zA-Z .]+$',last_name):
    print("What an interesting last name!")

print("Nice to meet you Mx", last_name)


# Low let's get student ID
#
student_id = input("Please enter your student id (GID): ")
#student_id = '01244199' # for testing

# Let's make sure they enter a valid GID
#
while not re.match('^\d{8}$',student_id):
    print("It should be of the format ######## (8 numbers please leave out",
          "the \"G\")")
    student_id = input("Please enter your student id (GID): ")
    
print("Your ID is", student_id)

my_id = 0
for num in student_id:
    my_id += int(num)
if my_id <= 0:
    raise Exception("That's not a real ID! You lied to me! Good day to you")
    
num_let = len(last_name) 

print("my_id is:", my_id)
print("num_let is:", num_let)

# Most of these are just a single line so I will put them in a dictionary
# to save typing
#
def two_decimal(float):
    # Helper function: takes in a float returns a flow formated to two
    # decimal places
    #
    return('{0:.2f}'.format(float))

exp_3 = 0
for i in range(2,num_let+1):
    exp_3 += i
    
expression_dictionary = {
    "Expression 1" : two_decimal(my_id / 2.0),
    "Expression 2" : my_id % 2,
    "Expression 3" : exp_3,
    "Expression 4" : my_id + num_let,
    "Expression 5" : abs(num_let - my_id),
    "Expression 6" : two_decimal((my_id) / (num_let + 1100)),
    "Expression 7" : bool((num_let % num_let)) and bool(my_id * my_id),
    "Expression 8" : bool(1) or bool(my_id / 0),
    "Expression 9" : two_decimal(round(3.14, 1)),
}

for key, value in expression_dictionary.items():
    print(key, ": ", value, sep='') 

print("Runtime:", datetime.datetime.now())




# output
#
'''
Please enter your family (last) name: Reggio
Nice to meet you Mx Reggio
Please enter your student id (GID): 01244199
Your ID is 01244199
my_id is: 30
num_let is: 6
Expression 1: 15.00
Expression 2: 0
Expression 3: 20
Expression 4: 36
Expression 5: 24
Expression 6: 0.03
Expression 7: False
Expression 8: True
Expression 9: 3.10
Runtime: 2020-01-29 12:47:53.373999
'''
