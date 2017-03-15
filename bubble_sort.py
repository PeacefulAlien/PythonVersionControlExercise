#bubble sort
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
	return (my_list, counter)

#below is the testing case

if __name__ == "__main__":
	number_list = list()
	i = 0
	for i in range(20):
		number_list.append(i + 1)
	random.shuffle(number_list)
	print("This is the original list:\n", number_list)
	
	sorted_number_list, counter = bubble_sort(number_list)
	print("After {} times go through the list, This is the sorted list:\n".format(counter), sorted_number_list)
	