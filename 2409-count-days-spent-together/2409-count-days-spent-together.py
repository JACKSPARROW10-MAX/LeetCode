class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        alice=self.getdates(arriveAlice,leaveAlice)
        bob=self.getdates(arriveBob,leaveBob)
        common=[]
        for i in alice:
            if i in bob:
                common.append(i)
        return len(common)

    def getdates(self,start,end):
        first=date.strptime(start,"%m-%d")
        last=date.strptime(end,"%m-%d")
        dates=[]
        while first<=last:
            dates.append(first.strftime("%m-%d"))
            first+=timedelta(days=1)
        return dates
