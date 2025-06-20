# Problem: Find the Substring With Maximum Cost - https://leetcode.com/problems/find-the-substring-with-maximum-cost/

class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
       
        custom_values = {c: v for c, v in zip(chars, vals)}
        max_cost = 0
        current_cost = 0

        for ch in s:
            val = custom_values.get(ch, ord(ch) - ord('a') + 1)
            current_cost = max(val, current_cost + val)
            max_cost = max(max_cost, current_cost)

        return max_cost