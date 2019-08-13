board=[]

#win=False
for i in range(0,9):
	board.append((raw_input()))

for m in range(0,3):
	if board[m]==board[m+3] and board[m]==board[m+6]:
#		win=True
		print "winner is: "+str(board[m])
		quit()
for m in [0,3,6]:
	if board[m]==board[m+1] and board[m+1]==board[m+2]:
#		win=True
		print "winner is: "+str(board[m])
		quit()
for m in [0,2]:
	if m==0 and board[m]==board[m+4] and board[m+4]==board[m+8]:
#		win=True
		print "winner is: "+str(board[m])
		quit()
	if m==2 and board[m]==board[m+2] and board[m+2]==board[m+4]:
#		win=True
		print "winner is: "+str(board[m])
		quit()

#if not win:
print "Draw"

