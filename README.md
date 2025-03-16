
<div align="center">

# Python Cheatsheet

</div>

## Table of Contents

- [Variables](#variables)
- [Datatypes](#datatypes)
- [Arithmetical operations](#arithmetical-operations)
- [Conditionals](#conditionals)
- [Cycles](#cycles)
- [Functions](#functions)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Credits](#credits)

## Variables

### A variable lets the program remember values such as ***numbers***, ***text***, ***True/False***, ***lists*** and ***dictionaries*** for use later in the program.

To define a variable write the name of the variable, an equal sign and the value to save in the variable. Like so:

```py
a = 69
b = 4.20
c = "Hello, World!"
d = True
e = [0, 1, 2]
f = {"Hello": "World"}
```

To change the value that is currently saved in a variable, simply save a value to the variable again.

```py
g = 69
g = 4.20
g = "Hello, World!"
g = True
g = [0, 1, 2]
g = {"Hello": "World"}
```

You do **not** need to specify the datatype of a variable.

## Datatypes

### Datatypes define the type of value being stored in a variable, such as `int` or `float` for ***numbers***.

```py
h = 69 # The `int` (Integer) datatype stores whole numbers.
i = 4.20 # The `float` (Floating point) datatype stores numbers with a decimal point.
j = "Hello, World!" # The `str` (String) datatype stores text. (We can use either 'single quotes' or "double quotes" to define a string.)
k = True # The `bool` (Boolean) datatype stores True/False values.
l = [0, 1, 2] # The `list` datatype stores a list of values. (The first value will be stored in position 0, and the values don't have to be of the same datatype.)
m = {"Hello": "World"}	# The `dict` (Dictionary) datatype stores a list of keys and values which can be refered to by their key. (In this case "Hello" is the key for the "World" value.)
```

Datatypes are assigned automatically in Python.

## Arithmetical operations

```py
n = 2 + 2 # Addition.
o = 2 - 2 # Subtraction.
p = 2 * 2 # Multiplication.
q = 2 / 2 # Division.
r = 2 ** 2 # Power.
s = 2 // 2 # Integer division.
t = 2 % 2 # Remainder after division.
```

To perform a square root you can either use the `sqrt()` function from the `math` library or use power to one half.

```py
import math

u = math.sqrt(3)
v = 3 ** .5
```

## Conditionals

### A conditional is used to change the path that the program takes when executing code.

This is very useful if you need some code to be execute only `if` a certain condition is met. For example:

```py
age = 18

if age >= 18:
	print("You are old enough to have a driver's licence.")
else:
	print("You are not yet old enough to have a driver's licence.")
```

The above code will output `You are old enough to have a driver's lincense.`, because the value stored in the `age` variable is more than or equal to 18. However, this would not be a case if the value of the `age` variable was less than 18.

You can also have multiple conditions for certain code to execute.

```py
playtimeHours = 460

if playtimeHours > 0 and playtimeHours <= 50:
	print("Average playtime.")
elif playtimeHours > 50 and playtimeHours <= 500:
	print("You might want to stop soon.")
elif playtimeHours > 500:
	print("You need a break.")
else:
	print("How did you get negative playtime?")
```

`elif` stands for `else if`, meaning that the condition is only checked if the previous one isn't met.\
The `and` keyword in the first two `if` statements requires both conditions within an `if` statement to be met.\
That means that the above code outputs `You might want to stop soon.`, due to the value of `playtimeHours` being more than 50 and less than or equal to 500.

```py
x = 10
y = 5

if x > 0 or y < 0:
	print(True)
else:
	print(False)
```

The `or` keyword requires for at least one of the conditions to be met.\
The output of the above code will therefore be `True`. Since `x` is more than 0.

Some of the coditions that can be writtene in an `if` statement are written below:

```py
if var1 == var2: pass # The `==` condition is met when var1 and var2 match.
if var1 != var2: pass # The `!` operator inverts the condition. (In this case the condition will be met if var1 and var2 do *not* match.)
if var1 > var2: pass # The `>` condition is met when var1 is more than var2.
if var1 >= var2: pass # The `>=` condition is met when var1 is more than or equal to var2.
if var1 < var2: pass # The `<` condition is met when var1 is less than var2.
if var1 <= var2: pass # The `<=` condition is met when var1 is less than or equal to var2.
```

## Cycles

### Cycles are used when you need to execute the same code multiple times.

One way to use a cycle is to do something with every item in a list.

```py
items = [0, 1, 2]
out = ""

for item in items:
	out += str(item)

print(out)
```

The above code will loop over every item in the variable `items` and append it to the `out` string.\
Afterwards it will output the contents of the `out` variable.\
Hence, the output will be `012`.

Another way to use a `for` loop is to execute code a certain number of times.

```py
for i in range(10):
	print(i)
```

The output of the above code will be:

```
0
1
2
3
4
5
6
7
8
9
```

Another way to define a cycle is with the `while` keyword.\
This is useful for infinite loops.

```py
while True:
	print("Hello, World!")
```

The above code with output `Hello, World!` repeatedly until the program is stopped manually.

## Functions

### Functions can be useful for when code is reused in multiple places, making it easier to maintain.

To define a function we use the `def` keyword.

```py
def func():
	return
```

If your function needs arguments (inputs), you can specify them in the parentheses.

```py
def func(a, b):
	return
```

The `return` keyword is the output of your function.

```py
def add(a, b):
	return a + b
```

You can also specify what datatype needs to be used for the arguments, and what datatype will be returned.

```py
def add(a:float, b:float) -> float:
	return a + b
```

Another way to define a function is to use the `lambda` keyword.

```py
add = lambda a, b: a + b
```

Note that both of the functions above do the same thing.

To use a function simply write the name of your function ending with parentheses.

```py
def func():
	return

func()
```

Again, arguments are written inside the parentheses.

```py
def add(a, b):
	return a + b

print(add(5, 3))
```

The output of the above code will be `8`.\
Note that the function itself doesn't output anything to the terminal. That's what the `print()` function is for.

## Inputs

### Sometimes you will need user input in your code.

To get user input you use the `input()` function.

```py
name = input()
```

However, with the above example the user woudn't know what to input.\
Which is why you can write a prompt inside the `input()` function.

```py
name = input("What is your name: ")
```

## Outputs

### Last but not least, outputs.

To output text to the terminal we use the `print()` function.

```py
print("Hello, World!")
```

Outputs `Hello, World!`.

The `print()` function automatically appends `\n` (new line) to the end of the text.\
However, this can be changed by using the `end` parameter.

```py
print("Hello, ", end="")
print("World!")
```

The code above also outputs `Hello, World!` on a single line. Since the first `print()` function doesn't append `\n`.

The `print()` function can also output other datatypes, not just strings.

```py
print(["Hello", "World"])
```

Outputs `['Hello', 'World']`.

## Credits

Author: Jakub Kopas
