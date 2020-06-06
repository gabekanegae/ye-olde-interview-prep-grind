from random import randint

class Solution:
    def __init__(self, w):
        self.w = w
        self.acc = []

    def pickIndex(self):
        if not self.acc:
            self.acc = [self.w[0]]
            for i in range(1, len(self.w)):
                self.acc.append(self.w[i] + self.acc[i-1])
        
        r = randint(0, self.acc[-1]-1)

        for i, v in enumerate(self.acc):
            if r < v: return i

n = 1000000
weights = [0, 1, 2, 3, 4]
sol = Solution(weights)

counts = [0 for i in range(len(weights))]
for i in range(n):
    counts[sol.pickIndex()] += 1

print(["{:.2f}%".format(c/n*100) for c in counts])