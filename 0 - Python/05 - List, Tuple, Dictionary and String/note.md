# List, Tuple, Dictionary and String

## Python List
![List](image.png)
### Example 1
```python
num = [1, 2, 3, 4, 5, 6, 7]
print(num)
print(num[4])
```
![output](image-1.png)
-----------------------------------
### Example 2
```python
num = [1, 2, 3, 4, 5, 6, 7]
print(num)
print(num[-4])
```
![output](image-2.png)
-----------------------------------
### Example 3
```python
#slicing
num = [1, 2, 3, 4, 5, 6, 7]
print(num[1:4])
```
![output](image-3.png)
----------------------------------
### Example 4
```python
#slicing
num = [1, 2, 3, 4, 5, 6, 7]
print(num)
print(num[1:])
```
![output](image-4.png)
----------------------------------
### Example 5
```python
#slicing
num = [1, 2, 3, 4, 5, 6, 7]
print(num)
print(num[:])
```
![output](image-5.png)
----------------------------------
### Example 6
```python
#slicing
num = [1, 2, 3, 4, 5, 6, 7]
print(num)
print(num[:4])
```
![output](image-6.png)
----------------------------------
### Example 7 -> appending at last-> .append(value)
```python
#adding element to list -> .appent()
num = [1, 2, 3, 4, 5, 6, 7]
print(num)
num.append(15)
print(num)
```
![output](image-7.png)
-----------------------------------
### Example 8 -> adding Element at specific position -> .insert(pos, val)
```python
#adding element to list
num = [1, 2, 3, 4, 5, 6, 7]
print(num)
num.insert(4, 100)
print(num)
```
![output](image-8.png)
----------------------------------
### Example 9 -> removing an element from the list -> .remove(valueToRemove)
```python
#deleting element from list
num = [1, 2, 3, 4, 5, 6, 7]
print(num)
num.remove(4)
print(num)
```
![output](image-9.png)
----------------------------------
### Example 10 -> deleting value using index number -> del array[index]
```python
#deleting element from list
num = [1, 2, 3, 4, 5, 6, 7]
print(num)
del num[5]
print(num)
```
![output](image-10.png)
----------------------------------
### Example 11 -> usage of membership operator in list
```python
num = [1, 2, 3, 4, 5, 6, 7]
print(5 in num)
print(100 in num)
```
![output](image-11.png)
----------------------------------
### Example 12 -> finding length of list
```python
num = [1, 2, 3, 4, 5, 6, 7]
print(len(num))
```
![output](image-12.png)
----------------------------------
### Example 13 -> list comprehensive
```python
list = [n**2 for n in range(1, 101)]
print(list)
```
![output](image-13.png)
---------------------------------

## Python Tuple -> it can not be changed after build
![Python Tuple](image-14.png)
![Tuple or List](image-15.png)
----------------------------------

## Python Dictionary
![python Dictionary](image-16.png)
----------------------------------

## Python Strings
![strings](image-17.png)