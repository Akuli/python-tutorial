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
The **i** is essentially an animal each iteration where it checks if the animal's name is 3 characters long and if it does it **also** changes that animal name to all lower case before it finally appends or adds it to the list.




