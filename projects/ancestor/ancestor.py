#
# Define data structures
#

class Graph:
    def __init__(self):
        self.vertices = {}
        # self.vertices = {
        #   3: {1,2},
        #   6: {3,5},
        #   7: {5},
        #   5: {4},
        #   8: {4,11},
        #   9: {8},
        #   1: {10},
        # }
    
    def add_vertex(self, parent, child):
        if child not in self.vertices:
            self.vertices[child] = set()

        self.vertices[child].add(parent)

#
# Define search utility
#

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for relationship in ancestors:
        graph.add_vertex(relationship[0], relationship[1])

    # print(f"graph.vertices {graph.vertices}")
    #=> {3: {1, 2}, 6: {3, 5}, 7: {5}, 5: {4}, 8: {11, 4}, 9: {8}, 1: {10}}

    if starting_node not in graph.vertices:
        return -1

    current_vertex = starting_node
    next_vertex = min(graph.vertices[current_vertex])
    while next_vertex in graph.vertices:
        current_vertex = next_vertex
        next_vertex = min(graph.vertices[current_vertex])
    
    return next_vertex

