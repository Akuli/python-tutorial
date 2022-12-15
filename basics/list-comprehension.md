# List Comprehension


## Definition
List comprehensions creates a new list from an existing list that is a shorter syntax than normal. It also processes the list much faster than using a for loop.


## Without List Comprehension
```python
animals = ["dog", "cat", "giraffe", "donkey", "ape"]
arr = []

for i in animals:
  if len(i) == 3:
    arr.append(i)
    
print(arr)
```
```python
['dog', 'cat', 'ape']
```
The example above shows a list of animals and the for loop iterates through the list of animals and the if statement filters the list and only adds the animal if their name is exactly 3 characters long.

## With List Comprehension
```python
animals = ["dog", "cat", "giraffe", "donkey", "ape"]

arr = [i for i in animals if len(i) == 3]
print(arr)
```
```python
['dog', 'cat', 'ape']
```
The example above does exactly the same thing but is in a much more concise syntax where it iterates through the list of animals and appends to the new list if their name is exactly 3 characters long.

## Syntax

newlist = [**expression** for **item** in **iterable** if **condition**]
This is the usual form in which list comprehension is used.

**Expression:** It is the current item for each iteration but also serves as the outcome which can be manipulated before it becomes added to the new list.
```python
animals = ["DOG", "CAT", "GIRAFFE", "DONKEY", "APE"]

arr = [i.lower() for i in animals if len(i) == 3]
print(arr)
```
```python
['dog', 'cat', 'ape']
```
The **i** is essentially the **item** which is an animal in each iteration where it checks if the animal's name is 3 characters long and if it does it **also** changes that animal name to all lower case before it finally appends or adds it to the list.

**Iterable:** The iterable is the object that is being iterated over and can be any iterable object such as a set, list, tuple etc.
```python
arr = [i for i in range(5)]
print(arr)
```
```python
[0, 1, 2, 3, 4]
```
This essentially adds 0 to 4 to the new array with range(5).

**Condition** The condition is a sort of filter that is specified to get the specific data that is wanted.
```python
arr = [i for i in range(10) if i < 5]
print(arr)
```
```python
[0, 1, 2, 3, 4]
```
For this example the condition is that only the numbers that is less than 5 would get put into the array.

## Summary
- List comprehensions are a good way to shorten code
- They are versatile when it comes to iterating through iterable datasets
- Not only can you filter out data with a condition you can also change the data before it gets added to the new list
- List comprehensions normally follow: newlist = [**expression** for **item** in **iterable** if **condition**]
