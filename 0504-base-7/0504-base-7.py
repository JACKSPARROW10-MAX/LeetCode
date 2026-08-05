import numpy as np
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        return str(np.base_repr(num,base=7))
        