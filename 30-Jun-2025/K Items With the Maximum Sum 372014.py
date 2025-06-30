# Problem: K Items With the Maximum Sum - https://leetcode.com/problems/k-items-with-the-maximum-sum/

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:


        if k <= numOnes:
            return k
        elif k <= numOnes + numZeros:
            return numOnes
        else:
            return numOnes - (k - numOnes - numZeros)
        # if numOnes >= k:
        #     return k
       
        # count = 0
        # summ = 0
        # while numOnes and count < k:
        #     summ += 1
        #     count += 1
        #     numOnes -= 1
        # if count == k:
        #     return summ
        # else:
        #     while numZeros and count < k:
        #         summ += 0
        #         count += 1
        #         numZeros -= 1
        # if count == k:
        #     return summ
        # else:
        #     while numNegOnes and count < k:
        #         summ -= 1
        #         count += 1
        #         numNegOnes -= 1
        #     return count

            
                


 