import itertools
import time
from GraphUtil import *

TIME_MAX = 30


def brute_force_VC(G):
    start_time = time.time()
    current_time = start_time
    for k in range(1, len(G.V) + 1):
        print('Checking subsets of size', str(k) + '...')
        for subset in itertools.combinations(G.V, k):
            current_time = time.time()
            if check_vertex_cover(G, set(subset)):
                return (set(subset), current_time - start_time)
            if current_time - start_time > TIME_MAX:
                return (None, TIME_MAX)
    return (None, current_time - start_time)











