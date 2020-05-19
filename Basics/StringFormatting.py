# Print Formatting with Strings
# String interpolation - ways to format strings for printing variables in them.
# Two methods for this: 
# 1. .format() method
# 2. f-strings (formatted string literals)
firstname = 'Fred'
lastname = 'Albino'

sentence = 'My first name is {}, last name {}'.format(firstname,lastname)
sentence2 = 'My first name is {1}, last name {0}'.format(firstname,lastname)
sentence3 = 'My full name is {f} {m} {l}.'.format(f=firstname, l=lastname, m='Araujo')

print(sentence)
print(sentence2)
print(sentence3)

# Float Formatting follow "{value:width.precision f}"

result = 100/777
print(result)
print("The result was {r:1.3f}".format(r=result)) # Update the precision to 3 decimal places.


# f-string (Formatted string literals)
name = "Jose" 
age = 15
print(f"{name} is {age} years old.")
