my_list = []

my_list_new = [10, 20, 30, 40] #list with items to be added to my_list

my_list.extend(my_list_new)

print("After adding the items from my_list_new, print the updated list.")
print(my_list) #After adding the items from my_list_new, print the updated list.

my_list[1] = 15 #Insert the value 15 at the second position in the list.

print("Insert the value 15 at the second position in the list.")
print(my_list)

del my_list[-1] #Remove the last element from the list.

my_list.sort() #Sort the list in ascending order.

print("Remove the last element from the list & Sort the list in ascending order.")
print(my_list)

#Find and print the index of the value 30 in my_list.
print("Find and print the index of the value 30 in my_list.")
print(my_list.index(30))