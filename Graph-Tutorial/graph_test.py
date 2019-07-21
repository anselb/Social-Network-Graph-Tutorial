#!python

from graph import Graph, Vertex
import unittest
# Python 2 and 3 compatibility: unittest module renamed this assertion method
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class Vertex(unittest.TestCase):

    def test_init(self):
        pass

    def test_add_neighbor(self):
        pass

    def test_get_neighbors(self):
        pass

    def test_get_edge_weight(self):
        pass


class GraphTest(unittest.TestCase):

    def test_init(self):
        g = Graph()
        assert g.size == 0

    def test_num_vertices(self):
        g = Graph()

        # size should increase when a vertex is added
        assert g.size == 0
        g.add_vertex('A')
        assert g.size == 1
        g.add_vertex('B')
        assert g.size == 2
        g.add_vertex('C')
        assert g.size == 3

        # size should increase once when an edge is added with a new vertex
        g.add_edge('A', 'B')
        assert g.size == 3
        g.add_edge('B', 'C')
        assert g.size == 3
        g.add_edge('C', 'D')
        assert g.size == 4

        # size should increase twice when an edge is added with two new vertices
        g.add_edge('E', 'F')
        assert g.size == 6

        # error should be raised when a vertex, that already exists, is added
        # size should not change when error is raised
        with self.assertRaises(KeyError):
            g.add_vertex('B')  # Vertex already exists
        assert g.size == 6
        with self.assertRaises(KeyError):
            g.add_vertex('D')  # Vertex already exists
        assert g.size == 6

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
