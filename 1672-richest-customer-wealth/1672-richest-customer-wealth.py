class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        mx=0
        for i in accounts:
            mx=max(mx,sum(i))
        return mx