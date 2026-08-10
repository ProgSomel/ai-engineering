#Password Retry System(while loop)
password = "somel"
tried = 3
while tried > 0:
    yourPass = input("Enter your pass: ")
    if yourPass == password:
        print("Password matched")
        break
    tried -= 1
    if tried == 0:
        print("Tried multiple times. Account is locked")
