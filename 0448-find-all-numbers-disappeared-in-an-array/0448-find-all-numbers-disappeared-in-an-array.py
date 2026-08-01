class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        st=set()
        for i in nums:
            st.add(i)
        ans=[]
        for i in range(1,len(nums)+1):
            if i not in st:
                ans.append(i)
        return ans