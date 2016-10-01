# Trey Hunner: zip and enumerate

Now we know how [for loops](loops.md#for-loops) work in Python. But
for loops aren't limited to printing each item in a list, they can
do a lot more.

To be able to understand for loop tricks we need to first know
assigning values to multiple variables at once. It works like this:

```py
>>> a, b = 1, 2
>>> a
1
>>> b
2
>>> 
```

We can use `()` and `[]` around these values however we want and
everything will still work the same way. `[]` creates a list, and
`()` creates a tuple. We'll talk more about tuples later.

```py
>>> [a, b] = (1, 2)
>>> a
1
>>> b
2
>>> 
```

We can also have `[]` or `()` on one side but not on the other
side.

```py
>>> (a, b) = 1, 2
>>> a
1
>>> b
2
>>> 
```

What actually happened is that Python created a tuple automatically.

```py
>>> 1, 2
(1, 2)
>>> 
```

If we're for looping over a list with pairs of values in it we
could do this:

```py
>>> items = [('a', 1), ('b', 2), ('c', 3)]
>>> for pair in items:
...     a, b = pair
...     print(a, b)
... 
a 1
b 2
c 3
>>> 
```

Or we can tell the for loop to unpack it for us.

```py
>>> for a, b in items:
...     print(a, b)
... 
a 1
b 2
c 3
>>> 
```

Now you're ready to read [this looping
tutorial](http://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/).
Read it now, then read the summary and do the exercises.

## Summary

Assigning multiple values at once:

```py
>>> a, b, c = 1, 2, 3
>>> a
1
>>> b
2
>>> c
3
>>> 
```

For looping over a list of pairs:

```py
>>> stuff = [('a', 1), ('b', 2), ('c', 3)]
>>> for a, b in stuff:
...     print(a, b)
... 
a 1
b 2
c 3
>>> 
```

For looping over two lists at once:

```py
>>> colors = ['red', 'green', 'blue']
>>> letters = ['R', 'G', 'B']
>>> for letter, color in zip(letters, colors):
...     print(letter, color)
... 
R red
G green
B blue
>>> 
```

For looping over a list with indexes:

```py
>>> fillernames = ['foo', 'bar', 'biz', 'baz', 'spam', 'eggs']
>>> for index, name in enumerate(fillernames):
...     print(index, name)
... 
0 foo
1 bar
2 biz
3 baz
4 spam
5 eggs
>>> 
```

## Exercises

1. Create a program that works like this. Here I entered everything
    after the `>` prompt that the program displayed.

    ```
    Enter something, and press Enter without typing anything when you're done.
    >hello there
    >this is a test
    >it seems to work
    >
    Line 1 is: hello there
    Line 2 is: this is a test
    Line 3 is: it seems to work
    ```

2. Create a program that prints all letters from A to Z and a to z
    next to each other:

    ```
    A a
    B b
    C c
    ...
    X x
    Y y
    Z z
    ```

    Start your program like this:

    ```py
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    ```

    **Hint:** how do strings behave with `zip`? Try it out on the
    `>>>` prompt and see.

3. Can you also make it print the indexes also?

    ```
    1 A a
    2 B b
    3 C c
    ...
    24 X x
    25 Y y
    26 Z z
    ```

***

You may use this tutorial freely at your own risk. See [LICENSE](LICENSE).

[Back to the list of contents](README.md)
