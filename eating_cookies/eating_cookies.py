#!/usr/bin/python

"""
Understand
----------
- passed an integer
- four different ways to subtract from that integer. 0, 1, 2, 3. Does 0 matter?
  - turns out yes, as zero is tested in line 7 haha. Conditional then, if n = zero then return 1
- always integers?
- Base case - n <= 1? There's only one way to eat one cookie. 
- 
 

Plan 
----
- recursive case (naive). Call the function on N, return 1 if N == 0, return N if N is 1 or 2. Return function on each of the possibilities for subtraction, i.e. 1, 2, 3. So return eating_cookings(n-1) + eating_cookies(n-2) + eating_cookies(n-3). 

Execute
-------


Analyze
-------


"""

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  if n == 0:
    return 1
  elif n <=2:
    return n
  else:
    return eating_cookies(n-1)+eating_cookies(n-2)+eating_cookies(n-3)
