class Vector:
	def __init__(self,*args):
		self.comp=[]
		for count,arg in enumerate(args):
			self.comp.append(arg)
	def __eq__(self,other):
		if len(self.comp)!=len(other.comp):
			return False
		for i in range(len(self.comp)):
			if self.comp[i]!=other.comp[i]:
				return False
		return True
	def __add__(self,other):
		result=[]
		if len(self.comp)<len(other.comp):
			other,self=self,other
		result=[self.comp[i]+other.comp[i] for i in range(len(other.comp))]
		result+=[self.comp[i] for i in range(len(other.comp),len(self.comp))]
		return result
	def __mul__(self,other):
		result=[]
		if len(self.comp)<len(other.comp):
			other,self=self,other
		result=[self.comp[i]*other.comp[i] for i in range(len(other.comp))]
		return result

v1=Vector(1,2,3)
v2=Vector(1,2,3)
v3=v1*v2
print(v3)
print(v1==v2)

