# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        output = []
        for num in nums:
            if num < 0:
                negative.append(num)
            else:
                positive.append(num)
        i = 0
        j = 0
        
        while i < len(positive) and j < len(negative):
            output.append(positive[i])
            output.append(negative[j])
            i += 1
            j += 1
        return output


        