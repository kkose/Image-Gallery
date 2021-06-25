# importing Image class from PIL package  
from PIL import Image 
import glob
import os,sys
import argparse
from tqdm import tqdm 

parser = argparse.ArgumentParser(description='Created Thumbnails from the images in a given folder')
parser.add_argument('--direc', default='./images', type=str,
                    help='Directory where the files reside')
args = parser.parse_args()

imageFolder = args.direc
if not os.path.exists(args.direc):
	print('Target Folder does not exists. !!!!!! Terminating !!!!!')
	sys.exit()

flist_Set1 = glob.glob(os.path.join(imageFolder,'*.jpg'))

# Create output folder -if necessary-
if not os.path.exists(os.path.join(imageFolder,'thumbnails')):
    os.makedirs(os.path.join(imageFolder,'thumbnails'))

# creating a object  
MAX_SIZE = (200, 200) 
  
print('There are %i files that needs to be processed'%(len(flist_Set1)))
for i,fname in tqdm(enumerate(flist_Set1)):
    tmp = Image.open(fname)
    tmp.thumbnail(MAX_SIZE) 
    _,fileName = os.path.split(fname)
    tmp.save(os.path.join(imageFolder,'thumbnails',fileName))
