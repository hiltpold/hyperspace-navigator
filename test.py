import unittest
import numpy as np
from main import astar, generate_basis, reconstruct_path

# dimensions
DIMENSIONS = 2
# elements in each dimension
ELEMENTS = 5
start_point = np.zeros(DIMENSIONS, int)
end_point = np.full(DIMENSIONS, ELEMENTS - 1, int)

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
                             [100., 100., 100., 100., 100.],
                             [100., 100., 100., 100., 100.],
                             [100., 100., 100., 100., 100.],
                             [100., 100., 100., 100., 100.]],
                            [[100., 100., 100., 100., 100.],
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
        DIMENSIONS = 2
        start_point = np.zeros(DIMENSIONS, int)
        end_point = np.full(DIMENSIONS, ELEMENTS - 1, int)
        standard_basis = generate_basis(DIMENSIONS)
        came_from_2D_1, costs_2D_1 = astar(hyperspace_2D_1, standard_basis, start_point, end_point)
        actual_path_2D_1 = reconstruct_path(came_from_2D_1, tuple(start_point), tuple(end_point))
        expected_path_2D_1 = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
        self.assertEqual(actual_path_2D_1, expected_path_2D_1)

    def test_2D_2(self):
        DIMENSIONS = 2
        start_point = np.zeros(DIMENSIONS, int)
        end_point = np.full(DIMENSIONS, ELEMENTS - 1, int)
        standard_basis = generate_basis(DIMENSIONS)
        came_from_2D_2, costs_2D_2 = astar(hyperspace_2D_2, standard_basis, start_point, end_point)
        actual_path_2D_2 = reconstruct_path(came_from_2D_2, tuple(start_point), tuple(end_point))
        expected_path_2D_2 = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]
        self.assertEqual(actual_path_2D_2, expected_path_2D_2)

    def test_3D_1(self):
        DIMENSIONS = 3
        start_point = np.zeros(DIMENSIONS, int)
        end_point = np.full(DIMENSIONS, ELEMENTS - 1, int)
        standard_basis = generate_basis(DIMENSIONS)
        came_from_3D_1, costs_3D_1 = astar(hyperspace_3D_1, standard_basis, start_point, end_point)
        actual_path_3D_1 = reconstruct_path(came_from_3D_1, tuple(start_point), tuple(end_point))
        print(hyperspace_3D_1[0, 0, 0], hyperspace_3D_1[0, 0, 1], hyperspace_3D_1[0, 0, 2])
        expected_path_3D_1 = [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 0, 3), (0, 0, 4), (1, 0, 4), (2, 0, 4), (3, 0, 4),
                              (4, 0, 4), (4, 1, 4), (4, 2, 4), (4, 3, 4), (4, 4, 4)]
        self.assertEqual(actual_path_3D_1, expected_path_3D_1)
