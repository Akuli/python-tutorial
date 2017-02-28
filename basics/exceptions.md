# Exceptions

So far we have made programs that ask the user to enter a string, and
we also know how to convert that to an integer.

```python
text = input("Enter something: ")
number = int(text)
print("Your number doubled:", number*2)
```

That works.

```
Enter a number: 3
Your number doubled: 6
```

But that doesn't work if the user does not enter a number.

```python
Enter a number: lol
Traceback (most recent call last):
  File "/some/place/file.py", line 2, in <module>
    number = int(text)
ValueError: invalid literal for int() with base 10: 'lol'
```

So how can we fix that?

## What are exceptions?

In the previous example we got a ValueError. ValueError is an
**exception**. In other words, ValueError is an error that can occur
in our program. If an exception occurs, the program will stop and we
get an error message. The interactive prompt will display an error
message and keep going.

```python
>>> int('lol')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'lol'
>>>
```

Exceptions are [classes](classes.md).

```python
>>> ValueError
<class 'ValueError'>
>>>
```

We can also create exceptions. We won't get an error message by doing
that, but we'll use this for displaying our own error messages later.

```python
>>> the_problem = ValueError('oh no')
>>> the_problem
ValueError('oh no',)
>>>
```

## Catching exceptions

If we need to try to do something and see if we get an exception, we
can use `try` and `except`. This is also known as **catching** the
exception.

```python
>>> try:
...     print(int('lol'))
... except ValueError:
...     print("Oops!")
...
Oops!
>>>
```

The except part doesn't run if the try part succeeds.

```python
>>> try:
...     print("Hello World!")
... except ValueError:
...     print("What the heck? Printing failed!")
...
Hello World!
>>>
```

ValueError is raised when something gets an invalid value, but the
value's type is correct. In this case, `int` can take a string as an
argument, but the string needs to contain a number, not `lol`. If
the type is wrong, we will get a TypeError instead.

```python
>>> 123 + 'hello'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>>
```

Exceptions always interrupt the code even if we catch them. Here the
print never runs because it's after the error but inside the `try`
block. Everything after the try block runs normally.

```python
>>> try:
...     123 + 'hello'
...     print("This doesn't get printed.")
... except TypeError:
...     print("Oops!")
...
Oops!
>>>
```

Does an `except ValueError` also catch TypeErrors?

```python
>>> try:
...     print(123 + 'hello')
... except ValueError:
...     print("Oops!")
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>>
```

No, it doesn't. But maybe we could except for both ValueError and
TypeError?

```python
>>> try:
...     int('lol')
... except ValueError:
...     print('wrong value')
... except TypeError:
...     print('wrong type')
...
wrong value
>>> try:
...     123 + 'hello'
... except ValueError:
...     print('wrong value')
... except TypeError:
...     print('wrong type')
...
wrong type
>>>
```

Seems to be working.

We can also also catch multiple exceptions by catching
[a tuple](lists-and-tuples.md#tuples) of exceptions:

```python
>>> try:
...     123 + 'hello'
... except (ValueError, TypeError):
...     print('wrong value or type')
...
wrong value or type
>>> try:
...     int('lol')
... except (ValueError, TypeError):
...     print('wrong value or type')
...
wrong value or type
>>>
```

Catching `Exception` will catch all errors. We'll learn more about why
it does that in a moment.

```python
>>> try:
...     123 + 'hello'
... except Exception:
...     print("Oops!")
...
Oops!
>>> try:
...     int('lol')
... except Exception:
...     print("Oops!")
...
Oops!
>>>
```

It's also possible to catch an exception and store it in a variable.
Here we are catching an exception that Python created and storing it in
`our_error`.

```python
>>> try:
...     123 + 'hello'
... except TypeError as e:
...     our_error = e
...
>>> our_error
TypeError("unsupported operand type(s) for +: 'int' and 'str'",)
>>> type(our_error)
<class 'TypeError'>
>>>
```

## When should we catch exceptions?

Do **not** do things like this:

```python
try:
    # many lines of code
except Exception:
    print("Oops! Something went wrong.")
```

There's many things that can go wrong in the `try` block. If something
goes wrong all we have is an oops message that doesn't tell us which
line caused the problem. This makes fixing the program really annoying.
If we want to catch exceptions we need to be specific about what exactly
we want to catch and where instead of catching everything we can in the
whole program.

There's nothing wrong with doing things like this:

```python
try:
    with open('some file', 'r') as f:
        content = f.read()
except OSError:     # we can't read the file but we can work without it
    content = some_default_content
```

Usually catching errors that the user has caused is also a good idea:

```python
import sys

text = input("Enter a number: ")
try:
    number = int(text)
except ValueError:
    print("'%s' is not a number." % text, file=sys.stderr)
    sys.exit(1)
print("Your number doubled is %d." % (number * 2))
```

## Raising exceptions

Now we know how to create exceptions and how to handle errors that
Python creates. But we can also create error messages manually. This
is known as **raising an exception** and **throwing an exception**.

Raising an exception is easy. All we need to do is to type `raise`
and then an exception we want to raise:

```python
>>> raise ValueError("lol is not a number")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: lol is not a number
>>>
```

Of course, we can also raise an exception from a variable.

```python
>>> oops = ValueError("lol is not a number")
>>> raise oops
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: lol is not a number
>>>
```

If we [define a function](defining-functions.md) that raises an
exception and call it we'll notice that the error message also
says which functions we ran to get to that error.

```python
>>> def oops():
...     raise ValueError("oh no!")
...
>>> def do_the_oops():
...     oops()
...
>>> do_the_oops()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in do_the_oops
  File "<stdin>", line 2, in oops
ValueError: oh no!
>>>
```

If our code was in a file we would also see the line of code
that raised the error.

## When should we raise exceptions?

Back in [the module chapter](modules.md) we learned to display error
messages by printing to `sys.stderr` and then calling `sys.exit(1)`, so
when should we use that and when should we raise an exception?

Exceptions are meant for **programmers**, so if we are writing something
that other people will import we should use exceptions. If our program
is working like it should be and the **user** has done something wrong,
it's usually better to use `sys.stderr` and `sys.exit`.

## Exception hierarchy

Exceptions are organized like this. I made this tree with [this
program](https://github.com/Akuli/classtree/) on Python 3.4. You may
have more or less exceptions than I have if your Python is newer or
older than mine, but they should be mostly similar.

    Exception
    ├── ArithmeticError
    │   ├── FloatingPointError
    │   ├── OverflowError
    │   └── ZeroDivisionError
    ├── AssertionError
    ├── AttributeError
    ├── BufferError
    ├── EOFError
    ├── ImportError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── MemoryError
    ├── NameError
    │   └── UnboundLocalError
    ├── OSError
    │   ├── BlockingIOError
    │   ├── ChildProcessError
    │   ├── ConnectionError
    │   │   ├── BrokenPipeError
    │   │   ├── ConnectionAbortedError
    │   │   ├── ConnectionRefusedError
    │   │   └── ConnectionResetError
    │   ├── FileExistsError
    │   ├── FileNotFoundError
    │   ├── InterruptedError
    │   ├── IsADirectoryError
    │   ├── NotADirectoryError
    │   ├── PermissionError
    │   ├── ProcessLookupError
    │   └── TimeoutError
    ├── ReferenceError
    ├── RuntimeError
    │   └── NotImplementedError
    ├── StopIteration
    ├── SyntaxError
    │   └── IndentationError
    │       └── TabError
    ├── SystemError
    ├── TypeError
    ├── ValueError
    │   └── UnicodeError
    │       ├── UnicodeDecodeError
    │       ├── UnicodeEncodeError
    │       └── UnicodeTranslateError
    └── Warning
        ├── BytesWarning
        ├── DeprecationWarning
        ├── FutureWarning
        ├── ImportWarning
        ├── PendingDeprecationWarning
        ├── ResourceWarning
        ├── RuntimeWarning
        ├── SyntaxWarning
        ├── UnicodeWarning
        └── UserWarning

Catching an exception also catches everything that's under it in this
tree. For example, catching `OSError` catches errors that we typically
get when [processing files](files.md), and catching Exception catches
all of these errors. You don't need to remember this tree, running
`help('builtins')` should display a larger tree that this is a part of.

There are also a few exceptions that are not in this tree like
SystemExit and KeyboardInterrupt, but most of the time we shouldn't
catch them. Catching Exception doesn't catch them either.

## Summary

- Exceptions are classes and they can be used just like all other classes.
- ValueError and TypeError are some of the most commonly used exceptions.
- The `try` and `except` keywords can be used for attempting to do
    something and then doing something else if we get an error. This is
    known as catching exceptions.
- It's possible to raise exceptions with the `raise` keyword. This
    is also known as throwing exceptions.
- Raise exceptions if they are meant to be displayed for programmers and
    use `sys.stderr` and `sys.exit` otherwise.

## Examples

Keep asking a number from the user until it's entered correctly.

```python
while True:
    try:
        number = int(input("Enter a number: "))
        break
    except ValueError:
        print("That's not a valid number! Try again.")

print("Your number doubled is:", number * 2)
```

This program allows the user to customize the message it prints by
modifying a file the greeting is stored in, and it can create the
file for the user if it doesn't exist already. This example also uses
things from [the file chapter](files.md), [the function defining
chapter](defining-functions.md) and [the module chapter](modules.md).

```python
# These are here so you can change them to customize the program
# easily.
default_greeting = "Hello World!"
filename = "greeting.txt"


import sys

def askyesno(question):
    while True:
        answer = input(question + ' (y or n) ')
        if answer == 'Y' or answer == 'y':
            return True
        if answer == 'N' or answer == 'n':
            return False

def greet():
    with open(filename, 'r') as f:
        for line in f:
            print(line.rstrip('\n'))

try:
    greet()
except OSError:
    print("Cannot read '%s'!" % filename, file=sys.stderr)
    if askyesno("Would you like to create a default greeting file?"):
        with open(filename, 'w') as f:
            print(default_greeting, file=f)
        greet()
```

***

If you have trouble with this tutorial please [tell me about
it](../contact-me.md) and I'll make this tutorial better. If you
like this tutorial, please [give it a
star](../README.md#how-can-i-thank-you-for-writing-and-sharing-this-tutorial).

You may use this tutorial freely at your own risk. See
[LICENSE](../LICENSE).

[Previous](modules.md) | [Next](classes.md) |
[List of contents](../README.md#basics)
