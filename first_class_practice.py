#first-class functions practice
#it simply means functions can be treated as 
#un-executed variables in python

#example_01
def grab_function_01():
	
	def inner_function_01(integer_a, integer_b):
		return integer_a + integer_b

	return inner_function_01

	
#example_02
def grab_function_02(denominator):
	
	def inner_function_02(numerator):
		return float(numerator / denominator)

	return inner_function_02
	


#test cases

addition = grab_function_01()
print(addition(12, 13))
	
division = grab_function_02(100)
print(division(9))

