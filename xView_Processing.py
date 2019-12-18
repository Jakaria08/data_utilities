import wv_util as wv
import matplotlib.pyplot as plt
import numpy as np
import csv
import glob
import os

images = list(sorted(glob.glob("/home/jakaria/Super_Resolution/Datasets/xView/train_images/"+"*.tif")))

labels = {}
with open('xview_class_labels.txt') as f:
    for row in csv.reader(f):
        labels[int(row[0].split(":")[0])] = row[0].split(":")[1]

for image in images[:6]:
    #img = wv.get_image(image)
    coords, chips, classes = wv.get_labels('../xView_train.geojson')
    coords = coords[chips==os.path.basename(image)]
    classes = classes[chips==os.path.basename(image)]
    print([labels[i] for i in np.unique(classes)])
