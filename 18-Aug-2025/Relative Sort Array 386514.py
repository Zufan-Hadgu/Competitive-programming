# Problem: Relative Sort Array - https://leetcode.com/problems/relative-sort-array/description/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        ans = []
        for num in arr2:
            ans.extend([num] * count[num])
            del count[num]  

    
        not_inarr2 = sorted(count.elements())
        ans.extend(not_inarr2)

        return ans