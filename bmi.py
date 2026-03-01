weight = float(input("Enter the weight in kg:"))
height = float(input("Enter the height in meter:"))

bmi = weight/(height ** 2)
print(f"BMI  = {bmi:.2f}")
print(f"Healthy weight: {18.5 <= bmi<= 24.9}")
