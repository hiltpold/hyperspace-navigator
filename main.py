from HyperspaceNavigator import HyperspaceNavigator
from utils import generate_hyperspace


def main():
    hyperspace = generate_hyperspace(5, 5)
    hyperspace_navigator = HyperspaceNavigator(hyperspace)
    start = (0, 0, 0, 0, 0)
    end = (4, 4, 4, 4, 4)
    path, cost = hyperspace_navigator.navigate(start, end)
    print(f'Costs for Traveling from {start} - {end}: {cost}')
    print(f'Calculated fastest route:\n {path}')


if __name__ == "__main__":
    main()
