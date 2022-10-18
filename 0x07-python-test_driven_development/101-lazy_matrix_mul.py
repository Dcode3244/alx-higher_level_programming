#!/usr/bin/python3
"""
module that multiplies matrix
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    a function that multiplies a matrix

    Args:
        m_a (list): a matrix to be multiplied
        m_b (list): a matrix to be multiplied

    """

    return (numpy.matmul(m_a, m_b))
