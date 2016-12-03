# Installing Python

If you want to learn to program with Python using this tutorial, you
need to try out the code examples. You can use a website like
[repl.it](https://repl.it/languages/python3), but I highly recommend
installing Python. That way you don't need to open a web browser just
to write code, and you can work without an Internet connection.

Let's get started!

## Downloading and installing Python

### Windows

Use the official Python installer, it will install Python and IDLE for
you.

1. Go to [the official Python website](https://www.python.org/).
2. Move your mouse over the blue Downloads button, but don't click it,
    Then click the button that downloads the latest version of Python.
3. Run the installer.
4. Install Python like any other program. Make sure the py.exe
    launcher gets installed.

### Mac OSX

I don't have an up-to-date copy of Mac OSX. If you would like to write
instructions for OSX, [tell me](contact-me.md).

### GNU/Linux

You already have Python, there's no need to download anything.

If you want to use IDLE (see below), install it. The name of the
package is `idle3` on Debian-based distributions, like Ubuntu and Linux
Mint, and you can install it with a software manager like any other
program. On other distributions you can just search for idle using the
distribution's package manager.

## Running Python

Now you have Python installed. There are several ways to run Python:

1. Directly from PowerShell, command prompt or terminal.
2. Using IDLE.
3. Using something else.

I'm not going to focus on the third option in this tutorial, but if you
know how to use Python with something else than PowerShell, command
prompt, a terminal or IDLE it's fine. Do whatever you want.

### If you are not an advanced user and you have no idea what PowerShell, command prompt and terminal are

Use IDLE. Experienced Python users will say that IDLE is garbage, but
don't listen to them. These people want you to use "better"
alternatives with more features, but that's exactly what you don't want
as a beginner. You should spend as little time as possible learning
your tools, and as much time as possible learning Python. Advanced
programming tools are not going to help you with this at all.

Launch Python's IDLE like any other program. You should see something
like this:

![IDLE](images/idle.png)

From now on, I'll instead show everything like this, so I don't have to
take more screenshots:

    Python 3.4.3 (default, Oct 14 2015, 20:28:29)
    [GCC 4.8.4] on linux
    Type "copyright", "credits" or "license()" for more information.
    >>>

The exact content of your Python's welcome message is probably different
than mine, it's ok.

### If you like working with PowerShell, command prompt or terminal

On Windows. you should be able to run Python from a PowerShell window,
or a command prompt window if you don't have PowerShell. Open one of
these programs from the start menu or start screen, type there `py` and
press Enter. You should see something like this in it:

    C:\Users\You> py
    Python 3.4.4 (v3.4.4:737efcadf5a6, Dec 20 2015, 19:28:18)
    [MSC v.1600 32 bit (Intel)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

On GNU/Linux or Mac OSX, you should have a terminal application installed
already. Run it and type `python3`:

    you@YourComputer:~$ python3
    Python 3.4.3 (default, Oct 14 2015, 20:28:29) 
    [GCC 4.8.4] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 

Now you can type `exit()` and press Enter to get out of Python.

You may also have an older version of Python installed, but don't remove
it. Your system may need it, so if you replace it with your own Python
some things might stop working. See
[this](https://docs.python.org/3/faq/installed.html) for more info.

## Summary

Now you should have Python installed, and you should be able run it.

***

You may use this tutorial freely at your own risk. See
[LICENSE](LICENSE).

[Previous](what-is-programming.md) | [Next](getting-started.md) |
[List of contents](README.md#list-of-contents)
