#binary search function for python practice
#obs:the list has to be sorted first

def binary_search(my_item, my_list):
	status = False
	bottom = 0
	top = len(my_list) - 1
	while bottom <= top and not status:
		middle = (bottom + top) // 2
		if my_list[middle] == my_item:
			status = True
		elif my_li[middle] <= my_item:
			bottom = middle + 1
		else:
			top = middle - 1
			
	return status, middle

#below is the testing case
if __name__ == "__main__":
	numberlist = list()
	for i in range(10):
		list[i] = i * i
	item = int(input("What number are you looking for? "))
	status, position = binary_search(item, numberlist)
	if status == True:
		print("the number {} is in the list at No.{}.".format(item, position + 1))
	else:
		print("the number {} is not in the list.\n This list is:".format(item), numberlist)
