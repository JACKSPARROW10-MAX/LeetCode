class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if self.dsum(nums[i])==i:
                return i
        return -1
    def dsum(self,num):
        a=str(num)
        sm=0
        for i in a:
            sm+=int(i)
        return sm
