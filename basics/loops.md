# Loops

In programming, a **loop** means repeating something multiple times.
There are different kinds of loops:

- [While loops](#while-loops) repeat something while a condition is true.
- [Until loops](#until-loops) repeat something while a condition is false.
- [For loops](#for-loops) repeat something for each element of something.

We'll talk about all of these in this tutorial.

## While loops

Now we know how if statements work.

```python
its_raining = True
if its_raining:
    print("Oh crap, it's raining!")
```

While loops are really similar to if statements.

```python
its_raining = True
while its_raining:
    print("Oh crap, it's raining!")
    # we'll jump back to the line with the word "while" from here
print("It's not raining anymore.")
```

If you're not familiar with while loops, the program's output may be a
bit surprising:

    Oh crap, it's raining!
    Oh crap, it's raining!
    Oh crap, it's raining!
    Oh crap, it's raining!
    Oh crap, it's raining!
    Oh crap, it's raining!
    Oh crap, it's raining!
    Oh crap, it's raining!
    Oh crap, it's raining!
    Oh crap, it's raining!
    Oh crap, it's raining!
    Oh crap, it's raining!
    Oh crap, it's raining!
    Oh crap, it's raining!
    Oh crap, it's raining!
    (much more raining)

Again, this program does not break your computer. It just prints the
same thing multiple times. We can interrupt it by pressing Ctrl+C.

In this example, `its_raining` was the **condition**. If something in
the while loop would have set `its_raining` to False, the loop would
have ended and the program would have printed `It's not raining anymore`.

Let's actually create a program that does just that:

```python
its_raining = True
while its_raining:
    print("It's raining!")
    answer = input("Or is it? (y=yes, n=no) ")
    if answer == 'y':
        print("Oh well...")
    elif answer == 'n':
        its_raining = False     # end the while loop
    else:
        print("Enter y or n next time.")
print("It's not raining anymore.")
```

Running the program may look like this:

    It's raining!
    Or is it? (y=yes, n=no) i dunno
    Enter y or n next time.
    It's raining!
    Or is it? (y=yes, n=no) y
    Oh well...
    It's raining!
    Or is it? (y=yes, n=no) n
    It's not raining anymore.

The while loop doesn't check the condition all the time, it only checks
it in the beginning.

```python
>>> its_raining = True
>>> while its_raining:
...     its_raining = False
...     print("It's not raining, but the while loop doesn't know it yet.")
...
It's not raining, but the while loop doesn't know it yet.
>>>
```

We can also interrupt a loop even if the condition is still true using
the `break` keyword. In this case, we'll set condition to True and rely
on nothing but `break` to end the loop.

```python
while True:
    answer = input("Is it raining? (y=yes, n=no) ")
    if answer == 'y':
        print("It's raining!")
    elif answer == 'n':
        print("It's not raining anymore.")
        break   # end the loop
    else:
        print("Enter y or n.")
```

The program works like this:

    Is it raining? (y=yes, n=no) who knows
    Enter y or n.
    Is it raining? (y=yes, n=no) y
    It's raining!
    Is it raining? (y=yes, n=no) n
    It's not raining anymore.

Unlike setting the condition to False, breaking the loop ends it
immediately.

```python
>>> while True:
...     break
...     print("This is never printed.")
...
>>>
```

## Until loops

Python doesn't have until loops. If we need an until loop, we can use
`while not`:

```python
raining = False
while not raining:
    print("It's not raining.")
    if input("Is it raining? (y/n) ") == 'y':
        raining = True
print("It's raining!")
```

## For loops

Let's say we have [a list](lists-and-tuples.md) of things we want to
print. To print each item in it, we could just do a bunch of prints:

```python
stuff = ['hello', 'hi', 'how are you doing', 'im fine', 'how about you']

print(stuff[0])
print(stuff[1])
print(stuff[2])
print(stuff[3])
print(stuff[4])
```

The output of the program is like this:

    hello
    hi
    how are you doing
    im fine
    how about you

But this is only going to print five items, so if we add something to
stuff, it's not going to be printed. Or if we remove something from
stuff, we'll get an error saying "list index out of range".

We could also create an index variable, and use a while loop:

```python
>>> stuff = ['hello', 'hi', 'how are you doing', 'im fine', 'how about you']
>>> length_of_stuff = len(stuff)
>>> index = 0
>>> while index < length_of_stuff:
...     print(stuff[index])
...     index += 1
...
hello
hi
how are you doing
im fine
how about you
>>>
```

But we have `len()` and an index variable we need to increment and a
while loop and many other things to worry about. That's a lot of work
just for printing each item.

This is when for loops come in:

```python
>>> for thing in stuff:
...     # this is repeated for each element of stuff, that is, first
...     # for stuff[0], then for stuff[1], etc.
...     print(thing)
...
hello
hi
how are you doing
im fine
how about you
>>>
```

Without the comments, that's only two simple lines, and one variable.
Much better than anything else we tried before.

```python
>>> for thing in stuff:
...     print(thing)
...
hello
hi
how are you doing
im fine
how about you
>>>
```

Note that `for thing in stuff:` is not same as `for (thing in stuff):`.
Here the `in` keyword is just a part of the for loop and it has a
different meaning than it would have if we had `thing in stuff` without
a `for`. Trying to do `for (thing in stuff):` creates an error.

Right now the while loop version might seem easier to understand for
you, but later you'll realize that for loops are much easier to work
with than while loops and index variables, especially in large projects.
For looping is also a little bit faster than while looping with an index
variable.

For loops are not actually limited to lists. We can for loop over many
other things also, including strings and
[tuples](lists-and-tuples.md#tuples). For looping over a tuple gives us
its items, and for looping over a string gives us its characters as
strings of length one.

```python
>>> for short_string in 'abc':
...     print(short_string)
...
a
b
c
>>> for item in (1, 2, 3):
...     print(item)
...
1
2
3
>>>
```

If we can for loop over something, then that something is **iterable**.
Lists, tuples and strings are all iterable.

There's only one big limitation with for looping over lists. We
shouldn't modify the list in the for loop. If we do, the results can
be surprising:

```python
>>> stuff = ['hello', 'hi', 'how are you doing', 'im fine', 'how about you']
>>> for thing in stuff:
...     stuff.remove(thing)
...
>>> stuff
['hi', 'im fine']
>>>
```

Instead, we can create a copy of stuff and loop over it.

```python
>>> stuff = ['hello', 'hi', 'how are you doing', 'im fine', 'how about you']
>>> for thing in stuff.copy():
...     stuff.remove(thing)
...
>>> stuff
[]
>>>
```

Or if we just want to clear a list, we can use the `clear`
[list method](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists):

```python
>>> stuff = ['hello', 'hi', 'how are you doing', 'im fine', 'how about you']
>>> stuff.clear()
>>> stuff
[]
>>>
```

## Summary

- A loop means repeating something multiple times.
- While loops repeat something as long as a condition is true, and
    they check the condition only in the beginning.
- For loops can be used for repeating something to each item in a list.
- An iterable is something that can be for looped over.
- The `break` keyword can be used to interrupt the innermost loop at
    any time.

## Examples

Repeat something an endless amount of times.

```python
message = input("What do you want me to say? ")
while True:
    print(message, "!!!")
```

Ask the user to enter five things and print them.

```python
things = []

print("Enter 5 things: ")
while len(things) < 5:
    thing = input("> ")
    things.append(thing)

print("You entered these things:")
for thing in things:
    print(thing)
```

Ask the user a bunch of questions.

```python
questions_and_answers = [
    # [question, answer], ...
    ["What is 2+4? ", "6"],
    ["What is 2-4? ", "-2"],
    ["What is 2*4? ", "8"],
    ["What is 2/4? ", "0.5"],
    # You could add more questions, but the code that asks them
    # wouldn't need to be changed in any way.
]

for qa in questions_and_answers:
    while True:
        if input(qa[0]) == qa[1]:
            print("Correct!")
            break
        else:
            print("That's not what I was thinking of... Try again.")
```

Store a list of names and let the user check if the program knows
the user.

```python
# You can add names here so the program will know them automatically
# when it starts.
namelist = []

print("Options:")
print("  0      Quit")
print("  1      Check if I know you")
print("  2      Introduce yourself to me")
print("  3      Make me forget you")
print("  4      Print a list of people I know")
print()     # print an empty line

while True:
    option = input("Choose an option: ")

    # Things like option == 0 don't work because option is a string
    # and it needs to be compared with a string:
    #   >>> 0 == 0
    #   True
    #   >>> '0' == '0'
    #   True
    #   >>> 0 == '0'
    #   False
    if option == '0':
        print("Bye!")
        break

    elif option == '1':
        name = input("Enter your name: ")
        if name in namelist:
            print("I know you! :D")
        else:
            print("I don't know you :/")

    elif option == '2':
        name = input("Enter your name: ")
        if name in namelist:
            print("I knew you already.")
        else:
            namelist.append(name)
            print("Now I know you!")

    elif option == '3':
        name = input("Enter your name: ")
        if name in namelist:
            namelist.remove(name)
            print("Now I don't know you.")
        else:
            print("I didn't know you to begin with.")

    elif option == '4':
        if namelist == []:
            print("I don't know anybody yet.")
        else:
            for name in namelist:
                print("I know %s!" % name)

    else:
        print("I don't understand :(")

    print()
```

## Exercises

1. This code is supposed to print the numbers 1,2,3,4,5. Fix it.

    ```python
    things = str([1, 2, 3, 4, 5])
    for thing in things:
        print(thing)
    ```

2. This code is supposed to print `[1, 2, 3, 4, 5, 6]`. Fix it without
    changing the `before` list.

    ```python
    before = [[1, 2], [3, 4], [5, 6]]
    after = []
    for number in before:
        after.append(number)
    print(after)
    ```

3.  This program is supposed to convert everything in a list to integers
    and then calculate their sum. It should print 6 because `1 + 2 + 3`
    is 6. Fix the program.

    ```python
    input = ['1', '2', '3']

    for string in input:
        numbers = []
        numbers.append(int(string))

    result = 0
    for n in numbers:
        result + n
    print("their sum is", result)
    ```

4. This program is supposed to print `[1, 2, 3]`. Fix it.

    ```python
    numbers = ['1', '2', '3']
    for number in numbers:
        number = int(number)
    print(numbers)
    ```

The answers are [here](answers.md#loops).

***

If you have trouble with this tutorial please [tell me about
it](../contact-me.md) and I'll make this tutorial better. If you
like this tutorial, please [give it a
star](../README.md#how-can-i-thank-you-for-writing-and-sharing-this-tutorial).

You may use this tutorial freely at your own risk. See
[LICENSE](../LICENSE).

[Previous](lists-and-tuples.md) | [Next](trey-hunner-zip-and-enumerate.md) |
[List of contents](../README.md#basics)
