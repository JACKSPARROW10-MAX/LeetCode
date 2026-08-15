class Solution(object):
    def wateringPlants(self, plants, capacity):
        x=capacity
        count=0
        for i in range(len(plants)):
            if(x<plants[i]):
                count=count+i+i+1
                x=capacity-plants[i]
            
            else:
                count=count+1
                x=x-plants[i]
                  
        return(count)