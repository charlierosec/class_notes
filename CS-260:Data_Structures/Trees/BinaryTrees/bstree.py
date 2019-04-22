#!usr/bin/python3

#Author: Charlie Chiccarine
#Email: src322@drexel.edu
#
#Purpose:
#  Implement a binary search tree with a class.
#
#Last Edit: 4/22/2019
#  Fixed minor errors

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

#Insert the value, x into T 
def insert(x, T):
	if T is None:
		T = BinTree(x)
	if x > T.data:
		insert(x, T.right)
	elif x < T.data:
		insert(x, T.left)
	else:
		T.count += 1

def stringTree(T):
	


class BinTree:
	def __init__(self, d, l = None, r = None):
		self.data = d
		self.left = l
		self.right = r
		self.count = 1
	def __str__(self):
		return self.data

if __name__ == "__main__":
