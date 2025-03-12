# Problem: Reveal cards in increasing order  - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck_deque = deque()
        deck.sort()
        
        output = [0]*len(deck)
        for i in range(len(deck)):
            deck_deque.append(i)

        for card in deck:
            position = deck_deque.popleft()
            output[position] =card
            if deck_deque:
                pos = deck_deque.popleft()
                deck_deque.append(pos)
        return output




        