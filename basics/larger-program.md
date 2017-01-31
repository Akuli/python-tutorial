# Writing a larger program

Now we know enough about Python for creating a program that is actually
useful. Awesome!

In this tutorial we'll write a program that reads questions and answers
in a text file and asks them. For example, this file would make the
program ask what "text displaying function" and "text asking function"
are:

```
text displaying function = print
text asking function = input
```

This might seem useless to you right now, but a program like this can
actually be really useful for learning different kinds of things. I
originally wrote a program like this to study words of a foreign
language, but then I realized that I could study pretty much anything
with it.

But there are many things the program needs to do and writing it seems
really difficult and complicated! How the heck can we do this?

## Write functions

Our program will need to do several different things:

1.  Read the questions from a file.
2.  Ask the questions.
3.  Print statistics about how many questions were answered correctly
    and how many wrong.

Now everything seems much easier. We know how to do each of these steps
one by one, but doing it all at once would be difficult. In situations
like this **it's important to [define
functions](defining-functions.md)**. We are going to write a
`read_questions` function, an `ask_questions` function and a `stats`
function.

Let's start with the function that reads the question file:

```py
def read_questions(filename):
    answers = {}
    with open(questionfile, 'r') as f:
        for line in f:
            line = line.strip()
            if line:    # ignore empty lines
                question, answer = line.split('=')
                answers[question.strip()] = answer.strip()
    return answers
```

At this point it's best to try out the function to see how it works. You
need to create a `questions.txt` file like the one in the beginning of
this tutorial if you didn't create it already.

**TODO:** Instructions for using the -i switch.

```py
>>> read_questions('questions.txt')
{'text displaying function': 'print', 'text asking function': 'input'}
>>>
```

If your function doesn't work correctly it doesn't matter, and fixing
the problem is easy because the function is so short. This is one of the
reasons why we write functions.

Next we'll write the rest of the functions the same way, first writing
and then testing and fixing. Here are my versions of them:

```py
def ask_questions(answers):
    correct = []
    wrong = []
    for question, answer in answers.items():
        if input(question + ' = ').strip() == answer:
            print("Correct!")
            correct.append(question)
        else:
            print("Wrong! The correct answer is %s." % answer)
            wrong.append(question)
    return (correct, wrong)

def stats(correct, wrong, answers):
    print("\n**** STATS ****\n")
    print("You answered", len(correct), "questions correctly and",
          len(wrong), "questions wrong.")
    if wrong:
        print("These would have been the correct answers:")
        for question in wrong:
            print(' ', question, '=', answers[question])
```

Let's try them out.

```py
>>> answers = read_questions('questions.txt')
>>> correct, wrong = ask_questions(answers)
text displaying function = print
Correct!
text asking function = elif
Wrong! The correct answer is input.
>>> correct
['text displaying function']
>>> wrong
['text asking function']
>>> stats(correct, wrong, answers)

*** STATS ***

You answered 1 questions right and 1 questions wrong.
These would have been the correct answers:
  text asking function = input
>>>
```

Everything is working! Now we just need something that runs everything
because we don't want to type this out on the `>>>` prompt every time.

You might have noticed that the stats function printed `1 questions`
instead of `1 question`, and it looks a bit weird. You can modify the
`print_stats` function to fix this if you want to.

## The main function

The last function in a program like this is usually called `main` and it
runs the program using other functions. Our main function consists of
mostly the same pieces of code that we just tried out on the `>>>`
prompt.

```py
def main():
    filename = input("Name of the question file: ")
    answers = read_questions(filename)
    correct, wrong = ask_questions(answers)
    stats(correct, wrong, answers)
```

The last thing we need to add is these two lines:

```py
if __name__ == '__main__':
    main()
```

The `__name__` variable is set differently depending on how we run the
file, and **it's `'__main__'` when we run the file directly instead of
importing**. So if we run the file normally it asks us the words, and if
we import it instead we can still run the functions one by one. If you
want to know more about `__name__` just make a file that prints it and
run it in different ways.

Now the whole program looks like this:

```py
def read_questions(filename):
    answers = {}
    with open(questionfile, 'r') as f:
        for line in f:
            line = line.strip()
            if line:    # ignore empty lines
                question, answer = line.split('=')
                answers[question.strip()] = answer.strip()
    return answers

def ask_questions(answers):
    correct = []
    wrong = []
    for question, answer in answers.items():
        if input('%s = ' % question).strip() == answer:
            print("Correct!")
            correct.append(question)
        else:
            print("Wrong! The correct answer is %s." % answer)
            wrong.append(question)
    return (correct, wrong)

def stats(correct, wrong, answers):
    print("\n**** STATS ****\n")
    print("You answered", len(correct), "questions correctly and",
          len(wrong), "questions wrong.")
    if wrong:
        print("These would have been the correct answers:")
        for question in wrong:
            print(' ', question, '=', answers[question])

def main():
    filename = input("Name of the question file: ")
    answers = read_questions(filename)
    correct, wrong = ask_questions(answers)
    stats(correct, wrong, answers)

if __name__ == '__main__':
    main()
```

This is just the beginning. Now [you can](../LICENSE) take your word
asking program and make your own version of it that suits **your**
needs. Then you can share it with your friends so they will find it
useful as well.

## Summary

- Make multiple functions when your program needs to do multiple things.
  Each function should do one thing.
- Try out the functions on the `>>>` prompt when you want to check if
    they work correctly.
- `__name__` is `'__main__'` when the program is supposed to run, and
something else when it's imported.

***

You may use this tutorial freely at your own risk. See
[LICENSE](../LICENSE).

[Previous](defining-functions.md) | [Next](what-is-true.md) |
[List of contents](../README.md#basics)
