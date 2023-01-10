# Homework 4 - While Loops and Abstraction

For this assignment, we will explore error checking with while loops, and also ways to reuse functions focusing on 'abstraction' of concepts. To be successful, you will want to **DEVELOP INCREMENTALLY** meaning write a little at  time, and run your tests then write some more. 

## Part 1: Update Star Rating Application 

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



## Part 3:  Reflection and Further Thinking

## 📝 Grading Rubric


Add (AG) and (MG) next to tiers, add major conditions to meet to pass each tier. 

1. Learning ()
   * 
2. Approaching  ()
   * 
3. Meets  ()
   * 
4. Exceeds  ()
   * 


AG - Auto-graded  
MG - Manually graded


## 📚 Additional Resources


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