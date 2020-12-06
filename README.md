# YOLOV5_safetyHat
检查人员是否正确佩戴安全帽



### 项目使用说明：

##### 1：首先克隆仓库

```
git clone https://github.com/daihuidai/YOLOV5_safetyHat.git
```

##### 2：下载本项目数据集

数据集压缩包在Release中：地址

##### 3：导入数据集

将压缩包解压后的`Annotations` 文件夹放入`/data`目录下, 解压后的`JPEGImages`文件夹重命名为`images`后放入`/data`下

##### 4：预处理数据集

先运行`data/makeTxt.py`生成包含数据划分的`ImageSets`文件夹；接着再运行`data/voc_label.py`生成转化 XML 后的`labels`文件夹，以及生成`data`文件夹下包含数据完整路径的 train.txt、test.txt、val.txt 文件。

##### 5：训练数据集

1：可以在命令行通过 python 调用 train.py 执行；2：可以直接在编译器中运行 train.py。完成训练后会在根目录下生成 `runs/train/exp` 目录，里面包含每次的训练结果以及模型。

##### 6：检测数据集

> 在 data/detectImg 中放入待检测的图片

1：可以在命令行通过 python 调用 detect.py 执行；2：可以直接在编译器中运行 detect.py。完成检测后会在根目录下生成 `runs/detect/exp` 目录，里面包含每次的训练结果图片。









