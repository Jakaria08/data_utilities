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

coords, chips, classes = wv.get_labels('../xView_train.geojson')
coords_chip = []
classes_chip = []
i = 0

for image in images[:20]:
    img = wv.get_image(image)
    coords_chip.append(coords[chips==os.path.basename(image)])
    classes_chip.append(classes[chips==os.path.basename(image)])

    c_img, c_box, c_cls = wv.chip_image(img=img, coords=coords_chip[i], classes=classes_chip[i],
                            shape=(256,256))

    print(np.unique(classes_chip[i]))
    i = i + 1
