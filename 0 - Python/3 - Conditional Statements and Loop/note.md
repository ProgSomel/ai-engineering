# Python Loop
## range()
![range()](image.png)
### Example 1:
```python  
for num in range(1):
    print(num)
```
![output](image-1.png)
--------------------------------------------
### Example 2:
```python
for num in range(5):
    print(num)
```
![output](image-2.png)
--------------------------------------------
### Example 3:
```python
for num in range(1, 12, 2):
    print(num)
```
![output](image-3.png)
--------------------------------------------
### Example 4:
```python
for num in range(1, 12, 2):
    if num == 5:
        continue #skip for the value 5
    print(num)
```
![output](image-5.png)
--------------------------------------------
### Example 5:
```python
for num in range(1, 12, 2):
    if num == 5:
        break #loop stop at value 5
    print(num)
```
![output](image-6.png)
-------------------------------------------
### Example 6:
```python
#1+2+3+4+....+n
n = int(input("Enter a number: "))
total = 0
for num in range(1, n+1):
    total += num

print(total)
```
![output](image-7.png)
-------------------------------------------
### Example 7:
```python
#Multiplication Table
n = int(input("Enter a number: "))
for num in range(1, 11):
    print(f"{n} X {num} = {n*num}")
```
![output](image-10.png)


## while loop
### Example 1:
```python
num = 1
while num <= 11:
    print(num)
    num += 1
```
![output](image-4.png)
------------------------------------------
### Example 2:
```python
#1+2+3+4+....+n
n = int(input("Enter a number: "))
num = 1
total = 0
while num <= n:
    total+=num
    num+=1

print(total)
```
![output](image-8.png)
-----------------------------------------
### Example 3:
#### Factorial
```python
#1+2+3+4+....+n
n = int(input("Enter a number: "))
num = 1
total = 1
while num <= n:
    total*=num
    num+=1

print(total)
```
![output](image-9.png)