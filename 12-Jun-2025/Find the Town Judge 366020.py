# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        people =  set()
        count = defaultdict(int)
        for trust,person in trust:
            people.add(trust)
            count[person] += 1
        print(count)
      
        for i in range(1,n+1):
            if i not in people and count[i] == n - 1:
                return i
        return -1

        