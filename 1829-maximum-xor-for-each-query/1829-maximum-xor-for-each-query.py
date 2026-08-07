class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        mask = (1 << maximumBit) - 1

        xor = 0
        for num in nums:
            xor ^= num

        ans = []
        for i in range(len(nums) - 1, -1, -1):
            ans.append(xor ^ mask)
            xor ^= nums[i]

        return ans