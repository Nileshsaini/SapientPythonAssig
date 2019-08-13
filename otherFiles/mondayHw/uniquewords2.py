import collections
import string
import sys

#words = {}

words = collections.defaultdict(int)
strip = string.whitespace + string.punctuation + string.digits + "\"'" 
for filename in sys.argv[1:]:
	for line in open(filename):
		for word in line.lower().split():
			word = word.strip(strip)
			if len(word) > 2:
				words[word] = words.get(word, 0) + 1
#sortedDict = collections.OrderedDict(words,reverse=True)
sortedDict = sorted(words.items(), key=lambda x:x[1], reverse=True)
#print sortedDict
for word,key in sorted(words.items(), key=lambda x:x[1], reverse=True) :
	print("'{0}' occurs {1} times".format(word, key))




