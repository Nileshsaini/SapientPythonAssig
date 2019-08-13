import os
import sys
import pickle
import shelve
#import io

#binary 
data = [["id","name","age","gender","skillSet"],[1,"name1",1,"M","ds"],[2,"name2",2,"F","sd"],[3,"name3",3,"M","code"],[4,"name4",4,"F","algo"]]

newFile = open("dsBinary.records","wb")

for row in data:
	for val in row:
		newFile.write(bytes(val)) if isinstance(val,int) else newFile.write(bytes(val,'utf8'))
	newFile.write(bytes("\n",'utf8'))	
newFile.close()
readFile = open("dsBinary.records","rb")
for line in readFile:
	print(line)
readFile.close()

newFile = open("dsUtf8.records", 'w', encoding='utf8')
for row in data:
	for val in row:
		newFile.write(str(val))
	newFile.write("\n")
newFile.close()
readFile = open("dsUtf8.records","r", encoding='utf8')
for line in readFile:
	print(line)
readFile.close()

#data = [["id","name","age","gender","skillSet"],["1","name1","1","M","ds"],["2","name2","2","F","sd"],["3","name3","3","M","code"],["4","name4","4","F","algo"]]
newFile = open("dsPickle.records", 'wb')
pickle.dump(data, newFile)

#readFile=open("dsPickle.records","rb")
#a = pickle.load(readFile)
#readFile.close()
#print("pickle: \n",readFile)

newFile = shelve.open("dsShelve.records")
data = [["name1",1,"M","ds"],["name2",2,"F","sd"],["name3",3,"M","code"],["name4",4,"F","algo"]]
i=1
for row in data:
	newFile[str(i)]=tuple(row)
	i+=1
newFile.close()
readFile = shelve.open("dsShelve.records")
for key in readFile:
	print(key, readFile[key])


