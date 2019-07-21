#!python

from graph import Graph, Vertex
import unittest
# Python 2 and 3 compatibility: unittest module renamed this assertion method
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class VertexTest(unittest.TestCase):

    def test_init(self):
        id = "A"
        v = Vertex(id)
        assert v.id == id
        self.assertDictEqual(v.neighbors, {})

    def test_add_neighbor(self):
        v1 = Vertex(1)
        v2 = Vertex(2)
        # Test default weight variable
        v1.add_neighbor(v2)
        self.assertDictEqual(v1.neighbors, {v2: 1})
        # Error should be raised if v2 is added again
        with self.assertRaises(KeyError):
            v1.add_neighbor(v2)
        # Test passed in weight variable
        v3 = Vertex(3)
        v1.add_neighbor(v3, 3)
        self.assertDictEqual(v1.neighbors, {v2: 1, v3: 3})
        # Error should be raised if v3 is added again
        with self.assertRaises(KeyError):
            v1.add_neighbor(v3, 3)
        # Test recursive adding
        v2.add_neighbor(v1)
        self.assertDictEqual(v2.neighbors, {v1: 1})
        v3.add_neighbor(v1)
        self.assertDictEqual(v3.neighbors, {v1: 1})

    def test_get_neighbors(self):
        v1 = Vertex(1)
        v2 = Vertex(2)
        v3 = Vertex(3)
        # Test getting neighbors
        v1.add_neighbor(v2)
        v1.add_neighbor(v3)
        self.assertCountEqual(v1.get_neighbors(), [v2, v3])
        v2.add_neighbor(v1, 2)
        v2.add_neighbor(v3, 2)
        self.assertCountEqual(v2.get_neighbors(), [v1, v3])
        v3.add_neighbor(v1, 3)
        v3.add_neighbor(v2, 3)
        self.assertCountEqual(v3.get_neighbors(), [v1, v2])

    def test_get_id(self):
        # Test alphabetical ids
        v_a = Vertex("A")
        assert v_a.get_id() == "A"
        v_b = Vertex("B")
        assert v_b.get_id() == "B"
        v_c = Vertex("C")
        assert v_c.get_id() == "C"
        # Test numerical ids
        v1 = Vertex(1)
        assert v1.get_id() == 1
        v2 = Vertex(2)
        assert v2.get_id() == 2
        v3 = Vertex(3)
        assert v3.get_id() == 3

    def test_get_edge_weight(self):
        v1 = Vertex(1)
        v2 = Vertex(2)
        v3 = Vertex(3)
        # Test default weight variable
        v2.add_neighbor(v1)
        assert v2.get_edge_weight(v1) == 1
        # Test passed in weight variable
        v2.add_neighbor(v3, 3)
        assert v2.get_edge_weight(v3) == 3


class GraphTest(unittest.TestCase):

    def test_init(self):
        g = Graph()
        self.assertDictEqual(g.vert_list, {})
        assert g.num_vertices == 0

    def test_num_vertices(self):
        g = Graph()

        # Size should increase when a vertex is added
        assert g.num_vertices == 0
        g.add_vertex('A')
        assert g.num_vertices == 1
        g.add_vertex('B')
        assert g.num_vertices == 2
        g.add_vertex('C')
        assert g.num_vertices == 3

        # Size should increase once when an edge is added with a new vertex
        g.add_edge('A', 'B')
        assert g.num_vertices == 3
        g.add_edge('B', 'C')
        assert g.num_vertices == 3
        g.add_edge('C', 'D')
        assert g.num_vertices == 4

        # Size should increase twice when edge is added with two new vertices
        g.add_edge('E', 'F')
        assert g.num_vertices == 6

        # Error should be raised when a vertex, that already exists, is added
        # Size should not change when error is raised
        with self.assertRaises(KeyError):
            g.add_vertex('B')  # Vertex already exists
        assert g.num_vertices == 6
        with self.assertRaises(KeyError):
            g.add_vertex('D')  # Vertex already exists
        assert g.num_vertices == 6

    def test_add_vertex(self):
        g = Graph()

        # graph should have newly added vertex
        assert g.size == 0
        g.add_vertex('A')
        assert g.size == 1
        assert g.has_vertex('A') is True
        g.add_vertex('B')
        assert g.size == 2
        assert g.has_vertex('B') is True
        g.add_vertex('C')
        assert g.size == 3
        assert g.has_vertex('C') is True

        # error should be raised when a vertex, that already exists, is added
        with self.assertRaises(KeyError):
            g.add_vertex('A')  # Vertex already exists
        with self.assertRaises(KeyError):
            g.add_vertex('B')  # Vertex already exists
        with self.assertRaises(KeyError):
            g.add_vertex('C')  # Vertex already exists

    def test_get_vertex(self):
        pass

    def test_add_edge(self):
        g = Graph()

        # start with graph that already has vertices in it
        g.add_vertex('A')
        assert g.has_vertex('A') is True
        g.add_vertex('B')
        assert g.has_vertex('B') is True
        g.add_vertex('C')
        assert g.has_vertex('C') is True
        assert g.size == 3

        # when edge is added with existing vertices, second vertex should be a neighbor of first vertex
        g.add_edge('A', 'B')
        self.assertCountEqual(g.get_neighbors('A'), ['B'])  # Item order does not matter
        self.assertCountEqual(g.get_neighbors('B'), [])
        g.add_edge('A', 'C')
        self.assertCountEqual(g.get_neighbors('A'), ['B', 'C'])  # Item order does not matter
        self.assertCountEqual(g.get_neighbors('C'), [])
        g.add_edge('B', 'C')
        self.assertCountEqual(g.get_neighbors('B'), ['C'])  # Item order does not matter
        self.assertCountEqual(g.get_neighbors('C'), [])

        # when edge is added with nonexistent vertices, add nonexistent vertices
        # then, second vertex should be a neighbor of first vertex
        g.add_edge('B', 'D')
        self.assertCountEqual(g.get_neighbors('B'), ['C', 'D'])  # Item order does not matter
        self.assertCountEqual(g.get_neighbors('D'), [])
        g.add_edge('E', 'F')
        self.assertCountEqual(g.get_neighbors('E'), ['F'])  # Item order does not matter
        self.assertCountEqual(g.get_neighbors('F'), [])

        # when duplicate edge is added, the duplicate edge should be ignored
        g.add_edge('A', 'C')
        self.assertCountEqual(g.get_neighbors('A'), ['B', 'C'])  # Item order does not matter
        self.assertCountEqual(g.get_neighbors('C'), [])
        g.add_edge('E', 'F')
        self.assertCountEqual(g.get_neighbors('E'), ['F'])  # Item order does not matter
        self.assertCountEqual(g.get_neighbors('F'), [])

    def test_get_vertices(self):
        g = Graph()

        # get_vertices should return all vertices added by add_vertex
        assert g.has_vertex('A') is False
        g.add_vertex('A')
        self.assertCountEqual(g.get_vertices(), ['A'])  # Item order does not matter
        assert g.has_vertex('B') is False
        g.add_vertex('B')
        self.assertCountEqual(g.get_vertices(), ['A', 'B'])  # Item order does not matter
        assert g.has_vertex('C') is False
        g.add_vertex('C')
        self.assertCountEqual(g.get_vertices(), ['A', 'B', 'C'])  # Item order does not matter

        # get_vertices should return all vertices added by add_edge
        assert g.has_vertex('D') is False
        assert g.has_vertex('E') is False
        g.add_edge('D', 'E')
        self.assertCountEqual(g.get_vertices(), ['A', 'B', 'C', 'D', 'E'])  # Item order does not matter


if __name__ == '__main__':
    unittest.main()
