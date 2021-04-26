#!/usr/bin/env python
# coding: utf-8

# Problem 3 - Applying the classifier (4 points)
# 
# Finally, we can bring together the pieces that we have created in problems 1 and 2. Here, your aim is to take
# advantage of your new functions and sort a dataset of temperatures in Fahrenheit into four different classes.
# 
# Notice: Closely follow the instructions! 
# 
# Your score on this problem will be based on following criteria:
# 
# - Creating a new script file called `temp_functions.py` with the functions that you wrote in Problems 1 and 2
# - Add a docstring to the script file
# - Converting and classifying the list of temperatures in Part 2
# - Storing the number of temperatures in each class in the specified variables
# - Answering some questions at the end of this problem

# ### Part 1: Creating a script file (1 point)
# 
# For this part you should
# 
# - Create a new script file called `temp_functions.py` in the current directory as we saw in the Lesson 4 materials. Copy and paste the functions that you wrote in Problems 1 and 2 into that script file (i.e., the `fahr_to_celsius` and `temp_classifier` functions)
# - Add a docstring to the script file (in addition to the separate docstrings in the functions)

# ### Part 2: Convert Fahrenheit temperatures to Celsius (3 points)
# 
# For this part you should
# 
# 1. Store the Fahrenheit temperatures below into the list `temp_data`.


# List of half-hourly temperature values (in degrees Fahrenheit) for one week
temp_data =  [19, 21, 21, 21, 23, 23, 23, 21, 19, 21, 19, 21, 23, 27, 27, 28, 30, 30, 32, 32, 32, 32, 
              34, 34, 34, 36, 36, 36, 36, 36, 36, 34, 34, 34, 34, 34, 34, 32, 30, 30, 30, 28, 28, 27,
              27, 27, 23, 23, 21, 21, 21, 19, 19, 19, 18, 18, 21, 27, 28, 30, 32, 34, 36, 37, 37, 37, 
              39, 39, 39, 39, 39, 39, 41, 41, 41, 41, 41, 39, 39, 37, 37, 36, 36, 34, 34, 32, 30, 30,
              28, 27, 27, 25, 23, 23, 21, 21, 19, 19, 19, 18, 18, 18, 21, 25, 27, 28, 34, 34, 41, 37, 
              37, 39, 39, 39, 39, 41, 41, 39, 39, 39, 39, 39, 41, 39, 39, 39, 37, 36, 34, 32, 28, 28,
              27, 25, 25, 25, 23, 23, 23, 23, 21, 21, 21, 21, 19, 21, 19, 21, 21, 19, 21, 27, 28, 32,
              36, 36, 37, 39, 39, 39, 39, 39, 41, 41, 41, 41, 41, 41, 41, 41, 41, 39, 37, 36, 36, 34,
              32, 30, 28, 28, 27, 27, 25, 25, 23, 23, 23, 21, 21, 21, 19, 19, 19, 19, 19, 19, 21, 23,
              23, 23, 25, 27, 30, 36, 37, 37, 39, 39, 41, 41, 41, 39, 39, 41, 43, 43, 43, 43, 43, 43,
              43, 43, 43, 39, 37, 37, 37, 36, 36, 36, 36, 34, 32, 32, 32, 32, 30, 30, 28, 28, 28, 27,
              27, 27, 27, 25, 27, 27, 27, 28, 28, 28, 30, 32, 32, 32, 34, 34, 36, 36, 36, 37, 37, 37,
              37, 37, 37, 37, 37, 37, 36, 34, 30, 30, 27, 27, 25, 25, 23, 21, 21, 21, 21, 19, 19, 19,
              19, 19, 18, 18, 18, 18, 18, 19, 23, 27, 30, 32, 32, 32, 32, 32, 32, 34, 34, 34, 34, 34,
              36, 36, 36, 36, 36, 32, 32, 32, 32, 32, 32, 32, 32, 30, 30, 30, 30, 30, 30, 30, 30, 30,
              30, 30, 30, 30, 28, 28]


# #### Part 2 (continues)
# 
# 2. Import the `fahr_to_celsius` and `temp_classifier` functions from your `temp_functions.py` 
# 3. Create an empty list called `temp_classes` (which will be filled with temperature class numbers later)
# 4. **Convert the Fahrenheit temperatures** in the `temp_data` list into Celsius and **classify the Celsius temperatures** using the importend functions. The output should be stored in the `temp_classes` list
#  
#    **You can do the temperature conversion and classification inside one for loop:**
# 
#     - Iterate over the list of Fahrenheit temperatures (create a `for` loop), and inside the loop:
# 
#         1. Create a new variable called `temp_celsius` in which you should assign the temperature in Celsius using the `fahr_to_celsius` function to convert the Fahrenheit temperature into Celsius.
#         2. Create a new variable called `temp_class` in which you should assign the temperature class number (0, 1, 2, or 3) using the `temp_classifier` function
#         3. Add the `temp_class` value to the `temp_classes` list


# YOUR CODE HERE

# #### Part 2 (continues)
# 
# 6. Calculate how many temperatures there are in each temperature class:
# 
#     1. Create four variables called `zeros`, `ones`, `twos`, and `threes` 
#     2. Count and assign to each variable how many times values 0, 1, 2, and 3 are present in the `temp_classes` list and print out the results below. In other words, assign the value of how many time `0` is in the list to the variable `zeros`, and so on. 
#   

# YOUR CODE HERE

# **TIP**: You might want to consider using a [**count()** function](https://www.tutorialspoint.com/python3/list_count.htm) OR a for loop for this.

# ### Problem 3 tests
# 

# Check that temp_classes is a list
assert type(temp_classes) == list

# Check that required variables exists and print their value (check manually that the answers make sense!):

# CAUTION! Don't edit this line starts
print(zeros,ones,twos,threes)
# CAUTION! Don't edit this line ends

# ### Check your code
#  
# - Remeber to check that your have commented your code and used the required variable names. 
# - If you have any comments and concerns at this point, you can write them below:

# YOUR ANSWER HERE. Write your answer as comments (with #)
#
#
#
#
#
# YOUR ANSWER ENDS HERE.

# #### All done!
# 
# That's it! Now you have finished all the problems for Exercise 4! 
# Don't forget to commit & push your changes. Otherwise, the instructor cannot see your works.