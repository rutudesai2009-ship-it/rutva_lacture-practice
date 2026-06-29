# python operators , variables and data Types

'''
1.Arithmetic operator
2.Assignment operator
3.Comparison operator
4.Logical operator
5.Bitwise operator
6.Type conversion
'''

a=10
b=2

print('addition:',a+b)
print('substraction:',a-b)
print('multiplication:',a*b)
print('Division:',a/b)
print('Modulus:',a%b)
print('Exponentiation:',a**b)
print('floor DIvision:',a//b)

# Assignment Operattor

x=5 # simple assignment

y=3

x+=y # x=x+y

print(x)
print(y)

x-=y

print(x)
print(y)

x/=y

print(x)
print(y)

x%=y

print(x)
print(y)

x**=y

print(x)
print(y)

x//=y

print(x)
print(y)

# comparision operator

x=10
y=20

print(x==y)
print(x!=y)
print(x<y)
print(x<=y)
print(x>y)
print(x>=y)
x=y

print(x)

# LOgical operator (and,or,not)

x=True
y=False
z=False

print(x and y)
print(y and z)
print(x or y)
print(y or z)
print(not x)
print(not y)

# Type conversion

'''
int()
float()
str()
tuple()
list()
set()
dict()
'''

num_str="123"
print(type(num_str))

num_int=int(num_str)

print(type(num_int))
print(num_int + 7)


# multiple assignment

x,y,z=10,20,30

print(x,y,z)

a=20
b=20

print(id(a))
print(id(b))








































