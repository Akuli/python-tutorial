# Setting up an editor for programming

Python comes with its IDLE, and you can use it in this tutorial. If you
don't like using it for some reason, you need
[PowerShell, command prompt or terminal](installing-python.md) for
trying out things. You also need an editor for writing code that will
be stored in files.

If you use IDLE as your editor, it comes with everything set up for you
and you can get started right away. If you are going to use some other
editor, you may need to set

## Automatic tab expanding

This is important. Never use tabs in Python. Nobody else is using tabs,
and the official style guide tells you to never use tabs.

However, **you don't need to press the spacebar four times every time
you want to indent**. Your editor should give you four spaces when you
hit the tab key. Your editor should also remove four spaces when you
hit backspace and there are four spaces before the cursor.

#### Geany

1. Create a file called `hello.py`, and open it in geany. Or create a
    file in geany and save it as `hello.py`.
2. Go to Edit at the top and select Preferences.
3. Go to Editor at left.
4. Go to Indenting at top.
5. Select spaces instead of tabs.

## Syntax highlighting

If you type a keyword, like `if`, it should show up with a different
color than the rest of your text. `"Strings"`, `# comments` and
everything else should also have their own colors. This makes it much
easier to write code.

#### Geany

Geany has syntax highlighting by default. You can also install more
[color schemes](https://www.geany.org/Download/Extras#colors) if you
don't like the default colorsm and change the color scheme by clicking
View, then Change Color Scheme.

## Plugins

Advanced editors support plugins. You may find some of them useful.

#### Geany

On Debian-based GNU/Linux distributions, install the geany-plugins
package. See [the Geany website](https://plugins.geany.org/) for
instructions for other platforms.
