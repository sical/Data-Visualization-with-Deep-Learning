import matplotlib.pyplot as plt
import argparse
import gzip
import os
import sys
import time
import numpy
from sklearn import svm
from sklearn import datasets
import imagePrep as ip
from PIL import Image
import os, os.path 
import glob

IMAGE_SIZE = 40
NUM_CHANNELS = 1
PIXEL_DEPTH = 255

def main():

    tt= datasets.load_digits()
    print(tt.data[-2:])
    path = '/home/theo/datas/train.tar.gz'
  #  imagePath = ip.getimgs(path)
   # bob = numpy.array( [list(numpy.array(Image.open(imagePath[i]).convert('L'), 'f')) for i in range(len(imagePath))] )    
   # bob.reshape(2,2)
    #print(bob[-2:])

   # for u in range(0,len(total)):
   
    #    print(list(total[u][0]))
   # for i in range(0,len(bob)):

      #  bob[i]  = (bob[i] - (PIXEL_DEPTH / 2.0)) / PIXEL_DEPTH
        train_labels = numpy.append(numpy.zeros(428),numpy.ones(351))
        d,t=data[:-10],train_labels[:-10]
        #print(d)
        clf.fit(d,t)
      

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--inp', type=str, default='/home/theo/Dropbox/TER/Images/bar chart/',
                      help='Directory for storing input data')
    parser.add_argument('--out', type=str, default='/home/theo/temp/la/',
                      help='Directory for storing output data')
    parser.add_argument('--ext', type=str, default='jpg',
                      help='Extention for output data')   
    parser.add_argument('--size', type=int, default=100,
                      help='Size for output data')
    FLAGS, unparsed = parser.parse_known_args()
    main()

