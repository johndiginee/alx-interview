#!/usr/bin/python3
"""Function to determine the fewest number of coins needed
   to meet a given amount total"""


def makeChange(coins, total):
    if total <= 0:
        return 0
    
    dp = [float('inf')] * (total + 1)  # Initialize DP array
    dp[0] = 0  # Base case: 0 coins needed for 0
    
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)  # Update minimum coins
    
    return dp[total] if dp[total] != float('inf') else -1  # Return result
