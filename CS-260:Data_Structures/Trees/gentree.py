#!usr/bin/python3

#Author: Charlie Chiccarine
#Email: src322@drexel.edu
#
#Purpose:
#  Implement a general tree with a class.
#
#Last Edit: 4/19/2019
#  Created implementation

#In order to calculate the height, I found the heights of all the children
#Then I took the child with the maximum height and added 1 to that
#If the node has no children, then it has a height of 0
def calcHeight(t):
	if len(t.children) == 0:
		return 0
	else:
		maxKid = calcHeight( t.children[0] )
		for i in range(1, len(t.children) ):
			newKid = calcHeight( t.children[i] )
			if newKid > maxKid:
				maxKid = newKid
		return (1 + maxKid)

class Tree:
	def __init__(self, d):
		self.data = d
		self.children = []

if __name__ == "__main__":
	print("")
	print("I have created the following tree:")
	print("   A")
	print("/  |  \\")
	print("B  C   D")
	print("|  |   /\\")
	print("E  F  G H")
	print("   |")
	print("   I")
	print("")
	
	a = Tree("A")
	b = Tree("B")
	c = Tree("C")
	d = Tree("D")
	e = Tree("E")
	f = Tree("F")
	g = Tree("G")
	h = Tree("H")
	i = Tree("I")

	a.children.append(b)
	a.children.append(c)
	a.children.append(d)
	b.children.append(e)
	c.children.append(f)
	d.children.append(g)
	d.children.append(h)
	f.children.append(i)

	allNodes = [a, b, c, d, e, f, g, h, i]

	print(" Node | Height | Children ")
	print("--------------------------")
	for node in allNodes:
		thestr = "   " + node.data + "  |"
		thestr += "    " + str(calcHeight(node)) + "   |"
		
		for kid in node.children:
			thestr += " " + kid.data + ","

		print(thestr)

