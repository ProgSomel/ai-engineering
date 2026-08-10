# 1 — Introduction to Python: I/O, Variables and Data Types

## What is a Data Type?

A data type specifies the kind of value a variable can hold. Python figures it
out automatically — you never declare it.

```python
num = 24
print(type(num))   # <class 'int'>
```

Use `type()` to check any value's type.

---

## The 8 Data Type Categories

| Category | Types |
|----------|-------|
| Numeric | `int`, `float`, `complex` |
| Text | `str` |
| Sequence | `list`, `tuple`, `range` |
| Mapping | `dict` |
| Set | `set`, `frozenset` |
| Boolean | `bool` |
| Binary | `bytes`, `bytearray`, `memoryview` |
| None | `NoneType` |

---

## 1. Numeric

```python
num1 = 5            # int   — whole number
num2 = 5.0          # float — decimal number
num3 = 3 + 4j       # complex — real + imaginary

print(type(num1))   # <class 'int'>
print(type(num2))   # <class 'float'>
print(type(num3))   # <class 'complex'>
```

---

## 2. String (Text)

```python
name = "Somel"
message = 'Hello, Python'
multiline = """This spans
multiple lines"""

print(type(name))     # <class 'str'>
print(len(name))      # 5
print(name[0])        # S
print(name[::-1])     # lemoS  (reversed)
```

Strings are **immutable** — you cannot change a character in place.

---

## 3. Sequence Types

### list — ordered, mutable

```python
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
fruits[0] = "orange"        # allowed

print(fruits)               # ['orange', 'banana', 'cherry', 'mango']
print(type(fruits))         # <class 'list'>
```

### tuple — ordered, immutable

```python
point = (10, 20)
colors = ("red", "green", "blue")
# point[0] = 99             # TypeError — cannot modify

print(point[0])             # 10
print(type(point))          # <class 'tuple'>
```

### range — sequence of numbers

```python
r = range(5)                # 0, 1, 2, 3, 4
print(list(range(2, 10, 2)))  # [2, 4, 6, 8]
print(type(r))              # <class 'range'>
```

---

## 4. Mapping — dict

Key–value pairs. Keys must be unique.

```python
person = {"name": "Somel", "age": 25, "city": "Dhaka"}

print(person["name"])       # Somel
print(person.keys())        # dict_keys(['name', 'age', 'city'])
print(person.values())      # dict_values(['Somel', 25, 'Dhaka'])
print(type(person))         # <class 'dict'>
```

---

## 5. Set Types

### set — unordered, unique, mutable

```python
numbers = {1, 2, 3, 3, 2}
print(numbers)              # {1, 2, 3}  duplicates removed

numbers.add(4)
print(type(numbers))        # <class 'set'>
```

### frozenset — unordered, unique, immutable

```python
fs = frozenset([1, 2, 3])
# fs.add(4)                 # AttributeError — cannot modify
print(type(fs))             # <class 'frozenset'>
```

---

## 6. Boolean

```python
is_active = True
is_deleted = False

print(type(is_active))      # <class 'bool'>
print(5 > 3)                # True
print(True + True)          # 2  — bool is a subclass of int
```

---

## 7. Binary Types

```python
b = b"hello"                       # bytes — immutable
ba = bytearray(5)                  # bytearray — mutable
mv = memoryview(bytes(5))          # memoryview

print(type(b))                     # <class 'bytes'>
print(type(ba))                    # <class 'bytearray'>
print(type(mv))                    # <class 'memoryview'>
```

---

## 8. None

Represents "no value".

```python
result = None
print(type(result))         # <class 'NoneType'>
print(result is None)       # True
```

---

## Mutable vs Immutable

| Mutable (can change) | Immutable (cannot change) |
|----------------------|---------------------------|
| `list`, `dict`, `set`, `bytearray` | `int`, `float`, `str`, `tuple`, `frozenset`, `bytes` |

---

## Type Conversion (Casting)

Two kinds: **implicit** (Python does it for you) and **explicit** (you call a
function to do it — a.k.a. casting).

### Implicit conversion

Python automatically widens numeric types when there's no data loss.

```python
num_int = 5
num_float = 1.5

result = num_int + num_float
print(result)          # 6.5
print(type(result))    # <class 'float'>  — int auto-promoted to float
```

### Explicit conversion — to int

```python
int("42")           # 42            — numeric string to int
int(3.9)             # 3             — truncates, does NOT round
int(-3.9)             # -3            — truncates toward zero
int(True)             # 1             — bool to int
int("3.14")           # ValueError    — can't parse a float string directly
```

### Explicit conversion — to float

```python
float("3.14")        # 3.14
float("42")           # 42.0
float(10)             # 10.0
float(True)           # 1.0
```

### Explicit conversion — to str

```python
str(100)             # '100'
str(3.14)             # '3.14'
str(True)             # 'True'
str([1, 2, 3])        # '[1, 2, 3]'
```

### Explicit conversion — to bool

```python
bool(0)              # False         — 0, 0.0 are falsy
bool(1)               # True          — any nonzero number is truthy
bool("")              # False         — empty string is falsy
bool("False")         # True          — non-empty string is ALWAYS truthy
bool([])               # False         — empty collections are falsy
bool([0])              # True          — non-empty collection is truthy
```

### Between collection types

```python
list("abc")          # ['a', 'b', 'c']
list((1, 2, 3))        # [1, 2, 3]

tuple([1, 2])          # (1, 2)
tuple("hi")             # ('h', 'i')

set([1, 1, 2])          # {1, 2}        — removes duplicates
set("aabbcc")            # {'a', 'b', 'c'}

dict([("a", 1), ("b", 2)])   # {'a': 1, 'b': 2}  — list of pairs to dict
```

### Common pitfalls

```python
# int("3.14")         # ValueError — go through float first
int(float("3.14"))     # 3

# int("abc")           # ValueError — not a numeric string
# list(123)            # TypeError  — int is not iterable
```

---

## Input and Output

### input() — always returns a string

```python
name = input("Enter your name: ")
print(type(name))                          # <class 'str'> — always, even for "42"

age = int(input("Enter your age: "))       # cast to int
height = float(input("Enter height: "))    # cast to float
```

### Reading multiple values on one line

```python
# user types: 3 5
a, b = input("Enter two numbers: ").split()
print(int(a) + int(b))                     # 8

# same thing, converting each piece with map()
x, y = map(int, input("Enter two numbers: ").split())
print(x + y)                               # 8

# user types: apple,banana,cherry
fruits = input("Enter fruits: ").split(",")
print(fruits)                              # ['apple', 'banana', 'cherry']
```

### print() basics

```python
print("Hello,", "World")                   # Hello, World  — args joined by a space
print("Hello", "World", sep=", ")           # Hello, World  — custom separator
print("Loading", end="...")                 # no newline after
print("Done")                               # Loading...Done
print(1, 2, 3, sep=" | ")                    # 1 | 2 | 3
```

### String formatting

```python
name = "Somel"
age = 25

print(f"Hello, {name}! You are {age}.")            # f-string (preferred)
print(f"Next year you'll be {age + 1}.")            # expressions allowed inside {}
print("Hello, {}! You are {}.".format(name, age))   # .format() method
print("Hello, %s! You are %d." % (name, age))       # %-formatting (old style)
```

### Formatting numbers

```python
pi = 3.14159265

print(f"{pi:.2f}")          # 3.14   — 2 decimal places
print(f"{1000000:,}")       # 1,000,000  — thousands separator
print(f"{pi:10.2f}")        # '      3.14'  — width 10, right-aligned
print(f"{5:03d}")           # 005    — zero-padded to 3 digits
```