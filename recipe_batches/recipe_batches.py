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

"""


def recipe_batches(recipe, ingredients):
  #only works if keys are identical, probably need a lower or uppercase thing here
  if recipe.keys() != ingredients.keys():
    return 0
  else:
    recipe_list = recipe.items()
    ingredients_list = ingredients.items()
    batches = 0
    #check the tuples - for each tuple in the recipe list, find the one in the ingredients list that matches it, divide the the numbers recipe/ingredient (i/j) and set it equal to batches if it's larger than batches currently is
    for i in recipe_list:
      name = i[0]
      amount = i[1]
      for j in ingredients_list:
        if j[0] == name:
          ratio = math.floor(j[1]/amount)
          print('recipe ', name, 'divided by ingredients ', j[0], 'equals ', ratio)
          if ratio > batches:
            batches = ratio
    
    return batches


print(recipe_batches(
  { 'milk': 100, 'butter': 50, 'flour': 5 },
  { 'milk': 138, 'butter': 48, 'flour': 51 }
))
