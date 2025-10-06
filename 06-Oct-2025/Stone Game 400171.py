# Problem: Stone Game - https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        
        # def minimax(piles,left,right,isAlice):
            
        #     if left == right:
        #         return piles[left] if isAlice else 0
        #     if isAlice:
        #         return max(
        #             piles[left] + minimax(piles,left + 1,right,False),
        #             piles[right] + minimax(piles,left,right - 1,False)
        #             )
        #     else:
        #         return min(minimax(piles,left + 1,right,True),
        #         minimax(piles,left,right - 1,True)
        #         )
        # total = sum(piles)
        # alice_score = minimax(piles, 0, len(piles) - 1, True)
        # return   alice_score > total//2
   
        n = len(piles)
        @cache
        def dp(i,j):
            if i > j:
                return 0
            return max(piles[i] - dp(i + 1,j,) ,piles[j] - dp(i,j - 1))
        return dp(0,n-1) > 0 


        