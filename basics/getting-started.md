# Getting started with Python

[Launch Python](installing-python.md).

The `>>>` means that Python is ready and we can enter a command. The
basic idea is really simple: we enter a command, press Enter, enter
another command, press Enter and keep going.

You probably don't know any Python commands yet. Let's see what happens
if we just write something and press Enter.

```python
>>> hello
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'hello' is not defined
>>>
```

Oops! That didn't work. But like I wrote in the
[introduction](what-is-programming.md), error messages are our friends.
This error message tells us what's wrong and where, and we'll learn what
"name 'hello' is not defined" means [later](variables.md).

Maybe we can press Enter without typing anything?

```python
>>>
>>>
>>>
>>>
```

That worked. How about numbers?

```python
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

```python
>>> 3,14
(3, 14)
>>>
```

We didn't get an error... but `(3, 14)` is not at all what we expected!
So from now on, let's use a dot with decimal numbers, because `3.14`
worked just fine. Later we'll learn what `(3, 14)` is.

## Comments

**Comments are text that don't do anything when they're run.** 
They can be created by typing a `#` and then some text after it, 
and they are useful when our code would be hard to understand without them.

```python
>>> 1 + 2     # can you guess what the result is?
3
>>>
```

Again, I put a space after the `#` and multiple spaces before it just to
make things easier to read.

If we write a comment on a line with no code on it, the prompt changes
from `>>>` to `...`. To be honest, I have no idea why it does that and I
think it would be better if it would just stay as `>>>`. The prompt goes
back to `>>>` when we press Enter again.

```python
>>> # hello there
...
>>>
```

## Strings

Strings are small pieces of text that we can use in our programs. We can
create strings by simply writing some text in quotes.

```python
>>> 'hello'
'hello'
>>> 'this is a test'
'this is a test'
>>> 
```

Strings can also be written with "double quotes" instead of 'single
quotes'. This is useful when we need to put quotes inside the string.

```python
>>> "hello there"
'hello there'
>>> "it's sunny"
"it's sunny"
>>> 
```

It's also possible to add single quotes and double quotes into the same
string, but most of the time we don't need to do that so I'm not going
to talk about it now.

It doesn't matter which quotes you use when the string doesn't need to
contain any quotes. If you think that one of the quote types looks nicer
than the other or you find it faster to type, go ahead and use that.

Strings can be joined together easily with `+` or repeated with `*`:

```python
>>> "hello" + "world"
'helloworld'
>>> "hello" * 3
'hellohellohello'
>>> 
```

Note that a `#` inside a string doesn't create a comment.

```python
>>> "strings can contain # characters"
'strings can contain # characters'
>>> 
```

## Using Python as a calculator

```diff
---------- WARNING: This part contains boring math. Proceed with caution. ----------
```

Let's type some math stuff into Python and see what it does.

```python
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

I added a space on both sides of `+`, `-`, `*` and `/`. Everything would
work without those spaces too:

```python
>>> 4 + 2 + 1
7
>>> 4+2+1
7
>>>
```

However, I recommend always adding the spaces because they make the code
easier to read.

Things are calculated in the same order as in math. The parentheses `(`
and `)` also work the same way.

```python
>>> 1 + 2 * 3        # 2 * 3 is calculated first
7
>>> (1 + 2) * 3      # 1 + 2 is calculated first
9
>>>
```

You can also leave out spaces to show what's calculated first. Python
ignores it, but our code will be easier to read for people.

```python
>>> 1 + 2*3         # now it looks like 2*3 is calculated first
7
>>>
```

Python also supports many other kinds of calculations, but most of the
time you don't need them. Actually you don't need even these
calculations most of the time, but these calculations are probably
enough when you need to calculate something.

## Summary

[comment]: # (the first line in this summary is exactly same as in)
[comment]: # (what-is-programming.md, and it's supposed to be like this)

- Error messages are our friends.
- We can enter any Python commands to the interactive `>>>` prompt, and
    it will echo back the result.
- `+`, `-`, `*` and `/` work in Python just like in math.
- Pieces of text starting with a `#` are comments and pieces of text in
    quotes are strings.
- You can use single quotes and double quotes however you want.

***

If you have trouble with this tutorial please [tell me about
it](../contact-me.md) and I'll make this tutorial better. If you
like this tutorial, please [give it a
star](../README.md#how-can-i-thank-you-for-writing-and-sharing-this-tutorial).

You may use this tutorial freely at your own risk. See
[LICENSE](../LICENSE).

[Previous](installing-python.md) | [Next](the-way-of-the-program.md) |
[List of contents](../README.md#basics)
