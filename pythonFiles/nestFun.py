import fun

def _sum(a,b):
	print("locals1: ",locals())
	return a+b

def _sub(a,b):
	return a-b


def operation(flag):
	print("locals2: ",locals())
	print("globals: ", globals())
	def sum(a,b):
		return a+b
	def sub(a,b):
		return a-b
	if flag==True:
		return sum
	else:
		return sub

op=operation(False)
print(op(10,20))

