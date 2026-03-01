#build shopping list app

shopping = []
shopping.append(input("enter the 1 items:"))
shopping.append(input("enter the 2 items:"))
shopping.append(input("enter the 3 items:"))
print(f"Shopping list - {shopping}")

shopping.pop(0)
print(f"Updated Shopping list - {shopping}")