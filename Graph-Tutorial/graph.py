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
        return f"Vertex({self.id})"

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
        # Check if vertex is already a neighbor
        if vertex in self.neighbors:
            # If so, raise KeyError
            raise KeyError(f"{vertex.id} is already a neighbor of {self.id}")
        # If not, add vertex to neighbors and assign weight
        self.neighbors[vertex] = weight

    def get_neighbors(self):
        """Return the neighbors of this vertex."""
        # Return the neighbors
        return set(self.neighbors.keys())

    def get_id(self):
        """Return the id of this vertex."""
        # Return the id of the vertex
        return self.id

    def get_edge_weight(self, vertex):
        """Return the weight of this edge."""
        # Return the weight of the edge from this vertex to the given vertex
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
        # Raise error if key already exists in graph
        if key in self.vert_list:
            raise KeyError(f"{key} is already in the Graph")
        # Increment the number of vertices
        self.num_vertices += 1
        # Create a new vertex
        new_vertex = Vertex(key)
        # Add the new vertex to the vertex list
        self.vert_list[key] = new_vertex
        # Return the new vertex
        return new_vertex

    def get_vertex(self, key):
        """Return the vertex if it exists, else raise KeyError."""
        # Raise error if key does not exist in graph
        if key not in self.vert_list:
            raise KeyError(f"{key} is not in the Graph")
        # Return the vertex if it is in the graph
        return self.vert_list[key]

    def add_edge(self, from_key, to_key, weight=1):
        """Add edge from vertex with key `from_key` to vertex with key `to_key`.

        If a weight is provided, use that weight.
        """
        # Add from_key vertex if it is not in the graph
        if from_key not in self.vert_list:
            self.add_vertex(from_key)

        # Add to_key vertex if it is not in the graph
        if to_key not in self.vert_list:
            self.add_vertex(to_key)

        # Get vertices from keys
        from_vert = self.vert_list[from_key]
        to_vert = self.vert_list[to_key]

        # When both vertices in graph, make from_vert a neighbor of to_vert
        from_vert.add_neighbor(to_vert, weight)

    def get_vertices(self):
        """Return all the vertices in the graph."""
        return set(self.vert_list.values())


# Driver code
if __name__ == "__main__":

    # Challenge 1: Create the graph and output the vertices & edges
    g = Graph()

    # Add your friends
    g.add_vertex("Myself")
    g.add_vertex("Friend 1")
    g.add_vertex("Friend 2")
    g.add_vertex("Friend 3")
    g.add_vertex("Friend 4")
    g.add_vertex("Friend 5")
    g.add_vertex("Friend 6")
    g.add_vertex("Friend 7")
    g.add_vertex("Friend 8")
    g.add_vertex("Friend 9")

    # Add connections (non weighted edges for now)
    g.add_edge("Myself", "Friend 1")
    g.add_edge("Myself", "Friend 2")
    g.add_edge("Myself", "Friend 3")
    g.add_edge("Myself", "Friend 4")
    g.add_edge("Myself", "Friend 5")
    g.add_edge("Myself", "Friend 6")
    g.add_edge("Myself", "Friend 7")
    g.add_edge("Myself", "Friend 8")
    g.add_edge("Myself", "Friend 9")

    g.add_edge("Friend 1", "Friend 9")
    g.add_edge("Friend 1", "Myself")
    g.add_edge("Friend 1", "Friend 3")

    g.add_edge("Friend 2", "Friend 8")
    g.add_edge("Friend 2", "Friend 7")
    g.add_edge("Friend 2", "Myself")
    g.add_edge("Friend 2", "Friend 5")

    g.add_edge("Friend 3", "Friend 1")
    g.add_edge("Friend 3", "Myself")

    g.add_edge("Friend 4", "Myself")
    g.add_edge("Friend 4", "Friend 7")
    g.add_edge("Friend 4", "Friend 6")
    g.add_edge("Friend 4", "Friend 5")

    g.add_edge("Friend 5", "Friend 4")
    g.add_edge("Friend 5", "Friend 2")
    g.add_edge("Friend 5", "Myself")
    g.add_edge("Friend 5", "Friend 9")
    g.add_edge("Friend 5", "Friend 6")

    g.add_edge("Friend 6", "Friend 5")
    g.add_edge("Friend 6", "Friend 4")
    g.add_edge("Friend 6", "Myself")
    g.add_edge("Friend 6", "Friend 7")

    g.add_edge("Friend 7", "Friend 6")
    g.add_edge("Friend 7", "Friend 4")
    g.add_edge("Friend 7", "Myself")
    g.add_edge("Friend 7", "Friend 2")
    g.add_edge("Friend 7", "Friend 9")

    g.add_edge("Friend 8", "Myself")
    g.add_edge("Friend 8", "Friend 2")

    g.add_edge("Friend 9", "Friend 7")
    g.add_edge("Friend 9", "Friend 5")
    g.add_edge("Friend 9", "Myself")
    g.add_edge("Friend 9", "Friend 1")

    # Print vertices
    print(f"The vertices are: {g.get_vertices()} \n")

    # Print edges
    print("The edges are: ")
    for v in g:
        for w in v.get_neighbors():
            print(f"( {v.get_id()} , {w.get_id()} )")
