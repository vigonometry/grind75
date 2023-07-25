from typing import List
from collections import defaultdict

class UF:
    def __init__(self, n):
        self.parents = list(range(n))  # create n disjoint sets
        self.ranks = [1] * n

    def find(self, i):
        while i != self.parents[i]:
            i, self.parents[i] = self.parents[i], self.parents[self.parents[i]]
        return self.parents[i]

    def union(self, i, j):
        pi, pj = self.find(i), self.find(j)
        if pi == pj:
            return False
        if self.ranks[pi] > self.ranks[pj]:
            self.parents[pj] = pi
            self.ranks[pi] += self.ranks[pj]
        else:
            self.parents[pi] = pj
            self.ranks[pj] += self.ranks[pi]
        return True


class Solution:
    def mergeAccounts(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UF(len(accounts))
        email_to_acc = {}
        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in email_to_acc:
                    uf.union(i, email_to_acc[e])
                else:
                    email_to_acc[e] = i
        
        email_group = defaultdict(list)
        for e, i in email_to_acc.items():
            leader = uf.find(i)
            email_group[leader].append(e)
        
        res = []
        for i, emails in email_group.items():
            res.append([accounts[i][0]] + sorted(emails))
        return res
