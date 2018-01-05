# If, else and elif

## Using if statements

Now we know what True and False are.

```python
>>> 1 == 1
True
>>> 1 == 2
False
>>>
>>> its_raining = True
>>> its_raining
True
>>>
```

But what if we want to execute different code depending on something?
That's when `if` comes in.

```python
>>> its_raining = True
>>> if its_raining:
...     print("It's raining!")
...
It's raining!
>>> its_raining = False
>>> if its_raining:
...     print("It's raining!")        # nothing happens
...
>>>
```

The prompt changed from `>>>` to `...`. It meant that Python was
expecting me to keep typing. When I was done, I just pressed Enter
twice. My code was executed and the prompt went back to `>>>`.

An important thing to notice is that the line with a print is
**indented**. You can press the tab key, or if it doesn't work
just press space a few times.

But why is that `if its_raining` instead of `if(its_raining)`?

Earlier we learned that `if` is a **keyword**.

```python
>>> if = 123
  File "<stdin>", line 1
    if = 123
       ^
SyntaxError: invalid syntax
>>>
```

**Functions** like `print` need `()` after their name to work. But `if`
is **a keyword**, not a function, so it doesn't need `()`. Python has
separate functions and keywords because it's possible to create custom
functions, but it's not possible to create custom keywords. That's why
keywords are usually used for "magic" things that would be difficult to
do with just functions.

Also note that if statements check the condition once only, so if we
set it to false later the if statement won't notice it.

```python
>>> its_raining = True
>>> if its_raining:
...     its_raining = False
...     print("It's not raining, but this runs anyway.")
...
It's not raining, but this runs anyway.
>>>
```

## Using else

What if we want to print a different message if it's not raining? We
could do something like this:

```python
its_raining = True                  # you can change this to False
its_not_raining = not its_raining   # False if its_raining, True otherwise

if its_raining:
    print("It's raining!")
if its_not_raining:
    print("It's not raining.")
```

Note that this code example doesn't start with `>>>`, so you should
[save it to a file and run the file](editor-setup.md).

Now our program will print a different value depending on what the
value of `its_raining` is.

We can also add `not its_raining` directly to the second if statement:

```python
its_raining = True

if its_raining:
    print("It's raining!")
if not its_raining:
    print("It's not raining.")
```

But we can make it even better by using `else`.

```python
its_raining = True

if its_raining:
    print("It's raining!")
else:
    print("It's not raining.")
```

The else part simply runs when the if statement doesn't run. It doesn't
check the condition again.

```python
>>> its_raining = True
>>> if its_raining:
...     its_raining = False
... else:
...     print("It's not raining, but this still doesn't run.")
...
>>>
```

By combining `else` with the input function we can make a program that
asks for a password and checks if it's correct.

```python
print("Hello!")
password = input("Enter your password: ")

if password == "secret":
    print("That's correct, welcome!")
else:
    print("Access denied.")
```

The program prints different things depending on what we enter:

```
Hello!
Enter your password: secret
Welcome!
```

```
Hello!
Enter your password: lol
Access denied.
```

Using the input function for passwords doesn't work very well because
we can't hide the password with asterisks. There are better ways to get
a password from the user, but you shouldn't worry about that just yet.

## Avoiding many levels of indentation with elif

If we have more than one condition to check, we could do this:

```python
print("Hello!")
word = input("Enter something: ")

if word == "hi":
    print("Hi to you too!")
else:
    if word == "hello":
        print("Hello hello!")
    else:
        if word == "howdy":
            print("Howdyyyy!")
        else:
            if word == "hey":
                print("Hey hey hey!")
            else:
                if word == "gday m8":
                    print("Gday 4 u 2!")
                else:
                    print("I don't know what", word, "means.")
```

This code is a mess. We need to indent more every time we want to check
for more words. Here we check for 5 different words, so we have 5 levels
of indentation. If we would need to check 30 words, the code would
become really wide and it would be hard to work with.

Instead of typing `else`, indenting more and typing an `if` we can
simply type `elif`, which is short for `else if`. Like this:

```python
print("Hello!")
word = input("Enter something: ")

if word == "hi":
    print("Hi to you too!")
elif word == "hello":
    print("Hello hello!")
elif word == "howdy":
    print("Howdyyyy!")
elif word == "hey":
    print("Hey hey hey!")
elif word == "gday m8":
    print("Gday 4 u 2!")
else:
    print("I don't know what", word, "means.")
```

Now the program is shorter and much easier to read.

Note that the `elif` parts only run if nothing before them matches, and
the `else` runs only when none of the `elifs` match. If we would have
used `if` instead, all possible values would be always checked and the
`else` part would run always except when word is `"gday m8"`. This is
why we use `elif` instead of `if`.

For example, this program prints only `hello`...

```python
if 1 == 1:
    print("hello")
elif 1 == 2:
    print("this is weird")
else:
    print("world")
```

...but this prints `hello` *and* `world`:

```python
if 1 == 1:
    print("hello")
if 1 == 2:
    print("this is weird")
else:
    print("world")
```

Now the `else` belongs to the `if 1 == 2` part and **it has nothing to
do with the `if 1 == 1` part**. On the other hand, the elif version
**grouped the multiple ifs together** and the `else` belonged to all of
them. Adding a blank line makes this obvious:

```python
if 1 == 1:
    print("hello")

if 1 == 2:
    print("this is weird")
else:
    print("world")
```

In general, adding blank lines to appropriate places is a good idea. If
you are asked to "fix code", feel free to add missing blank lines.

## Summary

- If a code example starts with `>>>` run it on the interactive prompt.
    If it doesn't, write it to a file and run that file.
- Indentation is important in Python.
- Indented code under an if statement runs if the condition is true.
- We can also add an else statement. Indented code under it will run
    if the code under the if statement does not run.
- elif is short for else if.

## Exercises

1. This program contains several problems. Copy-paste it to a file,
    then try to run it, fix the errors you got, try to run it again and
    keep going until it works.

    ```python
    print(Hello!)
    something == input('Enter something: )
    print('You entered:' something)
    ```

2. Fix this program the same way:

    ```python
    print('Hello!')
    something = input("Enter something: ")
    if something = 'hello':
        print("Hello for you too!")

    elif something = 'hi'
        print('Hi there!')
    else:
        print("I don't know what," something, "means.")
    ```

3. Write a program into a file that asks the user to write a word and
    then prints that word 1000 times. For example, if the user enters
    `hi` the program would reply `hihihihihihihihi` ...

4. Add spaces between the words, so the output is like `hi hi hi hi` ...

5. Make something that asks the user to enter two words, and prints
    1000 of each with spaces in between. For example, if the user
    enters `hello` and `hi` the program would print
    `hello hi hello hi hello hi hello hi hello hi` ...

6. Make a program that asks for a password and prints `Welcome!`,
    `Access denied` or `You didn't enter anything` depending on whether
    the user entered the correct password, a wrong password, or nothing
    at all by pressing Enter without typing anything.

The answers are [here](answers.md#if-else-and-elif).

***

If you have trouble with this tutorial please [tell me about
it](../contact-me.md) and I'll make this tutorial better. If you
like this tutorial, please [give it a
star](../README.md#how-can-i-thank-you-for-writing-and-sharing-this-tutorial).

You may use this tutorial freely at your own risk. See
[LICENSE](../LICENSE).

[Previous](editor-setup.md) | [Next](handy-stuff-strings.md) |
[List of contents](../README.md#basics)
