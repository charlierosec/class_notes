#!usr/bin/python3
#
#Author: Charlie Chiccarine
#Email: src322@drexel.edu
#
#Purpose :
#	Generate the values to enter into a truth table
# I'd like to implement a full boolean expression
# solver, but we'll see if we get there.
#
#Last Editted : 5/15/2019
#	Created the script

import sys

def printTT(vc):
	if vc == 0:
		print("\n", end="")
	else:
		print("0", end="")
		printTT(vc - 1)
		print("1", end="")
		printTT(vc - 1)

if __name__ == "__main__":

	if len(sys.argv) > 1:
		varCount = sys.argv[1]
	else:
		print("How may variables are in the expression?")
		try:
			varCount = int(input())
		except:
			print("ERROR : Enter a Number")
			sys.exit()

	printTT(varCount)
