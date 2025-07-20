# Problem: Open the Lock - https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        visited = set("0000")
        
        if "0000" in dead:
            return -1

        queue = deque([("0000", 0)])

        while queue:
            current, steps = queue.popleft()
            if current == target:
                return steps

            for i in range(4):
                digit = int(current[i])
                for move in [-1, 1]:
                    new_digit = (digit + move) % 10
                    new_combination = current[:i] + str(new_digit) + current[i+1:]

                    if new_combination not in dead and new_combination not in visited:
                        visited.add(new_combination)
                        queue.append((new_combination, steps + 1))
        
        return -1