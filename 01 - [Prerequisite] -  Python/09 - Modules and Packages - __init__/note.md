# Modules & Packages | __init__

## Modules -> A module is simply a python file that contains reusable code like variables, functions, or classes

### 1. Creating a module
Save the following as `calculator.py`. This file, on its own, is now a module named `calculator`.
```python
# calculator.py

pi = 3.14159  # a module-level variable

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2
```

### 2. Importing the whole module
Use `import module_name`, then access everything with `module_name.thing`.
```python
# main.py
import calculator

print(calculator.add(2, 3))        # 5
print(calculator.multiply(4, 5))   # 20
print(calculator.pi)               # 3.14159

c = calculator.Circle(2)
print(c.area())                    # 12.56636
```

### 3. Importing specific names
Use `from module_name import name1, name2` to pull specific items into your namespace, no prefix needed.
```python
from calculator import add, pi

print(add(10, 20))  # 30
print(pi)            # 3.14159
```

### 4. Importing with an alias
Use `as` to rename a module or function, handy for long names or avoiding clashes.
```python
import calculator as calc
from calculator import multiply as mul

print(calc.add(1, 1))  # 2
print(mul(3, 3))        # 9
```

### 5. Importing everything (`*`) — use sparingly
Pulls all public names into the current namespace. Can cause naming conflicts, so it's generally discouraged.
```python
from calculator import *

print(add(5, 5))       # 10
print(multiply(2, 2))  # 4
```

### 6. Built-in / standard library modules
Python ships with many ready-to-use modules — no installation needed.
```python
import math
import random
import datetime

print(math.sqrt(16))          # 4.0
print(random.randint(1, 10))  # a random int between 1 and 10
print(datetime.date.today())  # today's date
```

### 7. `__name__ == "__main__"`
Every module has a built-in variable `__name__`. When a file is run directly, `__name__` is `"__main__"`; when it's imported, `__name__` is the module's own name. This lets a file act as both a reusable module and a standalone script.
```python
# calculator.py
def add(a, b):
    return a + b

if __name__ == "__main__":
    # only runs when calculator.py is executed directly,
    # NOT when it's imported elsewhere
    print("Testing calculator module...")
    print(add(2, 3))
```
```python
# main.py
import calculator  # "Testing calculator module..." is NOT printed
print(calculator.add(1, 2))
```

### 8. Inspecting a module
```python
import calculator

print(dir(calculator))        # lists all names defined in the module
print(calculator.__name__)    # 'calculator'
print(calculator.__doc__)     # module's docstring, if any
print(calculator.__file__)    # path to the module's file
```

### 9. Reloading a module (rarely needed)
Useful mainly in interactive sessions/notebooks when a module's source changed after it was already imported.
```python
import importlib
import calculator

importlib.reload(calculator)
```

## Modules summary
| Syntax | What it does |
|---|---|
| `import module` | imports the whole module; access via `module.name` |
| `from module import name` | imports specific names directly |
| `import module as alias` | imports the module under a shorter/different name |
| `from module import name as alias` | imports a specific name under a different name |
| `from module import *` | imports everything (avoid — pollutes namespace) |

## Packages -> A package is a folder of modules that has an `__init__.py` file inside it, which tells Python to treat the folder as an importable package

### 1. Basic package structure
```
shapes/                  <- package (a directory)
├── __init__.py          <- makes this directory a package
├── circle.py            <- module
└── square.py            <- module
```
```python
# shapes/circle.py
def area(radius):
    return 3.14159 * radius ** 2
```
```python
# shapes/square.py
def area(side):
    return side ** 2
```
`__init__.py` can be empty — its mere presence marks `shapes/` as a package. (Since Python 3.3, "namespace packages" without `__init__.py` also work, but including it is still common and clearer.)

### 2. Importing from a package
```python
# main.py
import shapes.circle
import shapes.square

print(shapes.circle.area(2))   # 12.56636
print(shapes.square.area(3))   # 9
```
```python
from shapes import circle, square

print(circle.area(2))
print(square.area(3))
```
```python
from shapes.circle import area as circle_area

print(circle_area(2))
```

### 3. Using `__init__.py` to control the package's public API
Code in `__init__.py` runs automatically the moment the package is imported. It's commonly used to expose selected functions at the package level, so users don't need to know the internal file layout.
```python
# shapes/__init__.py
from .circle import area as circle_area
from .square import area as square_area

print("shapes package initialized")  # runs once, on first import
```
```python
# main.py
import shapes

print(shapes.circle_area(2))   # 12.56636  (no need for shapes.circle.area)
print(shapes.square_area(3))   # 9
```

### 4. Subpackages (packages inside packages)
```
shapes/
├── __init__.py
├── flat/
│   ├── __init__.py
│   ├── circle.py
│   └── square.py
└── solid/
    ├── __init__.py
    ├── sphere.py
    └── cube.py
```
```python
from shapes.flat import circle
from shapes.solid.sphere import volume

print(circle.area(2))
print(volume(3))
```

### 5. Relative imports (used inside a package's own modules)
```python
# shapes/solid/cube.py
from ..flat.square import area as base_area  # ".." goes up one package level

def volume(side):
    return base_area(side) * side
```
- `.` = current package
- `..` = parent package
- Relative imports only work inside a package (i.e. in a file that's imported as part of that package), not when a file is run directly as a script.

### 6. Controlling `from package import *` with `__all__`
By default `from shapes import *` imports every public name in `__init__.py`. `__all__` lets you explicitly whitelist what gets exported.
```python
# shapes/__init__.py
from .circle import area as circle_area
from .square import area as square_area

__all__ = ["circle_area"]  # only circle_area is exported with *
```
```python
from shapes import *

print(circle_area(2))  # works
print(square_area(3))  # NameError: not exported by *
```

## Packages summary
| Concept | Purpose |
|---|---|
| Package (folder) | groups related modules together |
| `__init__.py` | marks a folder as a package; runs on first import; can define its public API |
| `import package.module` | imports one module from the package |
| `from package import module1, module2` | imports specific modules from the package |
| Subpackage | a package nested inside another package |
| `.` / `..` relative import | imports from the current/parent package (inside package modules only) |
| `__all__` | controls what `from package import *` exposes |
