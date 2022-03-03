from HyperspaceNavigator import HyperspaceNavigator
from utils import generate_hyperspace


def main():
    hyperspace = generate_hyperspace(5, 5)
    hyperspace_navigator = HyperspaceNavigator(hyperspace)
    start = (0, 0, 0, 0, 0)
    end = (4, 4, 4, 4, 4)
    path_astar, cost_astar = hyperspace_navigator.navigate(start, end, algorithm='astar', metric='euclidean')
    #path_dijkstra, cost_dijkstra = hyperspace_navigator.navigate(start, end, algorithm='astar', metric='euclidean')

    #print(f'Generate Hyperspace:\n{hyperspace}')
    #print()
    #print(f'Costs for traveling from {start} - {end}: {cost_astar}')
    print(f'Costs for traveling from {start} - {end}: {cost_astar}')
    print()
    print(f'Calculated fastest route:\n{path_astar}')
    #print(f'Calculated fastest route:\n{path_dijkstra}')


if __name__ == "__main__":
    main()
