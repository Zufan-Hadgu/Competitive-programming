# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = 0
        index_letter = []
        for i in range(len(s)):
            if s[i].isalpha():
                index_letter.append(i)

        n = len(index_letter)
        total_subsets = 1<< n

        res = []   
        for mask in range(total_subsets):
            s_new = list(s)
            for i in range(n):       
                if mask & (1 << i) !=0:
                    if s_new[index_letter[i]].lower() == s_new[index_letter[i]]:
                        s_new[index_letter[i]] = s_new[index_letter[i]].upper() 
                    else:
                        s_new[index_letter[i]] = s_new[index_letter[i]].lower() 

            res.append(''.join(s_new))
        return res




 