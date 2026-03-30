#Functions
# Basic function
# def greet(name):
#     return f"Hello,{name}!"

# result = greet("Arya")     # => "Hello, Arya!"

# # Default arguments
# def greet(name, greeting="Hello"):
#     return f"{greeting},{name}!"

# greet("Arya")              # => "Hello, Arya!"
# greet("Arya", "Namaste")   # => "Namaste, Arya!"

# # Returning multiple values
# def min_max(nums):
#     return min(nums), max(nums)

# lo, hi = min_max([3, 1, 7, 2])   # lo=1, hi=7

# # Functions are just values — you can pass them around
# def apply(func, value):
#     return func(value)

# apply(len, "hello")    # => 5

# # IMPORTANT: if you don't return anything, function returns None
# def no_return(x):
#     x + 1           # calculates but doesn't return!

# result = no_return(5)   # result is None

#Practice: Write a function is_palindrome(s) that returns True/False. 
# Write a function two_sum(nums, target) that returns indices of two numbers that add up to target.
def is_palindromes (word):
    if (word == word[::-1]):
        return "word is palindrome"
    else:
        return "not a palindrome"
    
def is_palindromes(word):
    return word == word[::-1] 
print(f"check - {is_palindromes("aryafudke")}")

def is_palindrome(word):
    return word == word[::-1] 

nums = [3, 2, 4]
target = 6
def two_sums(nums, target):
    for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums):
            if (i != j and target == num1 + num2):
                return i, j 
    
print(two_sums(nums, target))

#Enumerate()
#Practice: Given a list of names, print each with its position: “1. Arya”, “2. Pawan”, etc.
names = ["Arya", "Pawan", "Rohan", "Priya"]
for i, names in enumerate(names, start=1):
    print(i,names)

#frequecy pattern 
#Find the first non-repeating character in “aabbcdd” using this pattern.
word = "aabbcdd"
def count_non_repeating(items):
    counts = {}
    for item in items:
        counts[item] = counts.get(item,0) + 1
    for item in items:
        if counts[item] == 1:
            return item

print(f"output -- {count_non_repeating(word)}")