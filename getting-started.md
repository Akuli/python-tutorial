# Getting started with Python

[Launch Python](installing-python.md).

The `>>>` means that Python is ready and we can enter a command. The
basic idea is really simple: we enter a command, press Enter, enter
another command, press Enter and keep going.

You probably don't know any Python commands yet. Let's see what happens
if we just write something and press Enter.

```py
>>> hello
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'hello' is not defined
>>>
```

Oops! That didn't work. But like I wrote in the
[introduction](what-is-programming.md), **errors don't matter**.

Maybe we can press Enter without typing anything?

```py
>>> 
>>> 
>>> 
>>> 
```

That worked. How about numbers?

```py
>>> 123
123
>>> -123
-123
>>> 3.14
3.14
>>> -12.3
-12.3
>>> 
```

There we go, it echoes them back.

In some countries, decimal numbers are written with a comma, like `3,14`
instead of `3.14`. Maybe Python knows that?

```py
>>> 3,14
(3, 14)
>>> 
```

We didn't get an error... but `(3, 14)` is not at all what we expected!
So from now on, let's use a dot with decimal numbers, because `3.14`
worked just fine. Later we'll learn what `(3, 14)` is.

What if we type a `#`?

```py
>>> #
>>> 
```

Nothing happened at all. Maybe we can type a `#` and then some text
after it?

```py
>>> # hello there
>>> 
```

Again, nothing happened.

If you're not using IDLE, the prompt will change from `>>>` to
`...`. Just press Enter again to get it back to `>>>`.

```py
>>> # hello again
... 
>>> 
```

In Python, these pieces of text starting with a `#` are known as
**comments**. They don't change how the code works in any way, but
we can use them to explain what our code does.

## Using Python as a calculator

Maybe we could type mathematical statements?

```py
>>> 17 + 3
20
>>> 17 - 3
14
>>> 17 * 3
51
>>> 17 / 3
5.666666666666667
>>>
```

It's working, Python just calculates the result and echoes it back.

The spaces between numbers and operators don't affect anything, they
just make the code easier to read when they are used correctly.

```py
>>> 14 + 2 + 1
17
>>> 14            +2+ 1
17
>>>
```

The evaluation order is similar to math. The parentheses `(` and `)`
also work the same way.

```py
>>> 1 + 2 * 3        # 2 * 3 is calculated first
7
>>> (1 + 2) * 3      # 1 + 2 is calculated first
9
>>>
```

Square brackets `[]` and curly brackets `{}` cannot be used to change
the evaluation order. We'll learn more about what they do later.

```py
>>> [1 + 2] * 3
[3, 3, 3]
>>> {1 + 2} * 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for *: 'set' and 'int'
>>>
```

## More advanced math

I decided to include this in my tutorial because some people might be
interested in this. Feel free to [skip this](#summary) if you're not
interested.

The `//` operator will divide and then throw away the dot and everything
after it. For example, `17 / 3` is `5.666666666666667`, and so `17 // 3`
is `5` because we throw away the `.666666666666667` part.

```py
>>> 17 / 3
5.666666666666667
>>> 17 // 3
5
>>>
```

The `%` operator gets the division remainder.

```py
>>> 17 % 3
2
>>>
```

For example, if there were 17 apples that should be given evenly to 3
people, everyone would get 5 apples and there would be 2 apples left
over.

```py
>>> 17 // 3
5
>>> 17 % 3
2
>>>
```

This is also useful for converting time from minutes to seconds. 500
seconds is 8 minutes and 20 seconds.

```py
>>> 500 // 60
8
>>> 500 % 60
20
>>>
```

`**` can be used to raise to a power, so 3² in math is `3**2` in Python.
Powers are calculated before `*` and `/`, but after `()`.

```py
>>> 2 ** 3
8
>>> 2 * 3 ** 2      # 3 ** 2 is calculated first
18
>>> (2 * 3) ** 2    # 2 * 3 is calculated first
36
>>>
```

## Summary

- Errors don't matter.
- You can enter any Python commands to the interactive `>>>` prompt, and
    it will echo back the result.
- Pieces of text starting with a `#` are comments.
- `+`, `-`, `*` and `/` work in Python just like in math.

***

You may use this tutorial freely at your own risk. See [LICENSE](LICENSE).

[Back to the list of contents](README.md)
