# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        
        def coin(total,index):
            if total < 0 or index >= len(coins):
                return 0
            if total == 0:
                return 1
            state = (total,index)
            if state not in memo:
                memo[state] = (coin(total - coins[index],index) + coin(total,index + 1))
            return memo[state]
        return coin(amount,0)