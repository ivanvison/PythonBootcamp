Thank you for getting to this point. This repository was created for a project to learn Python. "2022 Complete Python Bootcamp From Zero to Hero in Python
" from UDEMY.

Quick note: The trainer (Jose Portilla) uses Anaconda, Jupyter Notebooks. I tried to follow along using VSCode. 

## Topics Covered
- Section 1: Course Overview
- Section 2: Python Setup
- Section 3: Python Object and Data Structure Basics
- Section 4: Python Comparison Operators
- Section 5: Python Statements
- Section 6: Methods and Functions
- Section 7: Milestone Project - 1
- Section 8: Object Oriented Programming
- Section 9: Modules and Packages
- Section 10: Errors and Exception Handling
- Section 11: Milestone Project - 2
- Section 12: Python Decorators
- Section 13: Python Generators
- Section 14: Advanced Python Modules
- Section 15: Web-Scraping
- Section 16: Working-with-Images
- Section 17: PDFs-and-Spreadsheets
- Section 18: Emailing-with-Python
- Section 19: Advanced Python Objects and Data Structures
- Section 20: Milestone Project - 3
- Section 21: Bonus Material - Introduction to G

## Install / Usage Process (My personal setup)
1. Installed [VS Code](https://code.visualstudio.com).
2. Installed [Python](https://www.python.org/downloads/).
3. Installed several plugins from within VSCode related to Python.+

### Setting up Environment Variables in Windows 10 PRO x64

**Prerequisites:**
- Python

1. Press Start > Write `environment` > Click `Edit the system variables environment`
2. Click Environment Variables
3. Under System variables, click New
    - Variable Name = python
    - Variable Value = C:\Users\Ivan\AppData\Local\Programs\Python\Python310\
4. Ok > Ok


## Notes from the training per section

### Section 2. Python Setup
- CLI Basics (Windows)
- Upgraded current python installation: `py -3 -m pip install --upgrade pip`

### Section 3: Python Object and Data Structure Basics
- When to choose a list or dictionary?
    - Dictionary is OK when, for example, quickly wanting a value without needing to know its exact location--cons is that can't be sorted, sliced.

### Section 4: Python Comparison Operator
- Logical operators - Chain operators
    - and or not
    - Ex: 1 < 2 and 2 < 3

### Section 6: Methods and Functions
- *args to pass N values into a function in a tuple format
- **kwargs (keywords arguments) to create a dictionary based on the values sent to a function
- LEGB Rule
    - L: Local — Names assigned in any way within a function (def or lambda), and not declared global in that function.
    - E: Enclosing function locals — Names in the local scope of any and all enclosing functions (def or lambda), from inner to outer.
    - G: Global (module) — Names assigned at the top-level of a module file, or declared global in a def within the file.
    - B: Built-in (Python) — Names preassigned in the built-in names module : open, range, SyntaxError,...

### Section 8: Object Oriented Programming
- Allows users to create their own objects.
- Allows us to create code that is repeatable and organized.
- Camel Casing for classes
- Syntax sample:
- def when is inside of a class is called a method.
- __init__ is a special type that is always called when creating an instance of the class
- self keyword connects the method to the instance of the class
```python
class NameOfClass():

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def some_method(self):
        #perform some action
        print(self.param1)
```

### Section 9: Modules and Packages
- Packages is a collection of modules
- Modules are scripts that you can call from a different .py files.
- __init__ identifies a folder that should be a package or subpackage
- `if __name__=="__main__":` - original file or actual import
- Code organization


### Section 10: Errors and Exception Handling
- Keywords
    - try: attempt
    - except: execute if error
    - finally: 
- pylint
- unittest
- `pylint myexample.py -r y`
- PEP 8

### Section 12: Decorators
- On/Off Switch for functions
- @ operators is used and located above the function
- we can pass functions as arguments

### Section 13: Generators
- Generate a sequence of values over time
- usage of a yield statement
- range()
- Memory efficiency