### Helper_Computer_Vision_Project

##This porject is a helper project of my computer vision project which add snow and fog to the cityperson dataset

#File data_augumentation will add snow and fog to the dataset.
Please make sure cityperson validation dataset is copied to /images/val/

it should be like /images/val/frankfurt , /images/val/lindau , /images/val/munster

It will output augument dataset in /images/results/

#File data_seperate will fog dataset downloaded from site https://www.cityscapes-dataset.com/downloads/, this script will divide the dataset into 3 dataset(low, medium, high) based on intensity of fog


The Fog dataset downloaded from https://www.cityscapes-dataset.com/downloads/ have 3 intensities of fog images.

This script will seperate the fog dataset into three dataset based on the intensity of fog

Please make sure cityperson fog validation dataset is copied to project directory

it should be like /leftImg8bit_foggyDBF/val/frankfurt , /leftImg8bit_foggyDBF/val/lindau , /leftImg8bit_foggyDBF/val/munster

It will create three folder with name val1,val2,val3 which is for fog intensity  medium,high and low.

