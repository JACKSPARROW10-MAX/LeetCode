class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        a=sum(aliceSizes)
        b=sum(bobSizes)
        diff=(b-a)//2
        temp=set(bobSizes)
        for i in aliceSizes:
            if i+diff in temp:
                return [i,i+diff]

        
