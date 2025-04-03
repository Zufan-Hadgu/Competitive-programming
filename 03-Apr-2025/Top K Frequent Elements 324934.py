# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted = Counter(nums)
        print(counted)
       
        arr_c = []
        for key,val in counted.items():
                arr_c.append(val)
        arr_c = sorted(arr_c, reverse=True)
        print(arr_c)

        result = []
        for i in range(k):
            for keyy,vall in counted.items():
                if vall == arr_c[i] and keyy not in result:
                    result.append(keyy)
                    
           
        return result


             