# Using functions

Now we know how to make Python show text.

```python
>>> 'Hello!'
'Hello!'
>>>
```

But that includes `''`. One way to show text to the user without `''`
is with the print function. In Python, printing doesn't have anything
to do with physical printers, it just means showing text on the screen.

```python
>>> print('Hello!')
Hello!
>>>
```

Now we are ready for a classic example, which is also the first program
in many tutorials :)

```python
>>> print("Hello World!")
Hello World!
>>>
```

But what exactly is print?

## What are functions?

Let's see what happens if we type `print` without the `('Hello')` part.

```python
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

Sometimes people think that doing `thingy = print('hello')` means that
Python is going to print hello every time we type `thingy`. But **this
is not correct**! `print('hello')` runs print right away, and if we
type `thingy` later it's not going to run `print('hello')` again.

## Return values

Now we know that `thingy = print('hello')` doesn't store the
`print('hello')` call in a variable. But what does it do then?

```python
>>> thingy = print('hello')
hello
>>> print(thingy)       # thingy is now None
None
>>>
```

So doing `thingy = print('hello')` set `thingy` to None.

Here's what happened, explained in more detail:

- When we do `thingy = print('hello')`, the right side is processed
    first.
- `print('hello')` calls the print function with the argument
    `'hello'`.
- The function runs. It shows the word hello.
- The print function **returns** None. All functions need to return
    something, and print returns None because there's no need to return
    anything else.
- Now the right side has been processed. `print('hello')` returned
    None, so we can imagine we have None instead of `print('hello')`
    there, and the assignment now looks like `thingy = None`.
- `thingy` is now None.

Now we understand what **a return value** is. When we call the
function, Python "replaces" `function(arguments)` with whatever the
function returns.

Calling a function without assigning the return value to anything (e.g.
`print('hello')` instead of `thingy = print('hello')`) simply throws away
the return value. The interactive `>>>` prompt doesn't echo the return
value back because it's None.

Of course, `thingy = print('hello')` is useless compared to `print('hello')`
because the print function always returns None and we can do `thingy = None`
without any printing.

Not all functions return None. The input function can be used for
getting a string from the user.

```python
>>> stuff = input("Enter something:")
Enter something:hello
>>> stuff
'hello'
>>>
```

`input("Enter something:")` showed the text `Enter something:` on the
screen and waited for me to type something. I typed hello and pressed
Enter. Then input returned the hello I typed as a string and it was
assigned to `stuff`.

Usually we want to add a space after the `:`, like this:

```python
>>> stuff = input("Enter something: ")  # now there's space between : and where i type
Enter something: hello
>>>
```

## Handy things about print

We can also print an empty line by calling print without any
arguments.

```python
>>> print()

>>>
```

In Python, `\n` is a newline character. Printing a string that contains
a newline character also prints a newline:

```python
>>> print('hello\nworld')
hello
world
>>>
```

If we want to print a real backslash, we need to **escape** it by typing
two backslashes.

[comment]: # (For some reason, GitHub's syntax highlighting doesn't)
[comment]: # (work here.)

    >>> print('hello\\nworld')
    hello\nworld
    >>>

We can also pass multiple arguments to the print function. We need to
separate them with commas and print will add spaces between them.

```python
>>> print("Hello", "World!")
Hello World!
>>>
```

Unlike with `+`, the arguments don't need to be strings.

```python
>>> print(42, "is an integer, and the value of pi is", 3.14)
42 is an integer, and the value of pi is 3.14
>>>
```

## Variables names and built-in things

In [the previous chapter](variables.md) we learned that `if` is not a
valid variable name because it's a keyword.

```python
>>> if = 123
  File "<stdin>", line 1
    if = 123
       ^
SyntaxError: invalid syntax
>>>
```

But `print` and `input` are not keywords, so can we use them as
variable names?

```python
>>> print = "hello"
>>> print
'hello'
>>>
```

We can, but there's a problem. Now we can't even do our hello world!

```python
>>> print("Hello World!")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object is not callable
>>>
```

The error message complains that strings aren't callable because we just
set `print` to the string `'hello'` and now we're trying to call it like
a function. As you can see, **this is not a good idea** at all. Most
[editors](editor-setup.md) display built-in functions with a special
color, so you don't need to worry about doing this accidentally.

Exit out of Python and start it again, and `print("Hello World!")`
should work normally.

## Summary

- `function()` calls a function without any arguments, and
    `function(1, 2, 3)` calls a function with 1, 2 and 3 as arguments.
- When a function is called, it does something and returns something.
- `function(arguments)` is "replaced" with the return value in the code
    that called it. For example, `stuff = function()` calls a function,
    and then does `stuff = the_return_value` and the return value ends
    up in stuff.
- Python comes with `print` and `input`. They are built-in functions.
- Avoid variable names that conflict with built-in functions.

***

If you have trouble with this tutorial please [tell me about
it](../contact-me.md) and I'll make this tutorial better. If you
like this tutorial, please [give it a
star](../README.md#how-can-i-thank-you-for-writing-and-sharing-this-tutorial).

You may use this tutorial freely at your own risk. See
[LICENSE](../LICENSE).

[Previous](variables.md) | [Next](editor-setup.md) |
[List of contents](../README.md#basics)
