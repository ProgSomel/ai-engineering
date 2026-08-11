## Pickle
import pickle

with open("student.pkl", "rb") as file:
    data = pickle.load(file)
print(data)

