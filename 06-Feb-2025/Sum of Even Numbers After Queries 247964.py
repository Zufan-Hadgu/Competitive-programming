# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
            result = []
            summ = 0
            for num in nums:
                if num % 2 == 0:
                    summ += num
            for val, index in queries:
                if nums[index] % 2 == 0:
                    summ -= nums[index]
                nums[index] += val
                if nums[index] % 2 == 0:
                    summ += nums[index]
                result.append(summ)
            return result




                     




            # for j in range(len(queries)):
            #     val = queries[j][0]
            #     index = queries[j][1]
            #     nums[index] = nums[index] + val
            #     _sum = 0
                
            #     for i in range(len(nums)):
            #         if nums[i] % 2 == 0:
            #             _sum += nums[i]
            #     result.append(_sum)

            # return (result)
 
        