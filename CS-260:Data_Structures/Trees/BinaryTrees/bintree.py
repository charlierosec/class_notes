#!usr/bin/python3

#Author: Charlie Chiccarine
#Email: src322@drexel.edu
#
#Purpose:
#  Implement a binary tree with a class.
#
#Last Edit: 4/19/2019
#  Created implementation

#In order to calculate the height, I found the heights of all the children
#Then I took the child with the maximum height and added 1 to that
#If the node has no children, then it has a height of 0
def calcHeight(t):
	if t.leftC == None and t.rightC == None:
		return 0
	elif t.leftC == None:
		return calcHeight( t.rightC )
	elif t.rightC == None:
		return calcHeight( t.leftC )
	else:
		maxC = calcHeight( t.leftC )
		if calcHeight( t.rightC ) > maxC:
			maxC = calcHeight( t.rightC)
		return (maxC + 1)
				
class BinTree:
	def __init__(self, d, l = None, r = None):
		self.data = d
		self.left = l
		self.right = r

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

