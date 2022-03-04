import numpy as np
from typing import Tuple


def generate_hyperspace(dimensions: int, elements: int) -> np.ndarray:
    """
    :param dimensions: Dimensions of the hyperspace
    :param elements: Extent of each dimension
    :return: Hyperspace represented as numpy.ndarray
    """
    dim_ary = [elements for x in range(0, dimensions)]
    # generate hyperspace such that weights are all >= 1 and then the admissibility of the heuristic is always given.
    hyperspace = np.random.random_sample(tuple(dim_ary))*100
    return hyperspace


def distance(p1: np.ndarray, p2: np.ndarray, metric_name='euclidean') -> float:
    """
    :param p1: First point as numpy.ndarray
    :param p2: Second point as numpy.ndarray
    :param metric_name: Name of the distance metric
    :return: Distance between p1 and p2 as float according to the chosen metric
    """
    if metric_name == 'euclidean':
        sum_sq = np.sum(np.square(p1 - p2))
        return np.sqrt(sum_sq)
    elif metric_name == 'manhattan':
        return np.sum(np.abs(np.subtract(p1, p2)))
    else:
        raise Exception('This metric has not been implemented yet.')


def describe_ndarray(ndarray: np.ndarray) -> Tuple[int, int]:
    """
    :param ndarray: Any numpy.ndarray
    :return: Tuple with the number of dimensions as first and the extent of each dimension as second parameter.
             Assumes equal extent in each dimension of the input numpy.ndarray.
    """
    # get dimensions of the hyperspace
    dimensions = len(np.shape(ndarray))
    # extent in each dimension
    hyperspace_shape = np.shape(ndarray)
    # assuming equal extent in each dimension
    assert np.all(
        np.asarray(hyperspace_shape, int) == hyperspace_shape[0]), 'Assumes equal extent of each dimension'
    # extent
    extent = hyperspace_shape[0]
    return dimensions, extent

