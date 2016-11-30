# Answers

These are answers for exercises in the chapters. In programming, there's always more than one way to do things, so if your solution wasn't exactly like mine it's not necessarily wrong. Some Python users say that there should be only one right way, but that goal will never be fully reached.

## ThinkPython: The way of the program

1. With +, the strings get added together, and with * we get an error.
2. With + we get an error, and with * the string is repeated multiple times.
3. Python calculates the result and echoes it.

## Using if, else and elif

1. Just ask the word and print word * 1000.

    ```py
    word = input("Enter a word: ")
    print(word * 1000)
    ```

2. Add a space to the word before printing.

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

3. Like this:

    ```py
    first = input("Enter a word: ")
    second = input("Enter another word: ")
    words = first + " " + second + " "
    print(words * 1000)
    ```

4. You can compare the word against an empty string (`""` or `''`) to
    check if it's empty. In this example, the password is "secret".

    ```py
    word = input("Enter your password: ")

    if word == "secret":
        print("Welcome!")
    elif word == "":
        print("You didn't enter anything.")
    else:
        print("Access denied.")
    ```

5. Simply check the username first, then the password in indented
    blocks of code.

    ```py
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == "foo":
        if password == "biz":
            print("Welcome foo!")
        else:
            print("Wrong password!")
    elif username == "bar":
        if password == "baz":
            print("Welcome bar!")
        else:
            print("Wrong password!")
    else:
        print("Wrong username.")
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

1. Use `-value` (it works just like `-1`) to get the negative in
    the abs function, and for loops in the other two functions.

    ```py
    def my_abs(value):
        if value < 0:
            return -value
        # actually, this else is useless because returning ends the
        # function anyway
        else:
            return value

    def my_any(a_list):  # don't call this "list", see summary in the Lists chapter
        for item in a_list:
            if item:
                return True    # ends the function
        return False

    def my_all(a_list):
        for item in a_list:
            if not item:
                return False
        return True
    ```

2. Like this:

    ```py
    def print_box(message, character='*'):
        number_of_characters = len(message) + 4
        print(character * number_of_characters)
        print(character, message, character)
        print(character * number_of_characters)
    ```

***

You may use this tutorial freely at your own risk. See [LICENSE](LICENSE).

[Back to the list of contents](README.md#list-of-contents)

***

You may use this tutorial freely at your own risk. See
[LICENSE](LICENSE).
