# Object Oriented Programming (OOP)
'''
OOP is a programming paradigm that oraganize code using
classes and Objects. it helps in creating reusable , maintainable and scalable application.
'''

# 1. Class and Object

# A class is a blueprint or template for creating object.

# An Object is an instance of a class.

# syntax



class ClassName:
        pass

obj = ClassName()



# Student Class

class Student:
    
    def __init__(self , name , age):
        self.name = name
        self.age = age

    def display(self):
        print("Name : " , self.name)
        print("Age : " , self.age)

# creating objects

s1 = Student("Vivek" , 26)
s2 = Student("Rahul"  , 20)
s3 = Student("Roank", 21)

print(s1)

s1.display()
s2.display()
s3.display()

# self keyword

# self represent that current object of the class.

# Instance Variables
# Instance methods

# Employee

class Employee:

    def __init__(self , name , salary):
        self.name = name
        self.salary = salary

    def show(self):
        print("Employee Name : " , self.name)
        print("Salary : " , self.salary)

e1 = Employee("Rahul" , 50000)

e1.show()
'''
# del keyword

# delete variables
# delete objects
# delete object properties
'''
'''
x = 100
del x
print(x)

'''
# Student
'''
class Student:

    def __init__(self):

        self.name = "Vivek"


s1 = Student()

del s1

del s1.name
'''
# Encapsulation

'''
Encapsulation mean wrapping object(data) and function(methods) into a single unit (class) and restricting
direct access to some data
'''

# uses:

# Public
# Protected
# Private members

# Bank Account

class BankAccount:

    def __init__(self):

        self.__balance = 100000

    def deposit(self  , amount):

        self.__balance += amount

    def withdraw(self , amount):

        self.__balance -= amount

    def get_balance(self):
        return self.__balance

acc1 = BankAccount()

acc1.deposit(50000)

acc1.withdraw(20000)

print("Account Balance : " , acc1.get_balance())

# Polymorphism

# Polymorphism mean one interface , many forms.

# The same method behaves differently for different objects.

# Method Overriding

class Animal:

    def sound(self):
        print("Animal makes sound")

class Dog(Animal):

    def sound(self):
        print("Dog bhow bhow")


class Snack(Animal):

        def sound(self):
            print("Snack shreeeeeeeeee.....")

d = Dog()
s = Snack()

d.sound()
s.sound()

# same function different objects

class Car:

    def move(self):
        print("Car is running.")

class Plane:

    def move(self):
        print("Plane is flying.")

def action (vehical):
    vehical.move()

c = Car()
p = Plane()

action(c)
action(p)

# Abstraction

# Abstraction mean hiding implementation details and showing only essential features.

# Python provides abstraction using the abc module.

# Vehical

class Vehical():

    def start(self):
        pass

class Car(Vehical):

    def start(self):
        print("Car started.")

class Bike(Vehical):

    def start(self):
        print("Bike started.")

c = Car()
b = Bike()

c.start()
b.start()

# Inheritance

'''
Inheritance allows one class to acquire properties and method of another class.
'''

#1. single inheritance

class Parent:

    def show(self):
        print("Parent Class")

class Child(Parent):
        pass

c = Child()

c.show()

# Multilevel Inheritance

class GrandParent:

    def title(self):
        print("Grand Parent")

class Parent(GrandParent):

    def title1(self):
        print("Parent")

class Child(Parent):

    def title2(self):
        print("Child")

obj = Child()

obj.title()
obj.title1()
obj.title2()

# Multiple Inheritance

class Father:

    def father_property(self):
        print("Car")

class Mother:

    def mother_property(self):
        print("Jewelry")

class Child(Father, Mother):
    pass

c = Child()

c.father_property()
c.mother_property()

# Hierarchical Inheritance

class Parent:

    def display(self):
        print("Parent Class")

class Child1(Parent):
    pass

class Child2(Parent):
    pass

c1 = Child1()

c2 = Child2()

c1.display()
c2.display()

# Hybrid Inheritance

class A:

    def showA(self):
        print("A Class")

class B(A):

    def showB(self):
        print("B class")

class C(A):

    def showC(self):
        print("C class")

class D(B , C):

    def showD(self):
        print("D class")

obj  = D()

obj.showA()
obj.showB()
obj.showC()
obj.showD()









    
