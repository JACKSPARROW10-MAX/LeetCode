# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        temp=head
        nums=[]
        critical=[]
        while(temp!=None):
            nums.append(temp.val)
            temp=temp.next
        for i in range(1,len(nums)-1):
            if nums[i]<nums[i-1] and nums[i]<nums[i+1]:
                critical.append(i+1)
            elif nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                critical.append(i+1)
        print(critical)
        if critical==[] or len(critical)<2:
            return [-1,-1]
        b=max(critical)-min(critical)
        a=max(critical)
        for i in range(len(critical)-1):
            if abs(critical[i]-critical[i+1])<a:
                a=abs(critical[i]-critical[i+1])
        p=[a,b]
        return p

        