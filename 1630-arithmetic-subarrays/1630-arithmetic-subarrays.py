class Solution:
    def checkArithmeticSubarrays(self, nums: list[int], l: list[int], r: list[int]) -> list[bool]:
        ans=[]
        for i in range(len(l)):
            ans.append(self.seq(nums[l[i]:r[i]+1]))
        return ans

    def seq(self,arr):
        arr.sort()
        n=abs(arr[1]-arr[0])
        for i in range(len(arr)-1):
            if abs(arr[i]-arr[i+1])!=n:
                return False
        return True