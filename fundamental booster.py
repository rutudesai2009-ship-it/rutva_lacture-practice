# Fndamental Booster - Interactive Personal Data Collecter

# ========== Welcome section ========

print (" weclome to the interactive personal data collecter!")

print ("\n this will collect your personal information.")

print ("\n perform some calculation , and show you data type detalis.")

print ("\n let's get started!!!")

# ========Collect Information Section ============

print ("_"* 50)

name = input (" please enter your name:")

age_str = input (" please enter your age:")

age = int (age_str)

height_str = input("please enter your height in meters:")

height = float (height_str)

fav_num_str = input (" please enter your favourit numbers:")

fav_num = input ( fav_num_str)

# ============data processing============

print ("\n" + "=" * 50 )

print (" processing ypur data ...........")

print ("="* 50)

# calculate birth year

cur_year_age = 2026

birth_year = cur_year_age - age

print (" birth_year", birth_year)

# calculate height to centimeter

height_cm = height*100

# perform same arithmetic operation

sum_value =age * fav_num

product_value = age * fav_num

# type conversion

height_as_int = int (height)

age_as_float = float (age)

age_as_string = str(age)

# display result

print ("\n" + "="*50)

print (" thank you ! you here is the information we collectes:")

print ("="* 50 )

# display each variable with its type and memory address

print (f"\n varible details:")

print (f"name:{name} -> type:{type(name)} -> address:{id(name)}")

print (f"age:{age} -> type:{type(age)} -> address:{id(age)}")

print (f"height:{height} -> type:{type(height)} -> address:{id(height)}")

print (f"favourite number:{fav_num}-> type:{type(fav_num)}-> address:{id(fav_num)}")


# ====== display conversion ========

print ("="* 50)

print ("type conversion")

print ("=" *50 )

print ("\n height as integer :{ height_as_int} -> type:{type(height_as_int)}")

print ("\n age as float :{age_as_float} -> type:{type(age_as_float)}")

print (f"\n age as string: {age_as_string} -> type:{type(age_as_string)}")

# ========= display operation =========

print ("="* 50)

print (" caculated result:")

print ("="*50)

print ( f"\n your height in centimeter:{height_cm}cm")

print (f"approximately ! your birth year:{birth_year}")

print (f"\n product of your age and favourite number :{product_value}")

# string concation

greeting = " hello , " + name +"!"

message = f" your favourite number is (fav_num)"

print (f" -> '{ greeting }'")

print ( f" -> type :{ type ( greeting )}")

print (f" -> address : {id(greeting)}")

print (f" -> '{ message}'")

print (f" -> type : {id(message)}")

# ============summry table =============

print ("=" * 50)

print (" summary table:")

print ("="* 50)

print (f"\n {'variable' : <20}{'value': <20}{'type': <25}{'id': <15}")

print(f"\n {'name':<20} {str(name):<20} {str(type(name)):<25} {id(name):<15}")
# ========= closing meassage============

print ("="*50)

print (" thank you for using the personal data collecter!!")

print ("=" * 50 )

print ("\n you've successfully exolre:")

print ("\n input () and print() function")

print ("\n  string , integer and float data types")

print ("\n atrithmetic operation (+,_,*,/)")

print ("typr () and id() built_in functions")

print (" string concatination")

print ("type casting")

print ("+"*50)






























      


      


