# Dictionaries

Now we know how [lists and tuples](lists-and-tuples.md) work and how
to [for loop](loops.md#for-loops) over them. If we make some kind of
program that needs to keep track of people's usernames and passwords,
we can use a list for that:

```python
userlist = [
    ('me', 'my password'),
    ('you', 'your password'),
]
```

Then to check if a username and password are correct we can do
`(username, password) in userlist`. Or we can add a new user easily by
appending a new `(username, password)` tuple to the userlist.

But what if we need to check if a username exists, but we don't know
the password? `username in userlist` is always False because the user
list consists of `(username, password)` pairs instead of just
usernames, so we need to for loop over the whole userlist:

```python
username_exists = False
for user in userlist:
    if user[0] == username:
        username_exists = True
        break
if username_exists:
    # do something
```

Or how about getting a user's password if we know the username? This
also requires going through the whole list.

```python
password = None
for user in userlist:
    if user[0] == username:
        password = user[1]
        break
# make sure password is not None and do something with it
```

As you can see, a list of `(username, password)` pairs is not an ideal
way to store our usernames and passwords.

## What are dictionaries?

A better way to store user information might be a dictionary:

```python
passwords = {
    'me': 'my password',
    'you': 'your password',
}
```

Here `'me'` and `'you'` are **keys** in the dictionary, and
`'my password'` and `'your password'` are their **values**. Dictionaries
are often named by their values. This dictionary has passwords as its
values so I named the variable `passwords`.

There are a few big differences between dictionaries and lists of pairs:

- Dictionaries are not ordered. There are **no guarantees** about which
    order the `username: password` pairs appear in when we do something
    with the dictionary.
- Checking if a key is in the dictionary is simple and fast. We don't
    need to for loop through the whole dictionary.
- Getting the value of a key is also simple and fast.
- We can't have the same key in the dictionary multiple times, but
    multiple different keys can have the same value. This means that
    **multiple users can't have the same name, but they can have the
    same passwords**.

But wait... this is a lot like variables are! Our variables are not
ordered, getting a value of a variable is fast and easy and we can't
have multiple variables with the same name.

Variables are actually stored in a dictionary. We can get that
dictionary with the globals function. In this dictionary, keys are
variable names and values are what our variables point to.

```python
>>> globals()
{'userlist': [('me', 'my password'), ('you', 'your password')],
 'passwords': {'me': 'my password', 'you': 'your password'},
 ...many other things we don't need to care about...
}
>>>
```

So if you have trouble remembering how dictionaries work just compare
them to variables. A dictionary is a perfect way to store our usernames
and passwords. We don't care about which order the users were added in,
it's impossible to add multiple users with the same username and
getting a user's password is easy.

## What can we do with dictionaries?

Dictionaries have some similarities with lists. For example, both
lists and dictionaries have a length.

```python
>>> len(userlist)     # contains two elements
2
>>> len(passwords)    # contains two key:value pairs
2
>>>
```

We can get a value of a key with `the_dict[key]`. This is a lot easier
and faster than for-looping over a list of pairs.

```python
>>> passwords['me']
'my password'
>>> passwords['you']
'your password'
>>>
```

Trying to get the value of a non-existing key gives us an error, but we
can add new `key: value` pairs by doing `the_dict[key] = value`.

```python
>>> passwords['lol']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'lol'
>>> passwords["lol"] = "lol's password"
>>> passwords["lol"]
"lol's password"
>>> passwords
{'lol': "lol's password", 'you': 'your password', 'me': 'my password'}
>>>
```

For looping over a dictionary gets its keys, and checking if something
is in the dictionary checks if the dictionary has a key like that. This
can be confusing at first but you'll get used to this.

```python
>>> 'me' in passwords
True
>>> 'my password' in passwords
False
>>> for name in passwords:
...     print(name)
...
lol
you
me
>>>
```

Dictionaries have a values method that we can use if we want to do
something with the values:

```python
>>> passwords.values()
dict_values(["lol's password", 'your password', 'my password'])
>>>
```

The values method returned a `dict_values` object. Things like this
behave a lot like lists and usually we don't need to convert them to
lists.

```python
>>> for password in passwords.values():
...     print(password)
...
lol's password
your password
my password
>>>
```

We can do things like `list(passwords.values())` if we need a real list
for some reason, but doing that can slow down our program if the
dictionary is big. There's also a keys method, but usually we don't need
it because the dictionary itself behaves a lot like a list of keys.

If we need both keys and values we can use the items method with the
`for first, second in thing` trick.

```python
>>> passwords.items()
dict_items([('lol', "lol's password"),
            ('you', 'your password'),
            ('me', 'my password')])
>>> for name, password in passwords.items():
...     print(name + ": " + password)
...
lol: lol's password
you: your password
me: my password
>>>
```

This is also useful for checking if the dictionary has a `key: value`
pair.

```python
>>> ('me', 'my password') in passwords.items()  # correct username and password
True
>>> ('me', 'whatever') in passwords.items()    # wrong username or password
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

***

If you like this tutorial, please [give it a
star](../README.md#how-can-i-thank-you-for-writing-and-sharing-this-tutorial).

You may use this tutorial freely at your own risk. See
[LICENSE](../LICENSE).

[Previous](trey-hunner-zip-and-enumerate.md) | [Next](defining-functions.md) |
[List of contents](../README.md#basics)
