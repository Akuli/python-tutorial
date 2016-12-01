# Dictionaries

**TODO:** write the lists-and-tuples.md this tutorial links to.

Now we know how [lists and tuples](lists-and-tuples.md) work and how
to [for loop](loops.md#for-loops) over them. We also did an exercise
with code like this:

```py
userlist = [
    ('me', 'my password'),
    ('you', 'your password'),
]
```

Then to check if a username and password were correct we did
`(username, password) in userlist`. Adding new users was also easy as
appending to that list.

What if we need to check if a username is in the users, but we don't
need to know the password? `username in userlist` is always False
because the user list consists of (username,password) pairs, so we need
to for loop over the whole list:

```py
username_exists = False
for user in userlist:
    if user[0] == username:
        username_exists = True
        break
if username_exists:
    # do something
```

Getting a user's password also requires a similar loop:

```py
password = None
for user in userlist:
    if user[0] == username:
        password = user[1]
        break
# make sure password isn't still None and do something with it
```

This works just fine because our user list only contains two users, but
it would be slow if the userlist was bigger.

## What are dictionaries?

A better way to store user information might be a dictionary.

```py
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

- Dictionaries are not ordered. There's **no guarantees** about which
    order the username:password pairs appear in when we do something
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

```py
>>> globals()
{'userlist': [('me', 'my password'), ('you', 'your password')],
 'passwords': {'me': 'my password', 'you': 'your password'},
 ...many other things we don't need to care about...
}
>>> 
```

So if you have trouble remembering how dictionaries work just compare
them to variables.

## What can we do with dictionaries?

Dictionaries have some similarities with lists. For example, both
lists and dictionaries have a length.

```py
>>> len(userlist)     # contains two elements
2
>>> len(passwords)    # contains two key:value pairs
2
>>> 
```

We can get a value of a key with `the_dict[key]`. Trying to get the
value of a non-existing key gives us an error. We can also add new
key:value pairs by doing `the_dict[key] = value`.

```py
>>> passwords['me']
'my password'
>>> passwords['you']
'your password'
>>> passwords['lol']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'lol'
>>> passwords["lol"] = "lol's password"
>>> passwords
{'lol': "lol's password", 'you': 'your password', 'me': 'my password'}
>>> 
```

For looping over a dictionary gets its keys, and checking if something's
in the dictionary checks if the dictionary has a key like that. This can
be confusing at first but you'll get used to this.

```py
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

```py
>>> passwords.values()
dict_values(["lol's password", 'your password', 'my password'])
>>> 
```

The values method returned a `dict_values` object. Things like this
behave a lot like lists and usually we don't need to convert them to
lists.

```py
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

```py
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

**TODO:** lists as keys vs tuples as keys.

***

You may use this tutorial freely at your own risk. See
[LICENSE](LICENSE).

[Previous](trey-hunner-zip-and-enumerate.md) | [Next](defining-functions.md) |
[Back to the list of contents](README.md#list-of-contents)
