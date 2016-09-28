# Iterables and iterators

We have used for loops in many exercises and other things so far. One of
the simplest things we can for loop over are lists.

```py
>>> for item in ['a', 'b', 'c']:
...     print(item)
... 
a
b
c
>>> 
```

But what exactly is happening behind the scenes?

## Iterables

An **iterable** is anything we can put after a `for item in`. For
example, strings, lists, tuples and dictionaries are all iterable.
Iterating over an iterable is simple:

```py
string = 'hello'
for character in string:
    print(character)
```

You might think that under the covers Python does something like this:

```py
string = 'hello'
index = 0
while index < len(string):
    print(string[index])
    index += 1
```

But actually, th
