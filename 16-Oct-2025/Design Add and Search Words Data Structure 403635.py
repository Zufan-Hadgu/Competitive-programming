# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            num = ord(char) - 97
            if curr.children[num] is None:
                curr.children[num] = TrieNode()
            curr = curr.children[num]
        curr.is_end = True
        

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return node.is_end

            ch = word[i]
            if ch == '.':
                for child in node.children:
                    if child and dfs(i + 1, child):
                        return True
                return False
            else:
                num = ord(ch) - 97
                if node.children[num] is None:
                    return False
                return dfs(i + 1, node.children[num])

        return dfs(0, self.root)


        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)