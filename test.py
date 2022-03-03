import unittest
import numpy as np
from HyperspaceNavigator import HyperspaceNavigator
from utils import generate_hyperspace

hyperspace_2D_1 = np.array([[0., 100., 100., 100., 100.],
                            [0., 100., 100., 100., 100.],
                            [0., 100., 100., 100., 100.],
                            [0., 100., 100., 100., 100.],
                            [0., 0., 0., 0., 0.]])

hyperspace_2D_2 = np.array([[0., 0., 0., 0., 0.],
                            [100., 100., 100., 100., 0.],
                            [100., 100., 100., 100., 0.],
                            [100., 100., 100., 100., 0.],
                            [100., 100., 100., 100., 0.]])

hyperspace_3D_1 = np.array([[[0., 0., 0., 0., 0.],
                             [100., 100., 100., 100., 0.],
                             [100., 100., 100., 100., 100.],
                             [100., 100., 100., 100., 100.],
                             [100., 100., 100., 100., 100.]],
                            [[100., 100., 100., 100., 0.],
                             [100., 100., 100., 100., 100.],
                             [100., 100., 100., 100., 100.],
                             [100., 100., 100., 100., 100.],
                             [100., 100., 100., 100., 100.]],
                            [[100., 100., 100., 100., 0.],
                             [100., 100., 100., 100., 100.],
                             [100., 100., 100., 100., 100.],
                             [100., 100., 100., 100., 100.],
                             [100., 100., 100., 100., 100.]],
                            [[100., 100., 100., 100., 0.],
                             [100., 100., 100., 100., 100.],
                             [100., 100., 100., 100., 100.],
                             [100., 100., 100., 100., 100.],
                             [100., 100., 100., 100., 100.]],
                            [[100., 100., 100., 100., 0.],
                             [100., 100., 100., 100., 0.],
                             [100., 100., 100., 100., 0.],
                             [100., 100., 100., 100., 0.],
                             [100., 100., 100., 100., 0.]]
                            ])


class TestHyperSpaceNavigator(unittest.TestCase):
    def test_2D_1(self):
        hyperspace_navigator = HyperspaceNavigator(hyperspace_2D_1)
        actual_path_2D_1, actual_costs = hyperspace_navigator.navigate()
        expected_path_2D_1 = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
        self.assertEqual(actual_path_2D_1, expected_path_2D_1)
        self.assertEqual(actual_costs, 0)

    def test_2D_2(self):
        hyperspace_navigator = HyperspaceNavigator(hyperspace_2D_2)
        actual_path_2D_2, actual_costs = hyperspace_navigator.navigate()
        expected_path_2D_2 = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]
        self.assertEqual(actual_path_2D_2, expected_path_2D_2)
        self.assertEqual(actual_costs, 0)

    def test_3D_1(self):
        hyperspace_navigator = HyperspaceNavigator(hyperspace_3D_1)
        actual_path_3D_1, actual_costs = hyperspace_navigator.navigate()
        expected_path_3D_1 = [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 0, 3), (0, 0, 4), (1, 0, 4), (2, 0, 4), (3, 0, 4),
                              (4, 0, 4), (4, 1, 4), (4, 2, 4), (4, 3, 4), (4, 4, 4)]
        self.assertEqual(actual_path_3D_1, expected_path_3D_1)
        self.assertEqual(actual_costs, 0)

    def test_astar_dijkstra(self):
        hyperspace_navigator = HyperspaceNavigator(generate_hyperspace(5, 5))
        path_astar, costs_astar = hyperspace_navigator.navigate(algorithm='astar')
        path_dijkstra, costs_dijkstra = hyperspace_navigator.navigate(algorithm='dijkstra')
        self.assertEqual(path_astar, path_dijkstra)
        self.assertEqual(costs_astar, costs_dijkstra)
