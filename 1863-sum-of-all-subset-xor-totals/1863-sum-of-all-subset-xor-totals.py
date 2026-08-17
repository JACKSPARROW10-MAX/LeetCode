class Solution(object):
    def xor1(self,nums):
        p=0
        for i in nums:
            p^=i
        return p

    def subsetXORSum(self, nums):
        ans=[]
        for i in range(len(nums)+1):
            for j in combinations(nums,i):
                ans.append(j)
        res=0
        for i in ans:
            res+=self.xor1(i)
        return res

    