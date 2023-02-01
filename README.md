# Homework 4 - While Loops and Abstraction

For this assignment, we will explore error checking with while loops, and also ways to reuse functions focusing on 'abstraction' of concepts. To be successful, you will want to **DEVELOP INCREMENTALLY** meaning write a little at  time, and run your tests then write some more. 

You will want to make sure you complete the Module 4 workshop before beginning this assignment. 

## Part 1: Number Magic
For this part, you will write three functions. These functions are not an application, but instead three functions that are being used by another 'application'. As such, it is really important to test those functions. We have provided the start of your tests in [test_number_magic.py](test_number_magic.py).

👉🏽 **task**: You you will write [number_magic.py](number_magic.py). The three functions needed are:

1. evens(max)
2. odds(max)
3. number_string(number, max, invert, delim)

### Evens
`evens()` returns a string of even numbers up to including max separated by commas. For example, if we typed the function call into python.

```console
>>> evens(10)
'0,2,4,6,8,10'
>>> evens(20)
'0,2,4,6,8,10,12,14,16,18,20'
```
It should also *default* to 10 is nothing is entered.
```console 
>>> evens()
'2,4,6,8,10'
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
* It is alright to get evens and odds working *before* number_string
  * And then modify them later to use number_string. This may seem redundant, but it can help your brain think through the problem.
* When developing number string, get it working one step at a time
  * does it work with the default arguments. What if you change one? What modifications will you have to make?
* The trailing comma for an inverted number_string is by far the *hardest* thing to figure out, as an OB1 error is very possible. The trick is that you may have to modify the ending check depending on if the last value is divisible or not.

When we run our tests, we will first test with the default values, and then slowly update various options. **modify `test_number_magic.py`** it is missing some obvious tests! 

## Part 2: Update Star Rating Application 

Your client has come back to you, and requested more updates to Star Rating App. This is also a time for you to update the `run()` method so it is a bit more memory efficient.
Your client has asked for the application to ask the client to enter a whole number, and then keep asking if they enter in anything else for the rating. The client said they don't care if it is in bounds or not (as that is already resolved by default 1 to 5 stars) - just that it is a positive whole number that gets entered. They have provided a sample run as an example of what they want to see. 

```console
> python -m star_rating.app
What would you like to do (add, list, exit)? add
Enter a movie: Jurassic Shark
Enter a rating 1-5: -10 
Must be a positive whole number.
Enter a rating 1-5: 1.5
Must be a positive whole number.
Enter a rating 1-5: 1
What would you like to do (add, list, exit)? add
Enter a movie: Princess Bride
Enter a rating 1-5: 100
What would you like to do (add, list, exit)? add
Enter a movie: The Good, The Bad, The Ugly
Enter a rating 1-5: 3.14
Must be a positive whole number.
Enter a rating 1-5: sigh, never saw it, don't know what to rate it
Must be a positive whole number.
Enter a rating 1-5:
Must be a positive whole number.
Enter a rating 1-5:
Must be a positive whole number.
Enter a rating 1-5: ok fine
Must be a positive whole number.
Enter a rating 1-5: 3
What would you like to do (add, list, exit)? list
*      Jurassic Shark
*****  Princess Bride
***    The Good, The Bad, The Ugly
What would you like to do (add, list, exit)? exit
```

### Add get_valid_int(prompt)
 👉🏽 **task**: Add function `get_valid_int(prompt)` that requests the user based on the prompt, and then keeps looping as long as the return value is not `numeric`. Will then return an integer `int()` of the input. 

 For the looping  you will want to print the error statement: `Must be a positive whole number.`, and then ask them the prompt again if they don't enter a positive, whole number.
 
You may want to check the section on `isnumeric` in the resources below.


 👉🏽 **task**: Update `get_rating()` to use your new `get_valid_int(prompt)`. 

 Most the other functions in `star_rating_app.py` remain the same from HW3! The only function you will update will be `run()`. 

### update run()
The `run()` function in HW3 called itself to keep the program running. This however is fairly inefficient, and now that you know loops you want to update it.

👉🏽 **task**: Rewrite the `run()` function to use a loop. Doing that it means you won't need the parameter, so it will become `def run():`

Submit your new `star_rating_app.py`

## Part 3:  Reflection and Further Thinking

1. Why would we want to use a loop instead of a function() to loop for this assignment? Please know there are *very* good reasons to use function calls which we will explore in Module 7. However, this assignment may be better using a loop for the run() function.  

2. Take a moment to reflect on what you have learned, and what you need to work on. As a reminder, struggling is a sign of learning, so give yourself permission to struggle as that is giving yourself permission to learn! 

## 📝 Grading Rubric


Add (AG) and (MG) next to tiers, add major conditions to meet to pass each tier. 

1. Learning (AG)
   * number_magic works for evens and odds
2. Approaching  (AG)
   * number_magic works for basic number_string variations 
3. Meets  (AG)
   * number_magic handles more complex variations (invert at different max and numbers)
   * trailing comma is handled correctly (not there)
   * star_rating_app handles invalid input properly
   * files pass python style checker
1. Exceeds  (MG)
   * files commented 
   * README.md - reflection and further thinking added showing thought to the questions
   * number_magic evens and odds call number_magic instead of duplicating code
   * star_rating_app.run uses a while loop properly


AG - Auto-graded  
MG - Manually graded


## 📚 Additional Resources
* [pytutor.com](https://pythontutor.com/) - A good resource for visualizing code! This will especially help with answer the further thinking question. 
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


Highlight each major component with a section, add  👉🏽 **task** for tasks and include 👉🏽 or something obvious so they can be found easily. 