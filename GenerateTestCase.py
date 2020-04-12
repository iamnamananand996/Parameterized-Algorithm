import random

n = 22  # number of vertices
k = 22   # parameter

vertices = set([])
edges = {}

# add all vertices to the vertex set
for i in range(0, n):
    vertices.add('v_' + str(i))

# generate edges for each vertex

for start in vertices:
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

print(k)
for start in edges.keys():
    stops = edges[start]
    for stop in stops:
        print(start + ' ' + stop)
