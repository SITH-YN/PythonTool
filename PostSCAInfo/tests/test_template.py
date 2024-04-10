# -*- coding: utf-8 -*-
"""test_template."""

# Standard Library
import csv
import datetime
import glob
import os
import shutil
import time
import tkinter

# 3rd Party Library
import bs4
import dash
import dash_daq
import json
import numpy as np
import openpyxl
import pandas as pd
import plotly
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pytest
import webbrowser
import win32com.client


# Global Variable

# Global Constant Define


@pytest.mark.parametrize(("expected"), [
    (),
    (),
])
def test_func_template(expected):
    """test_func_template."""

    # Refer Global Variable

    # Local Variable

    # Local Constant Define

    assert template.func_template() == expected
