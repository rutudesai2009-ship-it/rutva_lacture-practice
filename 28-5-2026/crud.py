# CRUD operation in python
# C=Create
# R=Read
# U=Update
# D=Deleten

# Empty List

users = []

# CREATE
'''
users1 = {
    'id' : 1,
    'name' : 'Alice',
    'email' : 'alice@gmail.com'
    }

users2 = {
    'id' : 2,
    'name' : 'Zeel',
    'email' : 'zeel@gmail.com'
    }

users3 = {
    'id' : 3,
    'name' : 'karan',
    'email' : 'karan@gmail.com'
    }

# add users

users.append(users1)
users.append(users2)
users.append(users3)

print("users added successfully!")

# Read

print("\n All users:")

for user in users:
    print(user)
    
# search

search_id = 2

print("\n Searching User:")

for user in users :

    if user['id']==search_id :
        print ("User Found :",users )

# UPDATE

print("\n Updating User Email....")

for users in user:

    if user['id']==2:
        user['email']='zeel@example.com'

print("User Updated:")

#DELETE
'''
print("\n Deleting user....")

for user in users:

    if user ['id'] == 1:
           users.remove(user)
           break

print("User Deleted!")

'''
'''
# count users

print ("\n Total Users:",len(users))

# check emailexists

check_email = 'zeel@example.com'

found=False

for user in users:

    if user['email'] == check_email:
        found=True

if found:
    print("Email Exists")
else:
    print("Email not found")

# sort user by name

sorted_users=sorted(users,key=lambda x:x['name'])

print ('\n Sorted Users:')

for user in sorted_users:
    print(user)

#Final User List

print("\n====== Final Ussers ======") 

for user in users:

    print(f'''''
ID : {user['id']}
Name : {user['name']}
Email:{user['email']}
''''')

# Type casting constructor

# list()--->tuple()

a=[1,2,3,4]

b=tuple(a)

c=set(a)

print(b)

print(c)

# del keyword

# Used to delet variables,list element,disctionary keys , ect......

x = [10,20,30]

del x[1]

print(x)

person={'name':'vishva','age':30}

del person ['age']

print(person)

print(x)



    


    
