from __future__ import print_function, division
import os
import glob
from collections import Counter
from shutil import move
from random import shuffle

root = "/home/jakaria/Super_Resolution/Datasets/xView/chip_train_images/"
test_path = "/home/jakaria/Super_Resolution/Datasets/xView/chip_test_images/"
annotation = list(sorted(glob.glob(root+"*.txt")))

print(len(annotation))
print(annotation[0])
labels = list()
labels_new = list()

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
    '''
    low_freq_labels = [keys[i] for i in range(len(values)) if values[i]<100]
    low_freq = [values[i] for i in range(len(values)) if values[i]<100]
    print(low_freq_labels)
    print(low_freq)

    #delete low freqency labels

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
                if any(j==obj_class for j in low_freq_labels):
                    file_path = os.path.splitext(annotation_path)[0]+".png"
                    f.close()
                    os.remove(annotation_path)
                    os.remove(file_path)
                    break
    '''
def train_test_split():
    annotation_shuffled = shuffle(annotation)
    print(int(len(annotation)*0.65))
    print(annotation[0])
    for i in range(int(len(annotation_shuffled)*0.6)):
        if i%1000 == 0:
            print(i)
        annotation_source_path = os.path.join(root, annotation_shuffled[i])
        annotation_destination_path = os.path.join(test_path, annotation_shuffled[i])
        image_source_path = os.path.splitext(annotation_source_path)[0]+".png"
        image_destination_path = os.path.splitext(annotation_destination_path)[0]+".png"
        os.remove(annotation_source_path)
        os.remove(image_source_path)

train_test_split()
