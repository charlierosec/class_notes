#!usr/bin/python3

#Author: Charlie Chiccarine
#Email: src322@drexel.edu
#
#Purpose:
#  Implement a trie with a class.
#
#Last Edit: 4/19/2019
#  Created implementation

#Returns a list of all available words
def displayWords( t ):
	rv = []
	for kid in t.children:
		if kid.isWord:
			rv.append( kid.word )

def isWordinTrie( word, t ):
	if len(word) == 0:
		return False
	for kid in t.children:
		if kid.letter == word[0]:
			if len(word) == 1:
				return True
			else:
				return isWordinTrie( word[1:-1], kid )
	return False

def addWord( word, t ):
	for kid in t.children:
		if kid.letter == word[0]:
			if len(word) == 1:
				kid.isWord = True
				kid.isWord
			else:
				return isWordinTrie( word[1:-1], kid )
	return False



class Trie:
	def __init__(self, d):
		self.letter = d
		self.children = []
		self.isWord = False
		self.word = None

if __name__ == "__main__":
	#Make a gen tree with added property for word
	#display words function
	# iterate through the the children
	# if a word is reached, display the word
	#check if word exists
	# iterate through the children
	# return value
	#add word
	# iterate through kids
	# if word exists do nothign
	# add word if it don't

	myTrie = Trie("root")
	print(isWordinTrie("gay", myTrie))
