class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans=0
        for i in nums:
            ans=ans^i
        c=bin(ans^k)[2:]
        p=c.count("1")
        return p