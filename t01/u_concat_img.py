

# loop all images, find max width
# vertically concat images

# pip install opencv-python

import cv2
import numpy as np
import os

rootdir = '/Users/maxfan/Desktop/screen_temp/macd/'
save_as = 'vc_macd.jpg'

file_ext_whitelist = ['.jpg']

def vconcat_resize_min(im_list, interpolation=cv2.INTER_CUBIC):
    w_min = min(im.shape[1] for im in im_list)
    im_list_resize = [cv2.resize(im, (w_min, int(im.shape[0] * w_min / im.shape[1])), interpolation=interpolation)
                      for im in im_list]
    return cv2.vconcat(im_list_resize)

lst = []
for subdir, dirs, files in os.walk(rootdir):
    for file in sorted(files):
        filename, file_extension = os.path.splitext(file)
        if ( len(file_ext_whitelist) == 0 or (file_extension in file_ext_whitelist)):
            oldfile_name = subdir + '/' + file
            print(oldfile_name)
            img = cv2.imread(oldfile_name)
            constant= cv2.copyMakeBorder(img, 10, 10, 0, 0, cv2.BORDER_CONSTANT, value = (0,0,0))
            lst.append(constant)

im_v = vconcat_resize_min(lst)
cv2.imwrite(rootdir + save_as, im_v)

