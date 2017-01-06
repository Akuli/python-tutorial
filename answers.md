# Answers

These are my answers for exercises in the chapters. If your solution
isn't exactly like mine but it works just fine it's ok, and you can
[ask me](contact-me.md) why I didn't do it like you did it.

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

2. The broken code has mostly the same issues as exercise 1. On the
    last line the comma is on the wrong side. `"bla bla,"` is a string
    that **contains** a comma, but `"bla bla",` is a string and a
    **separate** comma. In this exercise, the last line should be
    `print("I don't know what", something, "means.")`

3. We can simply ask the word with input and print `word * 1000`.

    ```py
    word = input("Enter a word: ")
    print(word * 1000)
    ```

4. We can add a space to the word before we print it.

    ```py
    word = input("Enter a word: ")
    word += " "
    print(word * 1000)
    ```

    We can also add the space right away on the first line:

    ```py
    word = input("Enter a word: ") + " "
    print(word * 1000)
    ```

    Of course, there are 999 spaces between 1000 words and this will
    print 1000 spaces instead, so there will be a useless space at the
    end, but it doesn't matter. If we really want to get rid of the
    space, we can do something like this instead:

    ```py
    no_space = input("Enter a word: ")
    yes_space = no_space + " "
    print(yes_space * 999 + no_space)
    ```

5. Like this:

    ```py
    first = input("Enter a word: ")
    second = input("Enter another word: ")
    words = first + " " + second + " "
    print(words * 1000)
    ```

6. We can compare the word against an empty string (`""` or `''`) to
    check if it's empty. In this example, the password is "s3cr3t".

    ```py
    word = input("Enter your password: ")

    if word == "s3cr3t":
        print("Welcome!")
    elif word == "":
        print("You didn't enter anything.")
    else:
        print("Access denied.")
    ```

    This is not a good way to ask a password from the user because the
    password isn't hidden in any way, but this is just an example.

## Handy stuff: Strings

1. The program is not like you might expect it to be. It actually works
    just fine if we run it, but there's the problem. The last line is
    really long and it's hard to see what it does.

    The solution is string formatting. At the time of writing this, I
    recommend replacing the last line with one of these:

    ```py
    print("You entered %s, %s, %s and %s." % (word1, word2, word3, word4))
    print("You entered {}, {}, {} and {}.".format(word1, word2, word3, word4))
    ```

    In the future when most people will have Python 3.6 or newer, you
    can also use this:

    ```py
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

    ```py
    message = input("What do you want me to say? ")
    uppermessage = message.upper()
    print(uppermessage, "!!!")
    print(uppermessage, "!!!")
    print(uppermessage, "!!!")
    ```

    Or we can reuse the same variable name:

    ```py
    message = input("What do you want me to say? ")
    message = message.upper()
    print(message, "!!!")
    print(message, "!!!")
    print(message, "!!!")
    ```

    Or we can convert the message to uppercase right away on the first
    line:

    ```py
    message = input("What do you want me to say? ").upper()
    print(message, "!!!")
    print(message, "!!!")
    print(message, "!!!")
    ```

## Loops

1. For loop over the users, each user is a list that contains a
    username and a password.

    ```py
    users = [
        ['foo', 'biz'],
        ['bar', 'baz'],
    ]

    username = input("Username: ")
    password = input("Password: ")

    logged_in = False
    for user in users:
        if username == user[0] and password == user[1]:
            logged_in = True
            break

    if logged_in:
        print("Welcome, " + username + "!")
    else:
        print("Wrong username or password.")
    ```

2. Just put the whole thing in a `while True:`. Remember that a break
    will always break the innermost loop it's in.

    ```py
    users = [
        ['foo', 'biz'],
        ['bar', 'baz'],
    ]

    while True:
        username = input("Username: ")
        password = input("Password: ")

        logged_in = False
        for user in users:
            if username == user[0] and password == user[1]:
                logged_in = True
                break   # break the for loop

        if logged_in:
            print("Welcome, " + username + "!")
            break   # break the while loop
        else:
            print("Wrong username or password.")
    ```

3. Add a for loop that works as an attempt counter.

    ```py
    users = [
        ['foo', 'biz'],
        ['bar', 'baz'],
    ]

    for attempts_left in [3, 2, 1, 0]:
        if attempts_left == 0:
            print("No attempts left!")
            break   # break the outer for loop

        print(attempts_left, "attempts left.")
        username = input("Username: ")
        password = input("Password: ")

        logged_in = False
        for user in users:
            if username == user[0] and password == user[1]:
                logged_in = True
                break   # break the inner for loop

        if logged_in:
            print("Welcome, " + username + "!")
            break   # break the outer for loop
        else:
            print("Wrong username or password.")
    ```

## Trey Hunner: zip and enumerate

1. Read some lines with `input` into a list and then enumerate it.

    ```py
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

    ```py
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

    ```py
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'

    for upper, lower in zip(uppercase, lowercase):
        print(upper, lower)
    ```

3. This one is a bit more difficult than the other two because we
    need to combine `zip` and `enumerate`. One way to do this is
    to pass a `zip` result to `enumerate`, like this:

    ```py
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'

    for index, letterpair in enumerate(zip(uppercase, lowercase), start=1):
        upper, lower = letterpair
        print(index, upper, lower)
    ```

    We can also save the zip result to a variable. I would
    probably do this.

    ```py
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'

    letterzip = zip(uppercase, lowercase)
    for index, letterpair in enumerate(letterzip, start=1):
        upper, lower = letterpair
        print(index, upper, lower)
    ```

    Another alternative is to pass an `enumerate` result to `zip`. This is
    a bit more complicated, so I wouldn't do it this way.

    ```py
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'

    for upper, indexlowerpair in zip(uppercase, enumerate(lowercase, start=1)):
        index, lower = indexlowerpair
        print(index, upper, lower)
    ```

## Defining functions

1. The problem with the first example is that name is a local variable.
    I explained how to fix this in [the output section](defining-functions.md#output):

    ```py
    def ask_name():
        name = input("Enter your name: ")
        return name
    
    print("Your name is", ask_name())
    ```

2. If you run the next example, you get something like this:

        <function get_greeting at 0xb73a0a04>

    The problem is that we print the actual `get_greeting` function,
    but we need to **call** it like `get_greeting()`:

    ```py
    def get_greeting():
        return "Hello World!"
    
    print(get_greeting())
    ```

3. See [the return or print section](defining-functions.html#return-or-print).

    The greet function prints a greeting.

    ```py
    >>> greet("World")
    Hello World
    >>> 
    ```

    But it also returns None because we don't tell it to return anything else.

    ```py
    >>> return_value = greet("World")
    Hello World
    >>> print(return_value)
    None
    >>> 
    ```

    This code from the exercise does the same thing as the code above
    does, but without a temporary `return_value` variable:

    ```py
    >>> print(greet("World"))
    Hello World
    None
    >>> 
    ```

***

You may use this tutorial freely at your own risk. See
[LICENSE](LICENSE).

[List of contents](README.md#list-of-contents)
