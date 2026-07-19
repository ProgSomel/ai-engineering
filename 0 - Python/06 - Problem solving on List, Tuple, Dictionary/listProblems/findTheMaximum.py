numbers = [7, 2, 9, 4, 1, 5]
max_element = numbers[0]

for num in numbers:
    if num > max_element:
        max_element = num
print(max_element)