#!usr/bin/python3

#Author: Charlie Chiccarine
#Email: src322@drexel.edu
#
#Purpose:
#  Implement a binary tree with a class.
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
				
class BinTree:
	def __init__(self, d, l = None, r = None):
		self.data = d
		self.left = l
		self.right = r
	def __str__(self):
		return self.data

if __name__ == "__main__":
	print("")
	print("I have created the following tree:")
	print("   A")
	print("/    \\")
	print("B     D")
	print("\\     /\\")
	print(" E    G H")
	print("")
	
	a = BinTree("A")
	b = BinTree("B")
	d = BinTree("D")
	e = BinTree("E")
	g = BinTree("G")
	h = BinTree("H")

	a.left = b
	a.right = d
	b.right = e
	d.left = g
	d.right = h

	allNodes = [a, b, d, e, g, h]

	print(" Node | Height | Children ")
	print("--------------------------")
	for node in allNodes:
		thestr = "   " + node.data + "  |"
		thestr += "    " + str(calcHeight(node)) + "   |"
		thestr += "L: " + str(node.left) + ", R: " + str(node.right)		

		print(thestr)

