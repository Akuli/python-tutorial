# Defining your own functions

It's probably been a while since you read about using functions. [Read
about it again](using-functions.md) if you need to.

## Why should I use custom functions?

Have a look at this code:

```py
print("************")
print("Hello World!")
print("************")

print("*************")
print("Enter a word:")
print("*************")

word = input()

if word == 'python':
    print("*******************")
    print("You entered Python!")
    print("*******************")
else:
    print("**************************")
    print("You didn't enter Python :(")
    print("**************************")
```

Then compare it to this code:

```py
print_box("Hello World!")
print_box("Enter a word:")
word = input()
if word == 'python':
    print_box("You entered Python!")
else:
    print_box("You didn't enter Python :(")
```

That's nice, but where do we a box function like that?

## First functions

The `pass` keyword does nothing.

```py
>>> pass
>>> 
```

Let's use it to define a function that does nothing.

```py
>>> def do_nothing():
...     pass
... 
>>> do_nothing
<function do_nothing at 0x7f56b74e9598>
>>> 
```

Seems to be working so far, we have a function. Let's see what happens
if we call it.

```py
>>> do_nothing()
>>> 
```

There we go. It did nothing at all.

Maybe we could just do something in the function instead?

```py
>>> def print_hi():
...     print("Hi!")
... 
>>> print_hi()
Hi!
>>> 
```

It's working. How about printing a variable in the function?

```py
>>> def print_message():
...     print(message)
... 
>>> message = "Hello World!"
>>> print_message()
Hello World!
>>> 
```

Again, it works. How about setting a variable in the function?

```py
>>> def get_username():
...     username = input("Username: ")
... 
>>> get_username()
Username: me
>>> username
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'username' is not defined
>>> 
```

That was weird! Why didn't that work?

## Locals and globals

So far we have used nothing but **global variables**. They are called
globals because the same variables are available anywhere in our
program, even in functions.

```py
>>> a = 1
>>> b = "hi"
>>> c = "hello"
>>> def print_abc():
...     print(a, b, c)
... 
>>> print_abc()
1 hi hello
>>> 
```

But there are also **local variables**. They exist only inside
functions, and they are deleted when the function exits.

```py
>>> def thingy():
...     d = "hello again, i'm a local variable"
...     print('inside thingy:', d)
... 
>>> thingy()
inside thingy: hello again, i'm a local variable
>>> d
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'd' is not defined
>>> 
```

However, modifying a global variable in-place from a function is easy.

```py
>>> foo = ['global foo']
>>> def bar():
...     foo.append('bar foo')
... 
>>> bar()
>>> foo
['global foo', 'bar foo']
>>> 
```

This doesn't work if the value is of an immutable type, like string or
integer. Fortunately, Python will tell you if something's wrong.

```py
>>> foo = 1
>>> def bar():
...     foo += 1
... 
>>> bar()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in bar
UnboundLocalError: local variable 'foo' referenced before assignment
>>> 
```

## Input

So far our functions seem to be really isolated from the rest of our
code, and it sucks! But they really are not as isolated as you might
think they are.

Let's think about what the built-in function input does. It takes an
argument, and returns a value. Maybe a custom function could do that
also?

```
>>> def print_twice(message):
...     print(message)
...     print(message)
... 
>>> 
```

This function can be called in two ways:

- Using a **positional argument**.

    This is the recommended way for functions that take only one or two
    arguments. I would do this in my code.

        >>> print_twice("hi")
        hi
        hi
        >>> 

    Positional arguments are great for simple things like
    `print("hello")`, but if your function takes many positional
    arguments it may be hard to tell which argument is which.

- Using a **keyword argument**:

        >>> print_twice(message="hi")
        hi
        hi
        >>> 

    Keyword arguments are great when your function needs to take many
    arguments, because each argument has a name and it's easy to see
    which argument is which.

    Also note that there are no spaces around the `=` sign. That's
    because we are not assigning to a variable, we are giving the
    function a keyword argument and it can do whatever it wants with
    it.

Personally, I would use this function with a positional argument. It
only takes one argument.

Now it's time to solve our box printing problem:

```py
def print_box(message):
    print('*' * len(message))
    print(message)
    print('*' * len(message))
```

## Output

The built-in input function returns a value. Can our function return a
value also?

```py
>>> def times_two(x):
...     return x * 2
... 
>>> times_two(3)
6
>>> times_two("hello")
'hellohello'
>>> 
```

Yes, it can.

Note that **returning from a function ends it immediately**.

```py
>>> def return_before_print():
...     return None
...     print("This never gets printed.")
... 
>>> return_before_print()
>>> 
```

If we don't have any return statements or we have a return statement
that doesn't specify what to return, our function will return None.

```py
>>> def return_none_1():
...     print("This will return None.")
... 
>>> def return_none_2():
...     print("This will also return None.")
...     return
... 
>>> x = return_none_1()
This will return None.
>>> y = return_none_2()
This will also return None.
>>> print(x, y)
None None
>>> 
```

## Default values

What if we want to print different characters instead of always
printing stars?

We could change our print_box function to take two arguments:

```py
def print_box(message, character):
    print(character * len(message))
    print(message)
    print(character * len(message))
```

Then we could change our existing code to always call print_box with a
star as the second argument:

```py
print_box("Hello World", "*")
...
```

But we don't need to change our existing code. We can make the second
argument **optional** by giving it a **default value**.

```py
def print_box(message, character='*'):
    print(character * len(message))
    print(message)
    print(character * len(message))
```

We can print a row of stars using the function without specifying a
different character in two ways:

- Using a positional argument.

        print_box("Hello World!")

- Using a keyword argument.

        print_box(message="Hello World!")

Or we can give it a different character in a few different ways if we
need to:

- Using two positional arguments.

        print_box("Enter a word:", "?")

- Using two keyword arguments.

        print_box(message="Enter a word:", character="?")
        print_box(character="?", message="Enter a word:")

- Using one positional argument and one keyword argument.

    I would probably do this. If an argument has a default value, I
    like to use a keyword argument to change it if needed.

        print_box("Enter a word:", character="?")

    However, this doesn't work:

        print_box(character="?", "Enter a word:")

    The problem is that we have a keyword argument before a positional
    argument. Python doesn't allow this. You don't need to worry about
    this, because if you accidentally call a function like this you
    will get an error message.

## Exercises

**There is a lot to learn with functions, and I don't expect you to
learn everything at once.** However, there's also lots and lots of free
Python exercises about defining functions you can do. Do many of them
and spend a lot of time with them, so you'll get used to defining
functions.

1. Python comes with many built-in functions. Some of the simplest ones
    are abs, all and any. They can be used like this:

    - abs returns the absolute value of its only argument.

            >>> abs(1)
            1
            >>> abs(-1)
            1
            >>> 

    - any returns True if any of the elements of a list is true, and
        False otherwise.

            >>> any([True, False, True])
            True
            >>> any([False, False, False])
            False
            >>> 

    - all returns True if all elements of a list are true, and False
        otherwise.

            >>> all([True, True, True])
            True
            >>> all([True, False, True])
            False
            >>> 

    Define functions my_abs, my_all and my_any that work the same way
    without using built-in functions. Then run the program with IDLE,
    or with `py -i file.py` on Windows or `python3 -i file.py` on other
    operating systems. Then try the above examples with your functions.

2. The box printing function doesn't really print a box, it prints a
    message between two lines.

        ************
        Hello World!
        ************

    Modify it to print an actual box:

        ****************
        * Hello World! *
        ****************

3. Back in [Lists](lists.md), you needed to skip parts of the tutorial
    and all the exercises because you didn't know how to define
    functions. Read those parts now, and do the exercises.

4. Use a search engine (e.g. Google) to find more exercises about
    defining functions.

Answers for the first and second exercise are [here](answers.md).
