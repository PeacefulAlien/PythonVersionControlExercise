#Linear Search function for Python practice

def LinearSearch (myItem, myList):
	found = False
	position = 0
	while position < len(myList) and not found:
		if myList [position] == myItem:
			found = True
		position += 1
	return found

if __name__ = "__main__":
	shoplist  = ["apple", "orange", "pork", "egg", "melon", "potato", "tomato", "milk", "nut"]
	item = input("What are you looking for?")
	searchresult = LinearSearch(item, shopping)
	if searchresult:
		print("I will buy the stuff you want.\n")
	else:
		print("your stuff is not in my shopping list. But I will add it to the list.\n")
		shoplist.append(item)