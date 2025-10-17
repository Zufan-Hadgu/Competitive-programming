# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False


class Solution:
    def __init__(self):
        self.root = TrieNode()
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        longest_word = ""
        for word in words:
            curr = self.root
            possible = True
            for i in range(len(word)):
                char = ord(word[i]) - 97
                if curr.children[char] is None:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]

                if i != len(word)-1 and not curr.is_end:
                    possible = False
                    break
                curr.is_end = True
            if possible:
                if len(word) > len(longest_word):
                    longest_word = word
        return longest_word

      



                

            
        