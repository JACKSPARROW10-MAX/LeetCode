class Solution(object):
    def maxProduct(self, n):
        p=str(n)
        arr=[]
        for i in p:
            arr.append(int(i))
        print(arr)
        m1=max(arr)
        arr[arr.index(m1)]=0
        m2=max(arr)
        return m1*m2

        