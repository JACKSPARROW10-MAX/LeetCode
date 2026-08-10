class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i=0
        j=len(nums)-1
        ans=0
        while(i<j):
            ans=max((nums[i]+nums[j]),ans)
            i+=1
            j-=1
        return ans