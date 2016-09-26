# Managing files in Python

## What are files, directories and paths?

These are simple thing that many computer users already know, but I'll go
through them just to make sure you know them also.

### Files

- Each file has a **name**, like `hello.py`, `mytext.txt` or
    `coolimage.png`. Usually the name ends with an **extension** that
    describes the content, like `py` for Python, `txt` for text or `png`
    for "portable network graphic".
- With just names identifying the files, it wouldn't be possible to have
    two files with the same name. That's why files also have a
    **location**. We'll talk more about this in a moment.
- Files have **content** that consists of
    [8-bit bytes](https://www.youtube.com/watch?v=Dnd28lQHquU).

### Directories/folders

Directories are a way to group files. They also have a name and a location
like files, but instead of containing data directly like files do they
contain other files and directories.

### Paths

Directories and files have a path, like `C:\Users\me\hello.py`. That just
means that there's a folder called `C:`, and inside it there's a folder
called `Users`, and inside it there's a folder called `me` and inside it
there's a `hello.py`. Like this:

```
C:
└── Users
    └── me
        └── hello.py
```

`C:\Users\me\hello.py` is an **absolute path**. But there are also
**relative paths**. For example, if you're in `C:\Users`, `me\hello.py`
is same as `C:\Users\me\hello.py`. The place we are in is sometimes
called **current directory**, **working directory** or
**current working directory**.

So far we've talked about Windows paths, but not all computers run
Windows. For example, an equivalent to `C:\Users\me\hello.py` is
`/home/me/hello.py` on my Ubuntu, and if I'm in `/home`, `me/hello.py`
is same as `/home/me/hello.py`.

```
/
└── home
    └── me
        └── hello.py
```

## Writing to a file

Let's create a file and write a hello world to it.

```py
>>> with open('hello.txt', 'w') as f:
...     print("Hello World!", file=f)
... 
>>> 
```

Doesn't seem like it did anything. But actually it created a `hello.txt`
somewhere on your system. On Windows it's probably in `C:\Users\YourName`,
and on most other systems it should be in `/home/yourname`. You can open
it with notepad or any other plain text editor your system comes with.

So how does that code work?

First of all, we open a path with `open`, and it gives us a Python file
object that is assigned to the variable `f`.

```py
>>> f
<_io.TextIOWrapper name='hello.txt' mode='w' encoding='UTF-8'>
>>> 
```

So the first argument we passed to `open` was the path we wanted to write.
Our path was more like a filename than a path, so the file ended up in
the current working directory.

The second argument was `w`... but where the heck does that come from?
`w` is short for write, and that just means that we'll create a new file.
There's some other modes you can use also:

| Mode  | Short for | Meaning                                                               |
|-------|-----------|-----------------------------------------------------------------------|
| `r`   | read      | Read from an existing file.                                           |
| `w`   | write     | Write to a file. **If the file exists, its old content is removed.**  |
| `a`   | append    | Write to the end of a file, and keep the old content.                 |

The `w` and `a` modes create a new file if it exists already, but trying
to read from a non-existent file is an error.

But what is that `with ourfile as f` crap? That's just a fancy way to make
sure that the file gets closed, no matter what happens. As you can see,
the file was indeed closed.

```py
>>> f.closed
True
>>> 
```

When we had opened the file we could just print to it. The print is just
like any other print, but we also need to specify that we want to print
to the file we opened using `file=f`.

## Reading from files

After opening a file with the `r` mode you can for loop over it, just
like it was a list. So let's go ahead and read everything in the file
we created to a list of lines.

```py
>>> lines = []
>>> with open('hello.txt', 'r') as f:
...     for line in f:
...         lines.append(line)
... 
>>> lines
['Hello World!\n']
>>> 
```

But why is there a `\n` at the end of our hello world?

`\n` means newline. Note that it needs to be a backslash, so `/n`
doesn't have any special meaning like `\n` has. When we wrote the file
with print it actually added a `\n` to the end of it. It's good practise
to end the content of files with a newline character, but it's not
necessary.

So how does that work if we have more than one line in the file?

```py
>>> with open('hello.txt', 'w') as f:
...     print("Hello one!", file=f)
...     print("Hello two!", file=f)
...     print("Hello three!", file=f)
... 
>>> lines = []
>>> with open('hello.txt', 'r') as f:
...     for line in f:
...         lines.append(line)
... 
>>> lines
['Hello one!\n', 'Hello two!\n', 'Hello three!\n']
>>> 
```

There we go, each of our lines now ends with a `\n`. When we for
loop over the file it's divided into lines based on where the `\n`
characters are, not based on how we printed to it.

But how to get rid of that `\n`? The `rstrip`
[string method](handy-stuff-strings.md#string-methods) is great
for this:

```py
>>> stripped = []
>>> for line in lines:
...     stripped.append(line.rstrip('\n'))
... 
>>> stripped
['Hello one!', 'Hello two!', 'Hello three!']
>>> 
```

It's also possible to read lines one by one. Files have a
`readline()` method that reads the next line, and returns `''`
if we're at the end of the file.

```py
>>> with open('hello.txt', 'r') as f:
...     first_line = f.readline()
...     second_line = f.readline()
... 
>>> first_line
'Hello one!\n'
>>> second_line
'Hello two!\n'
```

There's only one confusing thing about reading files. If you try
to read it twice you'll find out that it only gets read once:

```py
>>> first = []
>>> second = []
>>> with open('hello.txt', 'r') as f:
...     for line in f:
...         first.append(line)
...     for line in f:
...         second.append(line)
... 
>>> first
['Hello one!\n', 'Hello two!\n', 'Hello three!\n']
>>> second
[]
>>> 
```

File objects remember their position. When we tried to read the
file again it was already at the end, and there was nothing left
to read. But if we open the file again, it's in the beginning
again and everything works.

```py
>>> first = []
>>> second = []
>>> with open('hello.txt', 'r') as f:
...     for line in f:
...         first.append(line)
... 
>>> with open('hello.txt', 'r') as f:
...     for line in f:
...         second.append(line)
... 
>>> first
['Hello one!\n', 'Hello two!\n', 'Hello three!\n']
>>> second
['Hello one!\n', 'Hello two!\n', 'Hello three!\n']
>>> 
```

Usually it's best to just read the file once, and use the
content you have read from it multiple times.

As you can see, files behave a lot like lists. The `join()`
string method joins together strings from a list, but we can
also use it to join together lines of a file:

```py
>>> with open('hello.txt', 'r') as f:
...     full_content = ''.join(f)
... 
>>> full_content
'Hello one!\nHello two!\nHello three!\n'
>>> 
```

But if you need all of the content as a string, you can just
use the `read()` method.

```py
>>> with open('hello.txt', 'r') as f:
...     full_content = f.read()
... 
>>> full_content
'Hello one!\nHello two!\nHello three!\n'
>>> 
```

You can also open full paths, like `open('C:\\Users\\me\\myfile.txt', 'r')`.
The reason why we need to use `\\` when we really mean `\` is that
backslash has a special meaning. There are special characters like
`\n`, and `\\` means an actual backslash.

[comment]: # (GitHub's syntax highlighting screws up with backslashes.)

```
>>> print('C:\some\name')
C:\some
ame
>>> print('C:\\some\\name')
C:\some\name
>>> 
```

Another way to create paths is to tell Python to escape them by
adding an `r` to the beginning of the string. In this case the `r`
is short for "raw", not "read".

```py
>>> r'C:\some\name' == 'C:\\some\\name'
True
>>> 
```

If you don't use Windows and your paths don't contain backslashes
you don't need to double anything or use `r` in front of paths.

```py
>>> print('/some/name')
/some/name
>>> 
```

## Examples

This program prints the contents of files:

```py
while True:
    filename = input("Filename or path, or nothing at all to exit: ")
    if filename == '':
        break

    with open(filename, 'r') as f:
        # We could read the whole file at once, but this is
        # faster if the file is very large.
        for line in f:
            print(line.rstrip('\n'))
```

This program stores the user's username and password in a file.
Plain text files are definitely not a good way to store usernames
and passwords, but this is just an example.

```py
# Ask repeatedly until the user answers 'y' or 'n'.
while True:
    answer = input("Have you been here before? (y/n) ")
    if answer == 'Y' or answer == 'y':
        been_here_before = True
        break
    elif answer == 'N' or answer == 'n':
        been_here_before = False
        break
    else:
        print("Enter 'y' or 'n'.")

if been_here_before:
    # Read username and password from a file.
    with open('userinfo.txt', 'r') as f:
        username = f.readline().rstrip('\n')
        password = f.readline().rstrip('\n')

    if input("Username: ") != username:
        print("Wrong username!")
    elif input("Password: ") != password:
        print("Wrong password!")
    else:
        print("Correct username and password, welcome!")

else:
    # Write username and password to a file.
    username = input("Username: ")
    password = input("Password: ")
    with open('userinfo.txt', 'w') as f:
        print(username, file=f)
        print(password, file=f)

    print("Done! Now run this program again and select 'y'.")
```

***

You may use this tutorial freely at your own risk. See [LICENSE](LICENSE).

[Back to the list of contents](README.md)
