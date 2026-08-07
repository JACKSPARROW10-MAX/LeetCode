class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        """
        :type nums: List[int]
        :type digit: int
        :rtype: int
        """
        count=0
        for i in nums:
            count+=str(i).count(str(digit))
        return count
