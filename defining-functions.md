# Defining your own functions

It's probably been a while since you read about using functions. [Read
about it again](using-functions.md) if you need to.

## Why should I use custom functions?

Have a look at this code:

```py
print("************")
print("Hello World!")
print("************")
print()

print("********************")
print("Enter your password:")
print("********************")
print()

word = input()

if word == 'python':
    print("********")
    print("Welcome!")
    print("********")
    print()
else:
    print("**************")
    print("Access denied.")
    print("**************")
    print()
```

Then compare it to this code:

```py
print_box("Hello World!")
print_box("Enter your password:")
word = input()
if word == 'python':
    print_box("Welcome!")
else:
    print_box("Access denied.")
```

That's nice, but where do we a box function like that?

## First functions

The `pass` keyword does nothing.

```py
>>> pass
>>> 
```

Let's use it to define a function that does nothing.

```py
>>> def do_nothing():
...     pass
... 
>>> do_nothing
<function do_nothing at 0x7f56b74e9598>
>>> 
```

Seems to be working so far, we have a function. Let's see what happens
if we call it.

```py
>>> do_nothing()
>>> 
```

There we go. It did nothing at all.

Maybe we could just do something in the function instead?

```py
>>> def print_hi():
...     print("Hi!")
... 
>>> print_hi()
Hi!
>>> 
```

It's working. How about printing a variable in the function?

```py
>>> message = "Hello World!"
>>> print_message()
Hello World!
>>> 
```

Again, it works. How about setting a variable in the function?

```py
>>> def set_username():
...     username = 'me'
... 
>>> set_username()
>>> username
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'username' is not defined
>>> 
```

That was weird! Why didn't that work?

## Locals and globals

So far we have used nothing but **global variables**. They are called
globals because the same variables are available anywhere in our
program, even in functions.

```py
>>> a = 1
>>> b = "hi"
>>> c = "hello there"
>>> def print_abc():
...     print(a, b, c)
... 
>>> print_abc()
1 hi hello there
>>> 
```

