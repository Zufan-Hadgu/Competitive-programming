# Problem: Arithmetic Subarrays - https://leetcode.com/problems/arithmetic-subarrays/

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        i = 0
        j = 0
        output = []
        while i < len(l) and j < len(r):
            newarry = nums[l[i]:r[j] + 1]  
            newarry.sort()
            k = 0
            m = 1
            first = newarry[m] - newarry[k]
            while k < len(newarry) - 1 and m < len(newarry):  
                if newarry[m] - newarry[k] != first:
                    output.append(False)
                    break
                k += 1
                m += 1
            else:
                output.append(True)
            i += 1
            j += 1
        return output
