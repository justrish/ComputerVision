# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 17:23:26 2016

@author: rish
"""

import numpy as np
import matplotlib.pyplot as plt

def plot_confusion_matrix(cm, title='Confusion matrix', cmap=plt.cm.Blues):
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len([0,1,2,3,4,5,6,7,8,9,10,11]))
    plt.xticks(tick_marks, [0,1,2,3,4,5,6,7,8,9,10,11], rotation=45)
    plt.yticks(tick_marks, [0,1,2,3,4,5,6,7,8,9,10,11])
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

print ("bayesian_segnet_camvid")
cm = np.array([[0.5922,    0.2005,    0.0121,    0.0014,    0.0013,   0.1770,    0.0081,    0.0004,    0.0024,   0.0038,   0.0009],
    [0.1210,    0.4606,    0.0240,    0.0103,    0.0477,   0.2224,    0.0114,    0.0321,    0.0407,   0.0268,   0.0030],
    [0.1674,    0.3350,    0.0403,    0.0215,    0.1013,   0.1726,    0.0153,    0.0447,    0.0428,   0.0528,   0.0064],
    [0.0011,    0.0240,    0.0032,    0.7607,    0.1192,   0.0047,    0.0001,    0.0067,    0.0690,   0.0075,   0.0039],
    [0.0010,    0.1012,    0.0121,    0.2029,    0.5380,   0.0120,    0.0004,    0.0298,    0.0658,   0.0301,   0.0068],
    [0.1918,    0.4428,    0.0256,    0.0090,    0.0202,   0.2220,    0.0266,    0.0193,    0.0148,   0.0258,   0.0021],
    [0.1851,    0.4085,    0.0290,    0.0062,    0.0171,   0.2782,    0.0231,    0.0108,    0.0211,   0.0196,   0.0013],
    [0.0112,    0.4212,    0.0382,    0.0505,    0.1260,   0.1133,    0.0036,    0.0545,    0.1200,   0.0554,   0.0061],
    [0.0038,    0.1808,    0.0149,    0.4252,    0.2132,   0.0175,    0.0021,    0.0143,    0.0902,   0.0304,   0.0074],
    [0.0081,    0.3306,    0.0315,    0.0540,    0.2972,   0.0743,    0.0021,    0.0553,    0.0686,   0.0608,   0.0175],
    [0.0052,    0.1462,    0.0238,    0.1480,    0.2783,   0.0545,    0.0001,    0.1892,    0.0506,   0.0568,   0.0472],
])
 

np.set_printoptions(precision=2)
print('Confusion matrix, without normalization')
plt.figure()
plot_confusion_matrix(cm)
