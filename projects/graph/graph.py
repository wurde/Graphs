"""
Simple graph implementation
"""

#
# Dependencies
#

from util import Stack, Queue

#
# Define data structure
#

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        print('\nBFT path:')

        visited = set()
        queue = Queue()
        queue.enqueue(starting_vertex)

        while queue.size() > 0:
            nextVertex = queue.dequeue()

            if nextVertex not in visited:
                print(nextVertex)
                visited.add(nextVertex)

                for vert in self.vertices[nextVertex]:
                    queue.enqueue(vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        print('\nDFT path:')

        visited = set()
        stack = Stack()
        stack.push(starting_vertex)

        while stack.size() > 0:
            nextVertex = stack.pop()

            if nextVertex not in visited:
                print(nextVertex)
                visited.add(nextVertex)

                for vert in self.vertices[nextVertex]:
                    stack.push(vert)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if set(self.vertices.keys()).difference(visited) == set():
            return

        if starting_vertex not in visited:
            print(starting_vertex)
            visited.add(starting_vertex)

            for vert in self.vertices[starting_vertex]:
                self.dft_recursive(vert, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        print('\nBFS path:')

        visited = set()
        previous_vertex = {}

        queue = Queue()
        queue.enqueue(starting_vertex)

        while queue.size() > 0:
            vertex = queue.dequeue()

            if vertex not in visited:
                visited.add(vertex)

                if vertex == destination_vertex:
                    current_vertex = destination_vertex
                    path = []

                    while current_vertex != starting_vertex:
                        path.append(current_vertex)
                        current_vertex = previous_vertex[current_vertex]

                    path.append(starting_vertex)
                    path.reverse()

                    return path

                for next_vert in self.vertices[vertex]:
                    if next_vert not in previous_vertex:
                        previous_vertex[next_vert] = vertex

                    queue.enqueue(next_vert)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        print('\nDFS path:')

        visited = set()
        previous_vertex = {}

        stack = Stack()
        stack.push(starting_vertex)

        while stack.size() > 0:
            vertex = stack.pop()

            if vertex not in visited:
                visited.add(vertex)

                if vertex == destination_vertex:
                    current_vertex = destination_vertex
                    path = []

                    while current_vertex != starting_vertex:
                        path.append(current_vertex)
                        current_vertex = previous_vertex[current_vertex]

                    path.append(starting_vertex)
                    path.reverse()

                    return path

                for next_vert in self.vertices[vertex]:
                    if next_vert not in previous_vertex:
                        previous_vertex[next_vert] = vertex

                    stack.push(next_vert)

#
# Execute commands
#

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("\nDFT recursive:")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
