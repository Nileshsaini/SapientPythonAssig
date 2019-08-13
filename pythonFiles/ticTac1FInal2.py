import random
import shelve

#win=False
class Tictac:
	def __init__(self, gameChoice=1):
		if gameChoice==1:
			self.board=[]
			for i in range(9):
				self.board.append('X')
			self.printBoard()
			self.turn=0
			self.game()
		else:
			d = shelve.open("ticsave")
			self.board=d["board"]
			self.turn = d["turn"]
			d.close()
			self.printBoard()
			self.game()
	def gameOver(self):
		for m in range(0,3):
			if self.board[m]!='X' and self.board[m]==self.board[m+3] and self.board[m]==self.board[m+6]:
				print("winner is: ",str(self.board[m]))
				return True
		for m in [0,3,6]:
			if self.board[m]!='X' and self.board[m]==self.board[m+1] and self.board[m+1]==self.board[m+2]:
				print("winner is: ",str(self.board[m]))
				return True
		for m in [0,2]:
			if self.board[m]!='X' and m==0 and self.board[m]==self.board[m+4] and self.board[m+4]==self.board[m+8]:
				print("winner is: ",str(self.board[m]))
				return True
			if self.board[m]!='X' and m==2 and self.board[m]==self.board[m+2] and self.board[m+2]==self.board[m+4]:
				print("winner is: ",str(self.board[m]))
				return True
		#print "Draw"
		return False
#if not win:
	def printBoard(self):
		for i in range(0,9):
			print(self.board[i], end=" ")
			if (i+1)%3==0:
				print("")

	def isValidMove(self):
		if self.move<9 and self.move>=0:
			if self.board[self.move]=='X':
				return True
			else:
				return False
		else:
			return False

	def game(self):
		print("Input your move value between 0 to 8")
		while self.turn<5:
			self.move = int(input("Your Move: "))
			self.turn+=1
			#print("i",i)
			if self.isValidMove():
				self.board[self.move]=1
			else:
				self.turn=self.turn-1
				print("Invalid Move")
	#			print("i dec:",i)
				continue
			if self.turn<5:
				self.compMove = random.randrange(0,9)
				while self.board[self.compMove]!='X':	
					self.compMove = random.randrange(0,9)
				self.board[self.compMove]=0
	#			print("compMove",compMove)
			self.printBoard()
			d = shelve.open("ticsave")
			d["board"]=self.board
			d["turn"]=self.turn
			d.close()
			if self.turn>1 and self.gameOver():
				break
			elif self.turn>4 and not self.gameOver():
				print("draw")
				break

print("Select one of the following option:")
print("1 - New Game \n2 - Saved game")
gameChoice = int(input("Enter the choice: "))
tic = Tictac(gameChoice)


