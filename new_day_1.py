### Variables, Data type, Operators, foe loops, while loops, if else

# TOPICS - Variables & Data type + Print and f strings
# create 5 varibales of diff types, print each with type()
name = "Arya Fudke"
age = 24
salary = 100000.00
is_working = True 
middle_name = None 

print (type(name))
print (type(age))
print (type(salary))
print (type(is_working))
print (type(middle_name))
print(f"My name is {name} and I am {age} years old, i earn {salary} per month")
# twist part

fav_food = "Sushi"
price = 500.50
print(f"My fav food is {fav_food}, which costs arround {price}rs")
print(f"string - {type(fav_food)}, int - {type(age)}, decimal - {type(price)}, boolean - {type(is_working)}, none - {type(middle_name)}")

# TOPIC - Arithmetic & Comparison operators
# Q - Check if a number is even using %. Check if a number is between 10 and 100 using and.
x = 12
print(x%2 == 0)
print(x>10 and x<100)

# Topic if/elif/else
score = 75 
if (score >= 90):
    print("A grade...yeppy")
elif score >= 70:
    print("B grade...keep going")
elif score >= 50:
    print("C grade... need more practice")
else:
    print("Fail... boo")

# challenge 1 
x = 101
if (x%3 == 0 and x%5 ==0):
    print("fizzbuzz")
elif (x%3 ==0):
    print("Fizz")
elif (x%5 == 0):
    print ("Buzz")
else :
    print(x)
    
# practice task 
num = 5 
if num > 0:
    print("positive")
elif num < 0 :
    print("negative")
else :
    print("zero")

# loops 
for fruit in ["apple", "banana", "mango"]:
    print(fruit)

# Loop with range
for i in range(5):         
    print(i)

for i in range(2, 8):       
    print(i)

for i in range(0, 10, 2):   
    print(i)

# break = stop the loop entirely
for i in range(100):
    if i == 5:
        break               

# continue = skip this iteration, go to next
for i in range(10):
    if i % 2 == 0:
        continue             
    print(i)    
    
#practice task: Print all numbers from 1 to 50 that are divisible by 7.
for i in range(1, 51):
    if i % 7 == 0:
        print(i)
for i in range(7, 51, 7):  
    print(i)       

# while loops 
count = 0
while count < 5:
    print(count)
    count += 1       # without this = infinite loop

# while with break
while True:
    user_input = input("Type 'quit' to exit: ")
    if user_input == "quit":
        break

# practice task : Write a while loop that doubles a number starting from 1 until it exceeds 1000. Print each step.
num = 1
while num <1000:
    print(num)
    num = num*2
    
