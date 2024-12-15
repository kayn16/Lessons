# Text Data - string
# Numeric Types - integer, float
# Squence Types: list, tuples, range
# Mapping Type: dict
# Boolen Types: true or false

# Code that shows the data type.
x = 5
print(type(x))

# String
x = "Hello Class"

# Integer: can be negative.
x = -5

# Float
x = 1.4

# List
x = ["banana", "apple", "cherry"]

# Range: shows numbers till the number that is written.
x = range(5)

# Dictionary: can store more than one data, can store different types of data. ( integer,string,boolen,float,etc.)
x = {
    "name" : "John",
    "Surname": "Smith",
    "age": 42
}

# Boolen is true or false.
x = bool(4)

# Import: can call module.

# " and ' is same.
x = "Yusuf"
x = 'Yusuf'

# Redline is error.

# """ You can write multiple lines of notes.
"""
qweasdqweasd
"""

# Strings are arrays.
x = "How are you today"
print(x[1]) # Prints o

# Important note : index starts with 0.

# for, repeatly prints every index one by one till it finishes.
for x in "kemal":
    print(x)

# len, gives the length of the list or index numbers in the string.
a = "Yusuf"
print(len(a))

txt = "Yusuf has a cat"
print("cat" in txt)

if "cat" in txt:
    print("Yes, cat is in it")

# String slicing
x = "Hello Class!"
print(x[:7]) # Starts at the beginning because there isn't a number.

z = "Hello Class!"
print(z[2:])

# negative index
x = "Hello Class!"
print(x[-5:-2])

# upper case
a = "yusuf"
print(a.upper())

# lower case
a = "YUSUF"
print(a.lower())

# strip()
x = " Yusuf Elber Dagtas "
print(x.strip())

# replace(
a = "Yusuf"
print(a.replace("u", "a"))

# split()
x = "Yusuf Elber Dagtas,Halil Ege Ozer,Eren Yıldız"
print(x.split(","))

# concatenation
a = "Yusuf"
b = "Dagtas"
c = a + b
print(c)

c = a + " " + b
print(c)

# age = 18
# name = "My name is Yusuf, I am" + age
# print(name)
# Doesn't work because age isn't a string

# f string
age = 18
name = f"My name is Yusuf, I am {age}"
print(name)

price = 80
x = f"car price is {price} turkish lira"
print(x)

price = 65
txt = f"the price is {price:.2f} dollars"
print(txt)

txt = f"the price is {50 + 90} dollars"
print(txt)

# txt = "I am a lecturer."kemal" " wrong

txt = "I am a lecturer. \"kemal\" " # correct
print(txt)

# boolean values
# true or false
print( 10 > 9)
print( 10 == 9)
print(10 < 9)

a = 250
b = 50

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# evaluate values
#True
bool("hi")
bool(15)
bool("abc")
bool(123)
bool(["apple", "orange"])

#False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])

def myFunction():
    return True

print(myFunction())

def myFunction():
    return True

if myFunction():
    print("yes")
else:
    print("no")

x = 120
print(isinstance(x, str))

# operators
# + addition
# - subtraction
# * multiplication
# / division
# +=   x + = 3   x = x + 3

x = 100
x += 3
print(x)

x = 100
x -= 3
print(x)

x = 100
x *= 3
print(x)

# == equal x == y
# != not equal x !=y
# >= greater than or equal to x >= y
# <= less than or equal to z <= y

x = 3
y = 3
print(x == y)

x = 3
y = 3
print(x != y)

# and operator
print(x < 4 and x < 10)
print(x > 1 and x < 4 and x < 10)

# or operator
x = 2
print(x < 4 or x > 10)

# not operator
x = 4
print(not(x < 5 and x < 10))
x = 5
print(not(x < 5 and x < 10))

# is
x = 3
y = 3
print(x is y)

# is not
x = 3
y = 3
print(x is not y)


## End