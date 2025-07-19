# Problem: X of a Kind in a Deck of Cards - https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        d = Counter(deck)
        values = list(d.values())
        if len(deck) < 2:
            return False
        group_size = values[0]
        for val in values[1:]:
            group_size = gcd(group_size, val)

        return group_size >= 2