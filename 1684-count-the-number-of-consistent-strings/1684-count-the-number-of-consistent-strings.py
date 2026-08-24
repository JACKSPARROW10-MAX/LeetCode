class Solution(object):
    def countConsistentStrings(self, allowed, words):
        count=0
        for i in words:
            for j in i:
                if j not in allowed:
                    count+=1
                    print(i)
                    break
        return len(words)-count