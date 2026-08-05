class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        a=word.upper()
        b=word.lower()
        c=word[0].upper()
        if a==word:
            return True
        elif b==word:
            return True
        elif c==word[0] and b[1:]==word[1:]:
            return True
        else:
            return False
        