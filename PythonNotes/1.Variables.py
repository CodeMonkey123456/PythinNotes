#variables= a container for storing data values

#what are the data types in python?
#integers, floats, strings, booleans, none

first_name="Joe"
last_name="Smith"
full_name=first_name+" "+last_name

#name is a string variable, strings cannot be used in math operations
print("Hello my name is "+full_name)

#type() is a function that returns the data type of the argument passed to it
print(type("Hello my name is "+full_name))

#integers are whole numbers and can be used in math operations
age=20
age+=1
print(age)
#prints age +1

#convert a data type to a string
print("I am "+str(age)+" years old")
#prints age as a string(word) not an integer(number)

#floats are numbers with decimals
height=5.5
print("your height is :",height)

#boolean variables are either true or false
humane=True
print("Are you humane?",humane)

#none is a special data type that represents nothing
#it is used to represent the absence of a value
#it is not the same as an empty string, 0, or false

