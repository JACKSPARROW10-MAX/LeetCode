class Solution(object):
    def missingMultiple(self, nums, k):
        a=max(nums)
        for i in range(1,a*2):
            if i*k not in nums:
                return i*k

        