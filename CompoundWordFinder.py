#!usr/local/bin/python

#Uses Python 2.7!

import sys
import random

with open("input.txt") as f:
	wordList = [line.rstrip('\n') for line in f]

answer = open("answer.txt", 'wb')
sys.stdout = answer

"""
	My helper which takes a list and returns it without a given item.

	Arguments:
	item - any object
	input_list - list

	Returns:
	A list without the given item.
"""
def list_without_item(item, input_list):
	new_list = input_list

	if item in input_list:
		new_list.remove(item)
		return new_list

	return new_list

"""
	Takes a list of words and finds all words in it that are made of up 
	other words in the list.

	Arguments:
	word_list - list of words

	Returns:
	Set of words which can be made from other words within the list.

"""
def find(word_list):
	final_list = []
	new_list = []

	#Here, I filter the list by iterating in conjunction with a lambda function.
	#Then, I add that filtered list to another list. 
	for word in word_list:
		new_list = filter(lambda x: word in x and word != x, word_list)
		final_list.append(new_list)

	final_final_list = []

	#Here, I reduce the master list by checking to see if any words are found in multiple
	#lists. By my filtering, only words that appear >1 times across the lists in 
	#final_list are kept in the result. 
	for l in final_list:
		for k in l:
			for j in list_without_item(l, final_list):
				if k in j:
					final_final_list.append(k)

	return set(final_final_list)

for i in find(wordList):
	print i

answer.close()