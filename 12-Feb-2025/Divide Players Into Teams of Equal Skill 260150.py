# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        target = skill[0] + skill[-1]

        l = 0
        r = len(skill)-1
        output = 0
        while l < r:
            if skill[l] + skill[r] != target:
                return -1
            output += skill[l] * skill[r]
            l += 1
            r -= 1
        return output



         
        