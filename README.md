# vada_pav_classification
It is a binary classification which tells whether the image is having vada pav in it.
Model is build with transfer learning using VGG19 and keras (tensorflow as backend).

## usage 
open vada_pav.ipynb in jupyter notebook

## Data collection

1. Collected the images of vada pav from google and used [Fatkun batch download image](https://chrome.google.com/webstore/detail/fatkun-batch-download-ima/nnjjahlikiabnchcpehcpkdeckfgnohf?hl=en) chrome extension to download images in bulk.
2. For no vada pav collected images of pet, people, furniture, houses and group of people.

 - Copied all the vada pav images in a single folder.
 - Copied all the non vada pav images in another folder.

Renamed the images as 1.png, 2.png....... with the help of rename_images.py.

NOTE :

use the script in the same directory where the fimage folders are present and change the name of folder in the script as required. 

## Image Data Augmentation

Since the collected data is small, augmentation is needed to train the model better.

Image Data Augmentation is done with help [Keras image preprocessing](https://keras.io/preprocessing/image/) and used [flow from directory](https://keras.io/preprocessing/image/#flow_from_directory) to generate the augmented images from the folder.

Keras also provides feature to split the data into training and validation sets with validation_split argument in ImageDataGenerator class that reserves the portion of dataset for validating the model.

## Model Construction flow

Data Collection -> Augmentation -> VGG19 pretrained download -> Exclude fullyconnected layer -> Addition of own fully connected layer -> Model commpile -> Model fit generator -> Plotting accurracy and loss 
