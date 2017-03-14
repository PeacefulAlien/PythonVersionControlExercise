#Linear Search function for Python practice

def linear_search (my_item, my_list):
	status = False
	position = 0
	while position < len(my_list) and not status:
		if my_list [position] == my_item:
			status = True
		position += 1
	return status, position

#below is the testing case
if __name__ == "__main__":
	shoplist  = ["apple", "orange", "pork", "egg", "melon", "potato", "tomato", "milk", "nut"]
	item = input("What are you looking for?")
	searchresult, position = linear_search(item, shoplist)
	if searchresult:
		print("Item is in the shopping list already.\n")
	else:
		shoplist.append(item)
		print("your stuff is not in my shopping list. But I will add it to the list. {}\n".format(position))
		print(shoplist)
		
