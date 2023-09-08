# Homework 04 - Submission


* Student: YOUR NAME
* Semester: SEMESTER

## Common

* List any coding practice problems you completed, feel free to comment at needed (did it help, was it too easy, etc):

* List any other resources you used to help you complete the assignment (make sure to share good ones to the Tips,Tricks, and Resources channel in teams!):
  

## Module Specific

1. Correct the following loop.
   ```python
   input = None
   while input == "quit":
       input = input("Enter a value or quit: ")
       print(input)
   ```
    ```python
    ## put your corrected code below this line

    ```

2. The above code uses a None value to initialize the input variable. This works because python can let a variable be multiple types, but in some languages, you would have to match the type. Assuming you had to match the type (str), what would be a good default input value, that could never cause the loop to not run at least once? Provide reasoning for your logic as there are multiple correct answers. With that said, there is one that is more 'standard' than the rest, so feel free to openly discuss options that come to mind (you do not have to come up with the standard answer, but try to!). 

3. In your `check(guess, number)` function, the options returned are -1, 0, 1. These are often common values when comparing two values. Why would this be better than just returning True or False?  It is also common to do less than 0, 0, and greater than 0 - why would they make that assumption over just -1, 0, 1?

4. In Homework 03, we used a function call to repeat itself until the user entered a valid input. In this homework we used loops. Work up an example of both using [PythonTutor](https://pythontutor.com/python-debugger.html#mode=edit). Provide your examples below in the python block, and then answer - which one do you think is more memory efficient out of the two examples.

```python
## put your examples - one using a function for input validation, one using a loop for input validation


```

5. While one is more memory efficient, in practice it often doesn't matter for this simple situation. Why would that be the case?

## Reflection

Reflection is a powerful tool that has been **repeatedly** documented to help computer scientests learn languages, concepts, and improve their problem solving skills. There is even research that shows CS majors who spend time reflecting often do better at technical interviews, and long term studies show those reflective students also tend to get higher paying jobs over time. It is also a great way to help you learn how to learn.  Please take a moment to reflect on your progress so far in the course. Write *at least a paragraph* (prose) documenting what you have learned, what areas you have struggled in, and ways you can seek to improve your learning process. 

