def fun(a,b):
	print("funLocal: ",locals())
	print("funGlobal: ",globals())
	return a+b
print(fun(2,3))

v=6
def f(x):
	print("global: ", list(globals().keys()))
	print("entry local; ",locals())
	y=x
	w=v
	print("exit local: ", locals().keys())
f(2)
