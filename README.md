# YOLOV5_safetyHat
检查人员是否正确佩戴安全帽



### 项目使用说明：

> 项目使用分为 6 个步骤

##### 1：首先克隆仓库

```
git clone https://github.com/daihuidai/YOLOV5_safetyHat.git
```

##### 2：下载本项目数据集

数据集 VOC2028 压缩包在Release中：[地址](https://github.com/daihuidai/YOLOV5_safetyHat/releases)

##### 3：导入数据集

将压缩包解压后的`Annotations` 文件夹放入`/data`目录下, 解压后的`JPEGImages`文件夹重命名为`images`后放入`/data`下

##### 4：预处理数据集

先运行`data/makeTxt.py`生成包含数据划分的`ImageSets`文件夹；接着再运行`data/voc_label.py`生成转化 XML 后的`labels`文件夹，以及生成`data`文件夹下包含数据完整路径的 train.txt、test.txt、val.txt 文件。

##### 5：训练数据集

1：可以在命令行通过 python 调用 train.py 执行；2：可以直接在编译器中运行 train.py。完成训练后会在根目录下生成 `runs/train/exp` 目录，里面包含每次的训练结果以及模型。

##### 6：检测数据集

> 在 data/detectImg 中放入待检测的图片

1：可以在命令行通过 python 调用 detect.py 执行；2：可以直接在编译器中运行 detect.py。完成检测后会在根目录下生成 `runs/detect/exp` 目录，里面包含每次的训练结果图片。



### 扩展使用说明：

> 扩展使用说明包括：更换预训练模型、添加数据集、训练新数据集。（配置文件中路径都以YOLOV5_safetyHat作为根目录）

##### 1：更换预训练模型

本项目中使用的预训练模型为官方提供的 yolov5m.pt 来训练数据集，另外三种模型分别为：yolov5l.pt、yolov5s.pt、yolov5x.pt。可以更换预训练模型来训练数据集。

**一：下载对应的模型**

下载地址：[地址](https://github.com/daihuidai/YOLOV5_safetyHat/releases)

**二：将模型放入`weights`文件夹下（实际上可以放入任何位置，只需要做相应的路径更改）**

**三：更改 train.py 下预训练模型的路径以及对应模型cfg配置文件的对应位置**

--weights 参数的 default 更改为：例如 weights/yolov5m.pt（使用命令行运行则直接 --weights 指定即可）

--cfg 参数的 default 更改为：例如对应的 models/yolov5m.yaml（使用命令行运行则直接 --cfg 指定即可）

**强调一点：**cfg 官方默认的 4 个 yaml 文件的配置为 coco 数据集的 80 个识别类别。如果你更换了预训练模型，yaml 里面的参数`nc`也需要修改为对应你自己项目的类别个数，例如本项目中 `nc: 2`。

**四：命令行或者直接运行 train.py 训练**



##### 2：添加数据集

> 可以根据需求添加自己标注的数据，添加的数据集必须满足本项目 VOC2028 中数据集的格式

**一：利用标注工具，比如：lableImg、labelme 等，可以标注自己的 VOC 数据集。**

**二：将标注后的 Annotations 中的 XML 文件复制到 `data/Annotations` 文件中，将 Images 中的原图片复制到 `data/images` 文件中。**

**三：依次运行 makeTxt.py 和 voc_label.py 得到训练数据**



**3：训练新数据集**

> 如果需要根据新场景训练新的检测目标模型，则需要更改训练数据集

**一：准备好新场景的 VOC 格式的数据集（通过标注工具或其它方式下载）**

**二：将新数据的 Annotations 文件放置到（替换） data 下，Images 中的原图片放置到（替换）data/images 下**

**三：首先运行 makeTxt.py 生成`ImageSets`下的划分数据文件，再修改 voc_label.py 文件的参数后再运行生成训练数据信息**

voc_label.py 中需要修改对应新数据的信息，以保证给后面模型训练的数据相对应。修改`classes = ["hat", "person"]`后的列表标签信息为新数据集中的标签信息，也就是标注时每个检测物的名字。（**！！这个classes还要用到**）

**四：修改 data/hatPerson.yaml 文件**

因为更换了新数据，所以需要更改项目中关于数据配置的信息。这里你可以新建一个 yaml，也可以直接在里面修改。

```python
train: ./data/train.txt	# 如果没做其它修改，这三个地址不变
val: ./data/val.txt
test: ./data/test.txt 

nc: 2	# 修改，检测目标数量，也就是classes的列表长度

names: ["hat", "person"]	# 修改，和voc_label.py中classes的列表信息一致
```

**五：修改你使用预训练模型所对应的 models 下的 yaml 文件**

同样，将 `nc: 2` 修改为新数据需要检测的类别数量（也就是第三步中 classes 的长度）

**六：非命令行使用时，修改 train.py 的配置文件**

--weights ：改为你使用的预训练模型路径，例如：weights/yolov5m.pt

--cfg ：改为你使用的预训练模型所对应的配置文件，例如：models/yolov5m.yaml

--data ：改为第四步中得到的项目使用数据配置文件，例如：data/hatPerson.yaml

**七：命令行或直接运行 train.py 开始训练**



### 项目优化说明：

本项目中默认 train.py 使用的 `epochs=10`，`batch-size=2`，`img-size=[640, 640]`，默认 detect.py 使用的 `img-size=[640, 640]`。所以可以根据实际情况来对你的场景做相应的修改。













