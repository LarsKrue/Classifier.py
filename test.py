# -*- coding: utf-8 -*-
"""
Created on Sun May 10 19:20:03 2020

@author: Lars Krüger
"""


import argparse

# TODO 1: Define get_input_args function below please be certain to replace None
#       in the return statement with parser.parse_args() parsed argument 
#       collection that you created with this function
    

   
# Create Parse using ArgumentParser
parser = argparse.ArgumentParser(description="Parsen von 3 User-Inputs", prog="Dog Classifier")
# Create 3 command line arguments as mentioned above using add_argument() from ArguementParser method
parser.add_argument('--dir', type = str, default='pet_images/', 
                    help='path to folder of images')
parser.add_argument('--arch',type = str, default = 'vgg', 
                    help='Type of Algorithm')
parser.add_argument('--dogfile', default = 'dognames.txt', help='dog labels') 

in_arg = parser.parse_args() 
print(in_arg.dir)
print(in_arg.arch)
print(in_arg.dogfile)
#return (in_arg)
    