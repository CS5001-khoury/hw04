# Homework 4 - While Loops and Abstraction

For this assignment, we will explore error checking with while loops, and also ways to reuse functions focusing on 'abstraction' of concepts. To be successful, you will want to **DEVELOP INCREMENTALLY** meaning write a little at  time, and run your tests then write some more. 

You will want to make sure you complete the Module 4 Team Activity before beginning this assignment. 

## Part 1: Number Magic
For this part, you will write three functions. These functions are not an application, but instead three functions that are being used by another application. As such, it is really important to test those functions. We have provided the start of your tests in [test_number_magic.py](../test_number_magic.py).

👉🏽 **task**: You you will write [number_magic.py](../number_magic.py). The three functions needed are:

1. evens(max)
2. odds(max)
3. number_string(number, max, invert, delim)

### Evens
`evens()` returns a string of even numbers up to including max separated by commas. For example, if we typed the function call into the python shell (after loading the file).

```console
>>> evens(10)
'0,2,4,6,8,10'
>>> evens(20)
'0,2,4,6,8,10,12,14,16,18,20'
```
It should also *default* to 10 is nothing is entered.
```console 
>>> evens()
'0,2,4,6,8,10'
```

### Odds
The same thing as evens, but odd numbers. It also defaults to 10 for max.

```console
>>> odds()
'1,3,5,7,9'
>>> odds(15)
'1,3,5,7,9,11,13,15'
```

### Number String
Number string takes a number (defaults to 2) and returns a string of numbers who are whole divisible by that number up to max (defaults to 10) separated by delim (defaults to ',').

For example, 3 will give every 3rd number. 4 will give every 4th, etc. Here are a couple examples:
```console
>>> number_string()
'0,2,4,6,8,10'
>>> number_string(3, 9)
'0,3,6,9'
```

However, if invert is set to `True` (defaults) to `False` it returns every value *not* divisible by number. For example:

```console
>>> number_string(invert=True)
'1,3,5,7,9'
>>> number_string(2, 15, True)
'1,3,5,7,9,11,13,15'
```

Additionally, if we want to change the delim (short for deliminator), from the default of ',', we can do that. For example.

```console
>>> number_string(2, 15, True, ' ')
'1 3 5 7 9 11 13 15'
```

### Hints

* You will want to develop the application incrementally! 
* You can use the code from the [Module 04 Team Activity](https://github.com/CS5001-khoury/TeamActivities/tree/main/Module04) as a starting point, but don't let the differences of printing and concatenating strings confuse you. Also function names may vary.
* It is alright to get evens and odds working *before* number_string
  * And then modify them later to use number_string. This may seem redundant, but it can help your brain think through the problem.
* When developing number string, get it working one step at a time
  * does it work with the default arguments. What if you change one? What modifications will you have to make?
* The trailing comma for an inverted number_string is by far the *hardest* thing to figure out, as an OB1 error is very possible. The trick is that you may have to modify the ending check depending on if the last value is divisible or not.

When we run our tests, we will first test with the default values, and then slowly update various options. **Modify [`test_number_magic.py`](../test_number_magic.py)** it is missing some obvious tests! 

## Part 2: Guessing Game

👉🏽 **task**:  You will be using [guessing_game](../guessing_game.py) as a template to write a Guessing Game application.

Looking at the template [guessing_game](../guessing_game.py), you will see a bunch of functions extensively documented with what they should do. Your quest is to complete each function. With that said, we encourage you to first read through all the documentation and write notes to yourself. What do you know? What do you not know? Ask questions for clarification on MS Teams! Learning to "sit" with an assignment before writing the code is an essential skill towards success.

Below are some hints and tips to help you get started.

### Global Variables
There is a section of global variables at the top (in all CAPS). You will use these extensively, and actually a fairly common design pattern, though in practice it is often not globals they use (but instead a class or dictionary). By isolating the "hard" values (strings, numbers that don't change) to variables, it becomes easier to write your code in the functions
without mistakes. It also allows for changes such as localization (changing the language) to be easier.

### get_command(), get_guess(), get_number()
All three of these functions are very similar. `get_command()` looks at strings and returns a int value based on which string is entered, while `get_guess()` and `get_number()` both ask for int values from the client. They all keep looping until the input is **correct**. 

For `get_command()` correct output is one of the options presented in help. If they don't provide that option, the loop continues. You will want to use `.casefold()` and `.strip()` to make sure the input is in the correct format.

For `get_guess()` and `get_number()` you will want to use the `.isnumeric()` along with checking ranges for get_guess(). You will also want to use `.strip()` as that is common to do with any input incase someone hits a space by accident. 

You may want to check the Resources section below. 


### computer_play()
The computer play is welcome to be "brute force" in which it checks every number.  You do not have to come up with a clever algorithm for it! 

> Reach Goal  
> After you finish the assignment, you can explore different algorithms for the computer play. For example, you could have the computer play guess the middle number, and then adjust the high and low values based on the feedback. Think about what that does to your total possible guesses. This is actually called a Binary Search, something we will explore in a future module.


### Testing guessing_game.py

Most of the functions in [guessing_game.py](../guessing_game.py) either take input from a client or print out feedback. That is the particular nature of this application, especially since we are still limited on some of our design tools. Testing
stdin(input) and stdout(print) can be difficult. While there are built in libraries often to help with that such as "mock" in python unittest, we don't expect students to be able to know how to test various inputs and outputs. Instead, there is something called a documented test, in which you carefully document a run of the program, and save that run for repeated testing. Eventually, you get to the point where you can save your input and expected output, and then compare it automatically with the expected output. 

To help prepare you with this type of testing, we want you to create a documented test for guessing_game.py. You will want to create a file called `test_guessing_game.txt` and then document a run of the program. The file will contain the full run of the program including inputs and outputs. It doesn't have to be correct btw! It just has to include them. As you do this more, we encourage you to create additional files such as `test_guessing_game01.txt`, copying and pasting your run into the text file. You will submit these files with your homework showing you did test and think about edge cases for your program. (and didn't just rely on the autograder). While only one documented run is required, you can submit multiple files if you want to show multiple runs.


### Partial Runs
It is 100% alright to run a program before it is complete! This program is a great example of where you could complete part of the program, and part of your main(), and run the program testing it! Don't feel the entire program as to be done to test it. You will thank yourself in the long run. 

### Sample Program Run
For reference, here is a sample run of the program. As long as you are using the global variables, your input/output should look very similar. 

```console
Welcome to the guessing game!
What would you like to do? help 
Enter one of the following commands:
    help - prints this message
    play - plays the game
    quit - exits the program
    set number - sets the maximum number of attempts
    set high - sets the highest value
    set low - sets the lowest value
    reset - resets to the default values

What would you like to do? play 
Enter a number between 1 and 100: 50
Too low!
Enter a number between 1 and 100: 75
Too low!
Enter a number between 1 and 100: 85
Too low!
Enter a number between 1 and 100: 95
Too high!
Enter a number between 1 and 100: 90
Too low!
Enter a number between 1 and 100: 92
Too low!
Enter a number between 1 and 100: 93
Correct!
Dave took 7 attempts to guess the number 93.
HAL took 4 attempts to guess the number 93.
The winner is HAL with 4 attempts!
What would you like to do? set min
Invalid command. Type 'help' for a list of commands.
Enter one of the following commands:
    help - prints this message
    play - plays the game
    quit - exits the program
    set number - sets the maximum number of attempts
    set high - sets the highest value
    set low - sets the lowest value
    reset - resets to the default values

What would you like to do? set low
Enter a new whole number value for lowest value: 5
What would you like to do? set high
Enter a new whole number value for highest value: 5
What would you like to do? play
Enter a number between 5 and 5: 5
Correct!
Dave took 1 attempts to guess the number 5.
HAL took 1 attempts to guess the number 5.
The winner is Dave with 1 attempts!
What would you like to do? reset
What would you like to do? play
Enter a number between 1 and 100: 50
Too high!
Enter a number between 1 and 100: 25
Too high!
Enter a number between 1 and 100: 10
Too low!
Enter a number between 1 and 100: 15
Too high!
Enter a number between 1 and 100: 13
Too high!
Enter a number between 1 and 100: 12
Correct!
Dave took 6 attempts to guess the number 12.
HAL took 7 attempts to guess the number 12.
The winner is Dave with 6 attempts!
What would you like to do? quit
Thanks for playing!
```

### Most Importantly!!
Don't attempt to write guessing_game.py all at once. Try to write it in sections, test it, and write some more. You will be much happier in the long run.

## Part 3: README.md

👉🏽 **Task**: Answer the questions in the [README.md](../README.md) file. 

Make sure to answer the questions in the [README.md](../README.md) file.

As always you are free to ask about the questions in MS Teams, including clarifications on the code. 


## 📝 Grading Rubric


Add (AG) and (MG) next to tiers, add major conditions to meet to pass each tier. 

1. Learning (AG)
   * number_magic works for evens and odds
2. Approaching  (AG)
   * number_magic works for basic number_string variations 
   * guessing_game handles correct/basic input for get_command, get_guess, and get_number
   * guessing_game works for basic 'human' play, including proper feedback
   * guessing_game works for basic 'computer' play
   * guessing_game properly prints help message
3. Meets  (AG)
   * number_magic handles more complex variations (invert at different max and numbers)
   * number_magic trailing comma is handled correctly (not there)
   * guessing_game handles error input for get_command, get_guess, and get_numbers
   * files pass python style checker
1. Exceeds  (MG)
   * files correctly commented 
   * test_number_magic.py is fully completed (check main), with a couple additional tests
   * README.md - questions answered
   * number_magic evens and odds call number_string instead of duplicating code
   * guessing_game correctly uses the global variables (no 'hard coding' in functions)
   * guessing_game is fully completed
   * student provides sample 'run' outputs for guessing_game.py testing runs (only one required, more better)


AG - Auto-graded  
MG - Manually graded

### Submission Reminder 🚨
For manually graded elements, we only guarantee time to submit for a regrade IF you submit by the DUE DATE. Submitting late may mean it isn't possible for the MG to be graded before the AVAILABLE BY DATE, removing any windows for your to resubmit in time. While it will be graded, it is always best to submit by the due date, so you have full opportunity to improve your grade.

## 📚 Additional Resources
* [pytutor.com](https://pythontutor.com/) - A good resource for visualizing code!  
* [w3schools Default Function Parameters](https://www.w3schools.com/python/gloss_python_function_default_parameter.asp)
* [Python Tutorial Default Parameter](https://www.pythontutorial.net/python-basics/python-default-parameters/)


 ### isnumeric
 One function that can help you is  `isnumeric()`. For example

```python
value = input("This is my prompt ")
if value.isnumeric():
   print("yay!")
else: 
   print("Not numeric")
```

`isnumeric()` checks to make sure it is a *whole*, *positive* number. As such, -1 will return False, 3.14 will return False, while 1 or 3 will return True. You will want to consider using this as an option to 'validate' the input.


### strip
Another function that can help you is `strip()`. For example

```python
value = input("This is my prompt ").strip()
```

.strip() removes the leading and trailing spaces. This is a common thing to do with input, as it is easy to accidentally hit a space.

### casefold

Another function that can help you is `casefold()`. For example

```python
value = input("This is my prompt ").strip().casefold()
small = "MAX".casefold()
print(small) #print "max"
```

Casefold essentially makes every character "lowercase". You will hear about `.lower()` and `.casefold()`, and they are very similar. The difference is that `.casefold()` is more accurate to the localized language, and will change more characters. For example, the German character ß is changed to ss. The older function `.lower()` doesn't have that ability. As such, if `.casefold()` is an option (not all languages have it), it is often better to use especially when dealing with inputs. 