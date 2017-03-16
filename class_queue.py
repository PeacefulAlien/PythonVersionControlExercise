#queue data structure 
#queue structure follows FIFO principle


class class_queue():
	
	def __init__(self):
		self.items_list = []
	
	def enqueue(self, item):
		self.items_list.append(item)
	
	#pop out the first element of the stack
	#False means empty queue
	def dequeue(self):
		if self.items_list != []:
			item = self.items_list.pop(0)
		else:
			item = False
			print("It is an empty queue!!!\n")
		return item
	
	#check if the queue	is empty
	#False is empty
	def check_status(self):
		print(bool(self.items_list != []))

		#print the queue
	def demo_queue(self):
		print(self.items_list)
	
	#erase the queue
	def erase_queue(self):
		warning = input("Are you sure you want to erase the whole queue?\ny for yes. n for no. ")
		if warning == "y":
			self.items_list = []
		else:
			self.items_list = self.items_list


#below is the testing case		
if __name__ == "__main__":
	my_queue = class_queue()
	
	my_queue.dequeue()
	my_queue.check_status()
	
	my_queue.enqueue("sunzao")
	my_queue.demo_queue()
	
	my_queue.enqueue("2070")
	my_queue.demo_queue()
	
	my_queue.dequeue()
	my_queue.demo_queue()
	
	my_queue.erase_queue()
	my_queue.check_status()
	
	test_index = 0
	for test_index in range(10):
		my_queue.enqueue(test_index)
	print(my_queue.items_list)
	for test_index in range(len(my_queue.items_list)):
		print("{}".format(my_queue.dequeue()))
	
	
