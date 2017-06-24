# Help and Docstrings

In this tutorial we have used `help()` a few times. It's great and you
can use it as much as you want to. For example, running `help(str)`
displays a nice list of all string methods and explanations of what they
do, and `help(list.extend)` explains what extending something to a list
does.

You can get help of many other things too. For example:

```python
>>> stuff = []
>>> help(stuff.append)
Help on built-in function append:

append(object, /) method of builtins.list instance
    Append object to the end of the list.

>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    ...
```

## Docstrings

Let's see what happens if we [define a function](defining-functions.md)
and call `help()` on that.

```python
>>> def thing(stuff):
...     return stuff * 2
...
>>> help(thing)
Help on function thing in module __main__:

thing(stuff)
>>>
```

That sucked! We have no idea about what it does based on this. All we
know is that it takes a `thing` argument.

This is when documentation strings or docstrings come in. All we need to
do is to add a string to the beginning of our function and it will show
up in `help(the_function)`. Like this:

```python
>>> def thing(stuff):
...     "hello there"
...     return stuff * 2
...
>>> help(thing)
Help on function thing in module __main__:

thing(stuff)
    hello there
```

Note that docstrings are not comments. If you add a `# comment` to the
beginning of the function it won't show up in `help()`.

## Multi-line strings

When we did `help(print)`, we got more than one line of help. Maybe we
could do that in our own docstring too?

```python
>>> def thing():
...     "This thing does stuff.\n\nIt always returns None."
...
>>> help(thing)
Help on function thing in module __main__:

thing()
    This thing does stuff.

    It always returns None.
>>>
```

That's better, but how what if we want to do 5 lines of prints? Our
`"stuff\n\nstuff\nstuff"` thing would be really long and hard to work
with. But Python has multi-line strings too. They work like this:

```python
>>> """bla bla bla
...
... bla bla
... bla bla bla"""
'bla bla bla\n\nbla bla\nbla bla bla'
>>>
```

So we can write documented functions like this:

```python
>>> def thing():
...     """This thing does stuff.
...
...     It always returns None.
...     """
...
>>> help(thing)
Help on function thing in module __main__:

thing()
    This thing does stuff.

    It always returns None.

>>>
```

It's recommended to always use `"""strings like this"""` for docstrings,
even if the docstring is only one line long. This way it's easy to add
more stuff to it later.

## Documenting other stuff

Docstrings aren't actually limited to functions. You can use them for
documenting [classes](classes.md) and their methods too. For example,
let's make a file like this and save it to `test.py`:

```python
"""A test module.

It contains a class and a function.
"""


class Thing:
    """This is a test class."""

    def thingy(self):
        """This is a test method."""
        print("hello")


def do_hello():
    """This is a test function."""
    thing = Thing()
    thing.thingy()
```

Then we can import it and call help on it:

[comment]: # (github screws up syntax highlighting here)

```
>>> import test
>>> help(test)
Help on module testie:

NAME
    testie - A test module.

DESCRIPTION
    It contains a class and a function.

CLASSES
    builtins.object
        Thing

    class Thing(builtins.object)
     |  This is a test class.
     |
     |  Methods defined here:
     |
     |  thingy(self)
     |      This is a test method.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)

FUNCTIONS
    do_hello()
        This is a test function.

FILE
    /home/akuli/testie.py
```

That's pretty cool. We just added docstrings to our code and Python made
this thing out of it.

You might be wondering what `__weakref__` is. You don't need to care
about it, and I think it would be better if `help()` would hide it.

## When should we use docstrings?

Always use docstrings when writing code that other people will import.
The `help()` function is awesome, so it's important to make sure it's
actually helpful.

If your code is not meant to be imported, docstrings are usually a good
idea anyway. Other people reading your code will understand what it's
doing without having to read through all of the code.

## Summary

- `help()` is awesome.
- A `"""triple-quoted string"""` string in the beginning of a function,
  class or file is a docstring. It shows up in `help()`.
- Docstrings are not comments.
- Usually it's a good idea to add docstrings everywhere

***

If you have trouble with this tutorial please [tell me about
it](../contact-me.md) and I'll make this tutorial better. If you
like this tutorial, please [give it a
star](../README.md#how-can-i-thank-you-for-writing-and-sharing-this-tutorial).

You may use this tutorial freely at your own risk. See
[LICENSE](../LICENSE).

[Previous](classes.md) | [Next](../advanced/datatypes.md) |
[List of contents](../README.md#basics)
