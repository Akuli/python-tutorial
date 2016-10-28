# Exceptions

So far we have made programs that ask the user to enter a string, and
we also know how to convert that to an integer.

```py
text = input("Enter something: ")
number = int(text)
print("Your number doubled:", number*2)
```

That works.

```
Enter a number: 3
Your number twice: 6
```

But that doesn't work if the user does not enter a number.

```py
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

```py
>>> int('lol')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'lol'
>>> 
```

Exceptions are [classes](classes.md).

```py
>>> ValueError
<class 'ValueError'>
>>> 
```

We can also create exceptions. We won't get an error message by doing
that, but we'll use this for displaying our own error messages later.

```py
>>> the_problem = ValueError('oh no')
>>> the_problem
ValueError('oh no',)
>>> 
```

## Catching exceptions

If we need to try to do something and see if we get an exception, we
can use `try` and `except`. This is also known as **catching** the
exception.

```py
>>> try:
...     print(int('123'))
... except ValueError:
...     print("Oops!")
... 
123
>>> try:
...     print(int('lol'))
... except ValueError:
...     print("Oops!")
... 
Oops!
>>> 
```

ValueError is raised when something gets an invalid value, but the
value's type is correct. In this case, `int` can take a string as an
argument, but the string needs to contain a number, not `lol`.

If the type is wrong, we will get a TypeError instead.

```py
>>> 123 + 'hello'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
```

Exceptions always interrupt the code even if we catch them. Here the
print never runs because it's after the error but inside the `try`
block. Everything after the try block runs normally.

```py
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

```py
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

```py
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

Catching `Exception` will catch all errors. We'll learn more about why
it does that in a moment.

```py
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

```py
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

Never do things like this:

```py
try:
    # many lines of code
except Exception:
    print("Oops! Something went wrong.")
```

There's many things that can go wrong in the `try` block. If something
goes wrong all we have is an oops message that doesn't tell us which
line caused the problem. This makes fixing problems a lot harder. If we
want to catch exceptions we need to be specific about what exactly we
want to catch instead of catching everything we can.

There's nothing wrong with doing things like this:

```py
try:
    with open('some file', 'r') as f:
        content = f.read()
except OSError:     # we can't read the file but we can work without it
    content = some_default_content
```

Usually catching errors that the user has caused is also a good idea:

```py
text = input("Enter a number: ")
try:
    number = int(text)
except ValueError:
    print("'%s' is not a number." % text, file=sys.stderr)
    sys.exit(1)
print("Your number doubled is %d." % (number * 2))
```

## Raising exceptions

Sometimes you may end up doing something like this:

```py
if number < 0:
    print("ERROR: number must be non-negative")
```

But that's not ideal. If there is an error, the code prints an error
message but it still keeps running. People using your code also don't know
which line in **their** code caused the error.

Instead you can **raise an exception** yourself. Sometimes this is also
called **throwing an exception**.

```py
if number < 0:
    raise ValueError("number must be non-negative")
```

Let's try that on the interactive prompt, and see what that does.

```py
>>> raise ValueError("number must be non-negative")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: number must be non-negative
>>> 
```

Of course, we can also raise an exception from a variable.

```py
>>> oops = ValueError("number must be non-negative")
>>> raise oops
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: number must be non-negative
>>> 
```

## When should we raise exceptions?

Back in [the module chapter](modules.md) we learned to display error
messages by printing to `sys.stderr` and then calling `sys.exit(1)`, so
when should we use that and when should we raise an exception?

Exceptions are meant for **programmers**, so if we're writing a module
that other people will import we should probably use exceptions. For
other errors (for example, if the **user** of the program has done
something wrong) it's usually better to use `sys.stderr` and `sys.exit`.

## Exception hierarchy

Exceptions are organized like this. I made this tree diagram with
[this program](https://github.com/Akuli/classtree/) on Python 3.4. You
may have more or less exceptions than I have if your Python is newer or
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
all errors. You don't need to remember this tree, running
`help('builtins')` should display a larger tree that this is a part of.

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
