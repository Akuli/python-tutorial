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

In some countries, decimal numbers are written like `3,14` instead of
`3.14`. Maybe Python knows that?

```python
>>> 3,14
(3, 14)
>>>
```

We didn't get an error... but `(3, 14)` is not at all what we expected!
So from now on, let's use a dot with decimal numbers, because `3.14`
worked just fine. Later we'll learn what `(3, 14)` is.

Python also supports simple math:

```python
>>> 3 + 2
5
>>> 3 - 2
1
>>> 3 * 2
6
>>> 3 / 2
1.5
>>> 
```

## Comments

**Comments are text that does nothing.** Everything after a `#` is ignored.
Like this:

```python
>>> 1 + 2     # can you guess what the result is?
3
>>>
```

Comments are useful for explaining something to people reading the code.

The interactive prompt does this if you enter a comment on a line with
nothing else on it:

```python
>>> # hello there
...
>>>
```

I have no idea why this happens and I think it would be better if the
prompt would just stay as `>>>`. Press Enter twice to get the prompt
back to `>>>`.

## Strings

Strings are small pieces of text that we can use in our programs. We can
create strings like this:

```python
>>> 'hello'
'hello'
>>> 'this is a test'
'this is a test'
>>> 'string with a # in it'
'string with a # in it'
>>> 'test'
'test'
>>> "test"
'test'
```

It doesn't matter if you use 'single quotes' or "double quotes". Python
prefers single quotes when displaying strings to us, but it understands
both quote styles. Double quotes are useful for strings that contain
single quotes, like `"it's weird"`.

You can also do this:

```python
>>> "hello" + "world"
'helloworld'
>>> "hello" * 3
'hellohellohello'
>>> 
```

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
