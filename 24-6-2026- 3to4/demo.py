
# python basics

# print your name
'''
print(" hello , my name is rutva !!")
'''
# add tow numbers
'''
a=5
b=10

sum=a+b

print("The sum is :",sum)
'''
# Ask user's name
'''
name=input("what is your name:")
print(name)
'''
# simple calcuator
'''
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

print("Addition:",a+b)
print("subtraction:",a-b)
print("Multiplication:",a*b)
print("Division:",a/b)
'''
# print() formatting using sep and end
'''
print("Apple","Banana","Cherry",sep="|",end="<---End of List\n")
'''
# formatting message from user input
'''
name=input("Enter your Name:")
age=input("Enter your age:")
hobby=input("Enter your favorite hobby:")
'''
# f-string
'''
print(f"Hello,{name},At{age},enjoying{hobby}sounds fun !!!")
'''
# Declare varriables of diffrent data types and show their types
'''
a=10
b=3.14
c="python"
d=True

print(a,"Type:",type(a))
print(b,"Type:",type(b))
print(c,"Type:",type(c))
print(d,"Type:",type(d))
'''
# python program
'''
subject=input("Enter 1st subject name:")
marks1=int(input("Enter your marks1:"))
           
subject2=input("Enter 2nd subject name:")
marks2=int(input("Enter your marks2:"))

subject3=input("Enter 3rd subject name:")
marks3=int(input("Enter your marks3:"))
'''
# calculate total and average
'''
total = marks1 + marks2 + marks3
average=total/3
'''
# Decide Grade

if average >= 90:
    grade="A"
elif average >= 75:
    grade="B"
elif average >= 60:
    grade="C"
elif average >= 40:
    grade="D"
else:
    grade="fail"

print("\n-------------------result---------------------")

print(f"{subject1}:{marks1}")
print(f"{subject2}:{marks2}")
print(f"{subject3}:{marks3}")
print(f"Total Marks:{total}")
print(f"Average Marks:{average}")
print(f"Grade:{Grade}")























        
