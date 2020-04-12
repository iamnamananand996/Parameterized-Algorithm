
import sys
from BruteForceVC import *
from ParameterizedVC import *


def read_graph(file_name):

    E = {}
    V = set([])

    input_file = open(file_name, 'r')
    k = int(input_file.readline())

    for line in input_file.readlines():
        line = line[:-1]    # remove '\n' toDo
        edge_list = line.split(' ')
        if len(edge_list) == 2:
            # it's a proper edge, not an isolated vertex
            start = edge_list[0]
            end = edge_list[1]
            if start in E:
                # append end to the adjacency list of start
                E[start].append(end)
            else:
                E[start] = [end]
            # ditto for end
            if end in E:
                E[end].append(start)
            else:
                E[end] = [start]
            # add start and end to vertices of the graph
            # since V is a set, duplicates will be taken care of automatically
            V.add(start)
            V.add(end)
        elif len(edge_list) == 1:
            # degree zero vertices
            # their edge set will be []
            vertex = edge_list[0]
            E[vertex] = []
            V.add(vertex)

    input_file.close()
    G = UndirectedGraph(V, E)
    return (G, k)


# compute vertex cover by brute force
G, k = read_graph(sys.argv[1])
pvc, pvc_time = parameterized_vc(G, k)

# uncomment the below lines to run brute force version
##brute_vc, brute_time = brute_force_VC(G)

if pvc != None:
    # write the VC to file
    with open(sys.argv[2], 'w') as f:
        for vertex in pvc:
            f.write(vertex)
            f.write('\n')
