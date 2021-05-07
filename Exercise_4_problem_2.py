#!/usr/bin/env python
# coding: utf-8

# ## Problem 2 - Temperature classifier (3 points)
# 
# In Problem 2 of Exercise 3 last week, we practiced how to classify temperatures into four different classes (*i.e., cold, slippery, comfortable, and warm*). Let's continue working with the same idea. 
# 
# Here, you should create a function called `temp_classifier` that accepts a temperature value in Celsius that will be reclassified into integer numbers 0-3 based on following criteria:
# 
# | Return value | Classification criteria                                                  |
# | :----------: | :----------------------------------------------------------------------- |
# | 0            | Temperatures below -2 degrees Celsius                                    |
# | 1            | Temperatures equal or warmer than -2, but less than +2 degrees Celsius   |
# | 2            | Temperatures equal or warmer than +2, but less than +15 degrees Celsius  |
# | 3            | Temperatures equal or warmer than +15 degrees Celsius                    |
# 
# Notice: Closely follow the instructions! 
# 
# Your score on this problem will be based on following criteria:
# 
# - Creating a new function called `temp_classifier` (0.5 points)
# - Defining one parameter called `temp_celsius` in your `temp_classifier` function (0.3 points)
# - Reclassifying input temperatures based on the criteria in the above table and returning the reclassified value as an integer number (i.e., 0, 1, 2, or 3) (1.2 points)
# - Adding comments in your code and a docstring that explains how to use your `temp_classifier` function (i.e., you should write the purpose of the function, parameters, and returned values) (1.0 points)


# YOUR CODE HERE to define temp_classifier
def temp_classifier(temp_celsius):
  """
  The function temp_classifier accepts temperature values in degrees Celsius that are reclassified into integers 0-3 based on the following criteria:
  Define the parameter temp_celsius.
  Return value classification criteria
  Temperatures below 0 degrees Celsius-2 degrees Celsius
  1 Temperature is -2 or higher and less than +2 degrees Celsius
  2 Temperatures above +2 and below +15 degrees Celsius
  Temperatures above 3 degrees Celsius + 15 degrees Celsius
  Returns the reclassified value as an integer (0, 1, 2, or 3).

"""

  if temp_celsius < -2 :
      return 0
  elif (temp_celsius >= -2) and (temp_celsius <2):
      return 1
  elif (temp_celsius >= 2) and (temp_celsius <15):
      return 2
  elif temp_celsius >=15 :
      return 3

# Use your newly created function to print the answers to the following questions:
print(temp_classifier.__doc__)

# 1. What is the class value for 16.5 degrees Celsius?
# YOUR CODE HEREtest_48 = fahr_to_celsius(48)
test_48 = temp_classifier(48)
print('1. '+ str(test_48))
# 2. What is the class value for +2 degrees Celsius?
# YOUR CODE HERE
test_2 = temp_classifier(2)
print('2. '+ str(test_2))


# ### Problem 2 tests
# 

# Check that the function produces correct answers for selected values:

# 1. What is the class value for 16.5 degrees (Celsius)?
assert temp_classifier(16.5) == 3, 'Wrong class'
print("ok :)")

# 2. What is the class value for +2 degrees (Celsius)?
assert temp_classifier(2) == 2, 'Wrong class'
print("ok :)")

# 3. What is the class value for +1 degrees (Celsius)?
assert temp_classifier(1) == 1, 'Wrong class'
print("ok :)")

# 4. What is the class value for -5 degrees (Celsius)?
assert temp_classifier(-5) == 0, 'Wrong class'
print("ok :)")


# ### Check your code
# 
#  - Are all the variable names are correct?
#  - Does your code has enough comments?
#  - Does your function has an informative dosctring?

# YOUR ANSWER HERE. Write your answer as comments
print("A. yes.")
#
#
#
#
# YOUR ANSWER ENDS HERE

# #### Done!
# 
# That's it! Now you are ready to continue with  Problem 3.
