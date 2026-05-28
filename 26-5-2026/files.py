# Polymorphism in python

# Polymorphism mean "many froms"in object-oriented programning(OOP)

# Plymorhism allows the same method name to perform diffrent task depending on the object or argumanet use

# Method Overloading
# Method Overriding

#It also Provide buit in functions

# issubclass()
# super()


# 1. Mehod Overloding

# Mthod overloading mean creating multiple method with the same name but with diffrent parameter.

class Calculator:
    def multiply (self,a,b,c =1):
        return a*b*c

# Object

calc=Calculator()

print("Multiplication of 2 Numbers:")

calc.multiply(2,4)

print("Multiplication of 3 Numbers:",calc.multiply(2,4,3))

# If only 2 arguments are passed, c takes default value l.

# if 3 orguments are passed are passed,all values are multiplied.

# same method name muktiply()perform diffrent operations.

# 2. Method Overriding

# Method Overriding occurs when a child class provides a specific implementation of amethod already defind tn the parent class.

class Animal:

    def speak(self):

        print("Animal makes a sound")

class Dog (Animal):

    def speak (self):
        print("Dog barks")

class cat (Animal):

    def speak (self):
        print ("cat meow")

# object

a=Animal()
d=Dog()
c=cat()

a.speak()
d.speak()
c.speak()

# Dog and cat inherite from Animal,

# Both child classes override the speak () method.

# issubclass () function

# issubclass () is a built-in python function used to check weather one class is drived from another class.

# syntax issubclass (child-class,parent_class)

# It"s return

# True__> if in hetitonce exists
# Flase__> otherwise

class person:
    pass

class student (person):
    pass

issubclass (student,person)

# student inerites from person

print(issubclass (student,person))

# polymorphism in function

def add (a,b):
    return a+b

print (" Addition of integers:",add(10,20))

print (" conactention of string:",add("Hello","world"))


        

  
