# hw2_VRDL
Street View House Numbers detection
> This is the hw2 of Selected Topics in Visual Recognition using Deep Learning (2021).
> This homework, I use yolov5 to train the model.
## Installation

You can use conda to create a new virtual enrivonment.
And then install the [Pytorch](https://pytorch.org/) from the official webside.


```shell
$ conda create -n hw2 python=3.6
$ git clone 
$ cd hw2_VRDL
$ pip install -r requirements.txt
```

## Data download and Prepare for training 
Please download the data from this [google drive  link](https://drive.google.com/drive/folders/1aRWnNvirWHXXXpPPfcWlHQuzGJdXagoc) and put the folder on below the data/svhn/

There are **33402** images for training.
And there are **13068** image for testing.

And then we need to prepare the labels format for training.
run mat_to_yolo.py
```shell
$ python mat_to_yolo.py
```
After creating the labes for each image, I manual spilt the training data to training and val.
I create a folder called "val", and move the image from 30001 to 33402.

The svhn folder should be like below.
![](https://i.imgur.com/o7Ogz7b.png)

## Train the model
We are ready to train the model 

```shell
$ python train.py --img 640 --batch 32 --epochs 200 --data svhn.yaml --weights yolov5m.pt
```
It will generate the results to runs/train/exp*

## detect test images

The model weight will be store in the exp/weights 

We can run detect.py to produce the results.

```shell
$ python detect.py --source data/svhn/test/ --weights runs/train/exp/weights/best.pt --save-txt --save-conf --img-size 640
```

To reproduce my result.
First download the weight from [google drive link ](https://drive.google.com/file/d/1ri04wi9TbMtEMvZCutzSGIuoJGCRWTsM/view?usp=sharing)

```shell
$ python detect.py --source data/svhn/test/ --weights path-to-file/best.pt --save-txt --save-conf --img-size 640
```

The detect result will be store to runs/detect/exp

## conver the output files to coco formate

Finally we create the results, we need to convert to coco format.
Simply run create_ans.py

Chage the filepath to your folder.
i.e. `filepath = 'runs/detect/exp/labels/'`

```shell
$ python create_ans.py
```

## Run benchmark from colab below

https://colab.research.google.com/drive/1e5-XSSXaHSqCsS_21CTv8O0YyXNy42ie?usp=sharing

## Reference 
- [Yolov5](https://github.com/ultralytics/yolov5) 
- https://github.com/chia56028/Street-View-House-Numbers-Detection