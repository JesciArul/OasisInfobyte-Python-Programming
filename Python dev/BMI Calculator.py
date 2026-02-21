weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)
print(f"Your BMI is {bmi:.2f}")

if bmi < 18.5:
    print("Underweight")
elif bmi < 24.9:
    print("Normal weight")
elif bmi < 29.9:
    print("Overweight")
else:
    print("Obese")
