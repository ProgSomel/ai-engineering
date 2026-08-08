num = int(input("Enter the Number: "))

numberOfDigits = 0;
temp = num

while temp > 0:
    numberOfDigits+=1
    temp//=10

total = 0
temp = num

for n in range(numberOfDigits):
    total+=(temp%10)**numberOfDigits
    temp //=10
    
if total == num:
    print("Armstrong")
else:
    print("Not Armstrong")
