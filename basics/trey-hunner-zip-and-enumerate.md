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
[comment]: # (Zip and Enumerarate by Tushar starts here)

## zip

What comes to your mind when you hear the word `zip`? A mechanism extensively used to tie two parts of something i.e. Shirt, Jacket etc. The `zip()` functions does pretty much same, it helps us tie two or more different items together.

### Syntax

`zip(iterator1, iterator2, iterator3 ...) `

### Parameter Values

`zip()` can take 2 or more iterator values like so `zip(iterator1, iterator2, iterator3....)`. These
iterators will be joined together once the function is executed.

### Example 1

Let's look at an example, suppose we wish to join 2 tuples together.

```python
>>> users = ("Tushar", "Aman", "Anurag", "Sohit")
uids = ("usr122", "usr123", "usr124", "usr125")
user_details = zip(uids, users)
print(user_details)
>>>
<zip object at 0x149648b0d5c0>
>>>
```

If we want to get some real output we can convert this zip object into List, tuple or a set.

### Example 2

```python
>>> users = ("Tushar", "Aman", "Anurag", "Sohit")
uids = ("usr122", "usr123", "usr124", "usr125")
user_details = zip(uids, users)
print(list(user_details)) # converting to list
>>>
[('usr122', 'Tushar'), ('usr123', 'Aman'), ('usr124', 'Anurag'), ('usr125', 'Sohit')]
>>>
```

What if these iterators were of different lengths? well, then the ones with the extra fields will be ignored like so.

### Example 3

```python
>>> users = ("Tushar", "Aman", "Anurag", "Sohit") 
uids = ("usr122", "usr123", "usr124") 
emails = ("tushar@example.com", "aman@example.com", "anurag@example.com", "sohit@example.com")
user_details = zip(uids, users, emails)
print(list(user_details))
>>>
[('usr122', 'Tushar', 'tushar@example.com'), ('usr123', 'Aman', 'aman@example.com'), ('usr124', 'Anurag', 'anurag@example.com')]
>>>
```

Length of `uids` is 3 thus it is the shortest tuple, now `zip()` function will crop other tuples to consider them equally and will finally join all of them together.

### Example 4: Using zip with for loop

```python
>>> roll_nums = (20, 25, 28) 
students = ("Joe", "Max", "Michel")
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

### Syntax

`enumerate(iterable, start=0)`

### Parameters

* Iterable: any iteration supporting object
* Start: Starting index value, default is 0

### Example 1: basic enumerate example

```python
>>> even_nums = [2, 4, 6, 8, 10, 12]
print(list(enumerate(even_nums)))
>>> 
[(0, 2), (1, 4), (2, 6), (3, 8), (4, 10), (5, 12)]
>>>
```

Now before we use it in a loop let's take a look how we would do the same thing in a traditional way.

### Example 2: looping without `enumerate()`

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

### Example 3: looping with `enumerate()`

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

[comment]: # (Zip and Enumerarate by Tushar ends here)

***

If you have trouble with this tutorial please [tell me about
it](../contact-me.md) and I'll make this tutorial better. If you
like this tutorial, please [give it a
star](../README.md#how-can-i-thank-you-for-writing-and-sharing-this-tutorial).

You may use this tutorial freely at your own risk. See
[LICENSE](../LICENSE).

[Previous](loops.md) | [Next](dicts.md) |
[List of contents](../README.md#basics)
