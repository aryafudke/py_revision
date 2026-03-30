## LISTS

# # Creating
# nums = [10, 20, 30, 40, 50]
# empty = []

# # Accessing 
# nums[0]       # => 10 (first)
# nums[-1]      # => 50 (last)
# nums[-2]      # => 40 (second from end)

# # Modifying
# nums.append(60)        # add to end → [10, 20, 30, 40, 50, 60]
# nums.insert(1, 15)     # insert 15 at index 1
# nums.pop()             # remove & return last → 60
# nums.pop(2)            # remove & return item at index 2
# nums.remove(20)        # remove first occurrence of value 20
# del nums[0]            # delete by index

# # Slicing — THIS IS IMPORTANT FOR DSA
# nums = [10, 20, 30, 40, 50]
# nums[1:3]     # => [20, 30]       (index 1 to 2, end excluded)
# nums[:3]      # => [10, 20, 30]   (start to index 2)
# nums[2:]      # => [30, 40, 50]   (index 2 to end)
# nums[::-1]    # => [50, 40, 30, 20, 10]  (REVERSED — used ALL the time)
# nums[::2]     # => [10, 30, 50]   (every 2nd element)

# # Length
# len(nums)     # => 5

# # Check if something exists
# 30 in nums    # => True
# 99 in nums    # => False

# # Sorting
# nums.sort()                    # sorts in place (modifies original)
# sorted(nums)                   # returns new sorted list (original unchanged)
# nums.sort(reverse=True)        # descending sort
# sorted(nums, key=lambda x: -x)  # same thing with sorted()

# # Sorting with custom key — VERY COMMON IN DSA
# pairs = [(1, 3), (2, 1), (4, 2)]
# pairs.sort(key=lambda x: x[1])   # sort by second element
# # => [(2, 1), (4, 2), (1, 3)]

# # Useful built-ins
# min(nums)        # smallest
# max(nums)        # largest
# sum(nums)        # total

##Task - Given [3, 1, 4, 1, 5, 9, 2, 6] — sort it, reverse it, find min/max/sum, slice first 3 elements.

list_1 = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"sort - {sorted(list_1)}")
print(f"reverse - {sorted(list_1,reverse=True)}")
print(f"reverse - {list_1[::-1]}")
print(f"min - {min(list_1)}")
print(f"max - {max(list_1)}")
print(f"sums - {sum(list_1)}")
print(f"first 3 elements - {list_1[:3]}")

## STRINGS
# s = "Hello World"

# # Indexing & slicing (same as lists)
# s[0]        # => 'H'
# s[-1]       # => 'd'
# s[0:5]      # => 'Hello'
# s[::-1]     # => 'dlroW olleH' (reverse — common DSA trick)

# # Length
# len(s)      # => 11

# # The methods you'll actually use
# s.lower()              # => 'hello world'
# s.upper()              # => 'HELLO WORLD'
# s.strip()              # removes leading/trailing whitespace
# s.split(" ")           # => ['Hello', 'World'] — splits string into a list
# " ".join(['a', 'b'])   # => 'a b' — joins a list into a string
# "lo" in s              # => True (check if substring exists)

# # IMPORTANT: strings are IMMUTABLE — you CANNOT do this:
# s[0] = "h"    # ERROR!
# # Instead you create a new string:
# s = "h" + s[1:]    # => 'hello World'

#Task - Take “racecar”, check if it equals its reverse (palindrome check). Split “apple,banana,mango” by comma into a list.

str = "racecar"

if(str == str[::-1]):
    print ("str is Palindrome")
else:
    print("not a palindrome")

str_2 = "apple,banana,mango"
str_3 = str_2.split(",")
print(str_3)

## DICTIONARY

# # Creating
# d = {}
# d = {"name": "Arya", "age": 24, "city": "Mumbai"}

# # Accessing
# d["name"]           # => "Arya"
# d["salary"]         # => KeyError! (key doesn't exist)
# d.get("salary")     # => None (safe way — no error)
# d.get("salary", 0)  # => 0 (returns this default if key not found)

# # Adding / Updating
# d["salary"] = 50000     # adds new key
# d["age"] = 25           # updates existing key

# # Deleting
# del d["city"]           # removes key "city"

# # Checking if key exists
# "name" in d        # => True
# "phone" in d       # => False


# ##looping 
# user = {"name": "Arya", "age": 24, "city": "Mumbai"}

# # Loop 1: just the keys (this is the default)
# for key in user:
#     print(key)
# # Output:
# #   name
# #   age
# #   city

# # Loop 2: keys AND values together (use .items())
# for key, value in user.items():
#     print(f"{key} ={value}")
# # Output:
# #   name = Arya
# #   age = 24
# #   city = Mumbai
# # Explanation: .items() gives you pairs like ("name", "Arya"), ("age", 24), etc.
# # The `key, value` unpacks each pair into two variables.

# # Loop 3: just the values
# for value in user.values():
#     print(value)
# # Output:
# #   Arya
# #   24
# #   Mumbai

# #THE DSA PATTERN — frequency counter (memorize)
# nums = [1, 2, 2, 3, 3, 3, 4]
# counts = {}

# for n in nums:
#     # .get(n, 0) means: "give me the current count of n, or 0 if n hasn't been seen yet"
#     current_count = counts.get(n, 0)
#     counts[n] = current_count + 1

# print(counts)
# # => {1: 1, 2: 2, 3: 3, 4: 1}
# #
# # What happened step by step:
# #   n=1 → counts.get(1, 0) = 0 → counts[1] = 0 + 1 = 1
# #   n=2 → counts.get(2, 0) = 0 → counts[2] = 0 + 1 = 1
# #   n=2 → counts.get(2, 0) = 1 → counts[2] = 1 + 1 = 2
# #   n=3 → counts.get(3, 0) = 0 → counts[3] = 0 + 1 = 1
# #   n=3 → counts.get(3, 0) = 1 → counts[3] = 1 + 1 = 2
# #   n=3 → counts.get(3, 0) = 2 → counts[3] = 2 + 1 = 3
# #   n=4 → counts.get(4, 0) = 0 → counts[4] = 0 + 1 = 1

# # ONE-LINE VERSION (same thing, just shorter):
# # counts[n] = counts.get(n, 0) + 1


#Task -  Count the frequency of each character in “abracadabra” using the frequency counter pattern.
word = "abracadabra"
counts = {}

for i in word :
    current_word = counts.get(i, 0)
    counts[i] = current_word + 1
    print(counts)

#max number of counts
most_common = max(counts,key=counts.get)
print(most_common)

##SETS
# Creating
# s = set()
# s = {1, 2, 3, 4, 5}

# # From a list (removes duplicates!)
# nums = [1, 2, 2, 3, 3]
# unique = set(nums)       # => {1, 2, 3}

# # Adding / Removing
# s.add(6)          # adds 6
# s.add(3)          # does nothing, already exists
# s.remove(2)       # removes 2, KeyError if not found
# s.discard(99)     # removes if exists, NO error if not found

# # THE POWER — O(1) membership check
# # List: 1 in [1,2,3,4,5] → scans all elements, O(n)
# # Set:  1 in {1,2,3,4,5} → instant lookup, O(1)

# # Set operations
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# a & b       # => {3, 4}         intersection (common elements)
# a | b       # => {1, 2, 3, 4, 5, 6}  union (all elements)
# a - b       # => {1, 2}         difference (in a but not b)
# a ^ b       # => {1, 2, 5, 6}   symmetric difference (in one but not both)

# # DSA PATTERN — "has this been seen before?"
# seen = set()
# for num in [1, 3, 5, 3, 1, 7]:
#     if num in seen:
#         print(f"{num} is a duplicate!")
#     seen.add(num)

#Practice: Given two lists [1,2,3,4,5] and [4,5,6,7,8], find common elements using sets.
a = [1,2,3,4,5]
b = [4,5,6,7,8]

c = set(a)
d = set(b)
print (c&d)
print(set(a) & set(b))
print(set(a) | set(b))
print(set(a) - set(b))

#TUPLES 
# t = (1, 2, 3)
# t[0]       # => 1 (access like a list)
# t[0] = 99  # ERROR! Can't modify.

# THE SWAP TRICK — used constantly in DSA
a = 1
b = 2
a, b = b, a    # now a=2, b=1 — no temp variable needed!
print(a, b)