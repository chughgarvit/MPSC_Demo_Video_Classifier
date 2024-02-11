
# Import libraries 
import os
import torch 
import pickle 
import matplotlib.pyplot as plt
import  time
import glob
from scipy.io import loadmat
import random
from random import seed, randint
from sklearn.model_selection import train_test_split
import pandas as pd
import sys
from queue import Queue
import numpy as np


def get_files(path_dir = "/Users/garvitchugh/Downloads/DEMO_Test_Run/Data/Pickle_files"):
    dataPath = os.path.join(path_dir, "*.pkl")
    return glob.glob(dataPath)  # care about the serialization


files = get_files(path_dir = "/Users/garvitchugh/Downloads/DEMO_Test_Run/Data/Pickle_files")

print(files)