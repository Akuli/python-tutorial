# zip and enumerate

Now we know how [for loops](loops.md#for-loops) work in Python. But
for loops aren't limited to printing each item in a list, they can
do a lot more.

To be able to understand for loop tricks we need to first know
assigning values to multiple variables at once. It works like this:

```python
>>> a, b = 1, 2
>>> a
1
>>> b
2
>>>
```

We can use `()` and `[]` around these values however we want and
everything will still work the same way. `[]` creates a list, and
`()` creates a tuple.

```python
>>> [a, b] = (1, 2)
>>> a
1
>>> b
2
>>>
```

We can also have `[]` or `()` on one side but not on the other
side.

```python
>>> (a, b) = 1, 2
>>> a
1
>>> b
2
>>>
```

Python created a tuple automatically.

```python
>>> 1, 2
(1, 2)
>>>
```

If we're for looping over a list with pairs of values in it we
could do this:

```python
>>> items = [('a', 1), ('b', 2), ('c', 3)]
>>> for pair in items:
...     a, b = pair
...     print(a, b)
...
a 1
b 2
c 3
>>>
```

Or we can tell the for loop to unpack it for us.

```python
>>> for a, b in items:
...     print(a, b)
...
a 1
b 2
c 3
>>>
```

## zip

What comes to your mind when you hear the word `zip`? A mechanism extensively used to tie two parts of something i.e. Shirt, Jacket etc. The `zip()` functions does pretty much same, it helps us tie two or more different items together.

```python
>>> users = ["Tushar", "Aman", "Anurag", "Sohit"]
>>> uids = ["usr122", "usr123", "usr124", "usr125"]
>>> user_details = zip(uids, users)
>>> print(user_details)
<zip object at 0x0000016938E311C0>
>>>
```

After calling zip, an iterator is returned. In order to see the content wrapped inside, we need to first convert it to a list. Basically, `zip()` is an iterator, i.e. lazy: it gives the items as needed, instead of calculating them and storing them into memory all at once. So the zip object cannot show its elements before the elements are used, because it hasn't computed them yet.

```python
>>> users = ["Tushar", "Aman", "Anurag", "Sohit"]
>>> uids = ["usr122", "usr123", "usr124", "usr125"]
>>> user_details = zip(uids, users)
>>> print(list(user_details))
[('usr122', 'Tushar'), ('usr123', 'Aman'), ('usr124', 'Anurag'), ('usr125', 'Sohit')]
>>>
```

If the lists are of different lengths, some items from the end of the longer list will be ignored.

```python
>>> users = ["Tushar", "Aman", "Anurag"]
>>> emails = ["tushar@example.com", "aman@example.com", "anurag@example.com", "sohit@example.com"]
>>> users_contact = zip(users, emails)
>>> print(list(users_contact))
[('Tushar', 'tushar@example.com'), ('Aman', 'aman@example.com'), ('Anurag', 'anurag@example.com')]
>>>
```

Here the shortest list is `users`, with length 3, so `zip(users, emails)` only takes the first 3 emails.
> We do not recommend calling `zip()` with lists of different lengths.

### Using zip with `for` loop

It is very common to `for` loop over a `zip()`, and unpack the returned tuples in the `for` loop.
This is why we introduced unpacking in the beginning of this page.

```python
>>> roll_nums = [20, 25, 28]
>>> students = ["Joe", "Max", "Michel"]
>>> for roll_num, student in zip(roll_nums, students):
...     print(f"Roll number of {student} is {roll_num}")
...
Roll number of Joe is 20
Roll number of Max is 25
Roll number of Michel is 28
>>>
```

## enumerate

`enumerate()` is an amazing Built-in function offered by python. When used, gives us the index and the item combined. long story short! `enumerate` comes in handy while working with loops as it gives us access to both the item and it's index at the same time.

```python
>>> even_nums = [2, 4, 6, 8, 10, 12]
>>> print(list(enumerate(even_nums)))
[(0, 2), (1, 4), (2, 6), (3, 8), (4, 10), (5, 12)]
>>>
```

### looping with `enumerate()`

```python
>>> even_nums = [2, 4, 6, 8, 10, 12]
>>> for index, item in enumerate(even_nums):
...     print(f"Index of {item} is {index}")
...
Index of 2 is 0
Index of 4 is 1
Index of 6 is 2
Index of 8 is 3
Index of 10 is 4
Index of 12 is 5
>>>
```

### looping without `enumerate()`

let's take a look at how we can do the same thing in a more traditional way.

```python
>>> even_nums = [2, 4, 6, 8, 10, 12]
>>> for index in range(0,  len(even_nums)):
...     print(f"Index of {even_nums[index]} is {index}")
...
Index of 2 is 0
Index of 4 is 1
Index of 6 is 2
Index of 8 is 3
Index of 10 is 4
Index of 12 is 5
>>>
```

* `range(0, len(even_nums))` gives 0,1,2,3,4,5, with the list length 6 excluded
* because these are the valid indexes of a list of length 6, `even_nums[index]` prints each element of `even_nums`

> This is complicated to think about and easy to get wrong, so it's better to use `enumerate()`

## Exercises

1. Create a program that works like this. Here I entered everything
    after the `>` prompt that the program displayed.

    ```
    Enter something, and press Enter without typing anything when you're done.
    >hello there
    >this is a test
    >it seems to work
    >
    Line 1 is: hello there
    Line 2 is: this is a test
    Line 3 is: it seems to work
    ```

2. Create a program that prints all letters from A to Z and a to z
    next to each other:

    ```
    A a
    B b
    C c
    ...
    X x
    Y y
    Z z
    ```

    Start your program like this:

    ```python
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    ```

    **Hint:** how do strings behave with `zip`? Try it out on the
    `>>>` prompt and see.

3. Can you make it print the indexes also?

    ```
    1 A a
    2 B b
    3 C c
    ...
    24 X x
    25 Y y
    26 Z z
    ```

The answers are [here](answers.md).

***

If you have trouble with this tutorial please [tell me about
it](../contact-me.md) and I'll make this tutorial better. If you
like this tutorial, please [give it a
star](../README.md#how-can-i-thank-you-for-writing-and-sharing-this-tutorial).

You may use this tutorial freely at your own risk. See
[LICENSE](../LICENSE).

[Previous](loops.md) | [Next](dicts.md) |
[List of contents](../README.md#basics)
