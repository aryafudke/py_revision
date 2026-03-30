#TRY/Except
#Write a function that takes two strings, converts them to ints, divides them, and handles both ValueError (bad input) and ZeroDivisionError.
def error_handling_function(str_1, str_2):
    try:
        x= int(str_1)
        y = int(str_2)
        divide_strs = x/y
        return divide_strs
    except (ValueError,ZeroDivisionError) as e:
         return f"Error: {e}"

print(error_handling_function("arya","pawan"))
print(error_handling_function("10", "2"))     
print(error_handling_function("10", "0"))      
print(error_handling_function("abc", "2"))   
print(error_handling_function("20", "4")) 


#CLASSES
#Practice: Create a BankAccount class with owner, balance, and methods deposit(amount) and withdraw(amount) that updates the balance.
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        
    def deposit_amount(self, amount):
        self.balance = self.balance + amount
        return self.balance
    
    def withdraw_amount(self,amount):
        self.balance = self.balance - amount
        return self.balance

account = BankAccount("Arya",50000)
account.deposit_amount(5555)
account.withdraw_amount(10000)
print(account.balance) 
print(account.name)  

#TYPE HINTS
def is_palindromes(word:str) -> bool:
    return word == word[::-1] 
print(f"check - {is_palindromes("aryafudke")}")

from typing import List, Tuple
nums = [3, 2, 4]
target = 6
def two_sums(nums: List[int], target: int) -> Tuple[int,int] :
    for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums):
            if (i != j and target == num1 + num2):
                return i, j 
    
print(two_sums(nums, target))
def add(x, y):
    return x + y 
from math_utils import add

print(add(4,5))