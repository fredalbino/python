# WHile Loops #
# Will continue to execute a block of  ode while some condition remains True 
# You can combine with an else if you want, example:
#while some_boolean_condition:
    #Do Something
#else:
    #Do something different

x = 50;

while x < 5:
    print(f'The current value of x is {x}');
    x += 1;
else:
    print('X is not less than 5')


name = "Fred Albino"

while len(name) > 4 and name != 'Fred':
    print(f'The updated name is {name}')
    name = name[:-1]
else:
    print(len(name))
    print(f'We have found {name}!!!')

# Break, continue, pass
# We can use break, continue, and pass statements in our loops to add additional functionality for various  cases. The three statements are defined by:
# Break - breaks out of the current closent enclosing loop.
# Continue - Goes to the top of the closest enclosign loop. 
# Pass - Does nothing at all. 

x = [1,2,3]

for item in x:
    # Update this pass here!
    pass                            # This will allow the remaining of the code to be executed without throwing an error. 
print('End of my script here!')

my_string = 'sammy'
for letter in my_string:
    if letter == 'a':
        continue                    # This will skip the print of letter 'a'
    print(letter)


stringerror = []
bignum = []
numlist = [1,2,'a',5,6,'b',100]

for value in numlist:
    if type(value) == str:
        print(f'This is not a number! Value: {value}');
        stringerror.append(value)
        continue
    if type(value) == int and value < 10:
        print(f'This is a real number. Value: {value}');
        continue
    else:
        bignum.append(value)
        print('End of Loop.')
        break
print(f'String Errors: {stringerror}. Big Numbers: {bignum}')


