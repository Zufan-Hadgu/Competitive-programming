# Problem: Relative Ranks - https://leetcode.com/problems/relative-ranks/description/

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        num_score = sorted(score, reverse = True)
        output = []
        for num in score:
            if num_score.index(num) == 0:
                output.append("Gold Medal")
            elif num_score.index(num) == 1:
                output.append("Silver Medal")
            elif num_score.index(num) == 2:
                output.append("Bronze Medal")
            else:
                output.append(str(num_score.index(num) + 1))
        return output
 