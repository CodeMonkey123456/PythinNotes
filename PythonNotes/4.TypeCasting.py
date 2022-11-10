#type casting is the process of converting a variable from one data type to another

x=1 #x is an integer
y=2.8 #y is a float
z="3" #z is a complex number

y=int(y) #convert y from a float to an integer, y is now 2
z=int(z) #convert z from a string to an integer

print(x)
print(y)
print(z*2) #z is now an integer so it can be used in math operations, prints 6

#you must convert an integer to a string before you can concatenate it with a string, such as:
print("I am "+str(x)+" years old")