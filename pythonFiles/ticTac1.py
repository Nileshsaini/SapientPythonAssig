import random
#win=False
#class Game:
def gameOver():
	for m in range(0,3):
		if board[m]!='X' and board[m]==board[m+3] and board[m]==board[m+6]:
			print("winner is: ",str(board[m]))
			return True
	for m in [0,3,6]:
		if board[m]!='X' and board[m]==board[m+1] and board[m+1]==board[m+2]:
			print("winner is: ",str(board[m]))
			return True
	for m in [0,2]:
		if board[m]!='X' and m==0 and board[m]==board[m+4] and board[m+4]==board[m+8]:
			print("winner is: ",str(board[m]))
			return True
		if board[m]!='X' and m==2 and board[m]==board[m+2] and board[m+2]==board[m+4]:
			print("winner is: ",str(board[m]))
			return True
	#print "Draw"
	return False
#if not win:
def printBoard():
	for i in range(0,9):
		print(board[i],end=" ")
		if (i+1)%3==0:
			print("")

def isValidMove(move):
	if move<9 and move>=0:
		if board[move]=='X':
			return True
		else:
			return False
	else:
		return False

board=[]
for i in range(0,9):
	board.append('X')
printBoard()
i=0
while i<5:
	move = int(input("Your Move: "))
	i+=1
	#print("i",i)
	if isValidMove(move):
		board[move]=1
	else:
		i=i-1
		print("Invalid Move")
	#	print("i dec:",i)
		continue
	if i<5:
		compMove = random.randrange(0,9)
		while board[compMove]!='X':	
			compMove = random.randrange(0,9)
		board[compMove]=0
	#	print("compMove",compMove)
	printBoard()
	if i>1 and gameOver():
		break
	elif i>4 and not gameOver():
		print("draw")
		break


