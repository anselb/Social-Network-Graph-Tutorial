#!python


class Vertex(object):
    """Helper class that defines vertices and vertex neighbors."""

    def __init__(self, vertex_id):
        """Initialize a vertex and its neighbors.

        id: a number or string to identify the vertex
        neighbors: set of vertices adjacent to self, stored in dictionary with:
            key = vertex object
            value = weight of edge between self and neighbor
        """
        self.id = vertex_id
        self.neighbors = {}

    def __repr__(self):
        """Return representation of vertex object."""
        return f"Vertex({self.id}) with neighbors {self.get_neighbors}"

    def __str__(self):
        """Output the list of neighbors of this vertex."""
        return f"{self.id} adjacent to {[x.id for x in self.neighbors]}"

    def __hash__(self):
        """Return hash of vertex class, for using this class as a dict key."""
        return hash(self.id)

    def __eq__(self, other):
        """Determine if two vertices are equal."""
        return self.id == other.id

    def __ne__(self, other):
        """Determine if two vertices are not equal."""
        return self.id != other.id

    def add_neighbor(self, vertex, weight=1):
        """Add a neighbor along a weighted edge."""
        # check if vertex is already a neighbor
        if vertex not in self.neighbors:
            # if not, add vertex to neighbors and assign weight
            self.neighbors[vertex] = weight

    def get_neighbors(self):
        """Return the neighbors of this vertex."""
        # return the neighbors
        return set(self.neighbors.keys())

    def get_id(self):
        """Return the id of this vertex."""
        # return the id of the vertex
        return self.id

    def get_edge_weight(self, vertex):
        """Return the weight of this edge."""
        # return the weight of the edge from this vertex to the given vertex
        return self.neighbors[vertex]


class Graph:
    """Demonstrates the essential facts and functionalities of graphs."""

    def __init__(self):
        """Initialize a graph object with an empty dictionary.

        vert_list: a dictionary of the vertices in this graph where:
            key = the id of a vertex
            value = a vertex object with an id that matches the key
        num_vertices: number of vertices in the graph
        """
        self.vert_list = {}
        self.num_vertices = 0

    def __iter__(self):
        """Iterate over the vertex objects in the graph.

        to use sytax: for v in g
        """
        return iter(self.vert_list.values())

    def add_vertex(self, key):
        """Add a new vertex object to the graph with the given key.

        Return the vertex if the vertex is new, else raise KeyError.
        """
        # raise error if key already exists in graph
        if key in self.vert_list:
            raise KeyError(f"{key} is already in the Graph")
        # increment the number of vertices
        self.num_vertices += 1
        # create a new vertex
        new_vertex = Vertex(key)
        # add the new vertex to the vertex list
        self.vert_list[key] = new_vertex
        # return the new vertex
        return new_vertex

    def get_vertex(self, key):
        """Return the vertex if it exists, else raise KeyError."""
        # raise error if key does not exist in graph
        if key not in self.vert_list:
            raise KeyError(f"{key} is not in the Graph")
        # return the vertex if it is in the graph
        return self.vert_list[key]

    def add_edge(self, from_key, to_key, weight=1):
        """Add edge from vertex with key `from_key` to vertex with key `to_key`.

        If a weight is provided, use that weight.
        """
        # add from_key vertex if it is not in the graph
        if from_key not in self.vert_list:
            self.add_vertex(from_key)

        # add to_key vertex if it is not in the graph
        if to_key not in self.vert_list:
            self.add_vertex(to_key)

        # get vertices from keys
        from_vert = self.vert_list[from_key]
        to_vert = self.vert_list[to_key]

        # when both vertices in graph, make from_vert a neighbor of to_vert
        if to_vert not in from_vert.get_neighbors():
            from_vert.add_neighbor(to_vert, weight)
            to_vert.add_neighbor(from_vert, weight)

    def get_vertices(self):
        """Return all the vertices in the graph."""
        return self.vert_list.keys()


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
    print(f"The vertices are: {g.get_vertices()} \n")

    # Print edges
    print("The edges are: ")
    for v in g:
        for w in v.get_neighbors():
            print(f"( {v.get_id()} , {w.get_id()} )")
