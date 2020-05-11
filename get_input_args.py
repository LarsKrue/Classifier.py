#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#                                                                             
# PROGRAMMER: Lars Krüger
# DATE CREATED: 05.05.2020                                  
# REVISED DATE: 05.05.2020
# PURPOSE: Create a function that retrieves the following 3 command line inputs 
#          from the user using the Argparse Python module. If the user fails to 
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#
##
# Imports python modules
import argparse

# TODO 1: Define get_input_args function below please be certain to replace None
#       in the return statement with parser.parse_args() parsed argument 
#       collection that you created with this function
    
def get_input_args():
   
    # Create Parse using ArgumentParser
    parser = argparse.ArgumentParser(description="Parsen von 3 User-Inputs", prog="Dog Classifier")
    # Create 3 command line arguments as mentioned above using add_argument() from ArguementParser method
    parser.add_argument('--dir', type = str, default='pet_images/', 
                        help='path to folder of images')
    parser.add_argument('--arch',type = str, default = 'alexnet', #vgg, resnet, alexnet 
                        help='Type of Algorithm')
    parser.add_argument('--dogfile', default = 'dognames.txt', help='Type of Algorithm') 
    
    in_arg = parser.parse_args() 
    return (in_arg)
    
    

