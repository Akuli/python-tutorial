# Answers

These are my answers for exercises in the chapters. If your solution
isn't exactly like mine but it works just fine it's ok, and you can
[ask me](../contact-me.md) why I didn't do it like you did it.

## ThinkPython: The way of the program

1. With +, the strings get added together, and with * we get an error.
2. With + we get an error, and with * the string is repeated multiple times.
3. Python calculates the result and echoes it.

## If, else and elif

1. Problems and solutions:

    - The first line should be `print("Hello!")` or `print('Hello!')`,
        not `print(Hello!)`. `Hello!` is a piece of text, so we need to
        tell Python that it's a string by putting quotes around it.
    - The second line will create an error message that says that
        there's no variable called `something`. But we are trying to
        create it here, so we need `=` instead of `==`. `=` is
        assigning, `==` is comparing.
    - The last line should have a comma between the arguments, like
        `print('You entered:', something)`.

2. The broken code has mostly the same issues as exercise 1. Here are
    the problems that excercise 1 doesn't have:

    - The if-elif-else has a blank line at a confusing place. Delete it.
    - After deleting the code, it looks quite dense. Add a new blank
      line before the `if`.
    - The elif line is missing a `:` at the end.
    - On the last line the comma is on the wrong side. `"bla bla,"` is
      a string that **contains** a comma, but `"bla bla",` is a
      string and a **separate** comma. In this exercise, the last
      line should be `print("I don't know what", something, "means.")`

3. We can simply ask the word with input and print `word * 1000`.

    ```python
    word = input("Enter a word: ")
    print(word * 1000)
    ```

4. We can add a space to the word before we print it.

    ```python
    word = input("Enter a word: ")
    word += " "
    print(word * 1000)
    ```

    We can also add the space right away on the first line:

    ```python
    word = input("Enter a word: ") + " "
    print(word * 1000)
    ```

    Of course, there are 999 spaces between 1000 words and this will
    print 1000 spaces instead, so there will be a useless space at the
    end, but it doesn't matter. If we really want to get rid of the
    space, we can do something like this instead:

    ```python
    no_space = input("Enter a word: ")
    yes_space = no_space + " "
    print(yes_space*999 + no_space)
    ```

5. Like this:

    ```python
    first = input("Enter a word: ")
    second = input("Enter another word: ")
    words = first + " " + second + " "
    print(words * 1000)
    ```

6. We can compare the word against an empty string (`""` or `''`) to
    check if it's empty. In this example, the password is "seKr3t".

    ```python
    word = input("Enter your password: ")

    if word == "seKr3t":
        print("Welcome!")
    elif word == "":
        print("You didn't enter anything.")
    else:
        print("Access denied.")
    ```

    Again, this is not a good way to ask a real password from the user.

## Handy stuff: Strings

1. The program is not like you might expect it to be. It actually works
    just fine if we run it, but there's a problem. The last line is
    really long and it's hard to see what it does.

    The solution is string formatting. At the time of writing this, I
    recommend replacing the last line with one of these:

    ```python
    print("You entered %s, %s, %s and %s." % (word1, word2, word3, word4))
    print("You entered {}, {}, {} and {}.".format(word1, word2, word3, word4))
    ```

    In the future when most people will have Python 3.6 or newer, you
    can also use this:

    ```python
    print(f"You entered {word1}, {word2}, {word3} and {word4}.")
    ```

2. If we have a look at `help(str.upper)` it looks like this:

        S.upper() -> str

        Return a copy of S converted to uppercase.

    We have two problems. First of all, the broken code uses
    `message.upper` instead of `message.upper()`. It also expects the
    message to magically make itself uppercased, but strings can't be
    changed in-place so it doesn't work.

    The solution is to do `message.upper()` and save the value we got
    from that to a variable:

    ```python
    message = input("What do you want me to say? ")
    uppermessage = message.upper()
    print(uppermessage, "!!!")
    print(uppermessage, "!!!")
    print(uppermessage, "!!!")
    ```

    Or we can reuse the same variable name:

    ```python
    message = input("What do you want me to say? ")
    message = message.upper()
    print(message, "!!!")
    print(message, "!!!")
    print(message, "!!!")
    ```

    Or we can convert the message to uppercase right away on the first
    line:

    ```python
    message = input("What do you want me to say? ").upper()
    print(message, "!!!")
    print(message, "!!!")
    print(message, "!!!")
    ```

## Lists and tuples

1.  Look carefully. The `namelist` is written in `()` instead of `[]`,
    so it's actually a tuple, not a list. Using confusing variable names
    is of course a bad idea, but you shouldn't be surprised if someone
    is doing that. Replace the `()` with `[]` and the code will work.

2. When we run the program we get a weird error:

        Hello!
        Enter your name: my name
        Traceback (most recent call last):
          File "program.py", line 3, in <module>
            print("Your name is " + name + ".")
        TypeError: Can't convert 'tuple' object to str implicitly

    So Python is trying to convert a tuple to a string. But
    `"Your name is "` and `"."` are strings, so maybe `name` is a
    tuple? Let's change the last line to just `print(name)` so our
    program looks like this:

    ```python
    print("Hello!")
    name = input("Enter your name: "),
    print(name)
    ```

    Let's run it.

        Hello!
        Enter your name: my name
        ('my name',)

    `name` is indeed a tuple! The problem is the second line. Look
    carefully, there's a comma after `input("Enter your name: ")`.
    Python created a tuple automatically, but that's not what we
    wanted. If we remove the comma, everything works just fine.

3. Again, the code gives us a weird error message.

        Enter your name: my name
        Traceback (most recent call last):
          File "program.py", line 3, in <module>
            if input("Enter your name: ") in namelist:
        TypeError: argument of type 'NoneType' is not iterable

    Now we need to remember that when the error messages talk about
    `NoneType` [they always mean None](variables.md#none). So
    `namelist` seems to be None. Let's make the program a bit simpler
    for working on the namelist:

    ```python
    namelist = ['wub_wub', 'RubyPinch', 'go|dfish', 'Nitori']
    namelist = namelist.extend('theelous3')
    print(namelist)
    ```

    Now fixing the namelist is easier, so I'll just go through the
    problems and solutions:

    - `namelist` is None. It should be `namelist.extend('theelous3')`,
        not `namelist = namelist.extend('theelous3')`. See [this
        thing](using-functions.md#return-values).
    - Now the namelist is like `['wub_wub', ..., 't', 'h', 'e', 'e', ...]`.
        Python treated `'theelous3'` like a list so it added each of its
        characters to `namelist`. We can use `namelist.append('theelous3')`
        or `namelist.extend(['theelous3'])` instead to solve this problem.

## Loops

1. The problem is that `things` is a string because we converted it to a
    string with `str`, so the for loop loops over the characters `[`,
    `1`, `,` and so on. Replace `str([1, 2, 3, 4, 5])` with
    `[1, 2, 3, 4, 5]`.

2. The code appends each list in `before` to `after`, so the `number`
    variable actually pointed to a list like `[1, 2]`. An easy solution
    is to just write two for loops inside each other:

    ```python
    before = [[1, 2], [3, 4], [5, 6]]
    after = []
    for sublist in before:
        for number in sublist:
            after.append(number)
    print(after)
    ```

    Lists also have an extend method that appends each item from another
    list, so we can also use that:

    ```python
    before = [[1, 2], [3, 4], [5, 6]]
    after = []
    for sublist in before:
        after.extend(sublist)
    print(after)
    ```

3. The code has some empty lines in it, and they divide it nicely into
    three parts. All of these parts have some problems, so I'll go
    through them one by one.

    The first part makes a variable called `input`. The problem is that
    now the rest of the program [can't use the input
    function](using-functions.md#variables-names-and-builtin-things). It
    doesn't really matter here because the rest of the program doesn't
    use it anyway, but I still recommend using some other variable name,
    like `inputlist`.

    The second part runs `numbers = []` three times. It was probably
    meant to be ran once before the loop started, like this:

    ```python
    numbers = []
    for string in inputlist:
        numbers.append(int(string))
    ```

    The third part calculates `result + n` but throws away the value.
    It was probably supposed to do `result += n` instead.

4. If you run this program you'll notice that nothing happened to the
    numbers list. The reason is that the `number` variable only works
    one way. It gets its values from the `numbers` list, but changing it
    doesn't change the `numbers` list. In general, `thing = stuff`
    changes the `thing` variable, and that's it. It doesn't change
    anything else.

    An easy solution is to just create a new list:

    ```python
    numbers = ['1', '2', '3']
    converted_numbers = []
    for number in numbers:
        converted_numbers.append(int(number))
    print(converted_numbers)
    ```

## Trey Hunner: zip and enumerate

1. Read some lines with `input` into a list and then enumerate it.

    ```python
    print("Enter something, and press Enter without typing anything",
          "when you're done.")

    lines = []
    while True:
        line = input('>')
        if line == '':
            break
        lines.append(line)

    for index, line in enumerate(lines, start=1):
        print("Line", index, "is:", line)
    ```

2. Let's start by trying out `zip` with strings:

    ```python
    >>> for pair in zip('ABC', 'abc'):
    ...     print(pair)
    ...
    ('A', 'a')
    ('B', 'b')
    ('C', 'c')
    >>>
    ```

    Great, it works just like it works with lists. Now let's create
    the letter printing program:

    ```python
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'

    for upper, lower in zip(uppercase, lowercase):
        print(upper, lower)
    ```

3. This one is a bit more difficult than the other two because we
    need to combine `zip` and `enumerate`. One way to do this is
    to pass a `zip` result to `enumerate`, like this:

    ```python
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'

    for index, letterpair in enumerate(zip(uppercase, lowercase), start=1):
        upper, lower = letterpair
        print(index, upper, lower)
    ```

    We can also save the zip result to a variable. I would
    probably do this.

    ```python
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'

    letterzip = zip(uppercase, lowercase)
    for index, letterpair in enumerate(letterzip, start=1):
        upper, lower = letterpair
        print(index, upper, lower)
    ```

    Another alternative is to pass an `enumerate` result to `zip`. This is
    a bit more complicated, so I wouldn't do it this way.

    ```python
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'

    for upper, indexlowerpair in zip(uppercase, enumerate(lowercase, start=1)):
        index, lower = indexlowerpair
        print(index, upper, lower)
    ```

## Defining functions

1. The problem with the first example is that name is a local variable.
    I explained how to fix this in [the output section](defining-functions.md#output):

    ```python
    def ask_name():
        name = input("Enter your name: ")
        return name

    print("Your name is", ask_name())
    ```

2. If you run the next example, you get something like this:

        <function get_greeting at 0xb73a0a04>

    The problem is that we print the actual `get_greeting` function,
    but we need to **call** it like `get_greeting()`:

    ```python
    def get_greeting():
        return "Hello World!"

    print(get_greeting())
    ```

3. See [the return or print section](defining-functions.md#return-or-print).

    The greet function prints a greeting.

    ```python
    >>> greet("World")
    Hello World
    >>>
    ```

    But it also returns None because we don't tell it to return anything else.

    ```python
    >>> return_value = greet("World")
    Hello World
    >>> print(return_value)
    None
    >>>
    ```

    This code from the exercise does the same thing as the code above
    does, but without a temporary `return_value` variable:

    ```python
    >>> print(greet("World"))
    Hello World
    None
    >>>
    ```

***

If you have trouble with this tutorial please [tell me about
it](../contact-me.md) and I'll make this tutorial better. If you
like this tutorial, please [give it a
star](../README.md#how-can-i-thank-you-for-writing-and-sharing-this-tutorial).

You may use this tutorial freely at your own risk. See
[LICENSE](../LICENSE).

[List of contents](../README.md#list-of-contents)
