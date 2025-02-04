# Problem: Richest Customer Wealth - https://leetcode.com/problems/richest-customer-wealth/description/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = []
        w = 0
        for i in range(len(accounts)):
            for j in range(len(accounts[i])):
                w += accounts[i][j]
                wealth.append(w)
            w = 0
        return max(wealth)

        