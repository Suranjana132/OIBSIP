print("===== BMI CALCULATOR =====")

weight = float(input("Enter your weight in kilograms: "))
print("If you don't know your height in meters, enter it in feet.")

height_feet = float(input("Enter your height in feet: "))

# Convertion
height_m = (height_feet * 12 * 2.54) / 100
print(f"Your height in meters is: {height_m:.2f}")

#BMI formula
bmi = weight / (height_m ** 2)

# Category
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal Weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print("\n----- BMI RESULT -----")
print(f"Your BMI is: {bmi:.2f}")
print(f"Category: {category}")
