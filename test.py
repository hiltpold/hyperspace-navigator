import unittest
import numpy as np
from HyperspaceNavigator import HyperspaceNavigator

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
