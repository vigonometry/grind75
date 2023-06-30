from typing import List

# Use a modified version of Kadane's max sub array algorithm


def maxProfit(prices: List[int]) -> int:
    lmax, gmax = 0, 0
    for i in range(1, len(prices)):
        lmax = max(0, lmax + prices[i] - prices[i - 1]) #I can only buy and sell once
        gmax = max(lmax, gmax)
    return gmax
