import unittest
import graf

class TestBoardFunctions(unittest.TestCase):

    def setUp(self):
        self.large_board = [
            ['2', '1', 'J', '1', '0', 'X'],
            ['J', '1', '2', '0', '1', '1'],
            ['2', '1', '1', 'J', '1', '4'],
            ['1', '1', '0', '2', 'J', '8'],
            ['4', 'X', '1', '3', '0', '1'],
            ['2', '1', '5', '1', '9', 'J']
        ]

        self.small_board = [
            ['J', 'X', 'J'],
            ['J', '0', '1'],
            ['X', '2', 'J']
        ]

        self.simple_board = [
            ['X', '2', 'J'],
            ['2', '0', '7'],
            ['J', '1', 'X']
        ]
        
        self.medium_board = [
            ['J', '1', '2', 'X'],
            ['1', 'J', '3', '4'],
            ['0', 'J', '1', 'J'],
            ['X', '2', 'J', '3']
        ]

    def test_find_xs_large_board(self):
        xs = graf.find_xs(self.large_board)
        self.assertEqual(xs, [(0, 5), (4, 1)])

    def test_get_neighbors_large_board(self):
        neighbors = graf.get_neighbors((2, 2), self.large_board)
        expected_neighbors = [(2, 3), (3, 2), (1, 2), (2, 1)]
        self.assertEqual(set(neighbors), set(expected_neighbors))

    def test_dijkstra_large_board(self):
        start, end = (0, 5), (4, 1)
        cost, paths = graf.dijkstra(self.large_board, start, end)
        path = graf.reconstruct_path(paths, end)
        expected_cost = 2
        expected_path = [(0, 5), (0, 4), (0, 3), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1)]
        self.assertEqual(cost, expected_cost)
        self.assertEqual(path, expected_path)

    def test_find_xs_small_board(self):
        xs = graf.find_xs(self.small_board)
        self.assertEqual(xs, [(0, 1), (2, 0)])

    def test_get_neighbors_small_board(self):
        neighbors = graf.get_neighbors((1, 1), self.small_board)
        expected_neighbors = [(0, 1), (2, 1), (1, 0), (1, 2)]
        self.assertEqual(set(neighbors), set(expected_neighbors))

    def test_dijkstra_small_board(self):
        start, end = (0, 1), (2, 0)
        cost, paths = graf.dijkstra(self.small_board, start, end)
        path = graf.reconstruct_path(paths, end)
        expected_cost = 0
        expected_path = [(0, 1), (0, 0), (1, 0), (2, 0)]
        self.assertEqual(cost, expected_cost)
        self.assertEqual(path, expected_path)

    def test_find_xs_simple_board(self):
        xs = graf.find_xs(self.simple_board)
        self.assertEqual(xs, [(0, 0), (2, 2)])

    def test_get_neighbors_simple_board(self):
        neighbors = graf.get_neighbors((1, 1), self.simple_board)
        expected_neighbors = [(0, 1), (2, 1), (1, 0), (1, 2)]
        self.assertEqual(set(neighbors), set(expected_neighbors))

    def test_dijkstra_simple_board(self):
        start, end = (0, 0), (2, 2)
        cost, paths = graf.dijkstra(self.simple_board, start, end)
        path = graf.reconstruct_path(paths, end)
        expected_cost = 2
        expected_path = [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]
        self.assertEqual(cost, expected_cost)
        self.assertEqual(path, expected_path)
        
    def test_find_xs_medium_board(self):
        xs = graf.find_xs(self.medium_board)
        self.assertEqual(xs, [(0, 3), (3, 0)])

    def test_get_neighbors_medium_board(self):
        neighbors = graf.get_neighbors((2, 2), self.medium_board)
        expected_neighbors = [(2, 3), (3, 2), (1, 2), (2, 1)]
        self.assertEqual(set(neighbors), set(expected_neighbors))

    def test_dijkstra_medium_board(self):
        start, end = (0, 3), (3, 0)
        cost, paths = graf.dijkstra(self.medium_board, start, end)
        path = graf.reconstruct_path(paths, end)
        expected_cost = 3
        expected_path = [(0, 3), (0, 2), (0, 1), (0, 0), (1, 0), (2, 0), (3, 0)]
        self.assertEqual(cost, expected_cost)
        self.assertEqual(path, expected_path)

if __name__ == '__main__':
    unittest.main()
