#!usr/bin/python3

#Author: Charlie Chiccarine
#Email: src322@drexel.edu
#
#Purpose:
#  Implement a binary tree with a linked list.
#
#Last Edit: 4/22/2019
#  Created implementation

def printTree(T, lvl):
	tabs = "\t" * lvl
	print("Node:", T[0])
	if T[1] is not None:
		print(tabs, "Left ", end="")
		printTree(T[1], lvl + 1)
	else:
		print(tabs ,"Left: None")

	if T[2] is not None:
		print(tabs, "Right ", end="")
		printTree(T[2], lvl + 1)
	else:
		print(tabs,"Right: None")

if __name__ == "__main__":
	print("")
	print("I have created the following tree:")
	print("   A")
	print("/    \\")
	print("B     D")
	print("\\     /\\")
	print(" E    G H")
	print("")

	print("Basic Format")
	print("[ Data, Left Child, Right Child]")
	print("")
	print("Since each subtree of a binary tree is a binary tree,")
	print("a leaf would have the following format:")
	print("[Data, None, None]")
	print("")
	
	myTree = ["A", ["B", None, ["E", None, None]], ["D", ["G", None, None], ["H", None, None]]]
	
	print("Formatted Display:")
	printTree( myTree, 0 )
	print("")
	print("List Display:")
	print(myTree)
	print("")
