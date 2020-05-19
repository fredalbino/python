# Sets
# Unordered collections of unique elements.
# Meaning there can only be one representative of the same object.

myset = set()

print(myset);

myset.add(1);
myset.add(2);

print(myset);

# If you add 2 again notice how 2 will not display twice in the result.
myset.add(2);
print(myset)

# You can also turn a List with possible repeated vablues into a Set with unique values!
mylist = [1,1,1,2,2,2,3,3,3];

mylistset = set(mylist);

print(mylistset);set