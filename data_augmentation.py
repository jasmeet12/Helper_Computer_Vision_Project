#!/usr/bin/env python
# coding: utf-8

# In[4]:


'''
This script will add rain and fog to the dataset

Please make sure cityperson validation dataset is copied to /images/val/

it should be like /images/val/frankfurt , /images/val/lindau , /images/val/munster

It will create dataset in /images/results/
'''

import os
import cv2
import imageio
import imgaug as ia
from imgaug import augmenters as iaa







# In[33]:

directory = "./images/val/"
dir_res = "./images/results/"
if not os.path.exists(directory):
    os.makedirs(directory)
if not os.path.exists(dir_res):
    os.makedirs(dir_res)

images = os.listdir(directory)



# In[35]:





def save_aug_file(seq:iaa.Sequential, pathstr:str):
    for dirr in os.listdir(directory):
        for image in os.listdir(directory + dirr):
            imgname1 = directory + dirr+"/"+image
            img = cv2.imread(imgname1)
            img_aug = seq.augment_image(img)
            path = dir_res + pathstr+"/"+dirr+"/"
            pathname = os.makedirs(path, exist_ok=True)
            cv2.imwrite(path+image, img_aug)




seq = iaa.Sequential([iaa.Snowflakes(flake_size=(0.7, 0.95), speed=(0.001, 0.03))])
save_aug_file(seq,"demoSnow")

# seq = iaa.Sequential([iaa.FastSnowyLandscape(lightness_threshold=(50, 195), lightness_multiplier=(3.0, 4.0))])
# save_aug_file(seq,"demoSnowLand")


# In[43]:

seq = iaa.Sequential([iaa.Clouds()])
save_aug_file(seq,"demoClouds")





# seq = iaa.Sequential([iaa.Fog()])
# save_aug_file(seq,"demoFog")



# In[ ]:




