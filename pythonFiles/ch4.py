import os

def listFiles():
	filesList=[]
	for file in os.listdir("."):
		extension = os.path.splitext(file)[1]
		if extension == ".lst":
			filesList.append(file)
	return fileList

def addFile(filesList):
	print("Choose file name")
	name=input()
	fileName,extension = os.path.splitext(file)
	if extension=="":
		fileName+=".lst"
	filesList.append(fileName)
	f= open(fileName)
	f.close()
	return filesList

def printList(filesList):
	if filesList=[]:
		return
	count=1
	for file in filesList:
		print(str(count),": ",file)
		count++

def isEmpty(fileName):
	if os.stat(fileName).st_size == 0:
		return True
	else:
		return False

def showFile(fileNo,fileList):
	fileNo=fileNo-1
	if isEmpty(fileList[fileNo]):
		print("no items are in the list")
		return
	for line in open(fileList[fileNo]):
		print(line)

def handleCommand(com,fileData):
	if com=="A" or com=="a":
		fileData.append(str(input("Add item")))
	elif com=="D" or com=="d":
		index=int(input("Delete item number (or 0 to cancel): "))
		if index!=0:
			fileData.remove(index-1)
	elif com=="S" or com=="s":
		with open(fileName, 'w') as f:
			for item in fileData:
				f.write("%s\n" % item)
	elif com=="Q" or com=="q":
		s = str(input("Save unsaved changes (y/n):"))
		if s=="y":
			handleCommand(s,fileData)
		

if __name__=="main":
	filesList=listFiles()
	if not filesList:
		print("--There are no files with .lst extension --")
	else:
		printList()
	inputNo=int(input())
	if inputNo==0:
		filesList=addFile(filesList)
		showFile(inputNo,filesList)
	elif not filesList:
		showFile(inputNo,filesList)
	if isEmpty(filesList[inputNo-1]):
		fileData=[]
		com = str(input("[A]dd  [Q]uit"))
	else:
		com =str(input("[A]dd  [D]elete  [S]ave  [Q]uit"))	
	

