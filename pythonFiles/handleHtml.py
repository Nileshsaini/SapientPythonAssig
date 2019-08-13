import string
import sys

def handleHtml(tag,file,startPos):
	openTag="<"+tag+">"
	closeTag="</"+tag+">"
	f=open(file)
	data=f.read()
	start=data.find(openTag)+len(openTag)
	stop=data.find(closeTag,start)
	print data[start:stop]

def handleAttr(file, tag, attr, attrValue):	
	tagData=handleHtml(file, tag,startPos)
	if(tagData.find(attr)!=-1):
		if(tagData.find(value)!=-1):
			print tagData

#	for line in open(file):
#		for word in line.split():
#			word=word.strip()
#			if word=="<"+tag
#			if len(word)>2:
#				words[word]=words.get(word,0)+1

for file in sys.argv[1:]:
	#handleHtml("body",file)
	for line in open(file):
		for word in line.split():
			word=word.strip()
			if len(word)>2:
				words[word]=words.get(word,0)+1
