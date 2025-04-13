# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(city):
            for neighbor in range(len(isConnected)):
                if isConnected[city][neighbor] == 1:
                    isConnected[city][neighbor] = isConnected[neighbor][city] = 0   
                    dfs(neighbor)

        provinces = 0
        for i in range(len(isConnected)):
            if isConnected[i][i] == 1:   
                provinces += 1
                dfs(i)
        
        return provinces
