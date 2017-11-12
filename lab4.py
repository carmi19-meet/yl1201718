class Animal(object):
	def __init__(self,sound,name,age,favorite_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.favorite_color = favorite_color
	def eat(self,food):
		print("yummy!!" + self.name + " is eating "+ food)
	def descrption(self):
		print(self.name + " is " + str(self.age) + " years old and loves the color " + self.favorite_color)
	def make_sound(self,n):
		print((self.sound + " ")*n)
#a = Animal("sss","snake", 10, "green")
#a.eat("apple")
#a.descrption()
#a.make_sound(6)
class Person(object):
	def __init__(self,name,age,city,gender,work):
		self.name = name
		self.age = age
		self.city = city
		self.gender = gender
		self.work = work
	def eat(self,bfood):
		print(self.name + " is eating his favorite breakfast, " + bfood)
	def cwork(self,nwork):
		print(self.name + "wants to change his job from " + self.work + " to " + nwork)

b = Person("bob", 40, "ney york city", "male", "programer")
b.eat("waffle")
b.cwork("chef")

class Song(object):
	def __init__(self,lyrics):
		self.lyrics = lyrics
	def sing_me_a_song(self):
		print(self.lyrics)
		a=0
		for i in range (len(self.lyrics)):
			print(self.lyrics[a])
			a+=1



	