'''
You are given an array of integers where each element represents the price of a stock on a given day.
You may complete at most one transaction, meaning:
You must buy on one day
You must sell on a later day
Your task is to determine the maximum profit you can achieve from this transaction.
If it is not possible to make a profit, return 0.
Example
Input:
prices = [7, 1, 5, 3, 6, 4]
Output:
5
Explanation:
Buy on day 2 at price 1
Sell on day 5 at price 6
Profit = 6 − 1 = 5
Constraints
You cannot sell before you buy
You may not hold multiple stocks at once
You must decide based only on past prices
'''




from math import inf


stocks_prices = [3,1,4,2,5]

def buyandsellstocks(stock_prices):
   min_price=inf
   maxprofit=0
   for p in stock_prices:
    if p < min_price:
        min_price = p
    else:
        maxprofit=max(maxprofit,p-min_price)
    

   print(maxprofit)

buyandsellstocks(stocks_prices)