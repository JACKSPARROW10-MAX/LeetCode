class Solution(object):
    def maxDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=set()
        for i in s:
            ans.add(i)
        return len(ans)
        