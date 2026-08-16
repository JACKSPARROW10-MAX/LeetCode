class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ans=[]
        for i in range(0,len(nums),3):
            if abs(nums[i]-nums[i+2])>k:
                return []
        row=[]
        for i in nums:
            row.append(i)
            if len(row)==3:
                ans.append(row)
                row=[]
        return ans
                