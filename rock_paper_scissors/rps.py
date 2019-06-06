#!/usr/bin/python

"""
Understand
----------
- takes in an integer (though could control for that using math.floor) which represents how many players are in the game 
- outputs a list of lists of strings. len(outer_list) = total number of possible combinations Inner lists are combinations of 'rock' 'paper' and 'scissor' and len(inner_list) = n
- three possible outcomes for each 1 of n. Number of total possible outcomes is equal to 3^n.
- return should be [[''],[''],[']...]
- each play can be any of r, p, s. What you play on the next play not controlled by what you played on the last play. number of plays = n.


Plan 
----
Create an outer function that houses the list to be returned and the list of 'rock' 'paper' and 'scissors
Recursion. 

Execute
-------

Analyze
-------

"""

import sys

def rock_paper_scissors(n):
  possibilities = 3**n
  return_list= possibilities*[[0]]
  rps = ['rock', 'paper', 'scissors']
  print([[return_list] + [rps]])
  # def rps_recur(n):0
    # base case: 


rock_paper_scissors(3)