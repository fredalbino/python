print('Hi \nFrederico!')
print('Hi \tFrederico!')

print(len('Hello World')) # Remember to include the print function to return the length. 

mystring = 'Hello World'
print(mystring)

# String Slicing and Indexing
print(mystring[0])
print(mystring[5])

# Reverse Slicing and Indexing - You can start at the last index position.
print(mystring[-1])
print(mystring[-11])

# Slicing - Getting a subportion of the string.
newstring = 'abcdefg'
print(newstring[4:])  # Starts at index 4 until the end. 
print(newstring[:3])  # Starts in the beginning until index 4. Does not include index 4. 
print(newstring[2:4]) # Starts at 2nd and ends on the 3rd index. 4th is not included. 

# Slicing on step size.
print(newstring[::])  # Returns everything. Still common syntax.
print(newstring[::2]) # Return every 2nd character of string. 
print(newstring[2:7:3]) # Return every third character starting at 2, stoping at 7th character. 
print(newstring[1:7:3]) # Returns every third character starting at index 1, stoping at index 7.
print(newstring[0:len(newstring):2]) # Return every 2nd character starting a 0 until the end of string.
print(newstring[::-1]) # A clever way to reverse a string!!!
print(newstring[::-2]) # Reverse the string a give me every 2nd character. 

