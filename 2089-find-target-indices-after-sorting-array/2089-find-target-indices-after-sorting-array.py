class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        ans = []
        if target not in nums:
            return ans

        j = nums.index(target)
        count = nums.count(target)

        for i in range(count):
            ans.append(j + i)

        return ans