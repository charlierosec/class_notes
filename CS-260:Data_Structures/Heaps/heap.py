#!usr/bin/python3

#Author: Charlie Chiccarine
#Email: src322@drexel.edu
#
#Purpose:
#  Implement a heap in an array and its accompanying algorithms
#
#Last Edit: 4/18/2019
#  Created implementation

import math


#Given the index of a node, returns the index of its left child
def left(i):
	return ((2 * i) + 1)

#Given the index of a node, returns the index of its right child
def right(i):
	return ((2 * i) + 2)

#Given the index of a node, returns the index of its parent
def parent(i):
	return (math.ceil(i/2) - 1)

#The last index of the heap
def last(H):
	return (len(H) - 1)

#Swaps two elements in the heap
def swap(x, y, H):
	H[x], H[y] = H[y], H[x]

#Given an index i and a heap H, upheap the element at that index in the array
def upheap(i, H):
	#so basically while the element isn't at the top and larger than it's parent
	while (i > 0) and (H[i] > H[parent(i)]):
		swap( i, parent(i), H)
		i = parent(i)

#Insert a value x into a heap H
def insert(x, H):
	H.append(x)
	upheap(last(H), H)

#Given an index i and a heap H, downheap the element at that index in the array
def downheap(i, H):
	if left(i) > last(H):
		return

	lci = left(i) #lci: larger child index

	if (right(i) <= last(H)) and (H[lci] < H[right(i)]):
		lci = right(i)
	
	if H[i] < H[lci]:
		swap(i, lci, H)
		downheap(lci, H)

#Remove the root H[0] from the heap
def remove(H):
	if len(H) == 0:
		return False
	
	rv = H[0]
	H[0] = H[last(H)]
	H.pop()
	
	downheap(0, H)
	return rv

if __name__ == "__main__":
	print()
	print("Implement a heap over an array")
	myHeap = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	print("Starting Heap:")
	print(myHeap)

	print("Upheap 9")
	upheap(last(myHeap), myHeap)
	print(myHeap)
	
	print("Downheap 0")
	downheap(1, myHeap)
	print(myHeap)

	print("Insert 10")
	insert(10, myHeap)
	print(myHeap)

	print("Remove the root")
	print("Return Value:", remove(myHeap))
	print(myHeap)

	print()
	newHeap = []
	print("New Heap Starting From Scratch")
	for i in range(10):
		print("Inserting", i)
		insert(i, newHeap)
		print(newHeap)
