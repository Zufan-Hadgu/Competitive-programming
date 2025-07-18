# Problem: Minimum Number of Operations to Move All Balls to Each Box - https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        output = []
        for i in range(len(boxes)):
            each = 0

            for j in range(len(boxes)):
                if boxes[j] == '1':
                    each += abs(i-j)
            output.append(each)
        return output

        