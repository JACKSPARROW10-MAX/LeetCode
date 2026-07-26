class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        return max(prod((q:=sorted(nums))[-3:]),q[0]*q[1]*q[-1])