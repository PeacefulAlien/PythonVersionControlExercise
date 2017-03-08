class animal:

	def __init__(self, type, name, color, gender, age, weight):
		self.type = type
		self.name = name
		self.color = color
		self.gender = gender
		self.age = age
		self.weight = weight
	
def main():
	animal_01 = animal("cat", "champagne", "three-colours", "female", "6", "3.5")
	print(animal_01.type)
	print(animal_01.name)

	