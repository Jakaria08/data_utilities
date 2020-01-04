from __future__ import print_function, division
import os
import glob
from collections import Counter

root = "/home/jakaria/Super_Resolution/Datasets/xView/chip_train_images/"
annotation = list(sorted(glob.glob(root+"*.txt")))

print(len(annotation))
for i in range(len(annotation)):
    annotation_path = os.path.join(root, annotation[i])
    if(i%1000):
        print(i)
    labels = list()
    with open(annotation_path) as f:
        for line in f:
            values = (line.split())
            if "\ufeff" in values[0]:
                values[0] = values[0][-1]
            obj_class = int(values[0])
            labels.append(obj_class)

print(Counter(labels).keys())
print(Counter(labels).values())
print(len(Counter(labels).values()))
