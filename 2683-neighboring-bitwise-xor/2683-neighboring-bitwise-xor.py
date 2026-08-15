class Solution(object):
    def doesValidArrayExist(self, derived):
        """
        :type derived: List[int]
        :rtype: bool
        """
        ans=0
        for i in range(len(derived)):
            ans=ans^derived[i]
        if ans==0:
            return True
        else:
            return False