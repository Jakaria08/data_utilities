import wv_util as wv
import matplotlib.pyplot as plt
import numpy as np
import csv
import glob
import os
from PIL import Image

images = list(sorted(glob.glob("/home/jakaria/Super_Resolution/Datasets/xView/train_images/*.tif")))

labels = {}
labels_one_sixty = {}
k = 1
with open('xview_class_labels.txt') as f:
    for row in csv.reader(f):
        labels[int(row[0].split(":")[0])] = row[0].split(":")[1]
        labels_one_sixty[int(row[0].split(":")[0])] = k
        k = k + 1

    labels_one_sixty[75] = k
    labels_one_sixty[82] = k + 1

coords, chips, classes = wv.get_labels('../xView_train.geojson')
coords_chip = []
classes_chip = []
i = 0

for image in images[:200]:
    img = wv.get_image(image)
    coords_chip.append(coords[chips==os.path.basename(image)])
    classes_chip.append(classes[chips==os.path.basename(image)])

    c_img, c_box, c_cls = wv.chip_image(img=img, coords=coords_chip[i], classes=classes_chip[i],
                            shape=(256,256))

    for j in range(c_img.shape[0]):
        im = Image.fromarray(c_img[j])
        if c_cls[j][0] == 0:
            im.save(os.path.join("/home/jakaria/Super_Resolution/Datasets/xView/empty_chip_train_images/",
                                    os.path.splitext(os.path.basename(image))[0]+"_"+str(j)+".png"))
            new_cls_box = np.c_[ c_cls[j], c_box[j]]
            new_cls_box = np.matrix(new_cls_box)
            np.savetxt(os.path.join("/home/jakaria/Super_Resolution/Datasets/xView/empty_chip_train_images/",
                                    os.path.splitext(os.path.basename(image))[0]+"_"+str(j)+".txt"), new_cls_box, fmt='%i')
        else:
            im.save(os.path.join("/home/jakaria/Super_Resolution/Datasets/xView/chip_train_images/",
                                    os.path.splitext(os.path.basename(image))[0]+"_"+str(j)+".png"))
            c_cls[j] = [labels_one_sixty[int(m)] for m in c_cls[j]]
            new_cls_box = np.c_[ c_cls[j], c_box[j]]
            new_cls_box = np.matrix(new_cls_box)
            np.savetxt(os.path.join("/home/jakaria/Super_Resolution/Datasets/xView/chip_train_images/",
                                    os.path.splitext(os.path.basename(image))[0]+"_"+str(j)+".txt"), new_cls_box, fmt='%i')

    i = i + 1
    print(i)
