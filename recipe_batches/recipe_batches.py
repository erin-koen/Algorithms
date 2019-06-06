#!/usr/bin/python

import math


"""
Understand
----------
- receives two dictionaries, recipe and the ingredients available
- returns the maximum number of batches you can make with the given ingredients, so it's the smallest number of ingredientKey/recipe key
- need to confirm keys in the recipes dictionary exist in the ingredients dictionary. If in recipe and not in keys, return 0

 

Plan 
----
- validate taht the ingedients keys are inclusive of the recipe keys. dictionary.keys() for both, figure out how to compare. Return 0 and a message if false.
- Assuming all ingredients are present, query ingredient dictionary for each key in recipe dictionary, divide one by the other


Execute
-------


Analyze
-------
Iterative example below. O(n^2) because it's a loop within a loop. 
I'm not sure how to go about doing this recursively because there's so much data manipulation that's needed. It seems like it'd be hard to do all that within a recursive loop. So maybe what needs to be done is - take the dictionaries and turn them into lists of tuples, then recurse against those lists somehow. 
"""


def recipe_batches(recipe, ingredients):
  #only works if keys are identical, probably need a lower or uppercase thing here
  if recipe.keys() != ingredients.keys():
    return 0
  else:
    # transform dictionaries to lists of tuples
    recipe_list = recipe.items()
    ingredients_list = ingredients.items()
    # declare the batches variable, which is what will eventually be returned
    batches = 0
    #check the tuples - for each tuple in the recipe list, find the one in the ingredients list that matches it, divide the the numbers recipe/ingredient (i/j) and set it equal to batches if it's larger than batches currently is
    for i in recipe_list:
      # declare variables for each part of the tuple against which we'll compare the ingredients list
      name = i[0]
      amount = i[1]
      # loop through ingredients list
      for j in ingredients_list:
        # validate that you're checking the correct tuple
        if j[0] == name:
          #figre out how many batches of that ingredient you've got
          ratio = math.floor(j[1]/amount)
          # if it's zero, you're done
          if ratio == 0:
            return 0
          # if it's not zero, and you haven't yet altered the batches variable, set it equal to the ratio
          elif batches == 0 and ratio != 0:
            batches = ratio
          # if the ratio is smaller than batches (but greater than zero), reassign batches
          elif ratio < batches:
            batches = ratio

    
    return batches


print(recipe_batches(
  { 'milk': 2 }, { 'milk': 200}
))
