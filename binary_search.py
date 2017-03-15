#binary search function for python practice
#obs:the list has to be sorted first

def binary_search(my_test_item, my_list):
	result = False
	index_bottom = 0
	index_top = len(my_list) - 1
	while index_bottom <= index_top and not result:
		index_middle = (index_bottom + index_top) // 2
		if my_list[index_middle] == my_test_item:
			result = True
		elif my_list[index_middle] <= my_test_item:
			index_bottom = index_middle + 1
		else:
			index_top = index_middle - 1
			
	return result, index_middle #create tuple

#below is the testing case	
if __name__ == "__main__":
	number_list = list()
	for i in range(10):
		number_list.append((i+1)*(i+1))
	test_item = int(input("What number are you looking for? "))
	test_result, index_result = binary_search(test_item, number_list)#tuple unpacking
	if test_result == True:
		print("the number {} is in the list at No.{}.".format(test_item, index_result + 1), number_list)
	else:
		print("the number {} is not in the list.\n This list is:".format(test_item), number_list)