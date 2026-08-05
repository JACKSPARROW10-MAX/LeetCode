class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        m=(1<<num.bit_length())-1
        return num^m