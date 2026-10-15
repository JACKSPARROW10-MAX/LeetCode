class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        sum=0
        for i in range(len(nums)):
            temp=[]
            n=0
            for j in range(i,len(nums)):
                temp.append(nums[j])
                n=len(set(temp))
                sum+=n*n
        return sum