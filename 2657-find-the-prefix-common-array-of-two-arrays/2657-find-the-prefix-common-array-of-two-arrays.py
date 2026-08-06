class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        c = []

        for k in range(len(A)):
            count = 0
            a = A[:k+1]
            b = B[:k+1]

            for x in range(1, len(A)+1):
                if x in a and x in b:
                    count += 1

            c.append(count)

        return c