print("hello from main.py--1... __name__:", __name__)
import hello_world
# hello_world will not print because in 
# hello_world.py __name__ is "hello_world"
# not "__main__"
print("hello from main.py--2")

# import utils_folder.utils
# utils_folder.utils.do_something_important()

# import utils_folder.utils as utils
# utils.do_something_important()
# examples of this:
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

from utils_folder.utils import do_something_important
do_something_important()