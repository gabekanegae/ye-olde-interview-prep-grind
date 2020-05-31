from random import randint
from time import time
from sys import argv
import SortingAlgorithms

funcs = [f for f in dir(SortingAlgorithms) if not f.startswith("__")]

k = 10 if len(argv) < 2 else int(argv[1])
n = 1000 if len(argv) < 3 else int(argv[2])

print("K={} tests of size N={} each...".format(k, n))

results = {f: [] for f in funcs}

for i in range(k):
    array = [randint(0, 100*n) for _ in range(n)]
    answer = sorted(array)

    for f in funcs:
        arrayCopy = array.copy()
    
        t0 = time()
        getattr(SortingAlgorithms, f)(arrayCopy)
        t1 = time()
    
        try:
            assert arrayCopy == answer
        except:
            print("Error running '{}':".format(f))
            print("  Exp: {}".format(answer))
            print("  Had: {}".format(arrayCopy))
            exit()
    
        results[f].append(t1-t0)

for f, r in results.items():
    print("{:>8.5f}s - {}".format(sum(r)/k, f))