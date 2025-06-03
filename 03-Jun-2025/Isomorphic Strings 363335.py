# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_s_t = {}
        mapping_t_s = {}

        for c1, c2 in zip(s, t):
            if c1 in mapping_s_t:
                if mapping_s_t[c1] != c2:
                    return False
            else:
                mapping_s_t[c1] = c2

            if c2 in mapping_t_s:
                if mapping_t_s[c2] != c1:
                    return False
            else:
                mapping_t_s[c2] = c1

        return True
