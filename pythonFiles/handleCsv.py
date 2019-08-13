import string
import sys

words={}
for file in sys.argv[1:]:
	for line in open(file):
		for word in line.split(","):
			word=word.strip()
			print(word),
			#if len(word)>2:
			#	words[word]=words.get(word,0)+1
		print ""

