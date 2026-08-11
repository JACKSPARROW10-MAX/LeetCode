class Solution(object):
    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = []

        for i in nums:
            a = str(i)
            a = a[::-1]
            temp.append(int(a))

        nums.extend(temp)

        return len(set(nums))