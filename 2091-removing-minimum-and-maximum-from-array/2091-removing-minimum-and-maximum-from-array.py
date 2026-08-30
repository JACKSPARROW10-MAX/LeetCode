class Solution(object):
    def minimumDeletions(self, nums):
        a=nums.index(min(nums))+1
        b=nums.index(max(nums))+1
        case1,case2,case3=0,0,0
        print(a)
        print(b)
        if a<b:
            case1=b
            case2=len(nums)-a+1
            case3=a+len(nums)-b+1
        else:
            case1=a
            case2=len(nums)-b+1
            case3=b+len(nums)-a+1
        return min(case1,case2,case3)
        
        