#!/usr/bin/python3
if __name__ = "__main__":

#Value of the variables
a = 1
b = 2

from add_0 import add #Import functions from add_0

output = add(a, b) #Imported result to be calculated

print("{} + {} = {}".format(a, b, output))
