# Handy classes in the standard library

So far we have learned to use lists, tuples and dictionaries. They are 
commonly used data types in Python. The standard library contains more 
handy types that behave a lot like the datatypes that we know already. 
You can always use the built-in types instead of the collections module, 
but sometimes the collections module makes everything a lot easier.

## Sets

Let's say we have two lists of strings

```python

```

## Named tuples

It can be tempting to make a class that just contains a bunch of data 
and that's it.

```python
class Website:

    def __init__(self, url, founding_year, free_to_use):
        self.url = url
        self.founding_year = founding_year
        self.free_to_use = free_to_use


github = Website('https://github.com/', 2008, True)
```

You should avoid making classes like this. This class has only one 
method, so it doesn't really need to be a class. We could just use a 
tuple instead:

```python
github = ('https://github.com/', 2008, True)
```

The problem with this is that if someone reading our code sees something 
like `website[1] > 2010` it's not going to make much sense, like 
`website.founding_year > 2010` would.

In cases like this, `collections.namedtuple` is handy:

```python
>>> Website = collections.namedtuple('Website', 'url founding_year free_to_use')
>>> github = Website('https://github.com/', 2008, True)
>>> github[1]
2008
>>> for thing in github:
...     print(thing)
... 
https://github.com/
2008
True
>>> github.founding_year
2008
>>> github
Website(url='https://github.com/', founding_year=2008, free_to_use=True)
>>> print(github)
Website(url='https://github.com/', founding_year=2008, free_to_use=True)
>>>
```

As you can see, our `github` behaves like a tuple, but 
`github.founding_year` also works and `github` looks nice when we have a 
look at it on the `>>>` prompt or we print it.

## Deques

To understand deques, we need to first learn about a list method I 
haven't talked about earlier. It's called `pop` and it works like this:

```python
>>> names = ['wub_wub', 'theelous3', 'Nitori', 'RubyPinch', 'go|dfish']
>>> names.pop()
'go|dfish'
>>> names
['wub_wub', 'theelous3', 'Nitori', 'RubyPinch']
>>> names.pop()
'RubyPinch'
>>> names
['wub_wub', 'theelous3', 'Nitori']
>>> names.pop()
'Nitori'
>>> names
['wub_wub', 'theelous3']
```

As you can see, the list shortens by one from the end when we pop from 
it, and we also get the removed value back. So now we know that we can 
add an item to the end of a list using `append`, and we can remove an 
item from the end using `pop`.

It's also possible to do this in the beginning of a list, but lists were 
not designed to be used that way and it would be slow if our list would 
be big.

The `collections.deque` class makes appending and popping from both ends 
easy and fast. It works just like lists, but it also has `appendleft` 
and `popleft` methods.

```python
>>> names = collections.deque(['theelous3', 'Nitori', 'RubyPinch'])
>>> names
deque(['theelous3', 'Nitori', 'RubyPinch'])
>>> names.appendleft('wub_wub')
>>> names.append('go|dfish')
>>> names
deque(['wub_wub', 'theelous3', 'Nitori', 'RubyPinch', 'go|dfish'])
>>> names.popleft()
'wub_wub'
>>> names.pop()
'go|dfish'
>>> names
deque(['theelous3', 'Nitori', 'RubyPinch'])
>>> 
```

Deques are often used as queues. It means that items are always added to 
one end and popped from the other end.


**TODO:** add some of ChainMap, Counter, OrderedDict, defaultdict, deque, sets
