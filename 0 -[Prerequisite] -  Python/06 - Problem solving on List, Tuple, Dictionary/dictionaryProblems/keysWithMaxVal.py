scores = {'Alice': 90, 'Bob': 85, 'Charlie': 90, 'David': 88}
max_value = max(scores.values())
max_keys = [key for key, value in scores.items() if value == max_value]
print(max_keys)
