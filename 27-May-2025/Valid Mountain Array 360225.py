# Problem: Valid Mountain Array - https://leetcode.com/problems/valid-mountain-array/description/


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        index = 0
        num = arr[0]

        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                return False   
            elif arr[i] > arr[i - 1]:
                index = i
            else:
                break
        if index == 0 or index == len(arr) - 1:
            return False

        
        for i in range(index + 1, len(arr)):
            if arr[i] >= arr[i - 1]:
                return False   

        return True
