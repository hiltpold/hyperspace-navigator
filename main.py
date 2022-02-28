import heapq
from typing import Dict, Optional, Tuple

import numpy as np
import heapq as pq

# dimensions
DIMENSIONS = 5

# elements in each dimension
ELEMENTS = 5

# generate elements in each dimension
dim_ary = [ELEMENTS for x in range(0, DIMENSIONS)]

# generate cell weights for each cell
cell_weights = np.random.rand(*dim_ary) * 100
# cell_weights = np.zeros(dim_ary)
"""
cell_weights = np.array([[0, 100., 100., 100., 100.],
                         [0., 100., 100., 100., 100.],
                         [0., 100., 100., 100., 100.],
                         [0., 100., 100., 100., 100.],
                         [0., 0, 0., 0., 0.]])


cell_weights = np.array([[[100., 0., 0., 0., 0.],
                          [0., 100., 0., 0., 0.],
                          [0., 0., 100., 0., 0.],
                          [0., 0., 0., 100., 0.],
                          [0., 0., 0., 0., 100.]],
                         [[100., 0., 0., 0., 0.],
                          [0., 100., 0., 0., 0.],
                          [0., 0., 100., 0., 0.],
                          [0., 0., 0., 100., 0.],
                          [0., 0., 0., 0., 100.]],
                         [[100., 0., 0., 0., 0.],
                          [0., 100., 0., 0., 0.],
                          [0., 0., 100., 0., 0.],
                          [0., 0., 0., 100., 0.],
                          [0., 0., 0., 0., 100.]],
                         [[100., 0., 0., 0., 0.],
                          [0., 100., 0., 0., 0.],
                          [0., 0., 100., 0., 0.],
                          [0., 0., 0., 100., 0.],
                          [0., 0., 0., 0., 100.]],
                         [[100., 0., 0., 0., 0.],
                          [0., 100., 0., 0., 0.],
                          [0., 0., 100., 0., 0.],
                          [0., 0., 0., 100., 0.],
                          [0., 0., 0., 0., 100.]]
                         ])
                         """
print(np.shape(cell_weights))


def generate_basis(d: int) -> np.ndarray:
    tmp_standard_basis = np.zeros((d, d), int)
    np.fill_diagonal(tmp_standard_basis, 1)
    return tmp_standard_basis


def distance(p1: np.ndarray, p2: np.ndarray, name='euclidean') -> float:
    if name == 'euclidean':
        sum_sq = np.sum(np.square(p1 - p2))
        return np.sqrt(sum_sq)
    elif name == 'manhattan':
        return np.sum(np.abs(np.subtract(p1, p2)))
    else:
        raise Exception('This metric has not been implemented yet.')


def get_neighbors(cell: np.ndarray, basis: np.ndarray, boundary: int) -> list:
    next_cells = []
    for b in basis:
        next_cell = cell + b
        # the index at which the standard basis is nonzero,
        # holds the dimension we are currently moving
        current_dim = np.nonzero(b)[0]
        # check bounds at this index
        if next_cell[current_dim] < boundary:
            next_cells.append(next_cell)

    return next_cells


def astar(space: np.ndarray, basis: np.ndarray, start: np.ndarray, end: np.ndarray) -> \
        Tuple[Dict[tuple, Optional[tuple]], Dict[tuple, int]]:
    # initialize the frontier as priority queue. The tuple (priority, node) can be handled
    # by the heapq library and builds the heap according to the priority.
    frontier = [(0, tuple(start))]
    heapq.heapify(frontier)
    # helper to keep track of the optimal predecessor.
    came_from = {tuple(start): None}
    # helper to keep track of the curr costs
    costs = {tuple(start): 0}

    # iterate main loop until frontier is empty
    while not len(frontier) == 0:
        current = heapq.heappop(frontier)[1]
        # print('current', current)
        # print('frontier', frontier)
        # print('neighbors', get_neighbors(current, basis, ELEMENTS))

        # reached the target, exit loop
        if current == tuple(end):
            break

        for n in get_neighbors(current, basis, ELEMENTS):
            neighbor = tuple(n)
            # print('new_costs', costs[current])
            # print('space',  space[tuple(current)])
            new_costs = costs[tuple(current)] + space[tuple(current)]
            # print('neighbor', neighbor)
            if neighbor not in costs or new_costs < costs[neighbor]:
                costs[neighbor] = new_costs
                priority = new_costs + distance(n, end, name='manhattan')
                heapq.heappush(frontier, (priority, tuple(neighbor)))
                came_from[tuple(neighbor)] = current

    return came_from, costs


def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:  # note: this will fail if no path found
        path.append(current)
        current = came_from[current]
    path.append(start)  # optional
    path.reverse()  # optional
    return path


"""
start_point = np.zeros(DIMENSIONS, int)
end_point = np.full(DIMENSIONS, ELEMENTS - 1, int)
standard_basis = generate_basis(DIMENSIONS)
print(standard_basis)
print('start: ', start_point)
print('end: ', end_point)
print(cell_weights)
"""
start_point = np.zeros(DIMENSIONS, int)
end_point = np.full(DIMENSIONS, ELEMENTS - 1, int)
standard_basis = generate_basis(DIMENSIONS)
a, b = astar(cell_weights, standard_basis, start_point, end_point)
print(a)
print(b)
print(reconstruct_path(a, tuple(start_point), tuple(end_point)))

