"""x = 5
y = ("Hello lucky kumar")
z = 3.14
bool_var = True #boolean variable
print(type(x))
print(type(y))
print(type(z))
print(type(bool_var))
x = 4,5
print(bool(x))
x = ""
print(bool(x))
x = "e"
print(bool(x))
my_var = 40
print(my_var)
x,y,z = "20", "30", "40"
print(x)
print(y)
print(z)    
x = "30","40","50"#tuple
print(type(x))  
y = {"apple", "banana", "cherry"}#set
print(type(y))
fruits = ["apple", "banana", "cherry"]#list
x,y,z = fruits
print(x)
print(y)
print(z)
print(type(fruits))
fruits = [2,4,7,8,34]
print(type(fruits))
x = "python"
y = "is"
z = "awesome"
print("x+y+z = " + x + " " + y + " " + z)

def my_function(): #local function variable
    x = "good"
    print("Python is " + x )
my_function()

def my_function():#global function variable
    global x    
    x = "good"
my_function()
print("Python is " + x )





x = 1j
print(type(x))

x = "good"
print(range)

my_list = ["apple", "banana", "cherry"]
print(type(my_list))
print(len(my_list))


my_list = ["apple", "banana", "cherry",  "orange", "kiwi", "melon"]
print(my_list[0])
print(my_list[1])
print(my_list[::-1])
print(my_list[2:5])
print(my_list[-5:-2])
print(my_list)
print(type(my_list))

print("Hello World ")

my_list = ["apple", "banana", 1,3,5,7]

my_list[2:5] = "abc"
print(my_list)


my_list = [1, 2, 4, 5, 6]

my_list.insert(2, "rajarya")
my_list.append("end")
my_list.index(1)

print(my_list)


list1 = [1,2,3, "apple",4,5,6]#remove item from list
#list1.remove("apple")
list1.pop(3)

print(list1)

list1 = [1,2,3, "apple",4,5,6]#remove item from list
#list1.remove("apple")
list1.pop()

print(list1)

list1 = [1,2,3, "apple",4,5,6]#remove item from list
#list1.remove("apple")
list1.pop(3)

print(list1)

my_list = [1, 2, 3,4]
my_list.insert(2, "banana")
my_list.append("apple")
print(my_list)
my_list.remove("apple")
print(my_list)
my_list2 = [5,6,7] 
my_list.extend(my_list2)
print(my_list)
my_list.pop()
print(my_list)  
my_list.clear()
print(my_list)

list1 = []
list1.append(1)
list1.append(2)
list1.append(3)
print(list1)
list1[0] = "Hello"
print(list1)
#loopslists
from unicodedata import name


list1 = [1,2,3,4,5,6,7]
for x in list1:
    print(x)
    
list2 = [1,2,3,4,4,4,4,4,5,6]
for x in list1:
    print(x)
    
#sort
list = [2,5,1,4,8]
list.sort()
print(list)

list1 = [2,5,1,4,8]
list1.sort(reverse=True)
print(list1)
#Common String Methods
text = "hello Python"
print(text.upper())
print(text.lower())
print(text.strip())
print(text.replace("Python", "World"))
print(text.split())
#format Strings

# 1. Using f-strings (Python 3.6+)
x = "Raja Arya"
y = 25
print(f"My name is {x} and I am {y} years old.")


# 2. Using str.format() method
print("My name is {} and I am {} years old.".format(x, y))


# 3. Using % formatting operator (old style)
print("My name is %s and I am %d years old." % (x, y))

#assignment operators
x = 5
x += 3
print(x)
x = 10
x -= 2
print(x)
x = 5
x *= 4
print(x)

x = 20
x /= 5
print(x)

x = 10
x %= 3
print(x)  

#comparison operators
x = 10
y = 7  
print(x == y)#equal
print(x != y)#not equal
print(x > y)#greater than
print(x < y)#less than
print(x >= y)#greater than or equal to
print(x <= y)#less than or equal to

#logical operators
x = 5
print(x > 3 and x < 10)#and operator(true if both)
print(x > 3 or x < 4)#or operator(true if any one)
print(not(x > 3))#not operator(reverses value)


#identity operators
x = [8]
y = x
z = [10]
print(x is y)#true(same object)
print(x is z)#false(different object)
print(x is not z)#true(different object)
print(x is not y)#false(same object)

#python Sets
colors = {"red", "green", "blue"}#create set
for x in colors:#loop through set
    print(x)
print(colors)
colors.add("yellow")#add item to set
print(colors)
colors.remove("green")#remove item from set
print(colors)
colors.clear()#remove all items from set
print(colors)

#python Dictionaries
student = {"name": "Raja Arya", "age": 17, "courses": ["Math", "CompSci"]}#create dictionary
print(student)
print(student["name"])#access value by key
print(student.get("age"))#access value by key using get()
student["age"] = 18#change value
print(student)
student ["age"] = 19
student["courses"] = ["Workshop technology"]#change value
print(student)
student.pop("age")#remove item by key
print(student)

#if... Else in python(condition Statements)
age = 20  # int(input("enter your age: "))


if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

marks = 86


if marks >= 90:
    print("Grade: A+")
elif marks >75:
    print("Grade: A")
    
elif marks >=60:
    print("Grade: B")
else:
    print("Grade: C")

marks = 78  # int(input("enter your marks: "))


if marks >= 90:
    print("Grade: A+")
elif marks >75:
    print("Grade: A")
    
elif marks >=60:
    print("Grade: B")
else:
    print("Grade: C")


age = 20

if age>18:
    print("you are adult")
elif age == 17 :
    print("you are 17")
elif age == 18:
    print("you are teen")
elif age == 16:
    print("you are 16")
else:
    print("you are not adult")


x = 15

if x>10:
    print("x is greater then 10")
    
    if x>20:
        print("x is greater then 20 ")
    else:
        print("x is not greater then 20")

#Question 1
x = 3
if x%2==0:
    print("x is even", x)
else:
    print("x is odd", x)

#Question 2
age = 18
if age >= 18:
    print("you can drive")
else:
    print("you can not drive")



#Python for Loops

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(fruits)



#Question1
world = "python"

for x in world:
    print(x)

#Question2
for i in range(5):
    print(i)


#Question 3
for i in range(1, 10,2):# 1 is start and 10 is end 2 gap one between number
    print(i)



#Question 4 (Nested for loops)

for i in range(1,4):
    for j in range(1,3):
        print(f"i={i}, j={j}")

# Question 5 (Using break statement in for loop)
for i in range(1,6):
    if i == 4:
        break
    print(i)

# Question 6 (Using continue statement in for loop)
for i in range(1,6):    
    if i == 3:
        continue
    print(i)



# Question 1 (Print numbers from 1 to 20) 
for i in range(1,21,1):

        print(i)


#Question 2 (Print even numbers from 1 to 30 using range)
for i in range(1,30):
    if i%2==0:
        print(i)



#Question 3 (Print each fruit from the list)
colour = ["red", "green", "blue", "yellow"]
for x in colour:
    print(x)


#Question 4

for i in range(1, 6):
    print(i)
    for j in range(1, 4):
        for k in range(1, 3):
            print(f"i={i}, j={j}, k={k}")
        




#Python Functions (Simple Function)

def greet(name):
    print(f"Hello, {name}")

greet("Alice")
greet("Raja Arya")

#function with Return value(addition)
def add(a, b):
    return a + b

result = add(5, 3)
print(result) #8


#subtraction
def add(a, b):
    return a - b

result = add(5, 3)
print(result) #8

#multiplication

def add(a, b):
    return a * b

result = add(5, 3)
print(result) #


#division

def add(a, b):
    return a / b

result = add(5, 3)
print(result) #1.6666666666666667   


 
def greet(name = "Student"):
    print(f"Hello, {name}!")
greet()#Hello Student

greet("Raja Arya")
 
 
 
x = 10

def my_func():
    y = 5
    print(x,y)
    
my_func()
print(x)

#Question 1
def greet():
    print("hello")
greet()
 
 #Question 2
def add(a,b):
     return a+b
result = add(9,5)
print(result)   
 
 #Question 3
x = 11
def my_function():
    global x
    y = 5
my_function()
print(x)

 #Oops in python
#Class
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self): #method
        print(f"{self.color} {self.brand} is driving🚗")

#Objects
car1 = Car("BMW", "Black")
car2 = Car("Tesla", "White")


car1.drive()
car2.drive()

#Arrays = an array is a collection of items of the same type.

import array


#Create an array of integers
number = array.array('i', [1, 2, 3, 4, 5])
print(number)

print(number[0])  # Access first element
print(number[2]) # Access third element

# python -m pip install numpy

from numpy import random
x = random.randint(100)
print(x)    
 

x = random.rand()
print(x)
 
[54]
[1,2,3,4,5]

[[1,2,3],
 [4,5,6]]

[[[1,2,3],
  [4,5,6]],
 [[7,8,9],
  [10,11,12]]]


#Question 1
from numpy import random
x = random.randint(100, size = (5))# columns
print(x)

#Question 2
x = random.randint(100, size = (3,5))# 3 rows and 5 columns
print(x)

#Question 3

x = random.randint(100, size = (2,2,3,5))# 2 blocks, 2 rows, 3 columns, 5 elements
print(x)

from numpy import random
x = random.choice([4,5,6], size = (2,3,5))

print(x)
# install pandas
#python3 -m pip install pandas(pandas is a library used for data manipulation and analysis)
#easy to handle tabular data

#labels for rows and columbs READ DATA FROM CSV FILE statuices anyalices
#large data handling

import pandas as pd 


data=[10,20,30,40]
s=pd.Series(data)
print(s)


#Example

import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24,27,22,32],
    "City": ["Delhi", "Mumbai", "Chennai","Kolkata"]

}

df = pd.DataFrame(data)
print(df)

# from a numpy array

import pandas as np

arr = np.array([1,2,3,4,5])

s = pd.Series(arr)
print(s)

# from a dictionary
data = {"Math":90, "Science":85, "English":78}

s = pd.Series(data)
print(s)


#Read data from CSV file
import pandas as pd
df = pd.read_csv("eda_data.csv")
print(df.head())
print(df.tail())"""


#Read datafrom CSV file
import pandas as pd
df = pd.read_csv("eda_data.csv")
print(df.head())
print(df.tail())