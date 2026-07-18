#BMI Calculator
height = float(input("Enter person's height: "))
weight = float(input("Enter person's weight: "))

bmi = (weight)/(height*height)
print(f"Your BMI is: {bmi:.2f}")

if bmi >= 30:
    print("obese")
elif bmi >= 25:
    print("overweight")
elif bmi >= 18.5:
    print("normal")
else:
    print("underweight")