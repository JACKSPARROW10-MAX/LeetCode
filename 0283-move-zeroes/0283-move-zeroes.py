class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        temp=nums[:]
        j=0
        for i in range(len(nums)):
            nums[i]=0
        for i in range(len(temp)):
            if temp[i]!=0:
                nums[j]=temp[i]
                j+=1
                