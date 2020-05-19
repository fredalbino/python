# Dictionaries
# Dictionaries are unordered mappings for storing objects. Dictionaries are MAPPINGS!!!
# Previously we saw how lists store objects in an ordered sequence.
# Dictionaries use a KEY-VALUE pairing instead. 
# This key-value pair allows users to quickly grab objects without needing to know an index location! You just have to call the Key and youll grab the value!
# Dictionaries use curly braces and colons to signify the keys and their associated values.
# {'key1':'value1' , 'key2':'value2'}
# So when to choose a list and when to choose a dictionary?!

# Dictonaries: Objects retrieved by Key Name. Unordered and can not be sorted.
# List: Objects retrieved by location. Ordered Sequence can be indexed or sliced.

my_dict = {'Name': 'Fred', 'Age': 32}
print(my_dict)

print(my_dict['Name'])  # Just call the Key that you would like to grab the value for.

prices_lookup = {'apples': 2.99, 'oranges': 3.99, 'watermelon': 10.00}
print(prices_lookup['watermelon'] + 20)

# Nested Data Structures

nested_dict = {'name': 'Fred Albino', 'cars': ['Sonata', 'Evolution', 'Ferrari'], 'houses': {'Mansion': 'Downtown', 'Lakehouse': 'Lake Travis'}}

print(nested_dict['cars'])  # Calling the entire List within the dictionary.
print(nested_dict['cars'][0]) # Calling one element from the list using the index within the Dictionary.
print(nested_dict['houses']['Mansion']) # Calling a key within a nested dictionary by using both Keys!

print(nested_dict['cars'][2].upper()) # Using a method after selecting the nested value needed. 

# Adding a new Key to the Dictionary. Add key inside the bracket and value outside after equals sign!
nested_dict['career'] = 'Data Engineer'
print(nested_dict)

# Override a current value.
nested_dict['career'] = 'Senior Data Engineer'
print(nested_dict)

# Useful dictionary methods!!!
print(nested_dict.keys()) # Return all the dictionary Keys. 
print(nested_dict.values()) # Return all the values within Dictionary. 
print(nested_dict.items()) # Return all key/value pairs. If no nested values are present, it returns the data structure in tuples. 

