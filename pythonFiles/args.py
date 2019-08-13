
def product(*args):
	result=1
	for arg in args:
		if type(arg)==str:
			result=str(result)
		result+=arg
	return result


print(product(1,2,3,4,5,"acx"))

def kproduct(**kwargs):
	result=""
	print(type(kwargs))
	print(kwargs)
	for key,value in kwargs.items():
		#if type(arg)==str:
		#	result=str(result)
		print(key+"=="+value)
	return result
print(kproduct(new="frist",sec="second",thir="third"))
