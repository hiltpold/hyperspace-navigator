import numpy as np


def generate_hyperspace(dimensions: int, elements: int) -> np.ndarray:
    dim_ary = [elements for x in range(0, dimensions)]
    hyperspace = np.random.random_sample(tuple(dim_ary))
    return hyperspace
