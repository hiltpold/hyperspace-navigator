import numpy as np
import heapq
from typing import Optional
from utils import describe_ndarray, distance


class HyperspaceNavigator:

    def __init__(self, hyperspace):
        assert type(hyperspace) == np.ndarray, 'Works only on a Hyperspace described by a numpy.ndarray'
        self.hyperspace: np.ndarray = hyperspace
        self.dimensions: int
        self.extent: int
        self.dimensions, self.extent = describe_ndarray(hyperspace)
        self.all_predecessors: dict[tuple, Optional[tuple]] = dict()
        self.all_costs: dict[tuple, int] = dict()

    def _generate_directions(self) -> np.ndarray:
        tmp_directions = np.zeros((self.dimensions, self.dimensions), int)
        np.fill_diagonal(tmp_directions, 1)
        return tmp_directions

    def _get_neighbors(self, position: np.ndarray) -> list[np.ndarray]:
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

    def _shortest_path(self, start: np.ndarray, end: np.ndarray, algorithm: str, metric: str):
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
                    priority = new_costs if algorithm == 'dijkstra' else new_costs + distance(n, end, metric)
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

    def navigate(self, start: tuple = None, end: tuple = None, algorithm='astar', metric='manhattan') -> \
            tuple[list[tuple], float]:
        """
        :param start: Start of the path represented as tuple in the hyperspace.
        :param end: End of the path represented as tuple in the hyperspace.
        :param algorithm: Name of the algorithm that calculates the shortest path and its costs. Chose between "astar"
         (A*) and "dijkstra". A* uses a heuristic in form of a distance to speed up the calculation. Be aware that in
          some cases the admissibility is not given and the path returned by A* is not the best available.
        :param metric: If astar is chosen as algorithm, provide a metric according to which positions ar prioritized
         during the calculation of the path.
        :return: The shortest path in the hyperspace between start and end with its costs
        """
        if start is None:
            start = tuple(np.zeros(self.dimensions, int))

        if end is None:
            end = tuple(np.full(self.dimensions, self.extent - 1, int))

        # do some basic tests before we start
        assert len(start) == self.dimensions, 'start has wrong dimensions'
        assert len(end) == self.dimensions, 'end has wrong dimensions'
        assert np.all(
            np.asarray(start, int) == start[0]), 'Assumes equal extent in each dimension'
        assert np.all(
            np.asarray(end, int) == end[0]), 'Assumes equal extent in each dimension'

        assert max(start) < self.extent, f'maximal index allowed: {self.extent - 1}'
        assert max(end) < self.extent, f'maximal index allowed: {self.extent - 1}'
        assert min(start) >= 0, f'minimal index allowed: {0}'
        assert min(end) >= 0, f'minimal index allowed: {0}'
        assert algorithm in {'astar', 'dijkstra'}, 'choose either "astar" or "dijkstra" as algorithm parameter'

        self._shortest_path(start, end, algorithm, metric)

        return self._reconstruct_path(tuple(start), tuple(end))
