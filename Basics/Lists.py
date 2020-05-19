#Lists
#Ordered sequences that can hold a variety of object types.
#Use brackets and commas to separate objects.
#Support indexing and slicing.
#Can be nested and also methods that can be called off of them.
#Elements in a Lists are muttable unlike strings.

my_list = [1,2,3]
my_list2 = ['STRING', 100, 23.3]
list_names = ['Fred', 'Felipe', 'Mara']
len(my_list2) # Prints the length of the List, how many elements in it. 
my_list2[0] # Grab valuie of the first index of the list.
my_list[1:] # Slices just like any string. 

print(my_list + my_list2)  #Concatenate two list

list_names[0] = list_names[0].upper() # Update first index to be all caps 
print(list_names)

list_names.append('Jasma')  # How to append a new element to the list - Use the append method.
print(list_names);

print(list_names.pop()) # Use the pop method to remove the last element from the list.
print(list_names.pop(0)) # Removes the first element using index 0.
print(list_names)

order_list = ['a', 'b', 'c', 'z', 'd']
num_list = [4 ,2 , 5, 1]
order_list.sort()  # How to sort an alphabetic or numeric list. 
num_list.sort()
print(order_list)
print(num_list)

order_list.reverse(); # Use the reverse method to reverse the order of the elements.
num_list.reverse();
print(order_list)
print(num_list)

