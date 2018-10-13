# Defining and using custom classes

When I was getting started in Python I learned to make classes for
tkinter GUI's before I understood how they work. Everything I did with
classes worked, but I didn't understand how. Hopefully you'll first
learn to understand classes, and then learn to use them.

## What are classes?

Python comes with many classes that we know already.

```python
>>> str
<class 'str'>
>>> int
<class 'int'>
>>> list
<class 'list'>
>>> dict
<class 'dict'>
>>>
```

Calling these classes as if they were functions makes a new **instance**
of them. For example, `str()` makes a `str` instance, also known as a
string.

```python
>>> str()
''
>>> int()
0
>>> list()
[]
>>> dict()
{}
>>>
```

We can also get an instance's class with `type()`:

```python
>>> type('')
<class 'str'>
>>> type(0)
<class 'int'>
>>> type([])
<class 'list'>
>>> type({})
<class 'dict'>
>>>
```

Let's say that we make a program that processes data about websites.
With a custom class, we're not limited to `str`, `int` and other classes
Python comes with. Instead we can define a Website class, and make
Websites and process information about websites directly. Defining our
own types like this is called **object-orientated programming**.

## First class

In Python, `pass` does nothing.

```python
>>> pass
>>>
```

Let's use it to define an empty class.

```python
>>> class Website:
...     pass
...
>>> Website
<class '__main__.Website'>
>>>
```

The `pass` is needed here, just like [when defining functions that do
nothing](defining-functions.md#first-functions).

Note that I named the class `Website`, not `website`. This way we know
that it's a class. Built-in classes use lowercase names (like `str`
instead of `Str`) because they are faster to type, but use CapsWord
names for your classes.

Now we can make a Website instance by calling the class.

```python
>>> github = Website()
>>> github
<__main__.Website object at 0x7f36e4c456d8>
>>> type(github)
<class '__main__.Website'>
>>>
```

We can say that `github` is "a Website instance", "a Website
object" or "a Website". All of these mean the same thing.

Now we can attach more information about github to our Website.

```python
>>> github.url = 'https://github.com/'
>>> github.founding_year = 2008
>>> github.free_to_use = True
>>>
```

We can also access the information easily.

```python
>>> github.url
'https://github.com/'
>>> github.founding_year
2008
>>> github.free_to_use
True
>>>
```

As you can see, our Website is mutable, like lists are, not immutable
like strings are. We can change the website in-place without creating a
new Website.

`url`, `founding_year` and `free_to_use` are not variables, they are
**attributes**. More specifically, they are **instance attributes**.
The biggest difference is that we need to use a dot for setting and
getting values of attributes, but we don't need that with variables.

Modules also use instance attributes for accessing their content. For
example, when we do `random.randint`, `random` is a module instance and
`randint` is one of its attributes.

If we make another Website, does it have the same `url`, `founding_year`
and `free_to_use`?

```python
>>> effbot = Website()
>>> effbot.url
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Website' object has no attribute 'url'
>>>
```

It doesn't. We'd need to define the attributes for effbot also.

The attributes are stored in a dictionary called `__dict__`. It's not
recommended to use it for code that needs to be reliable, but it's a
handy way to see which attributes the instance contains.

```python
>>> github.__dict__
{'free_to_use': True,
 'founding_year': 2008,
 'url': 'https://github.com/'}
>>> effbot.__dict__
{}
>>>
```

## Class attributes

What happens if we set an attribute of the `Website` class to some value
instead of doing that to an instance?

```python
>>> Website.is_online = True
>>> Website.is_online
True
>>>
```

Seems to be working, but what happened to the instances?

```python
>>> github.is_online
True
>>> effbot.is_online
True
>>>
```

What was that? Setting `Website.is_online` to a value also set
`github.is_online` and `effbot.is_online` to that value!

Actually, `is_online` is still not in github's or effbot's
`__dict__`. github and effbot get that attribute directly from
the `Website` class.

```python
>>> github.__dict__
{'free_to_use': True,
 'founding_year': 2008,
 'url': 'https://github.com/'}
>>> effbot.__dict__
{}
>>>
```

`Website.is_online` is `Website`'s class attribute, and in Python you can
access class attributes through instances also, so in this case
`github.is_online` points to `Website.is_online`. That can be
confusing, which is why it's not recommended to use class attributes like
this. Use instance attributes instead, e.g. `github.is_online = True`.

## Functions and methods

Let's [define a function](defining-functions.md) that prints information
about a website.

```python
>>> def website_info(website):
...     print("URL:", website.url)
...     print("Founding year:", website.founding_year)
...     print("Free to use:", website.free_to_use)
...
>>> website_info(github)
URL: https://github.com/
Founding year: 2008
Free to use: True
>>>
```

Seems to be working. We should be able to get information about all
websites, so maybe we should attach the `website_info` function to the
Website class?

```python
>>> Website.info = website_info
>>> Website.info(github)
URL: https://github.com/
Founding year: 2008
Free to use: True
>>>
```

It's working, but `Website.info(github)` is a lot of typing, so
wouldn't `github.info()` be much better?

```python
>>> github.info()
URL: https://github.com/
Founding year: 2008
Free to use: True
>>>
```

What the heck happened? We didn't define a `github.info`, it just
magically worked!

`Website.info` is our `website_info` function, so `github.info`
should also be the same function. But `Website.info` takes a `website`
argument, which we didn't give it when we called `github.info()`!

But is `github.info` the same thing as `Website.info`?

```python
>>> Website.info
<function website_info at 0x7f36e4c39598>
>>> github.info
<bound method website_info of <__main__.Website object at 0x7f36e4c456d8>>
>>>
```

It's not.

Instead, `github.info` is a **method**. If we set a function as a
class attribute, the instances will have a method with the same name.
Methods are "links" to the class attribute functions. So
`Website.info(github)` does the same thing as `github.info()`,
and when `github.info()` is called it automatically gets
`github` as an argument.

In other words, **`Class.method(instance)` does the same thing as
`instance.method()`**. This also works with built-in classes, for
example `'hello'.lower()` is same as `str.lower('hello')`.

## Defining methods when defining the class

Maybe we could define a method when we make the class instead of adding
it later?

```python
>>> class Website:
...     def info(self):     # self will be github
...         print("URL:", self.url)
...         print("Founding year:", self.founding_year)
...         print("Free to use:", self.free_to_use)
...
>>> github = Website()
>>> github.url = 'https://github.com/'
>>> github.founding_year = 2008
>>> github.free_to_use = True
>>> github.info()
URL: https://github.com/
Founding year: 2008
Free to use: True
>>>
```

It's working. The `self` argument in `Website.info` was `github`.
You could call it something else too such as `me`, `this` or `instance`,
but use `self` instead. Other Python users have gotten used to it, and
the official style guide recommends it also.

We still need to set `url`, `founding_year` and `free_to_use` manually.
Maybe we could add a method to do that?

```python
>>> class Website:
...     def initialize(self, url, founding_year, free_to_use):
...         self.url = url
...         self.founding_year = founding_year
...         self.free_to_use = free_to_use
...     def info(self):
...         print("URL:", self.url)
...         print("Founding year:", self.founding_year)
...         print("Free to use:", self.free_to_use)
...
>>> github = Website()
>>> github.initialize('https://github.com/', 2008, True)
>>> github.info()
URL: https://github.com/
Founding year: 2008
Free to use: True
>>>
```

That works. The attributes we defined in the initialize method are also
available in the info method. We could also access them directly from
`github`, for example with `github.url`.

But we still need to call `github.initialize`. In Python, there's
a "magic" method that runs when we create a new Website by calling the
Website class. It's called `__init__` and it does nothing by default. If
our `__init__` method takes other arguments than self we can call the
class with arguments and they will be given to `__init__`. Like this:

```python
>>> class Website:
...     def __init__(self, url, founding_year, free_to_use):
...         self.url = url
...         self.founding_year = founding_year
...         self.free_to_use = free_to_use
...     def info(self):
...         print("URL:", self.url)
...         print("Founding year:", self.founding_year)
...         print("Free to use:", self.free_to_use)
...
>>> github = Website('https://github.com/', 2008, True)
>>> github.info()
URL: https://github.com/
Founding year: 2008
Free to use: True
>>>
```

Classes have many other magic methods too, but I'm not going to cover
them in this tutorial.

## When should I use classes?

Don't do this:

```python
class MyProgram:

    def __init__(self):
        print("Hello!")
        word = input("Enter something: ")
        print("You entered " + word + ".")


program = MyProgram()
```

You should avoid using things like `print` and `input` in the `__init__`
method. The `__init__` method should be simple and it should just set
things up.

Usually you shouldn't use a class if you're only going to make one
instance of it, and you don't need a class either if you're only going
to have one method. In this example `MyProgram` has only one method and
only one instance.

Make functions instead, or just write your code without any functions if
it's short enough for that. This program does the same thing and it's
much more readable:

```python
print("Hello!")
word = input("Enter something: ")
print("You entered " + word + ".")
```

## Summary

- Object-orientated programming is programming with custom data types.
  In Python that means using classes and instances.
- Use CapsWords for class names and lowercase_words_with_underscores for
  other names. This makes it easy to see which objects are classes and
  which objects are instances.
- Calling a class as if it was a function makes a new instance of it.
- `foo.bar = baz` sets `foo`'s attribute `bar` to `baz`.
- Use class attributes for functions and instance attributes for other
  things.
- Functions as class attributes can be accessed as instance methods.
  They get their instance as the first argument. Call that `self` when
  you define the method.
- `__init__` is a special method, and it's ran when a new instance of a
  class is created. It does nothing by default.
- Don't use classes if your code is easier to read without them.

***

If you have trouble with this tutorial please [tell me about
it](../contact-me.md) and I'll make this tutorial better. If you
like this tutorial, please [give it a
star](../README.md#how-can-i-thank-you-for-writing-and-sharing-this-tutorial).

You may use this tutorial freely at your own risk. See
[LICENSE](../LICENSE).

[Previous](exceptions.md) | [Next](docstrings.md) |
[List of contents](../README.md#basics)
