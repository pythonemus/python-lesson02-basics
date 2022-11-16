# Python Basics - Lesson 2
In this lesson we will cover the basics of the python language.
You will learn simple concepts on the python language syntax, variables and operators.

## Execution of Python Syntax
We can execute python code by either typing directly into python CLI or creating a python file to be run by the Python engine.

**Python CLI Example**
```
>>> print("Hello, World!")
Hello, World!
```
**Execute python code from a file**
```
C:\Users\Your Name>python myfile.py
```

## Python Indentation
Indentation refers to the spaces at the beginning of a code line.
Python uses indentation to indicate a block of code.
Where most traditional programming languages use indentation for readability.
Python has a much more specific use for indentations.
```
if 5 > 2:
  print("Five is greater than two!")
```
The number of spaces is up to you as a programmer
The most common use is four, 
But it has to be at least one.
```
if 6 > 3:
  print("six is greater than three!")
if 6 > 3:
        print("six is greater than three!")
```
You must have the same number of spaces in the same block of code otherwise Python will give you an error:
The following code block will error due to the print statement not indented under the "if" statement
```
if 6 > 3:
print("six is greater than three!")
```