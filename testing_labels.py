from __future__ import print_function, division
import os
import glob
from collections import Counter
from shutil import move
from random import shuffle

train_path = "/home/jakaria/Super_Resolution/Datasets/xView/chip_train_images/"
test_path = "/home/jakaria/Super_Resolution/Datasets/xView/chip_test_images/"
annotation = list(sorted(glob.glob(train_path+"*.txt")))

#print(len(annotation))
#print(annotation[0])
labels = list()
labels_new = list()

def print_labels():
    # delete files with small annotation
    for i in range(int(len(annotation))):
        annotation_source_path = os.path.join(root, annotation[i])
        image_source_path = os.path.splitext(annotation_source_path)[0]+".png"
        j = 0
        with open(annotation_source_path) as f:
            for line in f:
                values = (line.split())
                if "\ufeff" in values[0]:
                  values[0] = values[0][-1]
                #get coordinates withing height width range
                '''
                x = float(values[1])*self.image_width
                y = float(values[2])*self.image_height
                width = float(values[3])*self.image_width
                height = float(values[4])*self.image_height
                '''
                #creating bounding boxes that would not touch the image edges
                x_min = 1 if int(values[1]) <= 0 else int(values[1])
                y_min = 1 if int(values[2]) <= 0 else int(values[2])
                x_max = 255 if int(values[3]) >= 256 else int(values[3])
                y_max = 255 if int(values[4]) >= 256 else int(values[4])

                if x_max - x_min < 3 or y_max - y_min < 3:
                    continue
                else:
                    j = j+1

        if j == 0:
            os.remove(annotation_source_path)
            os.remove(image_source_path)
            print("files removed..")


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
    shuffle(annotation)
    print(int(len(annotation)*0.2))
    for i in range(int(len(annotation)*0.2)):
        annotation_source_path = os.path.join(root, annotation[i])
        annotation_destination_path = os.path.join(test_path, os.path.basename(annotation[i]))
        image_source_path = os.path.splitext(annotation_source_path)[0]+".png"
        image_destination_path = os.path.splitext(annotation_destination_path)[0]+".png"
        move(annotation_source_path, annotation_destination_path)
        move(image_source_path, image_destination_path)
        if i%100 == 0:
            print(i)
            print(root)
            print(test_path)
            print(annotation[i])
            print(annotation_source_path)
            print(annotation_destination_path)
            print(image_source_path)
            print(image_destination_path)


def change_labels():
    # change labels 0 to n-1;
    for i in range(len(annotation)):
        annotation_path = os.path.join(train_path, annotation[i])
        if i%1000 == 0:
            print(i)
        with open(annotation_path) as f:
            for line in f:
                values = (line.split())
                if "\ufeff" in values[0]:
                    values[0] = values[0][-1]
                obj_class = int(values[0])
                labels.append(obj_class)

    keys = sorted(list(Counter(labels).keys()))
    #values = list(Counter(labels).values())
    print(keys)
    #print(values)
    print(len(keys))

    with open('labels_from_one_to_sixty.txt', 'w') as f:
        for item in keys:
            f.write("%s\n" % item)

#train_test_split()
#print_labels()
change_labels()
