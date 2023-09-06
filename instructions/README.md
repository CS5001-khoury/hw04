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

## Part 2: 

### Add get_valid_int(prompt)
 👉🏽 **task**: Add function `get_valid_int(prompt)` that requests the user based on the prompt, and then keeps looping as long as the return value is not `numeric`. Will then return an integer `int()` of the input. 

 For the looping  you will want to print the error statement: `Must be a positive whole number.`, and then ask them the prompt again if they don't enter a positive, whole number.
 
You may want to check the section on `isnumeric` in the resources below.


 👉🏽 **task**: Update `get_rating()` to use your new `get_valid_int(prompt)`. 


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

