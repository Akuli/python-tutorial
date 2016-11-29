# Using functions

Now we know how to make Python show text.

```py
>>> 'Hello!'
'Hello!'
>>> 
```

But that includes `''`. One way to show text to the user without `''`
is with the print function. In Python, printing doesn't have anything
to do with physical printers, it just means showing text on the screen.

```py
>>> print('Hello!')
Hello!
>>> 
```

Now we are ready for a classic example, which is also the first program
in many tutorials :)

```py
>>> print("Hello World!")
Hello World!
>>> 
```

But what exactly is print?

## What are functions?

Let's see what happens if we type `print` without the `('Hello')` part.

```py
>>> print
<built-in function print>
>>> 
```

We could also type `print(print)`, it would do the same thing. Python
replied to us with some information about print wrapped in `<>`.

As we can see, print is a function. Functions do something when they are
**called** by typing their name and parentheses. Inside the
parentheses, we can pass some arguments too. In `print("hello")` the
function is `print` and we give it one argument, which is `"hello"`.

Functions are easy to understand, They simply **do something when they
are called**. Functions run immediately when we call them, so the
text appears on the screen right away when we run `print(something)`.

## Return values

If we do `x = print('hello')`, what is x?

```py
>>> x = print('hello')
hello
>>> print(x)       # x is now None
None
>>> 
```

So doing `x = print('hello')` set x to None. Here's what happened,
explained in more detail:

- In `x = print('hello')`, the right side is processed first.
- `print('hello')` calls the print function with the argument
    `'hello'`.
- The function runs. It shows the word hello.
- The print function **returns** None. All functions need to return
    something, and print returns None because there's no need to return
    anything else.
- Now the right side has been processed. `print('hello')` returned
    None, so we can imagine we have None instead of `print('hello')`
    there, and the assignment now looks like `x = None`.
- x is now None.

Now we understand what a return value is. When we call the function,
Python "replaces" `function(args)` with whatever the function returns.

Calling a function without assigning the return value to anything (e.g.
`print('hello')` instead of `x = print('hello')`) simply throws away
the return value. The interactive `>>>` prompt doesn't echo the return
value back because it's None.

Of course, `x = print('hello')` is useless compared to `print('hello')`
because the print function always returns None and we can do `x = None`
without any printing.

Not all functions return None. The input function can be used for
getting a string from the user.

```py
>>> x = input("Enter something:")
Enter something:hello
>>> x
'hello'
>>> 
```

`input("Enter something:")` showed the text `Enter something:` on the
screen and waited for me to type something. I typed hello and pressed
Enter. Then input returned the hello I typed as a string and it was
assigned to x.

Usually we want to add a space after the `:`, like this:

```py
>>> x = input("Enter something: ")  # now there's space between : and where i type
Enter something: hello
>>> 
```

## More about print

We can also print an empty line by calling print without any
arguments.

```py
>>> print()

>>> 
```

In Python, `\n` is a newline character. Printing a string that contains
a newline character also prints a newline:

```py
>>> print('hello\nworld')
hello
world
>>> 
```

If we want to print a backslash, we need to **escape** it by typing
two backslashes.

[comment]: # (For some reason, GitHub's syntax highlighting doesn't)
[comment]: # (work here.)

    >>> print('hello\\nworld')
    hello\nworld
    >>> 

We can also pass multiple arguments to the print function. We need to
separate them with commas and print will add spaces between them.

```py
>>> print("Hello", "World!")
Hello World!
>>> 
```

Unlike with `+`, the arguments don't need to be strings.

```py
>>> print(42, "is an integer, and the value of pi is", 3.14)
42 is an integer, and the value of pi is 3.14
>>> 
```

## Summary

- `function()` calls a function without any arguments, and
    `function(1, 2, 3)` calls a function with 1, 2 and 3 as arguments.
- When a function is called, it does something and returns something.
- `function(stuff)` is "replaced" with the return value in the code
    that called it. For example, `x = function()` calls a function, and
    then does `x = the_return_value` and the return value ends up in x.
- Python comes with `print` and `input`. They are built-in functions.
