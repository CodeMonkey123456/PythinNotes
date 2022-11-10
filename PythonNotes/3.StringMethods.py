#String methods are used to manipulate strings in Python.

full_name="Joe Smith"
print(len(full_name))
#len() is a function that returns the length of the string passed to it

print(full_name.upper())
#upper() is a method that returns the string in all uppercase

print(full_name.lower())
#lower() is a method that returns the string in all lowercase

print(full_name.isdigit())
#isdigit() is a method that returns true if the string is a number

print(full_name.isalpha())
#isalpha() is a method that returns true if the string is a letter

print(full_name.count("o"))
#count() is a method that returns the number of times a character appears in a string

print(full_name.replace("o","a"))
#replace() is a method that replaces a character with another character

print(full_name*3)
#* is a operator that repeats a string
