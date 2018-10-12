#!/usr/bin/env python
# coding: utf-8

# In[8]:


'''
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

'''
sumSquares = 0  #sum of the squares
sum = 0  # Keep track of the the sums
    
for i in range (1,101):
    sum += i
    sumSquares += i**2
difference = sum**2 - sumSquares
print('The difference in sum is: ' + str(difference))
