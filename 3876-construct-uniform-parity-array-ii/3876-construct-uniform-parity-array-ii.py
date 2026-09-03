class Solution(object):
    def uniformArray(self, nums1):
        ev=float('inf')
        od=float('inf')
        for i in nums1:
            if i%2==0:
                ev=min(ev,i)
            else:
                od=min(od,i)
        if od==float('inf'):
            return True
        elif ev!=float('inf') and od<ev:
            return True
        elif ev==float('inf'):
            return True
        else: 
            return False 
        