# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def change(total,index):
            if total < 0 or index >= len(coins):
                return float("inf")
            if total == 0:
                return 0
            state = (total,index)
            if state not in memo:
                memo[state] =  min(
                1 + change(total - coins[index], index),
                change(total, index+1)
            )
            return memo[state]

        ans = change(amount,0)
        return ans if ans != float("inf") else -1
