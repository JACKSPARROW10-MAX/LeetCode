class Solution(object):
    def firstStableIndex(self, nums, k):
        n=len(nums)
        for i in range(n):
           mxl=max(nums[:i+1])
           mnr=min(nums[i:])

           if mxl-mnr<=k:
               return i
        return -1
        