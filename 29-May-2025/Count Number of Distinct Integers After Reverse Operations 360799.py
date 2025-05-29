# Problem: Count Number of Distinct Integers After Reverse Operations - https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        reversed_list = []
        answer_set = set(nums)
        for num in nums:
            if num < 10:
                reversed_list.append(num)
            if num >=10:
                new_num = ""
                
                while num > 0:
                    y = num % 10
                    new_num += str(y)
                    num = num // 10
                answer_set.add(int(new_num))         
        return len(answer_set)



    
        