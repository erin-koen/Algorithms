#!/usr/bin/python

"""
Understand
----------
- buying must occur before selling
  - selling can't happen at arr[0]
  - buying can't happen at arr[-1]
  - need to track when buying occured and confirm that selling happened after
- List is prices for a single stock
- one buy and one sell must occur? i.e. it's not max profit, it's least loss


Plan 
----
iterable - 
  - loop through array, set variable equal to buy and another equal to sell, control for position of min and max per above
  - edit sell variable if and only if it's after index where bought
  - keep track of max profit each pass through the loop? something like
  - control for arrays with negative numbers
  - 

recursive
  - 

Execute
-------


Analyze
-------






"""



def find_max_profit(prices):
  
  buy = 0
  sell = 0
  buy_index = 0
  sell_index = 0

  for i in range(0, len(prices)-1):
    if i == 0:
      buy = prices[i]
      buy_index = i
    elif prices[i] < buy:
      buy = prices[i]
      buy_index = i

  for i in range(1, len(prices)):
    if i > buy_index and prices[i] > sell:
      sell = prices[i]
  print(buy, buy_index, sell, sell_index)
  print('p/l: ', sell-buy)
  return sell - buy

print(find_max_profit([100, 90, 80, 50, 20, 10]))

