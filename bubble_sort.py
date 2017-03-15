#bubble sort, most basic sorting algorithm,
#generate sorted list for search functions to perform better.
#the function require a list input
#and will return the sorted list 
#and how many times have the algorithm go through the list.


import random


def bubble_sort(my_list):
	position = 0
	status = True
	counter = 0
	while status:
		status = False
		for position in range(len(my_list) - 1):
			if my_list[position] > my_list[position + 1]:
				status = True
				my_list[position], my_list[position + 1] = my_list[position + 1], my_list[position]
		counter += 1
	
	return my_list, counter #created tuple automatically

#below is the testing case
if __name__ == "__main__":
	number_list = list()
	i = 0
	random.seed()
	for i in range(20):
		number_list.append(random.randint(1, 20))
	print("This is the original list:\n", number_list)
	
	sorted_number_list, counter = bubble_sort(number_list)#automatic tuple unpacking
	print("After {} times go through the list, This is the sorted list:\n".format(counter), sorted_number_list)
	