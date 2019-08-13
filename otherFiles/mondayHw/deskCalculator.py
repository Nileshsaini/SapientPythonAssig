stack=[]

def pushNumber():
	n=int(input("enter a real number: "))
	stack.append(n)
def add():
	n=stack[-1]
	stack.pop()
	m=stack[-1]+n
	stack.pop()
	stack.append(m)
def sub():
	n=stack[-1]
	stack.pop()
	m=stack[-1]-n
	stack.pop()
	stack.append(m)
def mul():
	n=stack[-1]
	stack.pop()
	m=stack[-1]*n
	stack.pop()
	stack.append(m)
def div():
	n=stack[-1]
	stack.pop()
	m=stack[-1]/n
	stack.pop()
	stack.append(m)
def outTop():
	print(stack[-1])
	temp=False

temp=True
while temp:
	com=(input())
#	print("this is input"+com)
	switcher = {
		"?":pushNumber,
		"+":add,
		"-":sub,
		"*":mul,
		"/":div,
		"=":outTop
	}
	func = switcher.get(com, lambda: "Invalid")
	func()
	if com=="=":
		break;


