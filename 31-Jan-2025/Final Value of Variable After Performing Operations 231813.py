# Problem: Final Value of Variable After Performing Operations - https://leetcode.com/problems/final-value-of-variable-after-performing-operations

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0
        for opes in operations:
            if opes == "--X" or opes == "X--":
                X -= 1
            else:
                X += 1
        return X
            

        