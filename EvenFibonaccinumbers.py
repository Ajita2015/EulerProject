#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

'''
x=1 # First number
y=2 # Second number
sum=0 # Variable to hold the sum
while(y<=4000000):
    if y%2==0:
         # If the number is eve, add to sum
        sum+=y
    x,y=y,x+y

print('The sum is: ' + str(sum))


# In[ ]:



