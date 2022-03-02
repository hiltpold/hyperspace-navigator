import numpy as np
import heapq
from typing import Dict, Optional, Tuple


def distance(p1: np.ndarray, p2: np.ndarray, name='euclidean') -> float:
    """
    :param p1: First point as numpy.ndarray
    :param p2: Second point as numpy.ndarray
    :param name: Name of the distance metric
    :return: Distance between p1 and p2 as float according to the chosen metric
    """
    if name == 'euclidean':
        sum_sq = np.sum(np.square(p1 - p2))
        return np.sqrt(sum_sq)
    elif name == 'manhattan':
        return np.sum(np.abs(np.subtract(p1, p2)))
    else:
        raise Exception('This metric has not been implemented yet.')


class HyperspaceNavigator:

    def __init__(self, hyperspace):
        assert type(hyperspace) == np.ndarray, 'The HyperspaceNavigator works a Hyperspace described by a numpy.ndarray'
        self.hyperspace = hyperspace
        self.dimensions, self.extent = self.__describe_hyperspace()

    def __describe_hyperspace(self) -> Tuple[int, int]:
        # get dimensions of the hyperspace
        dimensions = len(np.shape(self.hyperspace))
        # extent in each dimension
        hyperspace_shape = np.shape(self.hyperspace)
        # assuming equal extent in each dimension
        assert np.all(
            np.asarray(hyperspace_shape, int) == hyperspace_shape[0]), 'Assumes equal extent of each dimension'
        # extent
        extent = hyperspace_shape[0]
        self
        return dimensions, extent

    def __generate_directions(self) -> np.ndarray:
        tmp_directions = np.zeros((self.dimensions, self.dimensions), int)
        np.fill_diagonal(tmp_directions, 1)
        return tmp_directions

    def __get_neighbors(self, position: np.ndarray) -> list:
        next_positions = []
        for direction in self.__generate_directions():
            next_position = position + direction
            # the index at which the standard basis is nonzero,
            # holds the dimension we are currently moving
            current_dim = np.nonzero(direction)[0]
            # check bounds at this index
            if next_position[current_dim] < self.extent:
                next_positions.append(next_position)

        return next_positions

    def astar(self, start: np.ndarray, end: np.ndarray) -> \
            Tuple[Dict[tuple, Optional[tuple]], Dict[tuple, int]]:

        # initialize the frontier as priority queue. The tuple (priority, node) can be handled
        # by the heapq library and builds the heap according to the priority.
        frontier = [(0, tuple(start))]
        heapq.heapify(frontier)

        # helper to keep track of the optimal predecessor.
        predecessors = {tuple(start): None}

        # helper to keep track of the curr costs
        costs = {tuple(start): 0}
        # iterate main loop until frontier is empty
        while not len(frontier) == 0:
            current = heapq.heappop(frontier)[1]

            # reached the target, exit loop
            if current == tuple(end):
                break

            for n in self.__get_neighbors(current):

                neighbor = tuple(n)
                # print('new_costs', costs[current])
                # print('space',  space[tuple(current)])
                new_costs = costs[tuple(current)] + self.hyperspace[tuple(current)]
                # print('neighbor', neighbor)
                if neighbor not in costs or new_costs < costs[neighbor]:
                    costs[neighbor] = new_costs
                    priority = new_costs + distance(n, end, name='manhattan')
                    heapq.heappush(frontier, (priority, tuple(neighbor)))
                    predecessors[tuple(neighbor)] = current

        return predecessors, costs
