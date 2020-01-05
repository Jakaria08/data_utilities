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

    keys = list(Counter(labels).keys())
    values = list(Counter(labels).values())
    print(keys)
    print(values)
    print(len(values))

    low_freq_labels = [keys[i] for i in range(len(values)) if values[i]<100]
    low_freq = [values[i] for i in range(len(values)) if values[i]<100]
    print(low_freq_labels)
    print(low_freq)
        #delete low freqency labels
        '''
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
        '''
def train_test_split():
    shuffle(annotation)
    for i in range(len(annotation)*0.2):
        pass

print_labels()
