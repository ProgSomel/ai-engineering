#Number Reverser
num = int(input("Enter a Number: "))
while num > 0:
    print(num%10, end="")
    num //= 10
print()