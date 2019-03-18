#!usr/bin/python3

#Author: Charles C
#Email: src322@drexel.edu

#Purpose:
# Implementation of a stack

import random

if __name__ == "__main__":
    print("This program implements a stack")
    print()
    
    theStack = []

    for i in range(25):
        theStack.append( random.randint(0, 100) )

    print( theStack )
    print("Popped Values:")

    for i in range(5):
        print( theStack.pop() )

    print("Updated Stack:")
    print( theStack )
    print()
    print("The .append works as a Push() would")
    print("The .pop works as a Pop() would")
