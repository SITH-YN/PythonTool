# -*- coding: utf-8 -*-
"""sample."""

# Standard Library
# import csv
# import os
# import shutil
# import tkinter

# 3rd Party Library

# Global Variable

# Global Constant Define


# def main():
#     """sample."""

#     # Refer Global Variable

#     # Local Variable
#     x = 0
#     y = 0
#     sum = 0

#     # Local Constant Define

#     x = 10
#     y = 20
#     sum = func_sum(x, y)
#     print(sum)


def func_sum(x, y):
    """
    func_sum.

    pramaeters
    --------------------
    arg1:int
    arg2:int
    --------------------

    return
    --------------------
    result:sum
    --------------------

    Examples
    --------------------
    >>> func_sum(10, 20)
    30
    """

    # Refer Global Variable

    # Local Variable
    sum = 0

    # Local Constant Define

    sum = x + y
    return sum


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # main()
