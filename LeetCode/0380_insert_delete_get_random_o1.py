import random

class RandomizedSet:
    def __init__(self):
        self.arr = []
        self.lookup = dict()

    def insert(self, val):
        if val in self.lookup:
            return False

        self.lookup[val] = len(self.arr)
        self.arr.append(val)

        return True

    def remove(self, val):
        if val not in self.lookup:
            return False

        i = self.lookup[val]
        last = len(self.arr) - 1

        self.lookup[self.arr[last]] = i
        self.arr[i], self.arr[last] = self.arr[last], self.arr[i]
        
        self.lookup.pop(val)
        self.arr.pop()

        return True

    def getRandom(self):
        return random.choice(self.arr)

randomizedSet = RandomizedSet()
print(randomizedSet.insert(1)) # True
print(randomizedSet.remove(2)) # False
print(randomizedSet.insert(2)) # True
print(randomizedSet.getRandom()) # 1 or 2 randomly
print(randomizedSet.remove(1)) # True
print(randomizedSet.insert(2)) # False
print(randomizedSet.getRandom()) # 2