# Exceptions

So far we have made programs that ask the user to enter a string.

```py
text = input("Enter something: ")
print("Your text twice:", text*2)
```

That works.

```
Enter something: hello
Your text twice: hellohello
```

But if the user enters a number, it's not going to be multiplied by two.

```
Enter something: 3
Your text twice: 33
```

Let's use `int` to convert that to an integer:

```py
text = input("Enter a number: ")
number = int(text)
print("Your number twice:", number*2)
```

That works...

```
Enter a number: 3
Your number twice: 6
```

...unless the user does not enter a number.

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
get an error message.

```py
>>> int('lol')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'lol'
>>> 
```

Exceptions are classes, just like int and str. We'll talk more about
classes later in this tutorial.

```py
>>> str
<class 'str'>
>>> int
<class 'int'>
>>> ValueError
<class 'ValueError'>
>>> 
```

You can also create an exception. You won't get an error message by doing
that, but we'll use this for displaying our own error messages later.

```py
>>> the_problem = ValueError('oh no')
>>> the_problem
ValueError('oh no',)
>>> type(the_problem)
<class 'ValueError'>
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

It's also possible to catch an exception, and store it in a variable:

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

## Raising exceptions

When working on something that other programmers are going to use,
you may end up doing something like this:

```py
if number < 0:
    print("ERROR: number must be non-negative")
```

But that's not ideal. If there is an error, the code prints an error
message but it still keeps running. People using your code also don't know
which line in their code caused the error.

Instead you can **raise** an exception yourself. Sometimes this is also
called **throwing** an exception.

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

It's working.

**TODO:** except Exception

**TODO:** introduce assert here?

## Summary

- Exceptions can be used just like any other variables.
- ValueError and TypeError are some of the most commonly used exceptions.
- The `try` and `except` keywords can be used for attempting to do
    something and then doing something else if it causes an error. This
    is known as catching exceptions. You can use one `try` statement with
    multiple `except` statements.
- It's also possible to raise exceptions with the `raise` keyword. This
    is also known as throwing exceptions.
