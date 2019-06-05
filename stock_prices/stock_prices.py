#!/usr/bin/python

"""
Understand
----------
- buying must occur before selling
  - selling can't happen at arr[0]
  - buying can't happen at arr[-1]


Plan 
----


Execute
-------


Analyze
-------






"""

import argparse

def find_max_profit(prices):
  pass


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))