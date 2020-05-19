# File Locations
# If you want to open files at another location on your computer,
# simply pass in the entire file path.
# For windows you need to use a double \ so pythong doesnt treat the second \ as an escape character, a file path is in the form:
# Windows  
# myfile = open("C:\\Users\\Username\\Folder\\test.txt")
# MacOS and Linux - Use slashes in the opposite direction
# myfile = open("/Users/Username/Folder/myfile.txt")

import os

print(os.getcwd())
print(os.path.dirname(os.path.realpath(__file__)) + "\n")

print("Path at terminal when executing this file")
print(os.getcwd() + "\n")

print("This file path, relative to os.getcwd()")
print(__file__ + "\n")

print("This file full path (following symlinks)")
full_path = os.path.realpath(__file__)
print(full_path + "\n")

print("This file directory and name")
path, filename = os.path.split(full_path)
print(path + ' --> ' + filename + "\n")

print("This file directory only")
print(os.path.dirname(full_path))