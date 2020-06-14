mylist = [1,2,3,4,5]

#Using the range function! Range function is a generator function. It creates data dynamically instead of taking up memory space like traditional variables.
for num in range(3,10,2):  # Print starting at 3 up to but no including 10. Inclding a stepsize of 2. So print only the odd numbers between those two. 
    print(num)

#For creating a list using the range function, cast it to a list. 
print(list(range(0,11,2)))
evenList = list(range(0,11,2))
print(evenList)

index_count = 0
for letter in 'Fred Albino':
    print('At index {}, the letter is {}'.format(index_count, letter))
    index_count += 1

# We can use the enumerate function to return a set of tuples for each letter on a string. 
# Using tuple enpacking
word = 'abcdef'
letterList = []
for index, letter in enumerate(word):
    print(index);
    print(letter)
    print('\n')
    letterList.append(f'Index {index} contains {letter}')
print(letterList)


