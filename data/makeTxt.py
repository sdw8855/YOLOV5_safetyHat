"""
    位置：放置在yolov5/data文件夹下
    功能：将Annotations文件夹下的xml文件划分成【train、testval、test、val】数据集，保存到ImageSets文件夹下，供voc_label.py临时过渡用
    参数：设置testval_percent和test_percent可改变划分比例
"""

import os
import random
testval_percent = 0.1
test_percent = 0.9
xmlfilepath = 'Annotations'
if not os.path.exists('ImageSets'):
    os.makedirs('ImageSets')
total_xml = os.listdir(xmlfilepath)
num = len(total_xml)
list = range(num)
tv = int(num * testval_percent)
te = int(tv * test_percent)
testval = random.sample(list, tv)
test = random.sample(testval, te)
ftestval = open('ImageSets/testval.txt', 'w')
ftest = open('ImageSets/test.txt', 'w')
ftrain = open('ImageSets/train.txt', 'w')
fval = open('ImageSets/val.txt', 'w')
for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in testval:
        ftestval.write(name)
        if i in test:
            ftest.write(name)
        else:
            fval.write(name)
    else:
        ftrain.write(name)
ftestval.close()
ftrain.close()
fval.close()
ftest.close()