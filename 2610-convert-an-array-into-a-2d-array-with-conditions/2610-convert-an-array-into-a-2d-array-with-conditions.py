class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        v=nums[:]
        ans=[]
        for i in range(len(nums)):
            row=[]
            ans.append(row)
        for i in range(len(ans)):
            temp=[]
            for j in nums:
                if j not in ans[i]:
                    ans[i].append(j)
                else:
                    temp.append(j)
                    nums=temp[:]
        l=0
        count=0
        for i in ans:
            l=l+len(i)
            count+=1
            if l==len(v):
                ans=ans[:count]
                break
        return ans
