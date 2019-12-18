import wv_util as wv
import matplotlib.pyplot as plt
import numpy as np
import csv
import glob

images = list(sorted(glob.glob("/home/jakaria/Super_Resolution/Datasets/xView/train_images/"+"*.tif")))
print(images)
