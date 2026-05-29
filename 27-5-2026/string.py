 # String Foramatting

name="Aisha"
age=21

# using f - string

print(f"My name is {name} and i am {age} year old.")

# using.format()

print("My name is {} and i am {} year old.". format (name, age))

# Using % formatting

print (" My name is %s and I am %d years old." % (name, age))

price=199.456

print(f"price:{price:.2f}")

# List and Tuple (Mutability)

# list

my_list = [10,20,30]

print("original List: " , my_list)

my_list [1]=200

print (" Modified List : ", my_list)

# append ()

my_list.append(50)

print("After append list :",my_list)

# remove()

my_list.remove(10)

print("After remove list:",my_list)

# Tuple -Immutable

my_tuple=(10,20,30,40)

print("Tuple:",my_tuple)

# Access Element

print("first Tuple Element:",my_tuple[1])

# Indexing and slicing

text="python"

# indexing

print("First letter:",text[0])
print("Last letter:",text[len (text)-1])
print("Last letter:",text[-1])

# slicing

print("First 3 letters:",text[0:3])
print("Last 3 letters:",text[3:])
print("Last 3 letters:",text[-3:])

#revese string

print("Reverse string:",text[::-1])

# Using list with slicing and formatting

students=["Dixit","Jinal","Raj","Janvi","Jiya","rutva"]

print("\n original List:",students)

print("\n first three students:",students[:3])

#loop

for student in students:
    print(f"welcome,{student}")

#length

print ("Length of List:",len(students))

#checking element

print("Is jiya present?:","jiya" in students)

#Nested list

matrix=[
      [1,2,3],
     [4,5,6],
     [7,8,9]
    ]

print("Matrix:",matrix)

#Accessing element

print("Middle element element:",matrix[1][1])

#string Method

message="python programming"

print("Uppercase:",message.upper())
print("Capitalized:",message.capitalize())
print("Replace:",message.replace("python","AI/ML"))
print("Split:", message.split())

#list method

numbers=[5,8,2,7,1]

numbers.sort()

print("Sorted List:",numbers)

numbers.reverse()

print("Reversed List:",numbers)

numbers.insert(1,100)

print("After insert:",numbers)






