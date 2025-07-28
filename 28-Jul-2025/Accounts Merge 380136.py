# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}

        def find(email):
            if parent[email] != email:
                parent[email] = find(parent[email])
            return parent[email]

        def union(e1, e2):
            parent.setdefault(e1, e1)
            parent.setdefault(e2, e2)
            root1 = find(e1)
            root2 = find(e2)
            if root1 != root2:
                parent[root2] = root1

        email_to_name = {}
        for account in accounts:
            name = account[0]
            emails = account[1:]
            for email in emails:
                email_to_name[email] = name
                union(emails[0], email)

        clusters = defaultdict(list)
        for email in email_to_name:
            root = find(email)
            clusters[root].append(email)

        result = []
        for root, emails in clusters.items():
            result.append([email_to_name[root]] + sorted(emails))

        return result