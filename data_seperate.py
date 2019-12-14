import os
from shutil import copyfile

'''
The Fog dataset downloaded from https://www.cityscapes-dataset.com/downloads/ have 3 intensities of fog images.

This script will seperate the fog dataset into three dataset based on the intensity of fog

Please make sure cityperson fog validation dataset is copied to project directory

it should be like /leftImg8bit_foggyDBF/val/frankfurt , /leftImg8bit_foggyDBF/val/lindau , /leftImg8bit_foggyDBF/val/munster

It will create three folder with name val1,val2,val3 which is for fog intensity  medium,high and low.
'''


def serperare_date():
    dirr = os.listdir('./leftImg8bit_foggyDBF/val/')
    if not os.path.exists('./leftImg8bit_foggyDBF/val1'):
        os.mkdir('./leftImg8bit_foggyDBF/val1/')
        os.mkdir('./leftImg8bit_foggyDBF/val2/')
        os.mkdir('./leftImg8bit_foggyDBF/val3/')
    for folder in dirr:
        if not os.path.exists('./leftImg8bit_foggyDBF/val1/' + folder + '/'):
            os.mkdir('./leftImg8bit_foggyDBF/val1/' + folder + '/')
        if not os.path.exists('./leftImg8bit_foggyDBF/val2/' + folder + '/'):
            os.mkdir('./leftImg8bit_foggyDBF/val2/' + folder + '/')
        if not os.path.exists('./leftImg8bit_foggyDBF/val3/' + folder + '/'):
            os.mkdir('./leftImg8bit_foggyDBF/val3/' + folder + '/')
        for image in os.listdir('./leftImg8bit_foggyDBF/val/'+folder):
            imagename = image.split("_foggy")[0]
            imagename += ".png"

            if "beta_0.01" in image:
                copyfile('./leftImg8bit_foggyDBF/val/'+folder+'/'+image,'./leftImg8bit_foggyDBF/val1/'+folder+'/'+imagename)
            elif "beta_0.02" in image:
                copyfile('./leftImg8bit_foggyDBF/val/' +folder+'/' + image, './leftImg8bit_foggyDBF/val2/'+folder+'/'+imagename)
            elif "beta_0.005" in image:
                copyfile('./leftImg8bit_foggyDBF/val/' +folder+'/' + image, './leftImg8bit_foggyDBF/val3/'+folder+'/'+imagename)


# serperare_date()

def rename_data():
    for i in ['val1','val2','val3']:
        path = './leftImg8bit_foggyDBF/'+i+'/'
        dirr = './leftImg8bit_foggyDBF/'+i+'/'
        for folder in os.listdir(dirr):
            for image in os.listdir(dirr+folder+"/"):
                imagename = imagename = image.split("_.")[0]
                imagename += ".png"
                os.rename(dirr+folder+'/'+image, dirr+folder+'/'+imagename)

rename_data()

