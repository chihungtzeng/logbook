#!/usr/bin/python
"""
Demonstrate how to use SVD to generate a similiar matrix. See LSI paper
(Using latent semantic analysis to improve access to textual information)
for a possible application.
"""
from __future__ import print_function
import numpy


def main():
    m = numpy.array([[2, 7, 8], [3, 9, 9], [5, 1, 0], [3, 3, 2], [7, 2, 9]])
    print("original matrix:")
    print(m)
    u, sigma, vt = numpy.linalg.svd(m, full_matrices=False)

    print("sigma shape: {}".format(sigma.shape))

    # Keep 2 largest singular values by setting others to 0
    sigma[2:] = 0
    approx_m = numpy.dot(u, numpy.dot(numpy.diag(sigma), vt))
    print("approximate matrix:")
    print(approx_m)

if __name__ == "__main__":
    main()
