"""
    位置：放置在yolov5/data文件夹下
    功能：依次读取ImageSets中划分的train、test、val里的文件名，再从Annotations中找到该文件，提取信息保存到labels下的同文件名的txt；
         同时在data下生成对应train、test、val的txt文件，里面分别保存的为完整图片路径（data/images/%s.jpg）
    参数：标准sets应该不需要修改，只需要根据实际情况依次在classes中写入标签（这个顺序十分重要，需要与data下配置文件yaml的names相对应）
"""

import xml.etree.ElementTree as ET
import os
from os import getcwd
sets = ['train', 'test', 'val']
classes = ["hat", "person"]


def convert(size, box):
    dw = 1. / size[0]   # 图片归一化的单位比例
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0     # 框中心点x
    y = (box[2] + box[3]) / 2.0     # 框中心点y
    w = box[1] - box[0]             # 框宽度w
    h = box[3] - box[2]             # 框高度h
    # 将图片中框的尺寸按图片大小归一化到0~1
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return x, y, w, h


def convert_annotation(image_id):
    in_file = open('Annotations/%s.xml' % (image_id))
    out_file = open('labels/%s.txt' % (image_id), 'w')
    try:
        tree = ET.parse(in_file)
    except Exception as e:
        in_file = open('Annotations/%s.xml' % (image_id), encoding='utf-8') # 有部分xml编码不统一为'gbk'，根据情况设置
        tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        print(str(cls_id) + " " + " ".join([str(a) for a in bb]))
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


wd = getcwd()
print(wd)
for image_set in sets:
    if not os.path.exists('labels/'):
        os.makedirs('labels/')
    image_ids = open('ImageSets/%s.txt' % (image_set)).read().strip().split()
    list_file = open('%s.txt' % (image_set), 'w')
    for image_id in image_ids:
        list_file.write('data/images/%s.jpg\n' % (image_id))
        convert_annotation(image_id)
    list_file.close()