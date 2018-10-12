#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
def isPrime(n):    
    if n < 2: return "Not a Prime number"
    # convert sqrt to int for range
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

sum = 0
for i in range(2, 2000000):
    if isPrime(i):
        # If number is prime, add to sum
        sum += i

print('The sum of all primes below 2 million is: ' + str(sum))
