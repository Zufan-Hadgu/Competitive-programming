# Problem: All Divisions With the Highest Score of a Binary Array - https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        total_ones = sum(nums)
        left_zeros = 0
        right_ones = total_ones
        max_score = -1
        ansd = defaultdict(list)

        for i in range(len(nums) + 1):
            score = left_zeros + right_ones
            ansd[score].append(i)
            max_score = max(max_score, score)

            if i < len(nums):
                if nums[i] == 0:
                    left_zeros += 1
                else:
                    right_ones -= 1

        return ansd[max_score]