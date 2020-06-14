# Iterable means you can iterate over the object or repeate an operation over every element in the object.

# Syntax of a for loop
my_iterable = ['Fred', 'Felipe', 'Jasma']

for item_name in my_iterable:
    print(item_name)

my_list = [1.0,2,3,4,5]
for num in my_list:
    print('The number is ' + str(num))

# Print out only the even number from that list.
for num in my_list:
    #Check for even. Use the modulus operator. It checks to see if the remainder is equals to 0!
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd number: {num}')

# Iterate through a list of strings and provide outputs based on them.
name_list = ['Fredinho', 'Felipinho', 'Jasma' , 'Mara', 'Beto', 'Random']
for name in name_list:
    if name[-4:] == 'inho':
        print(f'Small person is {name}!')
    elif name[-1:] == 'o':
        print(name + ' is a man!')
    elif name[-1:] == 'a':
        print(name + ' is a woman!')
    else:
        print('Dont recognize this person name ' + name)

# Getting a total by doing a loop in a List containing integers. Converting values to float.
# Printing string values that were converted.

my_list = [1.0,2,3,4,5,'6', False]
list_sum = 0.0
for num in my_list:
    if type(num) == int:
        list_sum = list_sum + float(num)
    elif type(num) == str:
        list_sum = list_sum + int(num)
        print(f'The string value converted is {num}!' )
    elif type(num) == float:    
        list_sum = list_sum + num
    else:
        print(f'Unrecognizable value: {num}')

print(list_sum)


# Printing even and odd numbers differently.
my_num_list = [1,2,3,4,5,6]

for num in my_num_list:
    if num % 2 == 0:
        print('The even number is {}!'.format(num))
    else:
        print(f'Odd number: {num}')

# Printing the sum
list_sum = 0
for num in my_num_list:
    list_sum = list_sum + num
print(list_sum)

# Iterate over string
mystring = 'Hello World'
for letter in mystring:
    print(letter)

# You can also iterate over a tuple.
tup = (1,2,3)
for item in tup:
    print(item);

# Tuple Enpacking
# Able to break down a tuple and use individual pieces.
new_tup = [('Fred',1),('Felipe',2),('Jasma',3)];

for a,b in new_tup:
    print(a + ' has ' + str(b) + ' goals in the season!')

# Iterate over dictionaries
# You get a returned set of tuples, where you can use the same technique of tuple enpacking.
d = {'k1': 1, 'k2': 2, 'k3': 3 , 'k4': 4 }
for item in d.items():
    print(item)

for key,value in d.items():
    print(key + ' has ' + str(value) + ' schools.')
