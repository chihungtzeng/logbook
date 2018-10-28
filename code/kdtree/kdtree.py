# -*- coding: utf-8 -*-
import numpy as np
from scipy.spatial import KDTree

POINTS = [[2, 0], [3, 7], [-3, -5]]

def main():
    ars = np.array(POINTS)
    tree = KDTree(ars)
    print(tree.data)
    query_points = np.array([[4, 2], [-2, 8], [-3, -9], [5, -1]])
    ret = tree.query(query_points)
    print(ret)
    for i in range(query_points.shape[0]):
        dist = ret[0][i]
        nearest_point_index = ret[1][i]
        print("Query point: {}, nearest neighbor: {}, dist: {}".format(
            query_points[i], tree.data[nearest_point_index], dist))

if __name__ == "__main__":
    main()
