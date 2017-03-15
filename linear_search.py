#Linear Search function for Python practice
#take an item and a list as arguments,
#find the item if it is in the list, 
#add the item if it is not in the list.


def linear_search (my_item, my_list):
	result = False
	index_01 = 0
	while index_01 < len(my_list) and not result:
		if my_list [index_01] == my_item:
			result = True
		else:
			index_01 += 1
		
	return result

#below is the testing case
if __name__ == "__main__":
	shopping_list  = ["apple", "orange", "pork", "egg", "melon", "potato", "tomato", "milk", "nut"]
	test_item = input("What are you looking for?")
	
	search_result = linear_search(test_item, shopping_list)
	if search_result:
		print("test_item is in the shopping list already.\n")
	else:
		shopping_list.append(test_item)
		print("your stuff is not in my shopping list. But I will add it to the list.\n", shopping_list)
		