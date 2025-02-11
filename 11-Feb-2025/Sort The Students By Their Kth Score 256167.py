# Problem: Sort The Students By Their Kth Score - https://leetcode.com/problems/sort-the-students-by-their-kth-score/

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(score)):
            for j in range(i+1,len(score)):
                if score[i][k]  < score[j][k]:
                    score[i],score[j] = score[j],score[i]

        return score


        