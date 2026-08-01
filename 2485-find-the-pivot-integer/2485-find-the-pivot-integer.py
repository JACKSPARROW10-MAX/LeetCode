class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr=[]
        for i in range(1,n+1):
            arr.append(i)
        for i in range(n):
            if sum(arr[:i+1])==sum(arr[i:]):
                return i+1
        return -1