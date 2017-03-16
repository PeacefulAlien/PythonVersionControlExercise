#stack data structure with python class.
#stack is a data structure follows LIFO principle.


class class_stack:
	
	def __init__(self):
		self.items_list = list()
	
	#push an element at the end of the stack
	def stack_push(self, item):
		self.items_list.append(item)
	
	#pop out the last element of the stack
	#False means empty stack
	def stack_pop(self):
		if self.items_list != []:
			item = self.items_list.pop()#list.pop() automatic pops out the last element 
		else:
			item = False
			print("It is an empty stack!!!\n")
		return item
		
	#check if the stack is empty
	#False is empty
	def check_status(self):
		print(bool(self.items_list != []))
	
	#print the stack
	def demo_stack(self):
		print(self.items_list)
	
	#erase the stack
	def erase_stack(self):
		warning = input("Are you sure you want to erase the whole stack?\ny for yes. n for no. ")
		if warning == "y":
			self.items_list = []
		else:
			self.items_list = self.items_list
			
#below is the testing case		
if __name__ == "__main__":
	my_stack = class_stack()
	
	my_stack.check_status()
	my_stack.stack_pop()
	my_stack.stack_push("sunzao")
	my_stack.check_status()
	
	my_stack.stack_push("2070")
	my_stack.demo_stack()
	
	my_stack.stack_pop()
	my_stack.demo_stack()
	
	my_stack.erase_stack()
	my_stack.check_status()
	
	
	test_index = 0
	for test_index in range(10):
		my_stack.stack_push(test_index)	
	print(my_stack.items_list)
	for test_index in range(len(my_stack.items_list)):
		print("{}".format(my_stack.stack_pop()))
	
