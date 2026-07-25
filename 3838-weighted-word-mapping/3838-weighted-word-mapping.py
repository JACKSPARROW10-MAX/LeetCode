class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        arr=[]
        ans=""
        for i in words:
            sm=0
            for j in i:
                sm+=weights[ord(j)-97]
            sm=sm%26
            ans+=chr(96+26-sm)
        return ans
      