import numpy as np
import heapq
from typing import Dict, Optional, Tuple, List
from utils import describe_ndarray, distance

class HyperspaceNavigator:

    def __init__(self, hyperspace):
        assert type(hyperspace) == np.ndarray, 'Works only on a Hyperspace described by a numpy.ndarray'
        self.hyperspace = hyperspace
        self.dimensions, self.extent = describe_ndarray(hyperspace)
        all_predecessors: dict[tuple, Optional[tuple]] = dict()
        all_costs: dict[tuple, int] = dict()

    def _generate_directions(self) -> np.ndarray:
        tmp_directions = np.zeros((self.dimensions, self.dimensions), int)
        np.fill_diagonal(tmp_directions, 1)
        return tmp_directions

    def _get_neighbors(self, position: np.ndarray) -> list:
        next_positions = []
        for direction in self._generate_directions():
            next_position = position + direction
            # the index at which the standard basis is nonzero,
            # holds the dimension we are currently moving
            current_dim = np.nonzero(direction)[0]
            # check bounds at this index
            if next_position[current_dim] < self.extent:
                next_positions.append(next_position)

        return next_positions

    def _astar(self, start: np.ndarray, end: np.ndarray):

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

            for n in self._get_neighbors(current):

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

        self.all_predecessors = predecessors
        self.all_costs = costs

    def _reconstruct_path(self, start: tuple, end: tuple) -> list[tuple]:
        current = end
        path = []
        while current != start:  # note: this will fail if no path found
            path.append(current)
            current = self.all_predecessors[current]
        path.append(start)  # optional
        path.reverse()  # optional
        return path, self.all_costs[end]

    def navigate(self, start: tuple = None, end: tuple = None, algorithm='astar') -> tuple[list[tuple], float]:
        if start is None:
            start = np.zeros(self.dimensions, int)

        if end is None:
            end = np.full(self.dimensions, self.extent - 1, int)

        if start is not None or end is not None:
            # check dimensions
            assert len(start) == self.dimensions, 'start has wrong dimensions'
            assert len(end) == self.dimensions, 'end has wrong dimensions'

        if algorithm == 'astar':
            self._astar(start, end)

        return self._reconstruct_path(tuple(start), tuple(end))
