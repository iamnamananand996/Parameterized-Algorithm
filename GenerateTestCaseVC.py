# -*- coding: utf-8 -*-
"""

Script that generates a test case and the solution
The vertex cover (answer) is saved in 'ans.txt'
Program generates test cases with vertex cover of size greater than
n/LOWER_LIMIT and n/UPPER_LIMIT
k is the size of the vertex cover rounded off to the next multiple
of ten.

"""

import random
from GraphUtil import *
from BruteForceVC import *
from ParameterizedVC import *

UPPER_LIMIT = 4
LOWER_LIMIT = 8


def generate_test_case(n, k):

    vertices = set([])
    edges = {}

    # add all vertices to the vertex set
    for i in range(0, n):
        vertices.add('v_' + str(i))

    # select the vertex cover

    vc_size = k

    # uncomment the below lines if you want the vc size to be
    # selected randomly

#    vc_size = int(n/UPPER_LIMIT)
#    while vc_size >= int(n/UPPER_LIMIT) or vc_size < int(n/LOWER_LIMIT):
#        vc_size = int(n * random.random())
#    k = (int(vc_size/10) + 1) * 10

    vertex_list = list(vertices)
    vc = [vertex_list[i]
          for i in random.sample(range(len(vertex_list)), vc_size)]
    vc = set(vc)

    # generate edges for each vertex in the vertex cover

    for start in vc:
        if not (start in edges):
            edges[start] = []
        no_of_edges = int(n * random.random())
        for i in range(0, no_of_edges):
            new_stop = int(n * random.random())
            new_stop_str = 'v_' + str(new_stop)
            if new_stop_str == start:
                continue
            if new_stop_str not in edges[start]:
                edges[start].append(new_stop_str)

    G = UndirectedGraph(vertices, edges)

    return (G, vc)


def run_all():
    """
    Generates test cases ranging from 25 to 625 for the value of n
    and n//10, 2n//10, 3n//10, 4n//10 and 5n//10 for the value of k
    """

    # stores the time taken by each of the algorithm
    # values will be stored as
    # {n1: {k1: (brute force, parameterized), k2: ...}, n2: ...}

    time_dict = {}

    for n in range(25, 625, 25):
        time_dict[n] = {}
        print('Running tests for graph of size', str(n) + '...\n')
        for k in range(n//10, 6*n//10, n//10):

            G, vc = generate_test_case(n, k)

            # write the generated graph into a file

            with open(str(n) + '_' + str(k) + '.txt', 'w') as f:
                f.write(str(k))
                f.write('\n')
                f.write(str(G))

            # write the vertex cover into a file

            with open(str(n) + '_' + str(k) + '_ans.txt', 'w') as f:
                for vertex in vc:
                    f.write(vertex)
                    f.write('\n')

            print('Running tests for vertex cover of size', str(k) + '...\n')

            print('Running brute force...')
            brute_vc, brute_time = brute_force_VC(G)
            print('Time taken for brute force =', brute_time, 'seconds\n')

            print('Running parameterized...')
            # run parameterized here
            param_vc, param_time = parameterized_vc(G, k)
            print('Time taken for parameterized algorithm =',
                  param_time, 'seconds\n')

            time_dict[n][k] = (brute_time, param_time)

    return time_dict


time_val = run_all()
BRUTE = 0
PARAM = 1

# write the dict values into a file

with open('time_report.csv', 'w') as f:
    for n in time_val.keys():
        for k in time_val[n].keys():
            csv_text = ''
            csv_text += str(n) + ','
            csv_text += str(k) + ','
            if time_val[n][k][BRUTE] >= TIME_MAX:
                csv_text += 'TIME_MAX'
            else:
                csv_text += str(time_val[n][k][BRUTE])
            csv_text += ','
            if time_val[n][k][PARAM] >= TIME_MAX:
                csv_text += 'TIME_MAX'
            else:
                csv_text += str(time_val[n][k][PARAM])
            csv_text += '\n'
            f.write(csv_text)

print(time_val)
