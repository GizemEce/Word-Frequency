from __future__ import division
from collections import Counter


#Contract:file->list
#Purpose: take a file and return list of words in the file
#Examples:
#alice.txt->['This', 'is', 'a', 'slow', 'train', 'anyway', 'and', 'it', 'has', 'slowed', 'some', 
#            'more', 'for', 'the', 'curve', 'Jackson', 'is', 'the', 'only', 'passenger', 'left', 'and', 'the', 
#            'next', 'stop', 'is', 'about', 'twenty', 'miles', 'ahead', 'Then', 'the', 'stop', 'at', 'Ripley', 
#            'then', 'Kincardine', 'and', 'the', 'lake', 'He', 'is', 'in', 'luck', 'and', 'it', 'is', 'not', 
#            'to', 'be', 'wasted', 'Already', 'he', 'has', 'taken', 'his', 'ticket', 'stub', 'out', 'of', 'its',
#            'overhead', 'notchHe', 'heaves', 'his', 'bag', 'and', 'sees', 'it', 'land', 'just', 'nicely', 'in', 
#            'between', 'the', 'rails', 'No', 'choice', 'now', 'the', 'train', 'is', 'not', 'going', 'to', 'get',
#            'any', 'slowerHe', 'takes', 'his', 'chance', 'A', 'young', 'man', 'in', 'good', 'shape', 'agile', 'as',
#            'he', 'will', 'ever', 'be', 'But', 'the', 'leap', 'the', 'landing', 'disappoints', 'him', 'He', 'is', 'stiffer', 
#            'than', 'he', 'would', 'thought', 'the', 'stillness', 'pitches', 'him', 'forward', 'his', 'palms', 'come', 'down',
#            'hard', 'on', 'the', 'gravel', 'between', 'the', 'ties', 'he', 'is', 'scraped', 'the', 'skin', 'Nerves']

def fileopen(filename):
	s="?.()',!:-;"
	with open(filename,'r') as f:
		for line in f:
			empty=[]
			for word in line.split():
				for i in s:
					word=word.replace(i,"")
				empty.append(word)
			return empty  

print fileopen("alice.txt")

#Contract:list->string,number
#Puporse: computes the term frequency

def termfrequency(low):
	dictionary=Counter(low)
	#total number of terms in the document
	total=sum(dictionary.values())
	empty={}
	for word,value in dictionary.iteritems():
		#how frequently a term ocuurs in the document
		tf=value/total
		empty[word]=tf
	return empty


print termfrequency(fileopen("alice.txt"))