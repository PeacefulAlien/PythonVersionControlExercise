#this is a special version of linear search
#on a ascending number list
#it takes in two arguments: item and number list
#return the result if item is in the number list


import random


def linear_search_ascending_number_list(my_item, my_list):
	index_01 = 0
	result = False
	stop = False
	while index_01 <= (len(my_list) - 1) and not result and not stop:
		if my_item == my_list[index_01]:
			result = True
		elif my_item < my_list[index_01]:
			stop = True
		index_01 += 1
	
	return result

#below is the testing case
if __name__ == "__main__":
	number_list = list()
	i = 0
	random.seed()
	for i in range(20):
		number_list.append(random.randint(1, 20))
		
	sorted_number_list = sorted(number_list)
	print(sorted_number_list)
	test_item = int(input("Please enter an integer:"))
	
	search_result = linear_search_ascending_number_list(test_item, sorted_number_list)
	if search_result:
		print("{} is in the list.".format(test_item), sorted_number_list)
	else:
		print("{} is not in the list.".format(test_item), sorted_number_list)