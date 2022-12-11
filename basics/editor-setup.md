# Setting up an editor for programming

An editor is a program that lets us write longer programs than we can
write on the `>>>` prompt. With an editor we can save the programs to files and
run them as many times as we want without writing them again.

When programmers say "editor" they don't mean programs like Microsoft
Word or LibreOffice/OpenOffice Writer. These programs are for writing
text documents, not for programming. **Programming editors don't support
things like bigger font sizes for titles or underlining bits of text**,
but instead they have features that are actually useful for programming,
like automatically displaying different things with different colors,
but also highlighting mistakes in the code, and coloring syntax.

If you are on Windows or Mac OSX you have probably noticed that your
Python came with an editor called IDLE. You can use IDLE, but we recommend exploring other options first.


## Which editor?

The choice of an editor is a very personal thing. There are many
editors, and most programmers have a favorite editor that they use for
everything and recommend to everyone.

The editors can be broadly divided into three categories:

#### The Basic Text Editors
These editors usually come with the operating system. They do not have features like
running code, auto-completion, etc. that make programming easier. They are usually used for relatively simple
text editing. Most programmers do not use these editors for programming.

A few popular ones in this category are:
- Notepad (Windows)
- Gedit (Linux)
- Notepad ++ (Windows)
- Nano (Linux/Mac OS)

#### Smart Text Editors
The text editors in this category have features like auto-completion, syntax highlighting,
running and debugging code, highlighting errors, etc. They are relatively easy to learn and have the necessary features
to start your programming journey.

A few popular ones in this category are:
- Visual Studio Code / VS Code (Windows/Linux/Mac OS)
- IDLE (Usually comes with Python) (Windows/Linux/Mac OS)
- Thonny (Windows/Linux/Mac OS)
- [Porcupine](https://github.com/Akuli/porcupine) (created by the author of this tutorial) (Windows/Linux/Mac OS)
- Geany (Windows/Linux/Mac OS)

**We recommend that you look into a few of these editors and install your favorite one.**

#### IDEs and advanced editors
This category of text editors are usually professional grade pieces of software. They are mostly proprietary and paid. They have a steep
learning curve because of how many features they have.
These types of editors are generally not preferred
in the beginning stage. They are meant to be used for writing complex and large pieces of software.

A few popular ones in this category are:
- Visual Studio (Not be confused with *Visual Studio Code*) (Windows)
- Pycharm (Windows/Linux/Mac OS)
- Vim (Windows/Linux/Mac OS)
- Emacs (Windows/Linux/Mac OS)

As already mentioned, there are no "right" or "wrong" editors. The preference of an editor
is a personal choice and we recommend trying different editors.
The lists on this page don't contain all editors, but just a few of the most popular ones.

## Editor or `>>>` prompt?

So far we have used the `>>>` prompt for everything. But now we also
have an editor that lets us write longer programs. So why not just
always use the editor?

The `>>>` prompt is meant to be used for experimenting with things. For
example, if you want to know what `"hello" + 123` does, just open the
prompt and run it.

If you want to write something once and then run it many times, write
the code to a file. For example, if you want to make a program that asks
the user to enter a word and then echoes it back, write a program that
does that in a file and run it as many times as you want to.

Note that if you write something like `'hello'` to the `>>>` prompt it
echoes it back, but if you make a file that contains nothing but a
`'hello'` it won't do anything when you run it. You need to use
`print('hello')` instead when your code is in a file.

***

If you have trouble with this tutorial, please
[tell me about it](../contact-me.md) and I'll make this tutorial better,
or [ask for help online](../getting-help.md).
If you like this tutorial, please [give it a
star](../README.md#how-can-i-thank-you-for-writing-and-sharing-this-tutorial).

You may use this tutorial freely at your own risk. See
[LICENSE](../LICENSE).

[Previous](using-functions.md) | [Next](if.md) |
[List of contents](../README.md#basics)
