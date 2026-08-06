class Solution(object):
    def countMaxOrSubsets(self, nums):
        temp=[]
        p=0
        for i in nums:
            p=p | i
        for j in range(1,len(nums)+1):
           for i in combinations(nums,j):
              temp.append(i)
        count=0
        for i in temp:
            ans=0
            for j in i:
                ans=ans | j
            if ans==p:
                count+=1
        return count