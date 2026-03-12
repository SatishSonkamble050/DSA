"""
Problem: Best Time to Buy and Sell Stock

You are given an array where:
prices[i] = price of stock on day i

Goal:
Find the maximum profit you can achieve by buying one day
and selling on another future day.

Rules:
1. You must buy before you sell.
2. Only one transaction allowed.

Example
-------
Input  : [4,2,3,4,5,2]
Output : 3
Buy at 2 → Sell at 5
"""


# -------------------------------------------------------
# 1️⃣ BRUTE FORCE APPROACH
# -------------------------------------------------------
# Check every possible buy and sell pair
# Time Complexity  : O(n²)
# Space Complexity : O(1)

def brute_force_stock(arr):
    max_profit = 0

    for buy in range(len(arr)):
        for sell in range(buy + 1, len(arr)):

            profit = arr[sell] - arr[buy]

            if profit > max_profit:
                max_profit = profit

    return max_profit


# -------------------------------------------------------
# 2️⃣ BETTER APPROACH (Two Pointer / Sliding Window idea)
# -------------------------------------------------------
# Maintain two pointers:
# buy  → day we buy stock
# sell → day we try selling stock
#
# If current price is lower than buy price,
# move buy pointer to that position.
#
# Time Complexity  : O(n)
# Space Complexity : O(1)

def better_stock(arr):

    max_profit = 0
    buy = 0
    sell = 1
    n = len(arr)

    best_buy = None
    best_sell = None

    while sell < n:

        # calculate profit
        profit = arr[sell] - arr[buy]

        print(f"BUY INDEX:{buy} SELL INDEX:{sell} PROFIT:{profit} MAX:{max_profit}")

        # update max profit
        if profit > max_profit:
            max_profit = profit
            best_buy = buy
            best_sell = sell

        # if we find smaller price, update buy
        if arr[sell] < arr[buy]:
            buy = sell

        sell += 1

    print("BEST BUY PRICE :", arr[best_buy])
    print("BEST SELL PRICE:", arr[best_sell])

    return max_profit


# -------------------------------------------------------
# 3️⃣ OPTIMAL APPROACH (Greedy)
# -------------------------------------------------------
# Track minimum price seen so far
# Compute profit for every price
#
# Time Complexity  : O(n)
# Space Complexity : O(1)

def optimal_stock(prices):

    min_price = float("inf")
    max_profit = 0

    for price in prices:

        # update minimum price
        min_price = min(min_price, price)

        # profit if sold today
        profit = price - min_price

        # update best profit
        max_profit = max(max_profit, profit)

    return max_profit


# -------------------------------------------------------
# DRIVER CODE
# -------------------------------------------------------

arr = [4, 2, 3, 4, 5, 2]

print("\nArray:", arr)

print("\nBrute Force Profit :", brute_force_stock(arr))

print("\nBetter Approach Profit :", better_stock(arr))

print("\nOptimal Approach Profit :", optimal_stock(arr))