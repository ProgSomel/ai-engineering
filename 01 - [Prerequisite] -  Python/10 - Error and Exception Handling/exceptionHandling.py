# finally -> cleanup
file = None

try:
    file = open("output.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not Found")
finally:
    if file:
        file.close()