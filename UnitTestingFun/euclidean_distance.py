import math

def compute_euclidean_distance(v1, v2):
    sum_squares = sum([(v1[i] - v2[i]) ** 2 for i in range(len(v1))])
    return math.sqrt(sum_squares)