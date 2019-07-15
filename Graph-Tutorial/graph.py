#!python

""" Vertex Class
A helper class for the Graph class that defines vertices and vertex neighbors.
"""


class Vertex(object):

    def __init__(self, vertex):
        """initialize a vertex and its neighbors

        id: a number or string to identify the vertex
        neighbors: set of vertices adjacent to self,
        stored in a dictionary with
            key = vertex
            value = weight of edge between self and neighbor.
        """
        self.id = vertex
        self.neighbors = {}

    def __str__(self):
        """output the list of neighbors of this vertex"""
        # possible refactor
        # return "{} adjancent to {}".format(self.id, [x.id for x in self.neighbors])
        return str(self.id) + " adjancent to " + \
            str([x.id for x in self.neighbors])

    def add_neighbor(self, vertex, weight=0):
        """add a neighbor along a weighted edge"""
        # TODO check if vertex is already a neighbot
        # TODO if not, add vertex to neighbors and assign weight.

    def get_neighbors(self):
        """return the neighbors of this vertex"""
        # TODO return the neighbors

    def get_id(self):
        """return the id of this vertex"""
        return self.id

    def get_edge_weight(self, vertex):
        """return the weight of this edge"""
        # TODO return the weight of the edge from this vertext to the given vertex.


""" Graph Class
A class demonstrating the essential facts and functionalities of graphs.
"""


class Graph:
    def __init__(self):
        """ initializes a graph object with an empty dictionary.
        """
        self.vertList = {}
        self.numVertices = 0

    def __iter__(self):
        """iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.vertList.values())

    def add_vertex(self, key):
        """add a new vertex object to the graph with
        the given key and return the vertex
        """
        # TODO increment the number of vertices
        # TODO create a new vertex
        # TODO add the new vertex to the vertex list
        # TODO return the new vertex

    def get_vertex(self, key):
        """return the vertex if it exists"""
        # TODO return the vertex if it is in the graph

    def add_edge(self, f, t, cost=0):
        """add an edge from vertex f to vertex t with a cost
        """
        # TODO if either vertex is not in the graph,
        # add it - or return an error (choice is up to you).
        # TODO if both vertices in the graph, add the
        # edge by making t a neighbor of f
        # and using the add_neighbor method of the Vertex class.
        # Hint: the vertex f is stored in self.vertList[f].

    def get_vertices(self):
        """return all the vertices in the graph"""
        return self.vertList.keys()


# Driver code
if __name__ == "__main__":

    # Challenge 1: Create the graph
    g = Graph()

    # Add your friends
    g.add_vertex("Friend 1")
    g.add_vertex("Friend 2")
    g.add_vertex("Friend 3")

    # ...  add all 10 including you ...

    # Add connections (non weighted edges for now)
    g.add_edge("Friend 1", "Friend 2")
    g.add_edge("Friend 2", "Friend 3")

    # Challenge 1: Output the vertices & edges
    # Print vertices
    print("The vertices are: ", g.get_vertices(), "\n")

    print("The edges are: ")
    for v in g:
        for w in v.get_neighbors():
            print("( %s , %s )" % (v.get_id(), w.get_id()))
