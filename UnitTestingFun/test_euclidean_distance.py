# using testing frameworks can make executing unit tests
# nice and easy!
# we will use pytest unit testing framework

# with pytest, modules and functions for testing start with
# test_
import numpy as np
from scipy.spatial.distance import euclidean
from euclidean_distance import compute_euclidean_distance

def test_compute_euclidean_distance():
    point1 = (-2, -2)
    point2 = (2, 6)
    distance_solution = 8.94

    distance = compute_euclidean_distance(point1, point2)
    # assert statement order: actual (was produced)
    # vs expected (solution)
    # assert distance == distance_solution # TODO: compare
    # floats in a "better" way
    # use numpy's isclose() function to assert
    # the two values are "close" (enough)
    assert np.isclose(distance, distance_solution, rtol=0.001)

    # the above test case was a "desk calculation"
    # we can also test against a validated library implementation
    # SciPy has a euclidean distance function that is tested and correct!
    # make up some more complicated test data
    np.random.seed(0) # for reproducible results
    v1 = np.random.random(10)
    v2 = np.random.random(10)
    distance_solution = euclidean(v1, v2)
    distance = compute_euclidean_distance(v1, v2)
    assert np.isclose(distance, distance_solution)

    # TODO: come up with additional test cases
    # perhaps vary the length of v1/v2 --> e.g. 1000
    # perhaps think of edge cases