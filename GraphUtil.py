"""
A script having a set of simple functions to check graph properties.

"""


class UndirectedGraph:

    def __init__(self, V, E):
        """
        Initialize the Graph class. Accepts a set of vertices V and edges E as input.
        V is implemented as a set
        E is implemented as an adjacency list in the form of a dictionary.
        """

        self.V = V
        self.E = E

    def __str__(self):

        graph_str = ''

        for start in self.E.keys():
            for stop in self.E[start]:
                graph_str += start + ' ' + stop + '\n'

        return graph_str


def check_vertex_cover(G, S):
    """
    Returns True if set S is a vertex cover of the edge set E,
    False otherwise.
    S is implemented as a set
    E is implemented as an adjacency list mapping a vertex to a list
    of edges
    """

    for start in G.E.keys():
        if start in S:
            # vertex start is already in the cover
            # so we needn't check its corresponding edges
            continue
        for end in G.E[start]:
            if not (end in S):
                return False
    return True
