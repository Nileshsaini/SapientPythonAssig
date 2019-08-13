import math
class Superpower:
	def fly(self):
		pass
	def saveWorld(self):
		pass

superpower = Superpower()
superpower.fly()
superpower.saveWorld()
print(type(superpower))


class Circle:
	pass
myCircle=Circle()

myCircle.radius=5
print(myCircle.radius)

class Circle():
	all_circles=[]
	pi=3.141
	def __init__(self,radius=1):
		self.radius=radius
		Circle.all_circles.append(self)
	def area(self):
		return Circle.pi*self.radius*self.radius
			#(in place of Circle.pi there can be self.pi but value of myCircle.area will change in later case not in the first case when doing myCicle.pi=2)	
	@staticmethod
	def totalArea():
		total_area=0
		for circle in Circle.all_circles:
			total_area=total_area+circle.area()
		return total_area
	@classmethod
	def totalAreaCls(cls):
		total_area=0
		for circle in cls.all_circles:
			total_area=total_area+circle.area()
		return total_area

c1=Circle()
c2=Circle(22)
print(Circle.totalArea())


myCircle=Circle(5)
print(myCircle.radius)
print(myCircle.area())
myCircle.pi=2
print(myCircle.area())

class Shape:
	def __init__(self,x,y):
		self.x=x
		self.y=y
class rectangle(Shape):
	def __init__(self,length=0,breadth=0,x=0,y=0):
		super().__init__(x,y)
		self.length=length
		self.breadth=breadth
	def area(self):
		print("area in rect:")
		return self.length*self.breadth

class square(rectangle):
	def __init__(self,side=1,x=0,y=0):
		super().__init__(side,side,x,y)
		#self.side=side

class circle(Shape):
	def __init__(self,radius=1,x=0,y=0):
		super().__init__(x,y)
		self.radius=radius
	def area(self):
		return math.pi*self.radius*self.radius

s=square()
#print(s.side,s.x,s.y)

c=circle()
print(c.radius,c.x,c.y)

s=square(side=10,x=2,y=2)
print(s.length,s.breadth,s.x,s.y)

c=circle(radius=5,x=3,y=3)
print(c.radius,c.x,c.y)






