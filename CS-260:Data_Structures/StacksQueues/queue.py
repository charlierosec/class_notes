#!usr/bin/python3

#Author: Charles C
#Email: src322@drexel.edu

#Purpose:
# Implementation of a queue

import random

def qPop(queue):
    rv = queue[0]

    for i in range( len(queue) ):
        if i+1 == len(queue):
            queue.pop()
        else:
            queue[i] = queue[i+1]

    return rv


if __name__ == "__main__":
    print("This program implements a queue")
    print()
    
    theQueue = []

    for i in range(25):
        theQueue.append( random.randint(0, 100) )

    print( theQueue )
    print("Popped Values:")

    for i in range(5):
        print( qPop(theQueue) )

    print("Updated Queue:")
    print( theQueue )
    print()
    print("The .append works as a Push() would")
    print("I wrote the qPop() function")
