#Creating A Varible
##############
"""
Python has no command for declaring a variable.
A variable is created the moment you first assign a value to it.
"""


#String - length of char between quotes
#makes a string
string = "thing is a string"
print(string)

#Integer - numbers and decimal
integer = 100
print(integer)

#boolean - is a varibale that is
#either set to True or False
boolean_true = True
boolean_false = False
print(boolean_true)
print(boolean_false)

#Casting on Variables
#######################

#If you want to specify the data type of a variable.
#This can be done using the casting methods native to python.

strg = str(10)
intgr = int(10)
print(type(strg))
print(type(intgr))

#String Concatenation
#########################
#String concatenation means adding strings together.
#Use the "+" plus character to glue variables.
#Only string can be concatenated 

x = "Python is "
y = "awesome"
z =  x + y
print(z)

#Convert integers to strings in order to concatenate
x = "Python"
version = 3
y = " is the latest version"
z =  x + str(version) + y
print(z)