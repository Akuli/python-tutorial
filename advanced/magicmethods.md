# Magic methods

In [the class tutorial](../basics/classes.md) we learned to define a
class like this:

```py
class Website:

    def __init__(self, url, founding_year, free_to_use):
        self.url = url
        self.founding_year = founding_year
        self.free_to_use = free_to_use

    def info(self):
        print("URL:", self.url)
        print("Founding year:", self.founding_year)
        print("Free to use:", self.free_to_use)
```

After doing that we can create a new Website object like
`Website('https://github.com/', 2008, True)`. Python first creates the
Website object, and then calls `__init__` with the arguments we passed
to Website to set it up. Methods that have a name `__like_this__` and a
special meaning are called **magic methods** or **special methods**.

Most magic methods define what the object has or what it can do, like
"does it have a length" or "can we for loop over it". There are other
magic methods that do other things also, like `__init__`.

Some magic methods have a default implementation that is used if the
class doesn't define anything else. For example, if we don't define an
`__init__` then our class will take no arguments and it won't have any
attributes by default. We'll learn more about this when we'll talk about
[inheritance](classes2.md).

**TODO:** write a `classes2.md`.

## Custom len()

Let's get started by defining an object that has a length:

```py
>>> class Thing:
...     def __len__(self):
...         return 5
...
>>> t = Thing()
>>> t
<__main__.Thing object at 0x7f05e4597198>
>>> t.__len__()
5
>>> len(t)
5
>>>
```

This is what most magic methods are like. So far we have learned to use
`len()` with lists, strings and other built-in types, but now we can
call `len()` on our own Thing object. Many things can be fully
customized with magic methods.

Note that magic methods like `__len__` need to be defined in the class,
just attaching an attribute called `__len__` doesn't work:

```py
>>> class EmptyThing:
...     pass
...
>>> def length():
...     return 5
...
>>> e = EmptyThing()
>>> e.__len__ = length
>>> e.__len__()
5
>>> len(e)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type 'EmptyThing' has no len()
>>>
```

You don't really need to worry about why Python works like this, but
it's explained
[here](https://docs.python.org/3/reference/datamodel.html#special-method-lookup)
if you want to know more about it.

## Custom str() and repr()

You have probably noticed that typing something to the interactive `>>>`
prompt is not quite the same thing as printing it. For example,
strings behave like this:

```py
>>> 'hello'
'hello'
>>> print('hello')
hello
>>>
```

Typing `'hello'` without a print displayed it with quotes, but printing
it displayed it without the quotes. Both of these can be customized with
magic methods. `print('hello')` does the same thing as
`print(str('hello'))`, and typing `'hello'` without a print does roughly
the same thing as `print(repr('hello'))`.

```py
>>> repr('hello')   # a string that literally contains 'hello'
"'hello'"
>>> str('hello')    # same as just 'hello'
'hello'
>>> print(repr('hello'))
'hello'
>>> print(str('hello'))
hello
>>>
```

As usual, `repr(thing)` does the same thing as `thing.__repr__()` and
`str(thing)` does the same thing as `thing.__str__()`. Usually you don't
need to and you shouldn't define `__str__` yourself because `__str__`
defaults to `__repr__`.

Here's an example that hopefully clarifies things:

```py
>>> class Website:
...     def __repr__(self):
...         return '<a Website object>'
...
>>> w = Website()
>>> w.__repr__()
'<a Website object>'
>>> repr(w)
'<a Website object>'
>>> w.__str__()
'<a Website object>'
>>> str(w)
'<a Website object>'
>>> w
<a Website object>
>>> print(w)
<a Website object>
>>>
```

The `repr()` values can also be easily used with string formatting.
Instead of this...

```py
>>> message = 'hello'
>>> print("message is " + repr(message))
message is 'hello'
>>>
```

...you can do this:

```py
>>> print("message is %r" % message)
message is 'hello'
>>> print("message is {!r}".format(message))
message is 'hello'
>>>
```

The `__repr__` method can return any string, but usually you should
follow one of these styles:

1. A piece of code that describes how another, similar object can be
    created.

    ```py
    >>> class Website:
    ...     def __init__(self, name, founding_year):
    ...         self.name = name
    ...         self.founding_year = founding_year
    ...     def __repr__(self):
    ...         return 'Website(name=%r, founding_year=%r)' % (
    ...             self.name, self.founding_year)
    ...
    >>> github = Website('GitHub', 2008)
    >>> github
    Website(name='GitHub', founding_year=2008)
    >>>
    ```

    This is useful for simple data containers like this Website class.

2. A description of the object wrapped between `<` and `>`.

    ```py
    >>> class Website:
    ...     def __init__(self, name, founding_year):
    ...         self.name = name
    ...         self.founding_year = founding_year
    ...     def __repr__(self):
    ...         return '<Website %r, founded in %r>' % (
    ...             self.name, self.founding_year)
    ...
    >>> github = Website('GitHub', 2008)
    >>> github
    <Website 'GitHub', founded in 2008>
    >>>
    ```

    This style is good when you want to tell more about the object than
    you can by showing the `__init__` arguments. Python's built-in
    things also use this style more:

    ```py
    >>> import random
    >>> random
    <module 'random' from '/some/path/random.py'>
    >>>
    ```

## Other magic methods

There are many more magic methods, and I don't see any reason to list
them all here. [The official
documentation](https://docs.python.org/3/reference/datamodel.html) has
more information about magic methods if you need it. You can also just
keep reading this tutorial, and we'll learn more about some of the most
useful and commonly used magic methods.

## When should we use magic methods?

Usually magic methods are overkill. `website.has_user(user)` or
`user in website.userlist` is way better than something weird like
`user @ website`. People expect `website.has_user(user)` to check if
the user has registered on the website, but nobody knows what
`user @ website` does. Explicit is better than implicit, and simple is
better than complex.

On the other hand, adding informative `__repr__` methods can make a
module much nicer to use. I recommend using `__repr__` methods in things
that other people will import and use in their projects, but `__repr__`
methods aren't worth it for simple scripts that aren't meant to be
imported.

## Summary

- Magic methods define what instances of a class can do and how, like
    "does it have a length" or "what does it look like when I print it".
- Python uses magic methods to implement many things internally.
- Defining custom `__repr__` methods is often a good idea when making
    things that other people will import and use in their own projects.
    Other than that, magic methods are usually not worth it.

***

You may use this tutorial freely at your own risk. See
[LICENSE](../LICENSE).

[Previous](../basics/classes.md) | [Next](iterators.md) |
[List of contents](../README.md#advanced)
