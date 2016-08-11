# ThinkPython: Lists

Now we have learned to save values to variables.

```py
thing = 'Hello World!'
```

Then we can do whatever we want with the variable.

```py
print(thing)
```

But what if you have a lot of values? You can just make a lot of
variables...

```py
thing1 = 'Hello World!'
thing2 = 'hi'
thing3 = 123
thing4 = 3.14
thing5 = 42
thing6 = 'This is yet another thing.'
thing7 = 'Python is fun!'

print(thing1)
print(thing2)
print(thing3)
print(thing4)
print(thing5)
print(thing6)
print(thing7)
```

...or you can use a list and keep everything in one variable.

```py
things = ['Hello World!', 'hi', 123, 3.14, 42,
          'This is yet another thing.', 'Python is fun!']
for thing in things:
    print(thing)
```

[Read more about lists in ThinkPython
here.](http://greenteapress.com/thinkpython2/html/thinkpython2011.html)
Skip the chapter "10.7 Map, filter and reduce" and the excercises. You
would need to know how to define functions using the `def` keyword, but
we haven't talked about that yet.

## Summary

- Lists are a way to store multiple values in one variable. We can
    create lists by putting whatever we want inside [square brackets],
    for example, `our_list = []` creates an empty list.
- Never do `list = ...`. `list` is a built-in class, and it's used for
    converting other values to lists, like `list_of_thingy = list(thingy)`.
    If we do `list = something`, then `list(thingy)` will probably do
    something else than we want it to do.
- When we have created a list, we can slice it. For example,
    `our_list[2:]` results in a new list with everything in the
    original list except the first two elements. Negative indexes start
    from the end of the list, for example, `our_list[-2:]` is a list of
    the last two elements.
- We can also index lists, `our_list[0]` is the first element in the
    list. Non-negative indexes start at zero, and negative indexes
    start at -1.
- You can assign to indexes and slices like `some_list[0] = 'hi'`, or
    delete them like `del some_list[:2]`.
- `a = b` does not create a copy of b.

    ```py
    >>> a = []
    >>> b = a            # this does not copy anything
    >>> b += [1, 2, 3]
    >>> a
    [1, 2, 3]
    >>> 
    ```

    If you want a copy, use the `.copy()` list method:

    ```py
    >>> a = []
    >>> b = a.copy()
    >>> b += [1, 2, 3]
    >>> a
    []
    >>> 
    ```

***

You may use this tutorial freely at your own risk. See [LICENSE](LICENSE).

[Back to the list of contents](README.md)
