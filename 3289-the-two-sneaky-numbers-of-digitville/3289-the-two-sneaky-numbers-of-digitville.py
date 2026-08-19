class Solution(object):
    def getSneakyNumbers(self, nums):
        ans=[]
        for i in nums:
            if nums.count(i)>1:
                if i in ans:
                   continue
                else:
                    ans.append(i)
        
        return ans