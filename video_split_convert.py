import numpy as np
import json

from os import listdir
from os.path import isfile, join


def convert(shape, coords):
    coords[2] -= coords[0]
    coords[3] -= coords[1]
    x_diff = int(coords[2]/2)
    y_diff = int(coords[3]/2)
    coords[0] = coords[0]+x_diff
    coords[1] = coords[1]+y_diff
    coords[0] /= int(shape[1])
    coords[1] /= int(shape[0])
    coords[2] /= int(shape[1])
    coords[3] /= int(shape[0])
    return coords


def main():
    mypath = './ann/'
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    index = 0
    for file in onlyfiles:
        with open(mypath + file) as f:
            data = json.load(f)
            width = data['size']['width']
            height = data['size']['height']
            f_txt = open("img/frame_" + str(index).zfill(5) + ".txt", 'w')
            for object in data['objects']:
                labels = object['points']['exterior']
                coords = np.asarray([float(labels[0][0]), float(
                    labels[0][1]), float(labels[1][0]), float(labels[1][1])])
                box = convert(shape=[height, width], coords=coords)
                strs = str(box[0]) + " " + str(box[1]) + " " + \
                    str(box[2]) + " " + str(box[3])
                print("0", strs, file=f_txt)
            f_txt.close()
            index += 30

    return 0


if __name__ == "__main__":
    main()
