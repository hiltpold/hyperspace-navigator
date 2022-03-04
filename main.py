import cProfile
from HyperspaceNavigator import HyperspaceNavigator
from utils import generate_hyperspace


def main():
    # generate 5 dimensional hyperspace with an extent of 5 in each dimension. The weights are floats >=1 (in this
    # case the admissibility of astar algorithm is true)
    hyperspace = generate_hyperspace(5, 5)
    hyperspace_navigator = HyperspaceNavigator(hyperspace)
    # start and end point as tuple (Keep in mind that the index for the max extent is the defined extent minus one)
    start = (0, 0, 0, 0, 0)
    end = (4, 4, 4, 4, 4)
    # generate the shortest path with its costs
    path_astar, cost_astar = hyperspace_navigator.navigate(start, end, algorithm='astar', metric='manhattan')
    path_dijkstra, cost_dijkstra = hyperspace_navigator.navigate(start, end, algorithm='dijkstra')
    # print(f'Generate Hyperspace:\n{hyperspace}')
    print('INFO-----------------------------------------')
    print(f'Start: {start}')
    print(f'End: {end}')
    print('COSTS-----------------------------------------')
    print(f'Dijkstra: {cost_dijkstra}')
    print(f'A*: {cost_astar}')
    print('PATH-----------------------------------------')
    print(f'Calculated fastest route dijkstra:\n{path_dijkstra}')
    print(f'Calculated fastest route A*:\n{path_astar}')
    print('---------------------------------------------')


if __name__ == "__main__":
    # cProfile.run('main()')
    main()
