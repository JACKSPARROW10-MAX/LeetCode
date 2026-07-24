class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if 0 not in nums:
            return 0
        else:
            req=n*(n+1)//2
            act=sum(nums)
            return req-act
        