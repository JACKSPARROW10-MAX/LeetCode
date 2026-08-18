class Solution(object):
    def leftRightDifference(self, nums):
        left=[]
        right=[]
        i=0
        j=len(nums)-1
        lsum=0
        rsum=0
        while i<len(nums):
            left.append(lsum)
            right.append(rsum)
            lsum+=nums[i]
            rsum+=nums[j]
            i+=1
            j-=1
        right=right[::-1]
        for i in range(len(left)):
            left[i]=abs(left[i]-right[i])
        return left

        