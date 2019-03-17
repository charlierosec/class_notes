#!usr/bin/python3

#Author: Charles C
#Email: src322@drexel.edu

#Purpose:
# Implementation of linked lists

import random

class LinkedList():
    head = None
    tail = None
    size = 0


    def __init__(self, start):
        self.head = start
        self.initTail()

    def initTail(self):
        curr = self.head
        currSize = 1
        
        while curr.next is not None:
            curr = curr.next
            currSize += 1

        self.tail = curr
        self.size = currSize

    def __str__(self):
        return str(self.head)

class Link():
    data = None
    next = None
    
    def __init__(self, dataN, nextL):
        self.data = dataN
        self.next = nextL

    def __str__(self):
        if self.next is None:
            return "[" + str(self.data) + " , None]"
        else:
            return "[" + str(self.data) + " , " + str(self.next) + "]"

if __name__ == "__main__":
    print("This program implements linked lists in a variety of methods")
    print()
    print("Class Implementation")

    classList = LinkedList( Link(random.randint(1, 10), None) )
    
    current = classList.head
    for i in range(10):
        current.next = Link( random.randint(1, 10), None)
        current = current.next

    classList.initTail()

    print("List:")
    print(classList)
    print("Size:", classList.size)
    print("Tail:", str(classList.tail))
    print()
    

###############################################################################
    print("Parallel Array Implementation")

    llData = []
    llNext = []
    ni = 0
    for i in range(11):
        llData.append( random.randint(1,10) )
        llNext.append(ni)
        ni += 1
    llNext[0] = None
    random.shuffle(llNext)

    currIndex = llNext.index(1)
    nextElem = llNext[currIndex]

    listString = "["
    while nextElem is not None:
        listString += str(llData[currIndex]) + " , "
        currIndex = llNext[currIndex]
        nextElem = llNext[currIndex]

    listString += "None]"

    print("List:")
    print(listString)
    print("Data Array:", llData)
    print("Next Array:", llNext)
