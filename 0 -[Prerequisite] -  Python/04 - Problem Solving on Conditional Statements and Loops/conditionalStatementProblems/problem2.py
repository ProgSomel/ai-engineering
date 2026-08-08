# Quadrant Identifier
x = int(input("Enter x coordinate: "))
y = int(input("Enter y coordinate: "))

if x > 0:
    if y > 0:
        print("1st")
    else:
        print("4th")
if x < 0:
    if y < 0:
        print("3rd")
    else:
        print("2nd")