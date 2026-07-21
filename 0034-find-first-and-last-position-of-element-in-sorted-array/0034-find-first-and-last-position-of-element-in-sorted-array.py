class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans=[]
        f=-1
        l=-1
        if target in nums:
            f=nums.index(target)
            l=len(nums)-nums[::-1].index(target)-1
        ans.append(f)
        ans.append(l)
        return ans