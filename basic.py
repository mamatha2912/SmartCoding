#!/usr/bin/env python

import sys

"""
Python does offer magic methods like sum() and others, please try to write down your algorithms or coding 
instructions clearly without using any shortcuts
"""
# adds two numbers together

def add(a, b):
    # complete with your solution
    return (a+b)

# If function `add` above works, then line 11 will not complain and hence fail
assert add(1,3) == 4

"""
Using data structures like list, can you find the total or the values in that list.
Do not use a function like sum(someList), that would be cheating ;-)
"""
# Data structure
numbers = [1,2,3,5]
def sumOfList(someList):
    # your solution
    total = 0;
    for x in numbers:
        total = total+x
    return total    
    
assert sumOfList(numbers) == 11  
sys.exit(0)