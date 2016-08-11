# Loops

In programming, a **loop** means repeating something multiple times.
There are different kinds of loops:

- **While loops** repeat something while a condition is true.
- **Until loops** repeat something until a condition is true.
- **For loops** repeat something for each element of a sequence.

We'll talk about all of these in this tutorial.

## While loops

Now we know how if statements work.

```py
its_raining = True
if its_raining:
    print("Oh crap, it's raining!")
```

While loops are really similar to if statements. 

```py
its_raining = True
while its_raining:
    print("Oh crap, it's raining!")
    # we'll jump back to the line with the word "while" from here
print("It's not raining anymore.")
```

If you're not familiar with while loops, the program's output may be a
bit surprising:

```
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
```

Again, this program does not break your computer. It just prints the
same thing multiple times. We can interrupt it by pressing Ctrl+C.

In this example, `its_raining` was the **condition**. If something in
the while loop would have set `its_raining` to False, the loop would
have ended and the program would have printed `It's not raining anymore`.

Let's actually create a program that does just that:

```py
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

```
It's raining!
Or is it? (y=yes, n=no) i dunno
Enter y or n next time.
It's raining!
Or is it? (y=yes, n=no) y
Oh well...
It's raining!
Or is it? (y=yes, n=no) n
It's not raining anymore.
```

We can also interrupt a loop even if the condition is still true using
the `break` keyword. In this case, we'll set condition to True and rely
on nothing but `break` to end the loop.

```py
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

```py
Is it raining? (y=yes, n=no) who knows              
Enter y or n.
Is it raining? (y=yes, n=no) y
It's raining!
Is it raining? (y=yes, n=no) n
It's not raining anymore.
```

## Until loops

Python doesn't have until loops. If you need an until loop, use
`while not`:

```py
raining = False
while not raining:
    print("It's not raining.")
    if input("Is it raining? (y/n) ") == 'y':
        raining = True
print("It's raining!")
```

## For loops

Let's say we have a list of things we want to print. To print each item
in stuff, we could just do a bunch of prints:

```py
stuff = ['hello', 'hi', 'how are you doing', 'im fine', 'how about you']

print(stuff[0])
print(stuff[1])
print(stuff[2])
print(stuff[3])
print(stuff[4])
```

The output of the program is like this:

```py
hello
hi
how are you doing
im fine
how about you
```

But this is only going to print five items, so if we add something to
stuff, it's not going to be printed. Or if we remove something from
stuff, we'll get an error saying "list index out of range".

We could also create an index variable, and use a while loop:

```py
>>> length_of_stuff = len(stuff)        # len(x) is the length of x
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

But there's `len()` and an index variable we need to increment. That's
a lot of stuff to worry about for just printing each item.

This is when for loops come in:

```py
>>> stuff = ['hello', 'hi', 'how are you doing', 'im fine', 'how about you']
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

```py
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

There's only one big limitation with for looping over lists. You
shouldn't modify the list in the for loop. If you do, the results can
be surprising:

```py
>>> stuff = ['hello', 'hi', 'how are you doing', 'im fine', 'how about you']
>>> for thing in stuff:
...     stuff.remove(thing)
... 
>>> stuff
['hi', 'im fine']
>>> 
```

Instead, you can create a copy of stuff and loop over it.

```py
>>> stuff = ['hello', 'hi', 'how are you doing', 'im fine', 'how about you']
>>> for thing in stuff.copy():
...     stuff.remove(thing)
... 
>>> stuff
[]
>>> 
```

Or if you want to clear a list, just use the `.clear()` list method.

```py
>>> stuff = ['hello', 'hi', 'how are you doing', 'im fine', 'how about you']
>>> stuff.clear()
>>> stuff
[]
>>> 
```

## Excercises

1. Back in "Using if, else and elif" we created a program that asked
    for username and password and checks them, and we made users "foo"
    and "bar" with passwords "biz" and "baz". Adding a new user would
    have required adding more code that checks the username and
    password. Add this to the beginning of your program:

    ```py
    users = [
        ['foo', 'bar'],
        ['biz', 'baz'],
    ]
    ```

    Then rewrite the rest of the program using a for loop.

2. Make the program ask the username and password over and over again
3. Can you limit the number of attempts to 3?
