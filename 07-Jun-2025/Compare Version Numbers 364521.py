# Problem: Compare Version Numbers - https://leetcode.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        parts = version1.split('.')
        parts2 = version2.split('.')

        n = len(parts)
        m = len(parts2)
        z = max(n, m)
        for i in range(z):
            if len(parts) < z:
                parts.append('0')
            if len(parts2) < z:
                parts2.append('0')

        i = 0
        j = 0
        while i < len(parts) and j < len(parts2):
            if int(parts[i]) > int(parts2[j]):
                return 1
            elif int(parts[i]) < int(parts2[j]):
                return -1
            i += 1
            j += 1

        return 0  
