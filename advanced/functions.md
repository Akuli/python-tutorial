# Advanced things with functions

Now we know [how to define functions](../basics/defining-functions.md).
Functions can take arguments, and they will end up with local variables
that have the same name. Like this:

```py
def print_box(message, border='*'):
    print(border * (len(message) + 4))
    print(border, message, border)
    print(border * (len(message) + 4))

print_box("hello")
```

In this chapter we'll learn more things we can do with defining
functions and how they are useful.

## Multiple return values

Function can take multiple arguments, but they can only return one
value. But sometimes it makes sense to return multiple values as well:

```py
def login():
    username = input("Username: ")
    password = input("Password: ")
    # how the heck are we going to return these?
```

The best solution is to return a tuple of values, and just unpack that
wherever the function is called:

```py
def login():
    ...
    return username, password


username, password = login()
...
```

That gets kind of messy if there are more than three values to return,
but I have never needed to return more than three values. If you think
you need to return four or more values you probably want to use [a
class](../basics/classes.md) instead and store the values like
`self.thing = stuff`.

## \*args

Sometimes you might see code like this:

```py
def thing(*args, **kwargs):
    ...
```

Functions like this are actually quite easy to understand. Let's make a
function that takes `*args` and prints it.

```py
>>> def thing(*args):
...     print("now args is", args)
...
>>> thing()
now args is ()
>>> thing(1, 2, 3)
now args is (1, 2, 3)
>>>
```

So far we have learned that if we want to call a function like
`thing(1, 2, 3)`, then we need to define the arguments when defining the
function like `def thing(a, b, c)`. But `*args` just magically gets
whatever positional arguments the function is given and turns them into
a tuple, and never raises errors. Of course, we could also use whatever
variable name we wanted instead of `args`.

Our function with nothing but `*args` takes no keyword arguments:

```py
>>> thing(a=1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: thing() got an unexpected keyword argument 'a'
>>>
```

We can also save our arguments to a variable as a list, and then pass
them to a function by adding a `*`. Actually it doesn't need to be a
list or a tuple, anything [iterable](../basics/loops.md#summary) will
work.

```py
>>> stuff = ['hello', 'world', 'test']
>>> print(*stuff)
hello world test
>>>
```

## \*\*kwargs

`**kwargs` is the same thing as `*args`, but with keyword arguments
instead of positional arguments.

```py
>>> def thing(**kwargs):
...     print('now kwargs is', kwargs)
...
>>> thing(a=1, b=2)
now kwargs is {'b': 2, 'a': 1}
>>> thing(1, 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: thing() takes 0 positional arguments but 2 were given
>>> def print_box(message, border='*'):
...     print(border * len(message))
...     print(message)
...     print(border * len(message))
...
>>> kwargs = {'message': "Hello World!", 'border': '-'}
>>> print_box(**kwargs)
------------
Hello World!
------------
>>>
```

Sometimes it's handy to capture all arguments our function takes. We can
combine `*args` and `**kwargs` easily:

```py
>>> def thing(*args, **kwargs):
...     print("now args is", args, "and kwargs is", kwargs)
...
>>> thing(1, 2, a=3, b=4)
now args is (1, 2) and kwargs is {'b': 4, 'a': 3}
>>>
```

This is often used for calling a function from another "fake function"
that represents it. We'll find uses for this later.

```py
>>> def fake_print(*args, **kwargs):
...     print(*args, **kwargs)
...
>>> print('this', 'is', 'a', 'test', sep='-')
this-is-a-test
>>> fake_print('this', 'is', 'a', 'test', sep='-')
this-is-a-test
>>>
```

## Keyword-only arguments

Let's say that we have a function that moves a file. It probably takes
`source` and `destination` arguments, but it might also take other
arguments that customize how it moves the file. For example, it might
take an `overwrite` argument that makes it remove `destination` before
moving if it exists already or a `backup` argument that makes it do a
backup of the file just in case the moving fails. So our function would
look like this:

```py
def move(source, destination, overwrite=False, backup=False):
    if overwrite:
        print("deleting", destination)
    if backup:
        print("backing up")
    print("moving", source, "to", destination)
```

Then we can move files like this:

```py
>>> move('file1.txt', 'file2.txt')
moving file1.txt to file2.txt
>>> move('file1.txt', 'file2.txt', overwrite=True)
deleting file2.txt
moving file1.txt to file2.txt
>>>
```

This works just fine, but if we accidentally give the function three
filenames, bad things will happen:

```py
>>> move('file1.txt', 'file2.txt', 'file3.txt')
deleting file2.txt
moving file1.txt to file2.txt
>>>
```

Oh crap, that's not what we wanted at all. We have just lost the
original `file2.txt`!

The problem was that now `overwrite` was `'file2.txt'`, and the
`if overwrite` part [treated the string as
True](../basics/what-is-true.md) and deleted the file. That's not nice.

The solution is to change our move function so that `overwrite` and
`backup` are keyword-only:

```py
def move(source, destination, *, overwrite=False, backup=False):
    ...
```

The `*` between `destination` and `overwrite` means that `overwrite` and
`backup` must be given as keyword arguments.

```py
>>> move('file1.txt', 'file2.txt', overwrite=True)
deleting file2.txt
moving file1.txt to file2.txt
>>> move('file1.txt', 'file2.txt', True)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: move() takes 2 positional arguments but 3 were given
>>>
```

As you can see, our new move function also forces everyone to use it
like `move('file1.txt', 'file2.txt', overwrite=True)` instead of
`move('file1.txt', 'file2.txt', True)`. That's good because it's hard to
guess what a positional `True` does, but it's easy to guess what
`overwrite=True` does.

## When should we use these things?

There's nothing wrong with returning a tuple from a function, and you
are free to do that whenever you need it.

We don't need `*args` and `**kwargs` for most of the functions we write.
Often functions just do something and arguments are a way to change how
they do that, and by not taking `*args` or `**kwargs` we can make sure
that we'll get an error if the function gets an invalid argument.

When we need to make something that takes whatever arguments it's given
or call a function with arguments that come from a list we need `*args`
and `**kwargs`, and there's no need to avoid them.

I don't recommend using keyword-only arguments with functions like our
`print_box`. It's easy enough to guess what `print_box('hello', '-')`
does, and there's no need to deny that. On the other hand, it's much
harder to guess what `move('file1.txt', 'file2.txt', True, False)` does,
so using keyword-only arguments makes sense and gets rid of the file
deleting problem.

## Summary

- If you want to return multiple values from a function you can return
    a tuple.
- Defining a function that takes `*args` as an argument makes `args` a
    tuple of positional arguments. `**kwargs` is the same thing with
    dictionaries and keyword arguments.
- Adding a `*` in a function definition makes all arguments after it
    keyword-only. This is useful when using positional arguments would
    look implicit, like the True and False in `move('file1.txt',
    'file2.txt', True, False)`.

***

You may use this tutorial freely at your own risk. See
[LICENSE](../LICENSE).

[Previous](../basics/classes.md) | [Next](magicmethods.md) |
[List of contents](../README.md#advanced)
