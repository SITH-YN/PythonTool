# -*- coding: utf-8 -*-
"""sample."""

# Standard Library
# import csv
# import os
# import shutil
# import tkinter

# 3rd Party Library
import pytest
import sample

# Global Variable

# Global Constant Define


@pytest.mark.parametrize(("x", "y", "expected"), [
    (10, 20, 30),
    (20, 40, 60),
])
def test_func_sum(x, y, expected):
    assert sample.func_sum(x, y) == expected
