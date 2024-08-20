 #print("hello world")

""" print ("let's start")
age= int(input("write your age"))
print (age)
question = eval(input("Write to get answer"))
print (question) """

# program to display person detail in diffrent line
"""" print("John \n")
print("18 \n")
print("californi anewyouk \n") """

#Program to swap two variable

""""
print("after swaping")
variable1= int(1)
variable2= int(3)
variable3= int(5)
variable2==variable1
variable1==variable3
print (variable2 , variable1) """
"""
a = 13
b = 67
a,b = b,a
print(a , b) """

# program to convert float into int
"""
a = 2.89
a = int(a)
print (type(a))
print (a) """

#program to take detail for id tard and print in next line
"""
name = input ("Write your name ")
Course = input("write your course name ")
Enroolmentno = input("write your enroll no ")
print( name )
print( Course )
print( Enroolmentno ) """

#program to take value as a int then convert it into float
""""
print("write your value to convert it into float")
value = int(input())
value = float(value)
print(value) """

#conditional statement
"""
age = int(input("Write your age:"))
if (age >= 18 and age<90):
    print("you can drive")
elif (age>90):
    print("you are too old to drive")   
else:
    print("you can't get lisence") """

# check no is positive or not
"""
print("check your num is positive or not")
num = int(input("Write your no"))
if num>0:
    print("your no is positive")
else:
    print("no is negative") """

#check no is odd or even
""""
num = int(input("check your no is even or odd:"))
if num%2:
    print("no is odd")
else:
    print("no is even") """#area calculator## """
""" ("" press 1 to get area of square
press 2 to get area of rectangle
press 3 to get area of triagle"")
press1 = int(input())
press2= int(input())
press3= int(input()) 
"""
"""press1:
     num = int(input("enter your "))
num = num*num
print(num)
if press2:
    length= int(input("enter your length"))
    breath= int(input("enter your breath"))
    print (length*breath)

else:
    length = int(input("enter your length"))
    breath = int(input("enter your breath"))
    print(length * breath*2) """

#program to check vowel

"""
alphabet = input("write your alphabet ton check vowel:")
if alphabet.lower() in "aeiou":
    print("Your alphabet is vowel ")
else:
    print("Hahdaha your alphabet is not vowel") 
    """

# introduction in loop for loop
"""
for i in range (1,11):
    print(i)
"""
#program for print table
""""
num = int(input("Write a for your table"))
for i in range (1,11):
    print(num*i)
    """
#while loop

"""
n = 0
while n<=10:
    print (n)
    n +=1
"""
 #print table using while loop
"""
 i = 1
 n = int(input("Write a no to print table"))
 while i <= 10:
     print (i*n)
     i += 1
"""

 #while true loop also know as infinie loop
"""
while True:
    num1 = int(input("Enter your number: "))
    num2 = int(input("Enter your number: "))
    print(num1 + num2)
    repeat = input("Do you want to stop the program? (yes to stop): ")
    if repeat.lower() == "yes":
        break
    else:
        print("Ok, no problem.") """

#Nested loop generally used to solve pattern problems
"""
for i in range (1,4):
    for j in range (1,11):
        print(j, end="")
        print()
        """
#pattern problem

""""
for i in range (1,6):
    for j in range (1,i+1):
        print(j,end = " ")
        print()
"""

#continue and break

"""
for i in range(1,11):
    if i == 5:
        continue
    else:
        print(i)
        """

#sum of 50 even even no
"""
sum = 0
for i in range (1,51):
    if i%2==0:
         sum+=i


print (sum)
"""

#program to find sqare of first 20 no
"""
for i in range (1,21):

  print("the sqare of no", i, "is:",i*i) 
  """

""""
sum = 1
i =0
while i<=20:
      if(i%2!=0):
       sum+=i
    i+=1

print(sum)
"""

#program to check if the no is divide by 8 & 12

"""
for i in range (1,101):
    if (i%8==0):
        print ("no is divisible by 8 :",i)

for i in range (1, 101):
    if (i%12==0):
        print("no is divisible by 12 :", i)

"""

# Supermarket cashiour system
"""
while True:
    Name = input("Write your name")
    total = 0
    while True:
        quantity = int(input("Write your Quantity "))
        amount = int(input("write your amout each"))
        total += quantity * amount
        print("Your total is : " ,total)
        print ("Next costumer") """

#play with string

"""
a = "Why fit in, When you are to Stand Out!"
print(len(a))
print(a.count("o"))
x = a.lower()
print(x)
y = a.upper()
print(y)
print (a.find("fit in"))
"""

#pattern problem

""" 
for i in range (1,6):
    for j in range (1,i+1):
        print("#" ,end = " ")
    print()
"""

"""
for i in range (1,6):
    for j in range (6,i,-1):
        print(i , end = " ")
    print() """

#slicing in string
"""
a = "Harry Potter and the Goblet of fire"
print (a[0:5])
print (a[6:12])
print(a[-4:]) """

#Fabonaci series

"""
a = 0
b = 1
n = int(input("Enter you number for fabonnaci series :"))
if n==1:
    print (1)
else:
    print (a)
    print(b)
    for i in range (2,n):
        c = a+b
        a = b
        b = c
        print ( c , end = " ")
"""

#prime no

"""
print("program for prime no: ")
num = int(input("Enter your no to check it is prime or not "))

for i in range (2,num):
    if num % i == 0:
        print("it is not prime")
        break


else:
    print("your no is a prime")

"""

#palidrome of integer
"""
num = int(input("check pallindrom"))
"""
#list
"""
fruit = ["apple" , "mango" , "Banana" , "Kivi"]
print(fruit)
print (type(fruit)) """

#slicing list
"""
a = ["java", "python", "C" , "ruby"]
print (a[-1]) """

#list iteration by simple for loop
"""
a = ["java", "python", "C" , "ruby"]
for i in a:
    print(i) """

#iteration by using range
"""
a = ["java", "python", "C" , "ruby"]
for i in range(len(a)):
    print(a[i]) """

#list function
#find lenght of list
"""
a = ["java", "python", "C" , "ruby"]
print(len(a)) """

#add element in list
"""
a = ["java", "python", "C" , "ruby"]
a.append("rush")
print(a) """

#count arrurent/reapet element

"""
a = ["java", "python", "C" , "ruby"]
print(a.count("java")) """

# add element on specific location

"""
a = ["java", "python", "C" , "ruby"]
a.insert(2,"html")
print(a) """

# remove specific element
"""
a = ["java", "python", "C" , "ruby"]
a.remove("java")
print(a) """

# remove from specific index
"""
a = ["java", "python", "C" , "ruby"]
print(a.pop(2))
print(a)
"""
#add element of other list

"""
a = ["java", "python", "C" , "ruby"]
b = ["rush", "dotnet", "html"]
a.extend(b)
print (a) """

#problem solving
"""
a = ["java", "python", "C" , "ruby"]
a.insert(1,"rush")
print(a)
"""

#Delete the value at 3rd position

"""
A = [13,7,12, 10]
print(A.pop(3))
print(A)
"""
#Swap 1st and 4th element

"""
A = [13,7,12, 10]
A[0],A[3]=A[3],A[0]
print(A) """

# arrange in accending order
"""
A = [13,7,12, 10]
A.sort()
print(A) """

#Tuples

"""
a = "java", "python", "C" , "ruby"
print(type(a))
print (a) """

#How to add value in tuple or conversion
"""
a = "java", "python", "C", "ruby"
a = list(a)
print(type(a))
a.append("rush")
print(a)
a = tuple(a)
print(type(a))
print(a.count("java")) """

#Dictionary
"""
Employdata = {"name" :"max", "age":24,"gender": "femael" }
print(Employdata ["name"]) """

#Iteration in dictionary
"""
Employdata = {"name" :"max", "age":24,"gender": "femael" }
print(Employdata ["name"])
for x in Employdata :
    print(x) """

# for getting value
"""
Employdata = {"name" :"max", "age":24,"gender": "femael" }
print(Employdata ["name"])
for x in Employdata :
    print(Employdata[x]) """

#for getting both value and name
"""
Employdata = {"name" :"max", "age":24,"gender": "femael" }
for x,y in Employdata.items() :
    print(x,y)
"""

#dictionary funtion

#keys
""" 
Employdata = {"name" :"max", "age":24,"gender": "femael" }
b = Employdata.keys()
print(b)"""

#value
"""
Employdata = {"name" :"max", "age":24,"gender": "femael" }
b = Employdata.values()
print(b) """

""""
Employdata = {"name" :"max", "age":24,"gender": "femael" }
b = Employdata.setdefault("age",22)
print(b)
"""

"""
#double dictonary
Employdata = {1: { "name": "EREN", "car":"lamb", "age": 23},
             2:{ "name": "ram", "car":"800", "age": 24}}
print(Employdata) """

"""
student = {1:{"name":"raj" , "age":23 , "stream":"science"},
           2:{"name": "ram" ,"age":25 , "class": "low"}}
print(student)
"""

#sort dictonary by value

"""
a = {"name" :"max", "age":24,"gender": "femael" }
a = sorted(a.values())
print(a)
"""
#set
"""
a = {"name" ,"max", "age","gender" , "femael"}
print (type(a))
print (a)
"""
#funtion of set

#add value
"""
a = {"name" ,"max", "age","gender" , "femael"}
a.add("hmm")
print (a)
"""
#pop value
"""
a = {"name" ,"max", "age","gender" , "femael"}
a.pop()
print (a) """

#remove particular element from set

"""
a = {"name" ,"max", "age","gender" , "femael"}
a.remove("max")
print (a) """

#function
"""
def hello():
    print("hello world")
hello() 
"""
# funtion for add no
"""
def add():
    x = 788
    y = 879
    print (x+y)
add() """

#parameter and arguments in funt
"""
def add(x,y): #x and y is parameter here
    print(x+y)
add (7887,8987) #here no we provided is argument """

#return statement and recursion

#return
"""
def add(x,y):
    return("the adding is",x+y)
print(add(233,3432)) """

#recursion
"""
def hello():
    print("hello")
    return hello()
print(hello()) """

#program of factorial
"""
def fact(n):
    if n==1:
        return 1
    else:
        return (n*fact(n-1))
print(fact(6)) """

#in-build module

#date and time module

"""
import datetime

x = datetime.datetime (2003,10,16) #NOW IF YOU WANT TO GET CURRENT TIME

print(x.strftime("%A"))

"""

#random module

"""
import random

x = random.randint(1,10)
print (x) """

"""
import random
l = ["Heads","Tails"]
x = random.choice(l)
print(x)
"""

#math modole

import math

"""
y = max(1,278,899)
print(y)"""

#math.sqrt (for square root)
#pow is for power

#Function in python

"""def avg(): #funtion defination
    a = 34
    b = 78
    c = 68
    print(a+b+c)
avg()
avg()
avg()
avg() #funtion call"""
###
"""def greet():
    print("good day")

greet() """

#funtion with argument
"""def greet(name, ending):
    print("good day, " + name +  ending)

greet("zaid", "Thank you")
greet("max", "Thank you") """

"""def greet(name, ending):
    print("good day, " + name +  ending)
    return "ohh ho"

a = greet("zaid", "Thank you")
print(a) """

#default perameter value

"""def greet(name, ending ="thank you"):
    print(f"good day, {name} ")
    print(ending)
greet("zaid") # here it takes by default value
greet("zaid" ,"chl be") """

# recursion funtion which call itself
#factorial

"""def fact(n):
    if (n==1 or n==0):
        return 1
    return n*fact(n-1)

n = int(input("enter no for factorial:"))
print(f"the factorial of no is: {fact(n)}" )"""

"""def table():
    num = int(input("Write a no which table you want"))
    for i in range (1,11):
        print(i*num)
table()
table()
table() """

#classes
"""class car:
    name = "aston "
    color = "black"
    price = 20000000

aston = car()
print(aston.name , aston.color, aston.price)"""

#class atribute
"""class car:
    name = "aston " #this is class atribute
    price = 20000000

black = car()
black.color= "white"
print(black.name, black.color, black.price)

model = car()
model.type = "Db" #this is object atribute also called instace atrinute
print(model.name ,model.type, model.price) """

#self parameter

"""class car:
    name = "aston " #this is class atribute
    price = 20000000

    def getinfo(self):
        print(f"the name is {self.name}. and price is {self.price}")

black = car()
black.color= "white"
print(black.name, black.color, black.price)

model = car()
model.type = "Db" #this is object atribute also called instace atrinute
print(model.name ,model.type, model.price)
black.getinfo() """

#init contructor
"""class car:
    name = "aston " #this is class atribute
    price = 20000000

    def getinfo(self):
        print(f"the name is {self.name}. and price is {self.price}")

    def  __init__(self): # dunter method which call itself
        print("I am good")

black = car()
black.color= "white"
print(black.name, black.color, black.price)

model = car()
model.type = "Db" #this is object atribute also called instace atrinute
print(model.name ,model.type, model.price)
black.getinfo() """

#practice
"""class Programmer():
    language = "python"
    salary = 1500000
    country = "India"

name = Programmer()
name.raj = "raj"
print(name.language, name.raj, name.salary, name.country)

name = Programmer()
name.raj = "ram"
print(name.language, name.raj, name.salary, name.country)"""

"""class calculator:
    def __init__(self,num):
        self.num = num

    def square(self):
        print(f"the squre is {self.num*self.num}")

    def cube(self):
        print(f"the cube is {self.num*self.num*self.num}")

a = calculator(6)
print()
a.square()
a.cube() """

#2 add static method

"""class calculator:
    def __init__(self,num):
        self.num = num

    @staticmethod
    def greet():
        print("Hello")

    def square(self):
        print(f"the squre is {self.num*self.num}")

    def cube(self):
        print(f"the cube is {self.num*self.num*self.num}")

a = calculator(6)
a.square()
a.cube()
a.greet() """

#3 railways
"""class Train:

    def booking(self):
        name = input("write your name ")
        location = input("write your location ")
        price = input("Write the ticket price ")
        print(f"the name is {name}: location is {location}: price is {price}")

    def getstatus(self):
        seats = 47
        print("the raimaning seats is",seats)

    def getfair(self):
        train = "fast train"
        priceof = 250
        destination = "leh"
        print(f"the train available is {train}, price is {priceof}, destination is {destination}")
        
a = Train()
a.booking()
a.getstatus()
a.getfair() """

#inheritance and more oops

"""class Employee:
    Company = "Amazon"
    def show(self):
        print("the name is  and the salary is ") """

####replace code this with inherite class####
"""class programmer:
    Comapy = "Amazon Tech"
    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary}")

    def showlanguae(self):
         print(f"the name is {self.name} and the he good with {self.language}") """

"""class programmer(Employee):
    company = "Amazon info"

    def showlanguae(self):
        print("the name is  and the he good with")

a = Employee()
b = programmer()
print(a.Company, b.company) """

#Multi level inheritence

"""class Employee:
  a = 1

class programmer(Employee):
    b = 2

class manager(programmer):
    c = 3
d = Employee()
d = manager()
print(d.a,d.b,d.c) """

#super method
"""
class Employee:
  a = 1
  def __init__(self):
      print("Constructor of employee ")

class programmer(Employee):
    b = 2

    def __init__(self):
        print("Constructor of programmer ")
class manager(programmer):
    c = 3
    def __init__(self):
        super().__init__() #super method used for run construtor or code of parent class
        print("Constructor of manager ")

#d = Employee()
d = manager()
print(d.a,d.b,d.c) """

# @class method
"""class Employee:
  a = 1
  @classmethod # class method is used when we don't want to print instance of class
  def show(cls):
    print(f"The class attribute of a is {cls.a}")

b = Employee()
b.a = 23

b.show() """

# operator overloading
"""
class Number:
  a =1
  b = 2 """

"""class vector:
    a = 1

class threedvec(vector):
    b = 1

c = threedvec()
print(c.a , c.b) """

#walrus oprator
"""
if (n := len([1,2,3,4,5])) > 3:
    print(f"List is too long {n}") """

#type defination
"""n : int = 5
name: str = "Zaid"

def sum(a: int, b:int):
    return a+b
print(sum(3,5)) """

#advance type hint

"""from typing import List,Tuple """

#match case it is similar to switch case from c language

"""def weekdays(day):
    match day:
        case 1:
         return ("it's mondaty ")
         
        case 2 :
            return ("it's tueday buddy")

        case _:
           return ("It other weekdays")

print(weekdays(1)) """

#exception handling
"""try:
    a = int(input("enter you no: "))
    print(a)

except Exception as j:
  print(j)

print("achhaaaa mazaa aariyaaa") """

#raising expections errors
"""a = int(input("Number likho bhai: "))
b = int(input("Dusra number likho: "))


if b==0:
    raise ZeroDivisionError ("Pagal hi ho kya bilkul devision ke rule nhi pata?")
else:
    print(f"The division of a/b is {a / b}") """

#try else

"""try:
    a = int(input("enter you no: "))
    print(a)

except Exception as j:
  print(j)

else:
 print("achhaaaa mazaa aariyaaa") """

#try finally
"""try:
    a = int(input("enter you no: "))
    print(a)

except Exception as j:
  print(j)

finally:
 print("Hy I am in finally block") """ #yeh chalga hi chalega zayada tarh function mai use hota hai

# if __name__== __main__

"""def myfunc():
    print("hello")

myfunc()
print(__name__)
if __name__=="__main__" """

#global variable

"""a = 4 #global variable
def fun():
    global a  #this global keyword make local variable global
    a = 3 #local variable
    print(a)

fun()
print(a)"""

#enumurate
"""l = [2,7,89,3]
index = 0
for item in l:
    print(f"the item at index {index} is {item}")
    index +=1 """

# this code by using enumurate function
"""l = [3,4,67,75,32,43]
for index, item in enumerate(l):
    print(f"the item number at index {index} is {item}")
"""

#list comprehension
"""mylist = [1,3,5,89,5]

sqaredlist = []
for item in mylist:
    sqaredlist.append(item*item)

print(sqaredlist) """

