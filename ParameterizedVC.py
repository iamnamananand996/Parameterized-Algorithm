
# Implementation of the parameterized algorithm for vertex cover


import itertools
from GraphUtil import *
import time

sorted_vertices = []
k = 0
start_time = time.time()
TIME_MAX = 30


def param_vc_wrapper(G, S, next_vertex_count):
    """
    S is the subset selected so far
    Other parameters are as below
    """

    current_time = time.time()

    if len(S) > k:
        # this VC has exceeded the budget
        return (None, current_time - start_time)

    if check_vertex_cover(G, S):
        return (S, current_time - start_time)

    if len(S) == k:
        return (None, current_time - start_time)

    # now we choose between the vertex that comes next in degree
    # or its neighbours

    new_vc = S.copy()
    new_vc.add(sorted_vertices[next_vertex_count])

    # check branch 1 (pick that vertex)
    current_time = time.time()
    if current_time - start_time > TIME_MAX:
        return (None, TIME_MAX)
    branch1, branch1_time = param_vc_wrapper(G, new_vc, next_vertex_count + 1)
    if branch1 != None:
        return (branch1, current_time - start_time)
    current_time = time.time()
    if current_time - start_time > TIME_MAX:
        # no time to check second branch
        return (None, TIME_MAX)

    # check branch 2 (pick the vertex's neighbours)
    current_time = time.time()
    if current_time - start_time > TIME_MAX:
        return (None, TIME_MAX)
    branch2, branch2_time = param_vc_wrapper(G, S.union(
        G.E[sorted_vertices[next_vertex_count]]), next_vertex_count + 1)
    if branch2 != None:
        return (branch2, current_time - start_time)

    current_time = time.time()
    return (None, current_time - start_time)


def parameterized_vc(G, k_val):
    """
    Runs the branching algorithm on the input instance
    G is an object of type UndirectedGraph
    k is an integer (parameter)
    """

    global sorted_vertices
    global k
    global start_time

    k = k_val
    sorted_vertices = sorted(G.E, key=lambda k: len(G.E[k]), reverse=True)
    start_time = time.time()
    return param_vc_wrapper(G, set([]), 0)
