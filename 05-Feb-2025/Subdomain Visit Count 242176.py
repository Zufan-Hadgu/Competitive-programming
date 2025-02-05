# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = defaultdict(int)
        for i in range(len(cpdomains)):
            splited = cpdomains[i].split()
            print(splited)
            domain = splited[1].split(".")
            print(domain)
            visited = splited[0]
            for j in range(len(domain)):
                sub_domain = '.'.join(domain[j:len(domain)])
                print(sub_domain)
                d[sub_domain] += int(visited)
        
        new_array = []
        for key,visit in d.items():
            new_array.append(str(str(visit) + " " + key))
        return (new_array)


               
                


        