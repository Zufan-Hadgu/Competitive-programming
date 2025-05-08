# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        output = []
        if len(s) > 12 or len(s) < 4:
            return []
        def backtrack(i, dot, ip):
            if dot == 4 and i == len(s):
                output.append(ip[:-1])
                return
            if dot >= 4:
                return
            for j in range(i, min(i + 3, len(s))):
                segment = s[i:j+1]
                if (len(segment) > 1 and segment[0] == '0') or int(segment) > 255:
                    continue
                backtrack(j + 1, dot + 1, ip + segment + ".")
        backtrack(0, 0, "")
        return output
