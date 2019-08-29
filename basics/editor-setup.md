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
Python came with an editor called IDLE. We are not going to use it
because it's lacking some important features, and most experienced
programmers (including me) don't use it or recommend it.

## Which editor?

The choice of an editor is a very personal thing. There are many
editors, and most programmers have a favorite editor that they use for
everything and recommend to everyone.

If you aren't sure about which editor you should use, I recommend
Porcupine. It's a simple editor I wrote in Python; it lets you edit
files and it doesn't have too many other featues. [Install it with these
instructions](https://github.com/Akuli/porcupine/wiki/Installing-and-Running-Porcupine),
and then [learn to use it by writing the classic Hello World
program](https://github.com/Akuli/porcupine/wiki/First-Program). Then
you can [skip the rest of this chapter](#editor-or--prompt).

Note that most other editors come with settings that are not suitable
for writing Python code. _**TODO:** add a link to the old editor setup
tutorial here._

Most of these editors lack some important features, they have so many
features that confuse people or they aren't free. You can use these
editors if you like them, but **these editors are BAD for getting
started with programming**:

- PyCharm
- IDLE
- Emacs
- Gedit
- Nano
- NetBeans
- Notepad
- Pluma
- Spyder
- Vim
- Wingware

This list doesn't contain all bad editors, but these are editors that
people often try to use. If you know a bad editor and you think I should
mention it here, please [let me know](../contact-me.md).

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

If you have trouble with this tutorial please [tell me about
it](../contact-me.md) and I'll make this tutorial better. If you
like this tutorial, please [give it a
star](../README.md#how-can-i-thank-you-for-writing-and-sharing-this-tutorial).

You may use this tutorial freely at your own risk. See
[LICENSE](../LICENSE).

[Previous](using-functions.md) | [Next](if.md) |
[List of contents](../README.md#basics)
