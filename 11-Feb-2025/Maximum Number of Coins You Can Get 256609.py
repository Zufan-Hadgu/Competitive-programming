# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()   
        coin = 0
        n = len(piles)//3
        for i in range(n,len(piles),2):
            coin += piles[i]  
        return coin
     


    
        