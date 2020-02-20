

# loop all images, find max width
# vertically concat images

# pip install opencv-python

import cv2
import os

rootdir = ''
save_as = 'merge.jpg'

#
# param: whitelist
#
file_ext_whitelist = ['.jpg']

#
# param: 縮細
#
scale_ratio = 50 # 50%

#
# param: crop 圖
#
# (y1,y2) = (340,1575)
# (x1,x2) = (450,2090)
(x1, x2) = (360, 2520)
(y1, y2) = (94, 1714)

def concat_img_with_min(im_list, interpolation=cv2.INTER_CUBIC):
    w_min = min(im.shape[1] for im in im_list)
    im_list_resize = [cv2.resize(im, (w_min, int(im.shape[0] * w_min / im.shape[1])), interpolation=interpolation) for im in im_list]
    return cv2.vconcat(im_list_resize)

def resize_img(img):
    global scale_ratio
    scale_percent = scale_ratio # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    return resized

lst = []

for subdir, dirs, files in os.walk(rootdir):
    for file in sorted(files):
        filename, file_extension = os.path.splitext(file)
        if ( len(file_ext_whitelist) == 0 or (file_extension in file_ext_whitelist)):
            oldfile_name = subdir + '/' + file
            print(oldfile_name)
            img = cv2.imread(oldfile_name)
            crop_img = resize_img(img[y1:y2, x1:x2])
            constant= cv2.copyMakeBorder(crop_img, 10, 10, 0, 0, cv2.BORDER_CONSTANT, value = (0,0,0))
            lst.append(constant)

im_v = concat_img_with_min(lst)
cv2.imwrite(rootdir + save_as, im_v)
