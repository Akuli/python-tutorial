# Dictionaries

Now we know how [lists and tuples](lists-and-tuples.md) work and how
to [for loop](loops.md#for-loops) over them. If we make some kind of
program that needs to keep track of people's names and favorite pets,
we can use a list for that:

```python
names_and_pets = [
    ('horusr', 'cats'),
    ('caisa64', 'cats and dogs'),
    ('__Myst__', 'cats'),
]
```

Then to check if cats are horusr's favorite pets we can do
`('horusr', 'cats') in names_and_pets`. Or we can add new people's
favorite pets easily by appending new `(name, pets)` tuples to the list.

But what if we need to check if we know anything about someone's
favorite pets? `'caisa64' in names_and_pets` is always False because the
pet list consists of `(name, pets)` pairs instead of just names, so we
need to for loop over the whole pet list:

```python
found_caisa64 = False
for pair in names_and_pets:
    if pair[0] == 'caisa64':
        found_caisa64 = True
        break
if found_caisa64:
    # do something
```

Or what if we need to find out what caisa64's favorite pets are? That
also requires going through the whole list.

```python
pets = None
for pair in names_and_pets:
    if pair[0] == 'caisa64':
        pets = pair[1]
        break
# make sure pets is not None and do something with it
```

As you can see, a list of `(name, pets)` pairs is not an ideal
way to store names and favorite pets.

## What are dictionaries?

A better way to store information about favorite pets might be a
dictionary:

```python
favorite_pets = {
    'horusr': 'cats',
    'caisa64': 'cats and dogs',
    '__Myst__': 'cats',
}
```

Here `'horusr'` and `'caisa64'` are **keys** in the dictionary, and
`'cats'` and `'cats and dogs'` are their **values**. Dictionaries are
often named by their values. This dictionary has favorite pets as its
values so I named the variable `favorite_pets`.

There are a few big differences between dictionaries and lists of pairs:

- Dictionaries are not ordered. There are **no guarantees** about which
    order the `name: pets` pairs appear in when we do something
    with the dictionary.
- Checking if a key is in the dictionary is simple and fast. We don't
    need to for loop through the whole dictionary.
- Getting the value of a key is also simple and fast.
- We can't have the same key in the dictionary multiple times, but
    multiple different keys can have the same value. This means that
    **multiple people can't have the same name, but they can have the
    same favorite pets**.

But wait... this is a lot like variables are! Our variables are not
ordered, getting a value of a variable is fast and easy and we can't
have multiple variables with the same name.

Variables are actually stored in a dictionary. We can get that
dictionary with the globals function. In this dictionary, keys are
variable names and values are what our variables point to.

```python
>>> globals()
{'names_and_pets': [('horusr', 'cats'),
                    ('caisa64', 'cats and dogs'),
                    ('__Myst__', 'cats')],
 'favorite_pets': {'__Myst__': 'cats',
                   'caisa64': 'cats and dogs',
                   'horusr': 'cats'},
 ...many other things we don't need to care about...
}
>>>
```

So if you have trouble remembering how dictionaries work just compare
them to variables. A dictionary is a perfect way to store these names
and favorite pets. We don't care about which order the names and pets
were added in, it's impossible to add the same name multiple times and
getting someone's favorite pets is easy.

## What can we do with dictionaries?

Dictionaries have some similarities with lists. For example, both
lists and dictionaries have a length.

```python
>>> len(names_and_pets)     # contains three elements
3
>>> len(favorite_pets)    # contains three key:value pairs
3
>>>
```

We can get a value of a key with `the_dict[key]`. This is a lot easier
and faster than for-looping over a list of pairs.

```python
>>> favorite_pets['caisa64']
'cats and dogs'
>>> favorite_pets['__Myst__']
'cats'
>>>
```

Trying to get the value of a non-existing key gives us an error.

```python
>>> favorite_pets['Akuli']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Akuli'
>>>
```

But we can add new `key: value` pairs or change the values of existing
keys by doing `the_dict[key] = value`.

```python
>>> favorite_pets['Akuli'] = 'penguins'
>>> favorite_pets['Akuli']
'penguins'
>>> favorite_pets['Akuli'] = 'dogs'
>>> favorite_pets['Akuli']
'dogs'
>>> favorite_pets
{'__Myst__': 'cats',
 'Akuli': 'dogs',
 'horusr': 'cats',
 'caisa64': 'cats and dogs'}
>>>
```

For looping over a dictionary gets its keys, and checking if something
is in the dictionary checks if the dictionary has a key like that. This
can be confusing at first but you'll get used to this.

```python
>>> 'Akuli' in favorite_pets
True
>>> 'dogs' in favorite_pets
False
>>> for name in favorite_pets:
...     print(name)
...
caisa64
Akuli
__Myst__
horusr
>>>
```

Dictionaries have a values method that we can use if we want to do
something with the values:

```python
>>> favorite_pets.values()
dict_values(['dogs', 'cats', 'cats and dogs', 'cats'])
>>>
```

The values method returned a `dict_values` object. Things like this
behave a lot like lists and usually we don't need to convert them to
lists.

```python
>>> for pets in favorite_pets.values():
...     print(pets)
...
dogs
cats
cats and dogs
cats
>>>
```

We can do things like `list(favorite_pets.values())` if we need a real
list for some reason, but doing that can slow down our program if the
dictionary is big. There's also a keys method, but usually we don't need
it because the dictionary itself behaves a lot like a list of keys.

If we need both keys and values we can use the items method with the
`for first, second in thing` trick.

```python
>>> favorite_pets.items()
dict_items([('Akuli', 'dogs'),
            ('__Myst__', 'cats'),
            ('caisa64', 'cats and dogs'),
            ('horusr', 'cats')])
>>> for name, pets in favorite_pets.items():
...     print("{} are {}'s favorite pets".format(pets, name))
...
dogs are Akuli's favorite pets
cats are __Myst__'s favorite pets
cats and dogs are caisa64's favorite pets
cats are horusr's favorite pets
>>>
```

This is also useful for checking if the dictionary has a `key: value`
pair.

```python
>>> ('horusr', 'cats') in favorite_pets.items()
True
>>> ('horusr', 'dogs') in favorite_pets.items()
False
>>>
```

## Limitations

Sometimes it might be handy to use lists as dictionary keys, but it
just doesn't work. I'm not going to explain why Python doesn't allow
this because usually we don't need to worry about that.

```python
>>> stuff = {['a', 'b']: 'c', ['d', 'e']: 'f'}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
>>>
```

On the other hand, tuples work just fine:

```python
>>> stuff = {('a', 'b'): 'c', ('d', 'e'): 'f'}
>>> stuff
{('a', 'b'): 'c', ('d', 'e'): 'f'}
>>>
```

The values of a dictionary can be anything.

```python
>>> stuff = {'a': [1, 2, 3], 'b': [4, 5, 6]}
>>> stuff
{'a': [1, 2, 3], 'b': [4, 5, 6]}
>>>
```

## Summary

- Dictionaries consist of `key: value` pairs.
- Variables are stored in a dictionary with their names as keys, so
    dictionaries behave a lot like variables:
    - Dictionaries are not ordered.
    - Setting or getting the value of a key is simple and fast.
    - Dictionaries can't contain the same key more than once.
- For-looping over a dictionary loops over its keys, and checking if
    something is in the dictionary checks if the dictionary has a key
    like that. The `values()` and `items()` methods return things that
    behave like lists of values or `(key, value)` pairs instead.

## Examples

This program counts how many times words appear in a sentence.
`sentence.split()` creates a list of words in the sentence, see
`help(str.split)` for more info.

```python
sentence = input("Enter a sentence: ")

counts = {}     # {word: count, ...}
for word in sentence.split():
    if word in counts:
        # we have seen this word before
        counts[word] += 1
    else:
        # this is the first time this word occurs
        counts[word] = 1

print()     # display an empty line
for word, count in counts.items():
    if count == 1:
        # "1 times" looks weird
        print(word, "appears once in the sentence")
    else:
        print(word, "appears", count, "times in the sentence")
```

Running the program might look like this:

    Enter a sentence: this is a test and this is quite long because this is a test

    is appears 3 times in the sentence
    long appears once in the sentence
    a appears 2 times in the sentence
    because appears once in the sentence
    this appears 3 times in the sentence
    quite appears once in the sentence
    and appears once in the sentence
    test appears 2 times in the sentence

**TODO:** Exercises.

***

If you have trouble with this tutorial please [tell me about
it](../contact-me.md) and I'll make this tutorial better. If you
like this tutorial, please [give it a
star](../README.md#how-can-i-thank-you-for-writing-and-sharing-this-tutorial).

You may use this tutorial freely at your own risk. See
[LICENSE](../LICENSE).

[Previous](trey-hunner-zip-and-enumerate.md) | [Next](defining-functions.md) |
[List of contents](../README.md#basics)
