#stack data structure with python class.
#stack is a data structure follows LIFO principle.


class stack:
	
	def __init__(self):
		self.items_list = list()
			
	def stack_push(self, item):
		self.items_list.append(item)
		
	def stack_pop(self):
		return self.items_list.pop() #list.pop() automatic pops out the last element
	
	def check_status(self):
		return bool(self.items_list == []) #bool(test)
		
	def demo_stack(self):
		print(self.items_list)

	def erase_stack(self):
		warning = input("Are you sure you want to erase the whole stack?\ny for yes. n for no. ")
		if warning == "y":
			self.items_list = []

			
#below is the testing case		
if __name__ == "__main__":
	my_stack = stack()
	
	#manual tests
	my_stack.check_status()
	my_stack.stack_push("sunzao")
	my_stack.stack_push("2070")
	my_stack.demo_stack()
	my_stack.stack_pop()
	my_stack.demo_stack()
	my_stack.erase_stack()
	
	#auto tests
	index = 0
	for index in range(10):
		my_stack.stack_push(index)
	my_stack.demo_stack()
	
	for index in range(len(my_stack.items_list)):
		temp = my_stack.stack_pop()
		print("{}".format(temp))
	
