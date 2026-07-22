# List, Tuple, Dictionary and String

## Python List
![List](images/image.png)
### Example 1
```python
num = [1, 2, 3, 4, 5, 6, 7]
print(num)
print(num[4])
```
![output](images/image-1.png)
-----------------------------------
### Example 2
```python
num = [1, 2, 3, 4, 5, 6, 7]
print(num)
print(num[-4])
```
![output](images/image-2.png)
-----------------------------------
### Example 3
```python
#slicing
num = [1, 2, 3, 4, 5, 6, 7]
print(num[1:4])
```
![output](images/image-3.png)
----------------------------------
### Example 4
```python
#slicing
num = [1, 2, 3, 4, 5, 6, 7]
print(num)
print(num[1:])
```
![output](images/image-4.png)
----------------------------------
### Example 5
```python
#slicing
num = [1, 2, 3, 4, 5, 6, 7]
print(num)
print(num[:])
```
![output](images/image-5.png)
----------------------------------
### Example 6
```python
#slicing
num = [1, 2, 3, 4, 5, 6, 7]
print(num)
print(num[:4])
```
![output](images/image-6.png)
----------------------------------
### Example 7 -> appending at last-> .append(value)
```python
#adding element to list -> .appent()
num = [1, 2, 3, 4, 5, 6, 7]
print(num)
num.append(15)
print(num)
```
![output](images/image-7.png)
-----------------------------------
### Example 8 -> adding Element at specific position -> .insert(pos, val)
```python
#adding element to list
num = [1, 2, 3, 4, 5, 6, 7]
print(num)
num.insert(4, 100)
print(num)
```
![output](images/image-8.png)
----------------------------------
### Example 9 -> removing an element from the list -> .remove(valueToRemove)
```python
#deleting element from list
num = [1, 2, 3, 4, 5, 6, 7]
print(num)
num.remove(4)
print(num)
```
![output](images/image-9.png)
----------------------------------
### Example 10 -> deleting value using index number -> del array[index]
```python
#deleting element from list
num = [1, 2, 3, 4, 5, 6, 7]
print(num)
del num[5]
print(num)
```
![output](images/image-10.png)
----------------------------------
### Example 11 -> usage of membership operator in list
```python
num = [1, 2, 3, 4, 5, 6, 7]
print(5 in num)
print(100 in num)
```
![output](images/image-11.png)
----------------------------------
### Example 12 -> finding length of list
```python
num = [1, 2, 3, 4, 5, 6, 7]
print(len(num))
```
![output](images/image-12.png)
----------------------------------
### Example 13 -> list comprehensive
```python
list = [n**2 for n in range(1, 101)]
print(list)
```
![output](images/image-13.png)
---------------------------------

## Python Tuple -> it can not be changed after build
![Python Tuple](images/image-14.png)
![Tuple or List](images/image-15.png)
----------------------------------

## Python Dictionary
![python Dictionary](images/image-16.png)
----------------------------------

## Python Strings
![strings](images/image-17.png)
------------------------------------------------

## Python set
![Python set](image.png)
------------------------------------------------
![Basic set operations](image-1.png)
------------------------------------------------
![Examples](image-2.png)