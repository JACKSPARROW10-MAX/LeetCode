class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        ans={}
        temp=[]
        for i in nums:
            if i not in ans:
                ans[i]=1
            else:
                ans[i]+=1
        print(ans)
        for k,v in ans.items():
            if v>1:
                temp.append(k)
        return temp