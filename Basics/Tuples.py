# Tuples
# Tuples are very similr to Lists, however they have one key difference, IMMUTABILITY! CANNOT BE CHANGED!!!
# Once an element is inside a tuple, it ca not be reassigned!
# Tuples use parenthesis: (1,2,3)

tuple1 = (1,2,3)
mylist = [1,2,3]

print(type(tuple1))
print(type(mylist))

mixed_tuple = ('Fred', 'Fred' ,'Fred', 32)

# You can use same slicing and indexing like Lists.
print(mixed_tuple[0])
print(mixed_tuple[:1])

# Methods for tuples.
print(mixed_tuple.count('Fred')) # Count how many times 'Fred' appeared in the tuple.

# Lenth of Tuple
print(len(mixed_tuple))

# Count how many times 'Fred' happens in the tuple.
print(mixed_tuple.count('Fred'))

# What index does 32 happen
print(mixed_tuple.index(32))



