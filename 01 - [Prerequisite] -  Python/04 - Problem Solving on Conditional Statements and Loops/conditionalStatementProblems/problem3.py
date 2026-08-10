# Age Classifier
age = int(input("Enter age: "))
if age >= 20:
    print("adult")
elif age >= 13:
    print("teenager") 
elif age >= 4:
    print("child")
elif age >= 2:
    print("toddler")
else:
    print("infant")