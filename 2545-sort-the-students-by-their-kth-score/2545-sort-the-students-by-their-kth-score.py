class Solution(object):
    def sortTheStudents(self, score, k):
        temp=[]
        for i in score:
            temp.append(i[k])
        temp.sort()
        temp=temp[::-1]
        ans=[]
        for i in temp:
            for j in range(len(score)):
                if i in score[j]:
                    ans.append(score[j])
        return ans     


        