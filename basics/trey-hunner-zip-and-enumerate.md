# Trey Hunner: zip and enumerate

Now we know how [for loops](loops.md#for-loops) work in Python. But
for loops aren't limited to printing each item in a list, they can
do a lot more.

To be able to understand for loop tricks we need to first know
assigning values to multiple variables at once. It works like this:

```python
>>> a, b = 1, 2
>>> a
1
>>> b
2
>>>
```

We can use `()` and `[]` around these values however we want and
everything will still work the same way. `[]` creates a list, and
`()` creates a tuple.

```python
>>> [a, b] = (1, 2)
>>> a
1
>>> b
2
>>>
```

We can also have `[]` or `()` on one side but not on the other
side.

```python
>>> (a, b) = 1, 2
>>> a
1
>>> b
2
>>>
```

Python created a tuple automatically.

```python
>>> 1, 2
(1, 2)
>>>
```

If we're for looping over a list with pairs of values in it we
could do this:

```python
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

```python
>>> for a, b in items:
...     print(a, b)
...
a 1
b 2
c 3
>>>
```

Now you're ready to read [this awesome looping
tutorial](http://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/).
Read it now, then come back here and do the exercises.

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

    ```python
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    ```

    **Hint:** how do strings behave with `zip`? Try it out on the
    `>>>` prompt and see.

3. Can you make it print the indexes also?

    ```
    1 A a
    2 B b
    3 C c
    ...
    24 X x
    25 Y y
    26 Z z
    ```

The answers are [here](answers.md).

***

If you have trouble with this tutorial please [tell me about
it](../contact-me.md) and I'll make this tutorial better. If you
like this tutorial, please [give it a
star](../README.md#how-can-i-thank-you-for-writing-and-sharing-this-tutorial).

You may use this tutorial freely at your own risk. See
[LICENSE](../LICENSE).

[Previous](loops.md) | [Next](dicts.md) |
[List of contents](../README.md#basics)
