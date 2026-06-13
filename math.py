# Python Module & Function

# 1.MATH Modul

# math module is used for mathemetical calculation

print("\n========Math Module========")

import math

# 1.sqrt()

# sqrt() is used to find the square root of a number.

# syntax
# math.sqrt(number)

number=36

result=math.sqrt(number)

print("Squre Root of",number,"=",result)

# 2.pow()

# pow() is used to calculate power.

base=2
power=5

result=math.pow(base,power)

print(base,"power","=",result)

# 3.ceil()

# ceil()rounds the number up to nearest integer.

number=4.2
result=math.ceil(number)

print(result)

# 4.floor()

# floor () rounds the number Down to nearest integer.

number=4.9

result=math.floor(number)

print(result)

#5. factorial()

# factorial()calculate fectorial of a number

number=5

result=math.factorial(number)

print(result)

# 6.gcd()

# gcd()find Greatest common dividor

num1=12
num2=18

result=math.gcd(num1,num2)

# 12:1,2,3,4,6,12
# 18:1,2,3,6,9,18

# 7.sin()

# sin()

result=math.sin(0)

print(result)

# 8.cos()

# cos()calculate cosine value

result=math.cos(0)

print(result)

# 9.tan()

# tan() calculate tengent value

result=math.tan(1)

print(result)

# 10.log()

# log()calculate logarithm value

number=10

result=math.log(number)

print(result)

# 11.pi

print(math.pi)

# 12. e

# math.e gives Euler's number

print(math.e)

# 2. RSNDOM Modulel

# random module is used to generate random lalues.

# It is useful for games,OTP generation,password gemeration

# random selection , ane many more applications.

import random

print("\n==========Random Module==========")


# 1.randint()

# randit() genererate a random integer between tow numbers.

# random.randint(start.end)

result=random.randint(1,10)

print(result)

# 2.random()

# random () generate a random float number
# between 0 to 1

# random.random()

result=random.random()
print(math.floor(result*10000))

# 3. choice()

# choice () selects a random item from a list

# random.choice()

colors=["Blue","Orange","Red","Yellow"]

result=random.choice(colors)

print(result)

# 4.shuffle()

# shuffle () mixes the element of a list

# random.shuffle()

numbers=[1,2,3,4,5,6]

print(numbers)

random.shuffle(numbers)

print(numbers)

# 5.uniform()

# uniform()generate a random decimal number.

# between tow value

# random.uniform (start,end)

result=random.uniform(1,100)

print(result)

# 6. randrange()

# randrange () generate a random number

# from a given range

# random.randrange (start,stop,step)

result=random.randrange(1,20,2)

print(result)

# 7. sample()

# sample () selects multiple unique random items.

# random.sample(list,count)

numbers=[10,20,30,40]

result=random.sample(numbers,2)

print(result)

# 3.UUID module

# uuid()generate aunique ID
#uuid1()generate uniaue multiple ID
# using current time and IP/MAC address.

#uuid.uuid1()

print("\n ==========UUID Module==========")
import uuid

result = uuid.uuid1()

print(result)

# uuid4()

# uuid4()generate a random unique ID

result=uuid.uuid4()

print(result)

# uuid3()

# uuid3()generate with Namespace,Name

# It uses  MD5 hasing

result = uuid.uuid3(uuid.NAMESPACE_DNS , "example.com")

print(result)

# uuid5()

# uuid5()

result = uuid.uuid5(uuid.NAMESPACE_DNS , "example.com")

print(result)

























        



  




















