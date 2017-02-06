# Setting up an editor for programming

Python comes with its IDLE, and you can use it in this tutorial. If you
don't like using it for some reason, you need [PowerShell, command
prompt or
terminal](basics/installing-python.md#if-you-like-working-with-powershell-command-prompt-or-terminal)
for trying out things. You also need an editor for writing code that
will be stored in files.

If you use IDLE as your editor, **it comes with everything set up for
you, and you don't need to worry about setting up anything**. If you
don't, you probably need to change some settings to make your editor
suitable for Python use.

Do **not** use word processors like Microsoft Word and LibreOffice
Writer for programming. They create their own files, but you need plain
text files for programming.

Start by creating an empty file called `hello.py` and opening it with
your editor. Or just open your editor and save a file as `hello.py`.

## Automatic tab expanding

This is important. Never use tabs in Python. Nobody else is using tabs,
and the official style guide tells you to never use tabs.

However, **you don't need to press the spacebar four times every time
you want to indent**. Your editor should give you four spaces when you
hit the tab key. Some editors also remove four spaces when you hit
backspace and there are four spaces before the cursor.

### Geany

1. Go to *Edit* at the top and select Preferences.
2. Go to *Editor* at left.
2. Go to *Indenting* at top.
4. Select *Spaces* instead of *Tabs*.

### gedit and pluma

1. Go to Edit at the top and select Preferences.
2. Go to Editor at top.
3. Change the indent width to 4 and select *Add spaces instead of tabs*.

### GNU Emacs

Emacs uses spaces with Python files by default.

### GNU Nano

Open your `~/.nanorc`.

    $ nano ~/.nanorc

Add these lines to it:

    set tabsize 4
    set tabstospaces

### Mousepad

1. Go to *Document* at the top, then *Tab Size*.
2. Select 4.
3. Also select *Insert Spaces*.

## Syntax highlighting

If you type a keyword, like `if`, it should show up with a different
color than the rest of your text. `"Strings"`, `# comments` and
everything else should also have their own colors. This makes it much
easier to write code.

Most of the editors below have syntax highlighting turned on by
default, but you can also change the colors.

### Geany

Install more [color schemes](https://www.geany.org/Download/Extras#colors),
then go to *View*, *Change Color Scheme*.

### gedit and pluma

Click *Fonts & Colors* in the preferences and select another color
theme.

### GNU Emacs

Type M-x, type `load-theme`, press Tab twice to see a list of theme
names, then enter a theme name and press Enter. If you want to
automatically set the theme when Emacs starts, add
`(load-theme 'your-theme-name)` to your `~/.emacs`.

### Mousepad

Click *View*, go to *Color Scheme* and select whatever you want.

## Is your editor using Python 3?

Some editors allow you to run your programs with a single keystroke,
usually by pressing F5. This tutorial is written for Python 3 or newer,
so your editor also needs to run the programs in Python 3 or newer.

If you are unsure which Python your editor runs, create a test file
with the following contents:

```python
import sys
print(sys.version)
```

If the version starts with 2, it's too old.

### Geany

1. Go to *Build*, then *Set Build Commands*.
2. Replace `python` or `python2` with `python3` everywhere. Or if you
    are using Windows, run `python` on a terminal and enter these
    commands:

    ```python
    >>> import sys
    >>> print(sys.executable)
    ```

    You'll get a path to your python.exe. Replace `python` in the build
    commands with this path. Most importantly, your *Execute* command
    should be `"C:\your\path" "%f"`.

### gedit, pluma and Mousepad

These editors don't support running programs with F5.

### GNU Emacs

Usually I write something in Emacs, then I press Ctrl+Z to suspend
Emacs, run the program myself and then I run `fg` to get back to Emacs.
If you know how to run Python programs in Emacs and you'd like to write
about it here, [tell me](contact-me.md).

***

If you have trouble with this tutorial please [tell me about
it](./contact-me.md) and I'll make this tutorial better. If you
like this tutorial, please [give it a
star](./README.md#how-can-i-thank-you-for-writing-and-sharing-this-tutorial).

You may use this tutorial freely at your own risk. See
[LICENSE](./LICENSE).

[List of contents](./README.md#list-of-contents)
