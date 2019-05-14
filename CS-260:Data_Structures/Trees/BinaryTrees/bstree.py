#!usr/bin/python3

#Author: Charlie Chiccarine
#Email: src322@drexel.edu
#
#Purpose:
#  Implement a binary search tree with a class.
#
#Last Edit: 5/3/2019
#  Editted Removal method (I don't think it works yet)

import random


#In order to calculate the height, I found the heights of all the children
#Then I took the child with the maximum height and added 1 to that
#If the node has no children, then it has a height of 0
def calcHeight(t):
	if t.left == None and t.right == None:
		return 0
	elif t.left == None:
		return (1 + calcHeight( t.right ))
	elif t.right == None:
		return (1 + calcHeight( t.left ))
	else:
		maxC = calcHeight( t.left )
		if calcHeight( t.right ) > maxC:
			maxC = calcHeight( t.right)
		return (maxC + 1)

def printTree(T, lvl = 0):
	tabs = "\t" * lvl
	print("Node:", T.data, "[", T.count, "]")
	if T.left is not None:
		print(tabs, "Left ", end="")
		printTree(T.left, lvl + 1)
	else:
		print(tabs ,"Left: None")

	if T.right is not None:
		print(tabs, "Right ", end="")
		printTree(T.right, lvl + 1)
	else:
		print(tabs,"Right: None")


#Insert the value, x into T 
def insert(x, T):
	if x > T.data:
		if T.right is None:
			T.right = BinTree(x)
		else:
			insert(x, T.right)
	elif x < T.data:
		if T.left is None:
			T.left = BinTree(x)
		else:
			insert(x, T.left)
	else:
		T.count += 1	

#Returns true or false if value x is in tree T
def findval(x, T):
	if T is None:
		return False
	if x == T.data:
		return True
	else:
		if x > T.data:
			return findval(x, T.right)
		elif x < T.data:
			return findval(x, T.left)

def removeval(x, T):
	rv = False
	if findval(x, T):
		if x == T.data:
			if T.count > 1:
				rv = T.data
				T.count -= 1
			else:
				if T.right is None:
					rv = T.data
					T = T.left
				elif T.left is None:
					rv = T.data
					T = T.right
				else:
					rv = T.data
					T.data = getleftmostchild(T)
		elif x > T.data:
			removeval(x, T.right)
		else:
			removeval(x, T.left)
	
	return rv

def getleftmostchild(T):
	if T.left is not None:
		getleftmostchild(T.left)
	
	rv = T.data
	T = T.right
	return rv

class BinTree:
	def __init__(self, d, l = None, r = None):
		self.data = d
		self.left = l
		self.right = r
		self.count = 1
	def __str__(self):
		return self.data

if __name__ == "__main__":
	print("")
	print("First I'm going to start with an empty tree, then use my insert function")
	print("to populate the tree.")
	print("In my Binary Search Trees, I hand duplicates by counting the amount of")
	print("each value in the tree and updating the count accordingly")
	print("")
	
	myTree = BinTree(5)
	print("Starting Tree:")
	printTree(myTree)
	print("")

	for i in range(10):
		newVal = random.randint(0,10)
		print("Inserting", newVal)
		insert(newVal, myTree)
	print("Inserting 5")
	insert(5, myTree)
	print("Resulting Tree:")
	printTree(myTree)
	print("")

	for i in range(10):
		lookVal = random.randint(0,15)
		print("Finding", lookVal, ":", findval(lookVal,myTree))
	print("")
	

	print("Removing 5")
	printTree(myTree)
