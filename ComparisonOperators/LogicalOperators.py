# We can use logical operators to combine comparisons:

print(1 < 2 < 3 < 2)

# Using and keyword - All conditions must be true.

print(1 < 2 and 2 > 3)
print('h' == 'h' and 2 == 2)

# Using OR keyword - One condition needs to be true.
print('h' == 'h' or 1 > 2)
print('h' == 'H' or 1 > 2)

# Using NOT keyword - Opposite boolean of what expected.
print(not(1 == 1))
print(not(2 == 3))