# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n=len(arr)
        prefix  = [0] * (n + 1)
       
        for i in range(1,n + 1):
            prefix[i] = arr[i-1] ^ prefix[i-1] 

        output = [0]* len(queries)

        for i,arr in enumerate(queries):
            u,v = arr
            output[i] = prefix[u] ^ prefix[v +1]
        return(output)
            


        
        