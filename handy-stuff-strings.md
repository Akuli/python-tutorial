# Handy stuff: Strings

Python strings are just pieces of text.

```py
>>> our_string = "Hello World!"
>>> our_string
'Hello World!'
>>> 
```

So far we know how to add them together.

```py
>>> "I said: " + our_string
'I said: Hello World!'
>>> 
```

We also know how to repeat them multiple times.

```py
>>> our_string * 3
'Hello World!Hello World!Hello World!'
>>> 
```

Python strings are **immutable**. That's basically a fancy way to say that
they cannot be changed in-place, and you need to create a new string to
change them. Even `some_string += another_string` creates a new string.
Python will treat that as `some_string = some_string + another_string`,
so it creates a new string but it puts it back to the same variable.

`+` and `*` are nice, but what else can we do with strings?

## Slicing

Slicing is really simple. It just means getting a part of the string.
For example, to get all characters between the second place between the
characters and the fifth place between the characters, we can do this:

```py
>>> our_string[2:5]
'llo'
>>> 
```

So the syntax is like `some_string[start:end]`.

This picture shows you how the slicing works:

![Slicing with non-negative values](images/slicing1.png)

But what happens if we slice with negative values?

```py
>>> our_string[-5:-2]
'orl'
>>> 
```

It turns out that slicing with negative values simply starts counting
from the end of the string.

![Slicing with negative values](images/slicing2.png)

If we don't specify the beginning it defaults to 0, and if we don't
specify the end it defaults to the length of the string. For example, we
can get everything except the first or last character like this:

```py
>>> our_string[1:]
'ello World!'
>>> our_string[:-1]
'Hello World'
>>> 
```

Remember that strings can't be changed in-place.

```py
>>> our_string[:5] = 'Howdy'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> 
```

There's also a step argument we can give to our slices, but I'm not
going to talk about it in this tutorial.

## Indexing

So now we know how slicing works. But what happens if we forget the `:`?

```py
>>> our_string[1]
'e'
>>> 
```

That's interesting. We got a string that is only one character long. But
the first character of `Hello World!` should be `H`, not `e`, so why did
we get an e?

Programming starts at zero. Indexing strings also starts at zero. The
first character is `our_string[0]`, the second character is
`our_string[1]`, and so on.

So string indexes work like this:

![Indexing with non-negative values](images/indexing1.png)

How about negative values?

```py
>>> our_string[-1]
'!'
>>> 
```

We got the last character.

But why didn't that start at zero? `our_string[-1]` is the last
character, but `our_string[1]` is not the first character!

That's because 0 and -0 are equal, so indexing with -0 would do the same
thing as indexing with 0.

Indexing with negative values works like this:

![Indexing with negative values](images/indexing2.png)

## The in keyword

We can use `in` and `not in` to check if a string contains another
string:

```py
>>> "Hello" in our_string
True
>>> "Python" in our_string
False
>>> "Python" not in our_string
True
>>> 
```

## String methods

Python's strings have many useful methods. [The official documentation]
(https://docs.python.org/3/library/stdtypes.html#string-methods) covers
them all, but I'm going to just show some of the most commonly used ones
briefly. **You don't need to remember all of these string methods, just
learn to use the link above so you can find them when you need them.**
Python also comes with built-in documentation about the string methods.
You can run `help(str)` to read it.

Remember that nothing can modify strings in-place. Most string methods
return a new string, but things like `our_string = our_string.upper()`
still work because the new string is assigned to the old variable.

Here's some of the most commonly used string methods:

- `upper` and `lower` can be used for converting to uppercase and
    lowercase.

    ```py
    >>> our_string.upper()
    'HELLO WORLD!'
    >>> our_string.lower()
    'hello world!'
    >>> 
    ```

- To check if a string starts or ends with another string we could just
  slice the string and compare with to the slice.

    ```py
    >>> our_string[:5] == 'Hello'
    True
    >>> our_string[-2:] == 'hi'
    False
    >>> 
    ```

    But that gets a bit complicated if we don't know the length of the
    substring beforehand.

    ```py
    >>> substring = 'Hello'
    >>> our_string[:len(substring)] == substring
    True
    >>> substring = 'hi'
    >>> our_string[-len(substring):] == substring
    False
    >>> 
    ```

    That's why it's recommended to use `startswith` and `endswith`:

    ```py
    >>> our_string.startswith('Hello')
    True
    >>> our_string.endswith('hi')
    False
    >>> 
    ```

- If we need to find out where a substring is located, we can do that
    with `index`:

    ```py
    >>> our_string.index('World')
    6
    >>> our_string[6:]
    'World!'
    >>> 
    ```

- The `join` method joins a list of other strings. We'll talk more about
    lists later.

    ```py
    >>> '-'.join(['Hello', 'World', 'test'])
    'Hello-World-test'
    >>> 
    ```

    The `split` method is the opposite of joining, it splits a string to
    a list.

    ```py
    >>> 'Hello-World-test'.split('-')
    ['Hello', 'World', 'test']
    >>> 

- Last but not least, we can use `strip`, `lstrip` and `rstrip` to
    remove spaces, newlines and some other whitespace characters from
    the end of a string. `lstrip` strips from the left side, `lstrip`
    strips from the right side and `strip` strips from both sides.

    ```py
    >>> '  hello 123 \n '.lstrip()
    'hello 123 \n '
    >>> '  hello 123 \n '.rstrip()
    '  hello 123'
    >>> '  hello 123 \n '.strip()
    'hello 123
    >>> 
    ```

It's also possible to combine string methods with slicing and other
string methods:

```py
>>> our_string.upper()[:7].startswith('HELLO')
True
>>> 
```

## String formatting

To add a string in the middle of another string, you can do something
like this:

```py
>>> name = 'Akuli'
>>> 'My name is ' + name + '.'
'My name is Akuli.'
>>> 
```

But that gets complicated if you have many things to add.

```py
>>> channel = '##learnpython'
>>> network = 'freenode'
>>> "My name is " + name + " and I'm on the " + channel + " channel on " + network + "."
"My name is Akuli and I'm on the ##learnpython channel on freenode."
>>> 
```

Instead it's recommended to use string formatting. It means putting
other things in the middle of a string.

Python has two ways to format strings. One is not better than the other,
they are just different. The two ways are:

- `.format()`-formatting, also known as new-style formatting. This
    formatting style has a lot of features, but it's a little bit more
    typing than `%s`-formatting.

    ```py
    >>> "Hello {}.".format(name)
    'Hello Akuli.'
    >>> "My name is {} and I'm on the {} channel on {}.".format(name, channel, network)
    "My name is Akuli and I'm on the ##learnpython channel on freenode."
    >>> 
    ```

- `%s`-formatting, also known as printf-formatting and old-style
    formatting. This has less features than `.format()`-formatting, but
    `'Hello %s.' % name` is shorter and faster to type than
    `'Hello {}.'.format(name)`.

    ```py
    >>> "Hello %s." % name
    'Hello Akuli.'
    >>> "My name is %s and I'm on the %s channel on %s." % (name, channel, network)
    "My name is Akuli and I'm on the ##learnpython channel on freenode."
    >>> 
    ```

Both formatting styles have many other features also:

```py
>>> 'Three zeros and number one: {:04d}'.format(1)
'Three zeros and number one: 0001'
>>> 'Three zeros and number one: %04d' % 1
'Three zeros and number one: 0001'
>>> 
```

If you need to know more about formatting I recommend reading
[this](https://pyformat.info/).

## Summary

- Slicing returns a copy of a string with indexes from one index to
    another index. The indexes work like this:

    ![Slicing](images/slicing3.png)

- Indexing returns one character of a string. Remember that you don't
    need a `:` with indexing. The indexes work like this:

    ![Indexing](images/indexing3.png)

- The `in` keyword can be used for checking if a string contains another
    string.

- Python has many string methods. Use [the documentation]
    (https://docs.python.org/3/library/stdtypes.html#string-methods)
    when you don't rememeber something about them.

- String formatting means adding other things to the middle of a string.
