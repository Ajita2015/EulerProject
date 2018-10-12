#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''
# result is a variable to hold sum value
result = 0
for i in range(1000):
# If i is divisible by 3 or 5, add to result
    if i % 3 == 0 or i % 5 == 0:
        result +=i
print ('The sum is: ' + str(result))


# In[ ]:




