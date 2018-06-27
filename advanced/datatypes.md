# Handy data types in the standard library

[comment]: # (this doesn't explain how dict.setdefault and collections.defaultdict)
[comment]: # (work because they're not as simple as the things that are here and i)
[comment]: # (don't actually use them that much)

Now we know how to use lists, tuples and dictionaries. They are commonly
used data types in Python, and there's nothing wrong with them. In this
chapter we'll learn more data types that make some things easier. You
can always do everything with lists and dictionaries, but these data
types can do a lot of the work for you.

> If it looks like a duck and quacks like a duck, it must be a duck.

Many things in this tutorial are not really something but they behave
like something. For example, we'll learn about many classes that behave
like dictionaries. They are not dictionaries, but we can use them just
like if they were dictionaries. This programming style is known as
**duck-typing**.

## Sets

Let's say we have a program that keeps track of peoples' names. We can
store the names in [a list](../basics/lists-and-tuples.md), and adding a
new name is easy as appending to that list. Lists remember their order
and it's possible to add the same thing multiple times.

```python
>>> names = ['wub_wub', 'theelous3', 'RubyPinch', 'go|dfish', 'Nitori']
>>> names.append('Akuli')
>>> names.append('Akuli')
>>> names
['wub_wub', 'theelous3', 'RubyPinch', 'go|dfish', 'Nitori', 'Akuli', 'Akuli']
>>>
```

This is usually what we need, but sometimes it's not. Sometimes we just
want to store a bunch of things. We don't need to have the same thing
twice and we don't care about the order.

This is when sets come in. They are like lists without order or
duplicates, or keys of [dictionaries](../basics/dicts.md) without the
values. We can create a set just like a dictionary, but without `:`.

```python
>>> names = {'wub_wub', 'theelous3', 'RubyPinch', 'go|dfish', 'Nitori'}
>>> names
{'RubyPinch', 'theelous3', 'go|dfish', 'wub_wub', 'Nitori'}
>>> type(names)
<class 'set'>
>>> 'wub_wub' in names
True
>>>
```

We can also convert anything [iterable](../basics/loops.md#summary) to a
set [by calling the
class](../basics/classes.md#what-are-classes).

```python
>>> set('hello')
{'o', 'e', 'h', 'l'}
>>> type(set('hello'))
<class 'set'>
>>>
```

When we did `set('hello')` we lost one `l` and the set ended up in a
different order because sets don't contain duplicates or keep track of
their order.

Note that `{}` is a dictionary because dictionaries are used more often
than sets, so we need `set()` if we want to create an empty set.

```python
>>> type({'a', 'b'})
<class 'set'>
>>> type({'a'})
<class 'set'>
>>> type({})
<class 'dict'>
>>> type(set())     # set() is an empty set
<class 'set'>
>>>
```

Sets have a `remove` method just like lists have, but they have an `add`
method instead of `append`.

```python
>>> names = {'theelous3', 'wub_wub'}
>>> names.add('Akuli')
>>> names
{'wub_wub', 'Akuli', 'theelous3'}
>>> names.remove('theelous3')
>>> names
{'wub_wub', 'Akuli'}
>>>
```

That's the boring part. Now let's have a look at some really handy
things we can do with sets:

```python
>>> a = {'RubyPinch', 'theelous3', 'go|dfish'}
>>> b = {'theelous3', 'Nitori'}
>>> a & b      # names in a and b
{'theelous3'}
>>> a | b      # names in a, b or both
{'Nitori', 'theelous3', 'go|dfish', 'RubyPinch'}
>>> a ^ b      # names in a or b, but not both
{'RubyPinch', 'Nitori', 'go|dfish'}
>>> a - b      # names in a but not in b
{'go|dfish', 'RubyPinch'}
>>>
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
like `website[1] > 2010` it doesn't make much sense, like
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
>>>
```

As you can see, our `github` behaves like a tuple, but things like
`github.founding_year` also work and `github` looks nice when we have a
look at it on the `>>>` prompt.

## Deques

To understand deques, we need to first learn about a list method I
haven't talked about earlier. It's called `pop` and it works like this:

```python
>>> names = ['wub_wub', 'theelous3', 'Nitori', 'RubyPinch', 'go|dfish']
>>> names
['wub_wub', 'theelous3', 'Nitori', 'RubyPinch', 'go|dfish']
>>> names.pop()
'go|dfish'
>>> names
['wub_wub', 'theelous3', 'Nitori', 'RubyPinch']
>>> names.pop()
'RubyPinch'
>>> names
['wub_wub', 'theelous3', 'Nitori']
>>>
```

The list shortens from the end by one when we pop from it, and we also
get the removed item back. So we can add an item to the end of a list
using `append`, and we can remove an item from the end using `pop`.

It's also possible to do these things in the beginning of a list, but
lists were not designed to be used that way and it would be slow if our
list would be big. The `collections.deque` class makes appending and
popping from both ends easy and fast. It works just like lists, but it
also has `appendleft` and `popleft` methods.

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

The deque behaves a lot like lists do, and we can do `list(names)` if we
need a list instead of a deque for some reason.

Deques are often used as queues. It means that items are always added to
one end and popped from the other end.

## Counting things

Back in [the dictionary chapter](../basics/dicts.md#examples) we learned
to count the number of words in a sentence like this:

```python
sentence = input("Enter a sentence: ")
counts = {}
for word in sentence.split():
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
```

This code works just fine, but there are easier ways to do this. For
example, we could use the `get` method. It works so that
`the_dict.get('hi', 'hello')` tries to give us `the_dict['hi']` but
gives us `'hello'` instead if `'hi'` is not in the dictionary.

```python
>>> the_dict = {'hi': 'this is working'}
>>> the_dict.get('hi', 'lol its not there')
'this is working'
>>> the_dict.get('hello', 'lol its not there')
'lol its not there'
>>>
```

So we could write code like this instead:

```python
sentence = input("Enter a sentence: ")
counts = {}
for word in sentence.split():
    counts[word] = counts.get(word, 0) + 1
```

Counting things like this is actually so common that there's [a
class](../basics/classes.md) just for that. It's called
`collections.Counter` and it works like this:

```python
>>> import collections
>>> words = ['hello', 'there', 'this', 'test', 'is', 'a', 'hello', 'test']
>>> counts = collections.Counter(words)
>>> counts
Counter({'test': 2, 'hello': 2, 'is': 1, 'this': 1, 'there': 1, 'a': 1})
>>>
```

Now `counts` is a Counter object. It behaves a lot like a dictionary,
and everything that works with a dictionary should also work with a
counter. We can also convert the counter to a dictionary by doing
`dict(the_counter)` if something doesn't work with a counter.

```python
>>> for word, count in counts.items():
...     print(word, count)
...
test 2
is 1
this 1
there 1
a 1
hello 2
>>>
```

## Combining dictionaries

We can add together strings, lists, tuples and sets easily.

```python
>>> "hello" + "world"
'helloworld'
>>> [1, 2, 3] + [4, 5]
[1, 2, 3, 4, 5]
>>> (1, 2, 3) + (4, 5)
(1, 2, 3, 4, 5)
>>> {1, 2, 3} | {4, 5}
{1, 2, 3, 4, 5}
>>>
```

But how about dictionaries? They can't be added together with `+`.

```python
>>> {'a': 1, 'b': 2} + {'c': 3}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
>>>
```

Dictionaries have an `update` method that adds everything from another
dictionary into it. So we can merge dictionaries like this:

```python
>>> merged = {}
>>> merged.update({'a': 1, 'b': 2})
>>> merged.update({'c': 3})
>>> merged
{'c': 3, 'b': 2, 'a': 1}
>>>
```

Or we can [write a function](../basics/defining-functions.md) like this:

```python
>>> def merge_dicts(dictlist):
...     result = {}
...     for dictionary in dictlist:
...         result.update(dictionary)
...     return result
...
>>> merge_dicts([{'a': 1, 'b': 2}, {'c': 3}])
{'c': 3, 'b': 2, 'a': 1}
>>>
```

Kind of like counting things, merging dictionaries is also a commonly
needed thing and there's a class just for it in the `collections`
module. It's called ChainMap:

```python
>>> import collections
>>> merged = collections.ChainMap({'a': 1, 'b': 2}, {'c': 3})
>>> merged
ChainMap({'b': 2, 'a': 1}, {'c': 3})
>>>
```

Our `merged` is kind of like the Counter object we created earlier. It's
not a dictionary, but it behaves like a dictionary.

```python
>>> for key, value in merged.items():
...     print(key, value)
...
c 3
b 2
a 1
>>> dict(merged)
{'c': 3, 'b': 2, 'a': 1}
>>>
```

Starting with Python 3.5 it's possible to merge dictionaries like this.
**Don't do this unless you are sure that no-one will need to run your
code on Python versions older than 3.5.**

```python
>>> first = {'a': 1, 'b': 2}
>>> second = {'c': 3, 'd': 4}
>>> {**first, **second}
{'d': 4, 'c': 3, 'a': 1, 'b': 2}
>>>
```

## Summary

- Duck typing means requiring some behavior instead of some type. For
  example, instead of making a function that takes a list we could make
  a function that takes anything [iterable](../basics/loops.md#summary).
- Sets and the collections module are handy. Use them.

***

If you have trouble with this tutorial please [tell me about
it](../contact-me.md) and I'll make this tutorial better. If you
like this tutorial, please [give it a
star](../README.md#how-can-i-thank-you-for-writing-and-sharing-this-tutorial).

You may use this tutorial freely at your own risk. See
[LICENSE](../LICENSE).

[Previous](../basics/docstrings.md) | [Next](functions.md) |
[List of contents](../README.md#advanced)
