#!/usr/bin/env python
# coding: utf-8


import os
dd=os.listdir('TIN')
f1 = open('train.txt', 'w')
f2 = open('test.txt', 'w')
for i in range(len(dd)):
    d2 = os.listdir ('TIN/%s/images/'%(dd[i]))
    for j in range(len(d2)-2):
        str1='TIN/%s/images/%s'%(dd[i], d2[j])
        f1.write("%s %d\n" % (str1, i))
    str1='TIN/%s/images/%s'%(dd[i], d2[-1])
    f2.write("%s %d\n" % (str1, i))

f1.close()
f2.close()


import cv2 
import numpy as np
from numpy import linalg as LA

def load_img(f):
    f=open(f)
    lines=f.readlines()
    imgs, lab=[], []
    print("loading images\n")
    for i in range(len(lines)):
        fn, label = lines[i].split(' ')
        
        im1=cv2.imread(fn)
        im1=cv2.resize(im1, (128,128))
        im1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
        
        
        vec = np.reshape(im1, [-1])
        imgs.append(vec) 
        lab.append(int(label))
    imgs= np.asarray(imgs, np.float32)
    lab= np.asarray(lab, np.int32)
    return imgs, lab 


x, y = load_img('train.txt')
tx, ty = load_img('test.txt')



#======================================
#X就是資料，Y是Label，請設計不同分類器來得到最高效能
#必須要計算出分類的正確率
#======================================


