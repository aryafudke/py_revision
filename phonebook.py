phonebook = {}
name = input("Enter name: ")
number = input("Enter number: ")
phonebook[name] = number
name = input("Enter name: ")
number = input("Enter number: ")
phonebook[name] = number
name = input("Enter name: ")
number = input("Enter number: ")
phonebook[name] = number

print(phonebook)

name = input("Search for a phone number: ")
result = phonebook.get(name)
if result:
    print(result)
else:
    print("Contact not found!")