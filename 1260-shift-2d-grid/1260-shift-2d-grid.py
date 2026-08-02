class Solution(object):
    def shiftGrid(self, grid, k):
       i=0
       m=len(grid)
       n=len(grid[0])
       temp=[]
       for i in grid:
        for j in i:
            temp.append(j)
       k=k%len(temp)
       temp=temp[-k:]+temp[:-k]
       ans=[]
       p=0
       for i in range(m):
           row=[]
           for j in range(n):
              row.append(temp[p])
              p+=1
           ans.append(row)
       return ans