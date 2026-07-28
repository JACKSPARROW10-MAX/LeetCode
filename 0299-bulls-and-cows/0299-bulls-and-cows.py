from collections import Counter

class Solution(object):
    def getHint(self, secret, guess):
        bulls = 0
        s = []
        g = []

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                s.append(secret[i])
                g.append(guess[i])

        s = Counter(s)
        g = Counter(g)

        cows = 0
        for ch in s:
            cows += min(s[ch], g[ch])

        return str(bulls) + "A" + str(cows) + "B"