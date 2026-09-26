class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        temp=[]
        k=len(nums[0])
        for i in nums:
            temp.append(int(i,2))
        for i in range(max(temp)+2):
            if i not in temp:
                return f"{i:0{k}b}"