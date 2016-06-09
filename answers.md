# Answers

These are answers for exercises in the chapters. In programming, there's always more than one way to do things, so if your solution wasn't exactly like mine it's not necessarily wrong. Some Python users say that there should be only one right way, but that goal will never be fully reached.

### Chapter 1

1. 18996.20 €

    ```py
    >>> 49.95 + 200
    249.95
    >>> 100 * 249.95
    24995.0
    >>> 1 - (24 / 100)
    0.76
    >>> 24995.0 * 0.76
    18996.2
    >>>
    ```

    All in one line:

    ```py
    >>> 100 * (49.95 + 200) * (1 - (24 / 100))
    18996.2
    >>>
    ```

2. About 523

    ```py
    >>> (4 / 3) * 3.14 * (5 * 5 * 5)
    523.3333333333334
    >>> 4 / 3 * 3.14 * 5 * 5 * 5      # parentheses aren't needed
    523.3333333333334
    >>>
    ```

    More advanced way:

    ```py
    >>> from math import pi
    >>> 4 / 3 * pi * 5 ** 3
    523.5987755982989
    >>>
    ```

    Spaces don't effect the calculating order, but you can use them to make the order easier to see:

    ```py
    >>> 4/3 * pi * 5**3
    523.5987755982989
    >>>
    ```

### Chapter 3

1. Content of the file:

    ```py
    word = input("Enter a word: ")
    print(word * 1000)
    ```

2. Content of the file:

    ```py
    word = input("Enter a word: ")
    word += " "
    print(word * 1000)
    ```

    You can also add the space right away on the first line:

    ```py
    word = input("Enter a word: ") + " "
    print(word * 1000)
    ```

    Of course, there are 999 spaces between 1000 words and this will print 1000 spaces instead, so there will be a useless space at the end, but it doesn't matter. To get rid of the space, you can do something like this instead:

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

### Chapter 4

1. You can compare the word against an empty string (`""` or `''`). In this example, the password is "secret".

    ```py
    word = input("Enter your password: ")

    if word == "secret":
        print("Welcome!")
    elif word == "":
        print("You didn't enter anything.")
    else:
        print("Access denied.")
    ```

2. Simply check the username first, then the password in indented blocks of code.

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

    Example output:

        >>> ================================ RESTART ================================
        >>>
        Enter your username: foo
        Enter your password: biz
        Welcome foo!
        >>> ================================ RESTART ================================
        >>>
        Enter your username: bar
        Enter your password: baz
        Welcome bar!
        >>> ================================ RESTART ================================
        >>>
        Enter your username: spam
        Enter your password: eggs
        Wrong username.
        >>> ================================ RESTART ================================
        >>>
        Enter your username: foo
        Enter your password: lol
        Wrong password!
        >>>

3. This is a great chance to use a while loop. In this example, the correct password is "secret".

    ```py
    running = True
    while running:
        password = input("Enter your password: ")
        if password == "secret":
            print("Welcome!")
            running = False
        else:
            print("Wrong password.")
    ```

    Another alternative:

    ```py
    while input("Enter your password: ") != "secret":
        print("Wrong password.")
    print("Welcome!")
    ```

4. One way to do this is to put the inputs directly to `if` and `elif` lines. Again, the correct password is "secret".

    ```py
    if input("Enter your password: (3 attempts left) ") == "secret":
        print("Welcome!")
    elif input("Enter your password: (2 attempts left) ") == "secret":
        print("Welcome!")
    elif input("Enter your password: (last attempt) ") == "secret":
        print("Welcome!")
    else:
        print("Access denied!")
    ```

    Example output:

        >>> ================================ RESTART ================================
        >>>
        Enter your password: (3 attempts left) asdf
        Enter your password: (2 attempts left) asdf
        Enter your password: (last attempt) asdf
        Access denied!
        >>> ================================ RESTART ================================
        >>>
        Enter your password: (3 attempts left) asdf
        Enter your password: (2 attempts left) secret
        Welcome!
        >>>

[Home](README.md)
