temp = float(input("Enter temperature: "))

if temp > 0:
    far = (temp *(9/5))+32
    print(f"{far}F")
else:
    print(f"{temp + 273.15}K")