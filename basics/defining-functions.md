# Defining custom functions

It's probably been a while since you read about using functions.
[Read about it again](using-functions.md) if you need to.

## Why should I use custom functions?

Have a look at this code:

```python
print("************")
print("Hello World!")
print("************")

print("*************")
print("Enter a word:")
print("*************")

word = input()

if word == 'python':
    print("*******************")
    print("You entered Python!")
    print("*******************")
else:
    print("**************************")
    print("You didn't enter Python :(")
    print("**************************")
```

Then compare it to this code:

```python
print_box("Hello World!")
print_box("Enter a word:")
word = input()
if word == 'python':
    print_box("You entered Python!")
else:
    print_box("You didn't enter Python :(")
```

In this tutorial we'll learn to define a `print_box` function
that prints text in a box. We can write the code for printing the
box once, and then use it multiple times anywhere in the program.

[Dividing a long program into simple functions](larger-program.md) also
makes the code easier to work with. If there's a problem with the code
we can test the functions one by one and find the problem easily.

## First functions

The `pass` keyword does nothing.

```python
>>> pass
>>>
```

Let's use it to define a function that does nothing.

```python
>>> def do_nothing():
...     pass
...
>>> do_nothing
<function do_nothing at 0x7f56b74e9598>
>>>
```

Seems to be working so far, we have a function. It's just a value that
is assigned to a variable called `do_nothing`. You can ignore the
`0xblablabla` stuff for now.

The `pass` is needed here because without it, Python doesn't know when
the function ends and it gives us a syntax error. We don't need the
`pass` when our functions contain something else.

Let's see what happens if we call our function.

```python
>>> do_nothing()
>>>
```

There we go. It did nothing at all.

Maybe we could just do something in the function instead?

```python
>>> def print_hi():
...     print("Hi!")
...
>>> print_hi()
Hi!
>>>
```

It's working. How about printing a variable in the function?

```python
>>> def print_message():
...     print(message)
...
>>> message = "Hello World!"
>>> print_message()
Hello World!
>>>
```

Again, it works. How about setting a variable in the function?

```python
>>> def get_username():
...     username = input("Username: ")
...
>>> get_username()
Username: me
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

```python
>>> a = 1
>>> b = "hi"
>>> c = "hello"
>>> def print_abc():
...     print(a, b, c)
...
>>> print_abc()
1 hi hello
>>>
```

But there are also **local variables**. They exist only **inside**
functions, and they are deleted when the function exits.

```python
>>> def thingy():
...     d = "hello again, i'm a local variable"
...     print('inside thingy:', d)
...
>>> thingy()
inside thingy: hello again, i'm a local variable
>>> d
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'd' is not defined
>>>
```

Let's draw a diagram of these variables:

![Locals and globals.](../images/locals-and-globals.png)

However, modifying a global variable in-place from a function is easy.

```python
>>> stuff = ['global stuff']
>>> def add_stuff():
...     stuff.append('local stuff')
...
>>> add_stuff()
>>> stuff
['global stuff', 'local stuff']
>>>
```

This only works for changing in-place, we cannot assign a new value to
the variable.

```python
>>> def set_stuff_to_something_new():
...     stuff = ['more local stuff']
...
>>> set_stuff_to_something_new()
>>> stuff
['global stuff', 'local stuff']
>>>
```

## Input

**Note:** This section has nothing to do with the `input` function that
is used like `word = input("enter something: ")`.

So far our functions seem to be really isolated from the rest of our
code, and it sucks! But they really are not as isolated as you might
think they are.

Let's think about what the print function does. It takes an argument
and prints it. Maybe a custom function could also take an argument?

```python
>>> def print_twice(message):
...     print(message)
...     print(message)
...
>>>
```

Here `message` is an argument. When we call the function we'll get a
local variable called message that will point to whatever we passed
to `print_twice`.

This function can be called in two ways:

- Using a **positional argument**.

    This is the recommended way for functions that take only one or two
    arguments. I would do this in my code.

    ```python
    >>> print_twice("hi")
    hi
    hi
    >>>
    ```

    When the function was running it had a local `message` variable
    that pointed to `"hi"`. The function printed it twice.

    Positional arguments are great for simple things, but if our
    function takes many positional arguments it may be hard to tell
    which argument is which.

- Using a **keyword argument**:

    ```python
    >>> print_twice(message="hi")
    hi
    hi
    >>>
    ```

    The name "keyword argument" is a little bit confusing because
    keyword arguments don't actually have anything to do with keywords
    (`if`, `else` etc). Keyword arguments are just a way to give names
    for our arguments.

    Keyword arguments are great when our function needs to take many
    arguments, because each argument has a name and it's easy to see
    which argument is which.

    Also note that there are no spaces around the `=` sign. This is
    just a small style detail that Python programmers like to do
    because `message = "hi"` and `some_function(message="hi")` do two
    completely different things.

Now it's time to solve our box printing problem:

```python
def print_box(message):
    print('*' * len(message))
    print(message)
    print('*' * len(message))
```

## Default values

What if we want to print different characters instead of always
printing stars?

We could change our `print_box` function to take two arguments:

```python
def print_box(message, character):
    print(character * len(message))
    print(message)
    print(character * len(message))
```

Then we could change our code to always call `print_box` with a star as
the second argument:

```python
print_box("Hello World", "*")
...
```

But we don't need to change our existing code. We can make the second
argument **optional** by giving it a default value.

```python
def print_box(message, character='*'):
    print(character * len(message))
    print(message)
    print(character * len(message))
```

We can print a row of stars using the function without specifying a
different character in two ways:

- Using a positional argument.

    ```python
    print_box("Hello World!")
    ```

- Using a keyword argument.

    ```python
    print_box(message="Hello World!")
    ```

Or we can give it a different character in a few different ways if we
need to:

- Using two positional arguments.

    ```python
    print_box("Enter a word:", "?")
    ```

- Using two keyword arguments.

    ```python
    print_box(message="Enter a word:", character="?")
    print_box(character="?", message="Enter a word:")
    ```

- Using one positional argument and one keyword argument.

    I would probably do this. If an argument has a default value, I
    like to use a keyword argument to change it if needed.

    ```python
    print_box("Enter a word:", character="?")
    ```

    However, this doesn't work:

    ```python
    print_box(character="?", "Enter a word:")
    ```

    The problem is that we have a keyword argument before a positional
    argument. Python doesn't allow this. We don't need to worry about
    this, because if we accidentally call a function like this we
    will get an error message.

## Output

The built-in input function [returns a value](using-functions.md#return-values).
Can our function return a value too?

```python
>>> def times_two(thing):
...     return thing * 2
...
>>> times_two(3)
6
>>> times_two(5)
10
>>>
```

Yes, it can. Now typing `times_two(3)` to the prompt does the same
thing as typing `6` to the prompt.

We can call the `times_two` function and use the result however we
want, just like we can use built-in functions:

```python
>>> times_two(2) + times_two(3)     # calculate 4 + 6
10
>>> print('2 * 5 is', times_two(5))
2 * 5 is 10
>>>
```

Note that **returning from a function ends it immediately**.

```python
>>> def return_before_print():
...     return None
...     print("This never gets printed.")
...
>>> return_before_print()
>>>
```

If we don't have any return statements or we have a return statement
that doesn't specify what to return, our function will return None.

```python
>>> def return_none_1():
...     pass
...
>>> def return_none_2():
...     return
...
>>> print(return_none_1())
None
>>> print(return_none_2())
None
>>>
```

## Return or print?

There are two ways to output information from functions. They can print
something or they can return something. So, should we print or return?

Most of the time **returning makes functions much easier to use**. Think
about the `input()` function. It asks the user to enter something, and
then the user enters something and that value is returned. If the input
function would print the value instead of returning it, things like
`name = input("Name: ")` wouldn't work and assigning the result to a
variable would be much more difficult. Printing things is fine when we
know that we'll only need to print the result and we'll never need to
assign it to a variable.

If our function returns a value we can always print it, like this:

```python
>>> def return_hi():
...     return "hi"
...
>>> print(return_hi())
hi
>>>
```

## Common problems

Functions are easy to understand, but you need to pay attention to how
you're calling them. Note that `some_function` and `some_function()` do
two completely different things.

```python
>>> def say_hi():
...     print("howdy hi")
...
>>> say_hi     # just checking what it is, doesn't run anything
<function say_hi at 0x7f997d2a8510>
>>> say_hi()   # this runs it
howdy hi
>>>
```

Typing `say_hi` just gives us the value of the `say_hi` variable, which
is the function we defined. But `say_hi()` **calls** that function, so
it runs and gives us a return value. The return value is None so the
`>>>` prompt [doesn't show it](#variables.md#none).

But we know that the print function shows None, so what happens if we
wrap the whole thing in `print()`?

```python
>>> print(say_hi)       # prints the function, just like plain say_hi
<function say_hi at 0x7fd913f58488>
>>> print(say_hi())     # runs the function and then prints the return value
howdy hi
None
>>>
```

The `print(say_hi())` thing looks a bit weird at first, but it's easy to
understand. There's a print inside `say_hi` and there's also the print
we just wrote, so two things are printed. Python first ran `say_hi()`,
and it returned None so Python did `print(None)`. Adding an extra
`print()` around a function call is actually a common mistake, and I
have helped many people with this problem.

## Examples

Ask yes/no questions.

```python
def ask_yes_no(prompt):
    while True:
        answer = input(prompt + ' (y or n) ')
        if answer == 'y' or answer == 'Y':
            return True    # returning ends the function
        if answer == 'n' or answer == 'N':
            return False
        print("Answer 'y' or 'n'.")

if ask_yes_no("Do you like ice cream?"):
    print("You like ice cream!")
else:
    print("You don't like ice cream.")
```

Ask questions with multiple answers.

```python
def ask_until_correct(prompt, correct_options,
                      error_message="I don't know what you meant."):
    while True:
        answer = input(prompt + ' ')
        if answer in correct_options:
            return answer
        print(error_message)


colors = ['red', 'yellow', 'blue', 'green', 'orange', 'pink', 'black',
          'gray', 'white', 'brown']
choice = ask_until_correct("What's your favorite color?", colors,
                           error_message="I don't know that color.")
print("Your favorite color is %s!" % choice)
```

## Summary

- Functions are a way to write code once, and then use that same
    code in multiple places.
- Variables inside functions are **locals**, and variables outside
    functions are **globals**. Functions can access all variables, but
    by default, they can only create and change the value of local
    variables.
- Functions can take **arguments** and they can behave differently
    depending on what arguments they get. Arguments are just local
    variables.
- Functions can also **return** one value, like the built-in input
    function does. Returning also ends the function immediately.
- Return a value instead of printing it if you need to do something with
    it after calling the function.
- Remember that `thing`, `thing()`, `print(thing)` and `print(thing())`
    do different things.

## Exercises

**There are many things to learn about functions, and I don't expect
you to learn everything at once.** However, there are also many free
exercises about defining functions you can do.

1. What's wrong with this code?

    ```python
    def ask_name():
        name = input("Enter your name: ")

    ask_name()
    print("Your name is", name)
    ```

2. How about this code?

    ```python
    def get_greeting():
        return "Hello World!"

    print(get_greeting)
    ```

3. Why does this print None after greeting the world?

    ```python
    def greet(target):
        print("Hello", target)

    print(greet("World"))
    ```

4. Find more exercises about defining functions online.

Answers for the first, second and third exercise are
[here](answers.md#defining-functions).

***

If you have trouble with this tutorial please [tell me about
it](../contact-me.md) and I'll make this tutorial better. If you
like this tutorial, please [give it a
star](../README.md#how-can-i-thank-you-for-writing-and-sharing-this-tutorial).

You may use this tutorial freely at your own risk. See
[LICENSE](../LICENSE).

[Previous](dicts.md) | [Next](larger-program.md) |
[List of contents](../README.md#basics)
