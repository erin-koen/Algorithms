#!/usr/bin/python

"""
Understand
----------
- takes in an integer (though could control for that using math.floor) which represents how many players are in the game 
- outputs a list of lists of strings. len(outer_list) = total number of possible combinations Inner lists are combinations of 'rock' 'paper' and 'scissor' and len(inner_list) = n
- three possible outcomes for each 1 of n. Number of total possible outcomes is equal to 3^n.
- return should be [['', '', ''],[''],[']...]
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

    # define the length of the output array
    possibilities = 3**n

    # instantiate an array with the correct number of sub lists
    return_list = possibilities*[[]]

    # declare rps
    rps = ['rock', 'paper', 'scissors']

    # loop through RPS and assign one string at a time
    for i in range(0, len(rps)):
        play = rps[i]
        insert_posish = i
        # for each play, loop through the return_list and assign it to an incremented (or double-decremented position within the correct list)
        for j in range(0, possibilities):

            print(play, 'goes in the sublist at index ', j,' within the return_list. In the sublist, it will be inserted at index ', insert_posish)
            return_list[j].insert(insert_posish, play)
            if insert_posish == 0:
                insert_posish += 1
            elif insert_posish == 1:
                insert_posish += 1
            else:
                insert_posish -= 2

    return return_list


print(rock_paper_scissors(3))
