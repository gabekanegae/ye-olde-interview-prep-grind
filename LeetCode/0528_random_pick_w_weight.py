from random import randint

def pickIndex(w):
    acc = []

    r = randint(0, sum(w)-1)
    
    acc.append(w[0])
    for i in range(1, len(w)):
        acc.append(w[i] + acc[i-1])
        
    for i, v in enumerate(acc):
        if r < v: return i

print(pickIndex([0, 1, 2, 3, 4]))