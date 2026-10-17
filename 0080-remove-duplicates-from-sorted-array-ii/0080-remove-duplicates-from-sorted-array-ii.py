class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        ans=[]
        temp=set()
        for i in nums:
            if nums.count(i)<3:
                ans.append(i)
            else:
                temp.add(i)
        for i in temp:
            ans.append(i)
            ans.append(i)
        ans.sort()
        for i in range(len(ans)):
            nums[i]=ans[i]
        nums=nums[:len(ans)]
        return len(nums)