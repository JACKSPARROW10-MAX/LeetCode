class Solution(object):
    def minimumEffort(self, tasks):
        tasks.sort(key=lambda x: x[1] - x[0])
        req = 0
        for i in tasks:
            req = max(req + i[0], i[1])
        return req