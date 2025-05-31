# Problem: Defanging an IP Address - https://leetcode.com/problems/defanging-an-ip-address/description/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        list_address = list(address)
        print(list_address)
        for i in range(len(list_address)):
            if list_address[i] == '.':
                list_address[i] = '[.]'
        return ''.join(list_address)
        