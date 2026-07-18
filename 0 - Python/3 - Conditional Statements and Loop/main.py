#1+2+3+4+....+n
n = int(input("Enter a number: "))
num = 1
total = 1
while num <= n:
    total*=num
    num+=1

print(total)

