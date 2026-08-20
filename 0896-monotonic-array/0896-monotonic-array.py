class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums==sorted(nums) or nums==sorted(nums)[::-1]:
            return True
        else:
            return False