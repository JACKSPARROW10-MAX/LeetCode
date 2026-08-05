class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ans=""
        temp="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        for i in s:
            if i in temp:
                ans+=i
        ans=ans.lower()
        if ans=="":
            return True
        if ans==ans[::-1]:
              return True
        return False