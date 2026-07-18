# sum of digits
#6381
num = 6381
sum = 0
while num > 0:
    sum += (num %10)
    num //= 10
print(sum)