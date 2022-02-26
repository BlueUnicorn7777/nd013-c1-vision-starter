import argparse
import glob
import os, errno
import random

import numpy as np

from utils import get_module_logger

def symlink_force(target, link_name):
    try:
        os.symlink(target, link_name)
    except OSError as e:
        if e.errno == errno.EEXIST:
            os.remove(link_name)
            os.symlink(target, link_name)
        else:
            raise e
            
def split(source, destination):
    """
    Create three splits from the processed records. The files should be moved to new folders in the
    same directory. This folder should be named train, val and test.

    args:
        - source [str]: source data directory, contains the processed tf records
        - destination [str]: destination data directory, contains 3 sub folders: train / val / test
    """
    # TODO: Implement function
    
    #Get data from filename
    
    try:
        files = glob.glob(f'{source}/*.tfrecord')
    except Exception as err:
        print(err)
    
    # we need certain minimum number of tfrecords
    
    np.random.shuffle(files)
    
    # we are splitting training = 75% , validation = 15% and testing = 1% of the data set.
    
    if (len(files)) > 10 :
        train_files, val_files, test_files = np.split(files, [int(.75*len(files)), int(.9*len(files))])
        
    print(len(train_files) , len(val_files) , len(test_files))
   
    #Make destination directories
    
    train = os.path.join(destination, 'train')
    val = os.path.join(destination, 'val')
    test = os.path.join(destination, 'test')
    
    try:
        os.makedirs(train,exist_ok=True)
        os.makedirs(val,exist_ok=True)
        os.makedirs(test,exist_ok=True)
    except OSError as error:
        print("Desitination directory structure can not be created")  
        
    
    print("Creating symlink for train files")
    for file in train_files:
        #print(file)
        dest = os.path.join(train,os.path.basename(file))
        symlink_force(file,dest)
            
    print("Creating symlink for validation files")
    for file in val_files:
        #print(file)
        dest = os.path.join(val,os.path.basename(file))
        symlink_force(file,dest)
           
    print("Creating symlink for testing files")
    for file in test_files:
        #print(file)
        dest = os.path.join(test,os.path.basename(file))
        symlink_force(file,dest)    
    
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--source', required=True,
                        help='source data directory')
    parser.add_argument('--destination', required=True,
                        help='destination data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.source, args.destination)
