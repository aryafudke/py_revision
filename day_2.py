#list - an ordered collection
fruits = ["apple", "banana","mango"]

print(fruits)
print(fruits[0])    # first item
print(fruits[-1])   # last item 

#list operations 

# add = append() 
fruits.append("kiwi")
print(fruits)

#delete = remove()
fruits.remove("banana")
print(fruits)
#remove("nail paint") → remove by value (what it is)
#pop(0) → remove by position (where it is)
print(len(fruits)) 

#insert at position 1
fruits.insert(1, "grapes")    
print(fruits)

#slicing 

numbers = [10,20,30,40,50]

print(numbers[1:3]) #20,30
print(numbers[:2]) #10,20
print(numbers[2:]) #30,40,50
print(numbers[::-1])  #50,40,30,20,10

# list methods
nums = [3,1,4,1,5,9,2,6]

print(nums.count(1)) #how many times 1 appears
print(nums.index(5)) #position of 5
nums.sort() # sort the list
print(nums)
nums.reverse() # reverse it 
print(nums)
print(1 in nums) # check if 1 is in list

