class Solution(object):
    def decode(self, encoded, first):
        ans=[first]
        for c in encoded:
            b=c^first
            ans.append(b)
            first=b
        return ans
        