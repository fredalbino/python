# File Operations

# Opening the file withing the same directory.
myfile = open('myfile.txt');

print(myfile.read())

# This resets the cursor to the begining of the file! So now you can read it again.
myfile.seek(0)
print(myfile.read())
myfile.seek(0)

contents = myfile.read();

# Use the \n to concatenate strings in a new line. 
print(contents + '\n' +'IM THE BEST!');


myfile.seek(0)
# Each line in the file is a separete object in a list
print(myfile.readlines())


# Make sure to close the connection to the file!
myfile.close()

# For you to not have to worry about closing the connection to the file, use the following.
# Notice the indentation in the second line!
with open('myfile.txt') as my_new_file:
    new_content = my_new_file.read()

print(new_content)

# File updates
# The mode determines the operation being done to the file
# Mode: #
# r for read
# w for write (will overwrite files or create new!)
# a for append only (will add on to files)
# r+ is reading and writing
# w+ is writing and reading (Overwrites existing files or creates a new file!)

with open('myfile.txt', mode= 'r') as myfile:
    content = myfile.read()

print(content)

# Adding a new line to the FIle!
# Use mode='a' to append and f.write method for adding a new line.

# with open('my_new_file.txt', mode= 'a') as f:
#     f.write('\nFive on Fifth');

# with open('my_new_file.txt', mode='r') as f:
#     print(f.read())

# Exploring mode='w' for writing. Again this will overwrite or create new file.
with open('new_newest_file.txt', mode='w') as f:
    f.write('THIS IS THE NEWEST FILE!')

with open('new_newest_file.txt', mode='r') as f:
    print(f.read())
