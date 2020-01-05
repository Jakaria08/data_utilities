from __future__ import print_function, division
import os
import glob
from collections import Counter
from shutil import move
from random import shuffle

root = "/home/jakaria/Super_Resolution/Datasets/xView/chip_train_images/"
annotation = list(sorted(glob.glob(root+"*.txt")))

print(len(annotation))
labels = list()

def print_labels():
    for i in range(len(annotation)):
        annotation_path = os.path.join(root, annotation[i])
        if i%1000 == 0:
            print(i)
        with open(annotation_path) as f:
            for line in f:
                values = (line.split())
                if "\ufeff" in values[0]:
                    values[0] = values[0][-1]
                obj_class = int(values[0])
                labels.append(obj_class)

    print(list(Counter(labels).keys()))
    print(list(Counter(labels).values()))
    print(len(Counter(labels).values()))

def train_test_split():
    shuffle(annotation)
    for in range(len(annotation)*0.2)

print_labels()
