# Function in python

# Function,Recursion,Lambda Function,Global Keyword and Multiple return Value

# What is Function 
# Reusability,Cleaner code,Better Optimization,Reduce repetition

# Type of Function

# Bulit-in Function

# UDF Functions

def prints():
    print("Welcome students!!")

print()

def multi(a,b):
    print("Multiplication:",a*b)

multi(4,5)

# Recursion Function

# A function calling itself.

# Factorial,Fibonacci,Tree structure,Problem Solving

def factorial(n):

    if(n==1):
        return 1
    return n* factorial(n-1)

print (factorial(5))


# 2.Sum of two numbers

def total (n):

    if n ==0:
        return 0

    return n + total (n-1)

print (total(5))

# Anonymous/Lambda function

# Small anonymous function
# Written in one line
# No function name
# Systax

# lambda argunents : expression

square = lambda x:x*x

print(square(5))


add=lambda a,b:a+b

print (add(10,20))


# list

numbers=[1,2,3,4,5]

result = list (map(lambda x:x*2,numbers))

print (result)

# filter

numbers =[1,2,3,4,5]

odd=list(filter(lambda x:x%2!=0,numbers))

print (odd)

# Normal Function
'''
def Keyword
Multiple line
Named
'''
# Lambda Function
'''
lambda Keyword
single line
Anonymous
'''

# Global keyword

# variables created outside function are called golbal variables

# to modify global variable inside function use 'global'

x=10

def show():
    print (x)

show()

count=0

def increment():
    global count
    count + 1

increment()
increment()
increment()

# Rrturn Multiple value

# Python  function can return:

# single value
# multiple value

def calculation (a,b):

    return a+b,a-b

result = calculation (10,5)

print (result)


def student():

    name="Alice"
    marks=90

    return name,marks

n,m=student()

print(n)
print(m)

# Returning multiple calculation
# Returning user data
# Returning API responses


# Bulti in functions

numbers=[1,2,3,4,5]

print("Length:",len(numbers))
print("Maximum:",max(numbers))
print("Minimum:",min(numbers))

# this is pre-defined function inside python you don't create them

# user difined function (UDF)

def greet(name):
    return "Hello" + name

print(greet("students"))

# Arbitraty Argyuments (*args)

# when number of inputs is unkown

def add_number(*args):
    total=0

    for  num in args:
        total += num
    return total

print (add_number(1,2,3))

# *args collects multiple value into a tuple

# key word Argument(**kwargs)

# when passing named values

def student_info(**kwargs):
    for key , value in kwargs.items():
        print(key , ":" , value)

student_info(name="Rahul",age=20)

# **kwargs stored data in dictionary

# doc (Documentation string)

#nused to describe function

def multiply(a,b):
    """This function returns the multiplication of two numbers"""
    return a*b
print(multiply(4,5))
print(multiply.__doc__)

# TNRN classifivation

'''
T->Take Arguments
N->No Arguments
R->Return Value
N->Noreturn Value
'''
'''
TNRN->Take No Arguments,Return No Value
TSRN->Take Some Arguments,Return No Value
TNRS->Take No Arguments,Return Some Value
TSRS->Take Some Arguments,Return Some Value
'''

# 1.TNRN

'''
No Parameter
No Return statement
def function_name():
#code
'''

def greet():
    print("Hello,python students")

greet()

# 2.TSRN

'''
Accept parameter
Does not return result
'''

def add (a,b):
    print ("Addition:",a+b)

add(10,20)

# 3.TNRS

'''
No parameter
Return value using return
'''

def message():
    return"Hello student"
print(message())

# TSRS Function

'''
Accept parameter
Return output
'''

def multiply(a,b):
    return a*b

result = multiply(4,7)

print(result)


    
