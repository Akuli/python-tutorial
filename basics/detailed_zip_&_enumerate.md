# zip and enumerate in detail

## zip

What comes to your mind when you hear the word `zip`? A mechanism extensively used to tie two parts of something i.e. shirt, Jackect etc. The `zip()` functions does pretty much same, it helps us tie two or more different items together.

### Syntax

`zip(iterator1, iterator2, iterator3 ...) `

### Parameter Values

`zip()` can take 2 or more iterator values like so `zip(iterator1, iterator2, iterator3....)`. These
iterators will be joined together once the function is executed.

### Example 1

Let's look at an example, suppose we wish to join 2 tuples together.

```python
users = ("Tushar", "Aman", "Anurag", "Sohit")
uids = ("usr122", "usr123", "usr124", "usr125")
user_details = zip(uids, users)
print(user_details)
```

### Output 1

```shell
<zip object at 0x149648b0d5c0>
```

If we want to get some real output we can convert this into List, tuple or a set.

### Example 2

```python
users = ("Tushar", "Aman", "Anurag", "Sohit")
uids = ("usr122", "usr123", "usr124", "usr125")
user_details = zip(uids, users)
print(list(user_details)) # converting to list
```

### Output 2

```shell
[('usr122', 'Tushar'), ('usr123', 'Aman'), ('usr124', 'Anurag'), ('usr125', 'Sohit')]
```

The keen-eyed amongst you might ask what if these iterators were of different lengths? well, then the ones with the extra fields will be ignored like so.

### Example 3

```python
users = ("Tushar", "Aman", "Anurag", "Sohit") 
uids = ("usr122", "usr123", "usr124") 
emails = ("tushar@example.com", "aman@example.com", "anurag@example.com", "sohit@example.com")
user_details = zip(uids, users, emails)
print(list(user_details))
```

### Output 3

```shell
[('usr122', 'Tushar', 'tushar@example.com'), ('usr123', 'Aman', 'aman@example.com'), ('usr124', 'Anurag', 'anurag@example.com')]
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
even_nums = [2, 4, 6, 8, 10, 12]
print(list(enumerate(even_nums)))
```
### Output 1

```shell
[(0, 2), (1, 4), (2, 6), (3, 8), (4, 10), (5, 12)]
```

Now before we use it in a loop let's take a look how we would do the same thing in a traditional way.

### Example 2: looping without enumerate

```python
even_nums = [2, 4, 6, 8, 10, 12]
for index in range(0,  len(even_nums)):
    print(f"Index of {even_nums[index]} is {index}")
```

### Output 2

```shell
Index of 2 is 0
Index of 4 is 1
Index of 6 is 2
Index of 8 is 3
Index of 10 is 4
Index of 12 is 5
```

### Example 3: looping with `enumerate()`

```python
even_nums = [2, 4, 6, 8, 10, 12]
for index, item in enumerate(even_nums):
    print(f"Index of {item} is {index}")
```

### Output 2

```shell
Index of 2 is 0
Index of 4 is 1
Index of 6 is 2
Index of 8 is 3
Index of 10 is 4
Index of 12 is 5
```

***

If you have trouble with this tutorial please [tell me about
it](../contact-me.md) and I'll make this tutorial better. If you
like this tutorial, please [give it a
star](../README.md#how-can-i-thank-you-for-writing-and-sharing-this-tutorial).

You may use this tutorial freely at your own risk. See
[LICENSE](../LICENSE).

[Previous](loops.md) | [Next](dicts.md) |
[List of contents](../README.md#basics)
