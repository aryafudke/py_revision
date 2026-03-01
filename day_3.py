#tuples - are like list but cant be changed 

person = ("Arya", 24, "Mumbai")

print(person)
print(person[-1])   

#assigns 
name, age, city = person
print(name)
print(age)
print(city)

#swapping variables 
a = 0
b = 3
temp = a
a = b
b = temp

# in tuples swapping 
a = "hello"
b = "world"

a, b = b, a   # swap in ONE line!

print(a)  
print(b)   


### Dictionary - key value pair

person = {
    "name": "Arya",
    "age": 24,
    "city": "Mumbai"
}

print(person["name"])

## Dictionary Operations 

# add new key 
person["email"] = "aryafudke@gmail.com"
print(person)

# update existing key
person["age"] = 25
print(person["age"])

# delete a key 
del person["city"]
print(person)

#checking
print("name" in person)

# a key can have None as a value
person["phone"] = None

## methods
print(person.keys())     # all keys
print(person.values())   # all values
print(person.items())    # both together

#nested dictionary
students = {
    "Arya": {
        "age": 24,
        "grade": "A",
        "city": "Mumbai"
    },
    "Rahul": {
        "age": 22,
        "grade": "B",
        "city": "Delhi"
    }
}

print(students["Arya"]["grade"])   
print(students["Rahul"]["city"]) 