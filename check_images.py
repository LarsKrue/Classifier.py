"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py
#
# TODO 0: Add your information below for Programmer & Date Created.                                                                             
# PROGRAMMER: Lars Krüger
# DATE CREATED: 14.04.2020                                  
# REVISED DATE: 
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, and
#          summarizes how well the CNN performed on the image classification task. 
#          Note that the true identity of the pet (or object) in the image is 
#          indicated by the filename of the image. Therefore, your program must
#          first extract the pet image label from the filename before
#          classifying the images using the pretrained CNN model. With this 
#          program we will be comparing the performance of 3 different CNN model
#          architectures to determine which provides the 'best' classification.
#
# Use argparse Expected Call with <> indicating expected user input:
#      python check_images.py --dir <directory with images> --arch <model>
#             --dogfile <file that contains dognames>
#   Example call:
#    python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
#
"""

# Imports python modules
import time 
# Imports print functions that check the lab
from print_functions_for_lab_checks import *

# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

# Main program function defined below

def main():
    
    #TODO 0 ------------------------------------------------------------------
    
    print("3 Eingaben")
    start_time = time.time() 
    
    # Todo 1
    in_arg = get_input_args() 
    print(in_arg)
    #check_command_line_arguments(in_arg)
    
    #TODO 2
    results_dic = get_pet_labels(in_arg.dir)
    print("Results_dic", results_dic) 
    #TODO 3
    results = classify_images(in_arg.dir, results_dic, in_arg.arch) #updated Dict
    
    print("neu Dict", results)   
    print("neu Dict.keys", results.keys())
    
    #TODO 4
    results_dic= adjust_results4_isadog(results, in_arg.dogfile)
    print(results_dic)
    
    # TODO 5
    results_stats = calculates_results_stats(results) 
    print(results_stats)
    
    # TODO 6
    print_results(results_dic, results_stats, in_arg.arch, False, False) 
    
    end_time = time.time()
    tot_time = end_time - start_time 
    print("\n** Total Elapsed Runtime:",
          str(int((tot_time/3600)))+":"+str(int((tot_time%3600)/60))+":"
          +str(int((tot_time%3600)%60)) )
    
    
    #-----------------------------------------------------------------------
    
    # TODO 5: Define calculates_results_stats function within the file calculates_results_stats.py
    # This function creates the results statistics dictionary that contains a
    # summary of the results statistics (this includes counts & percentages). This
    # dictionary is returned from the function call as the variable results_stats    
    # Calculates results of run and puts statistics in the Results Statistics
    # Dictionary - called results_stats
   # results_stats = calculates_results_stats(results)

    # Function that checks Results Statistics Dictionary using results_stats
    #check_calculating_results(results, results_stats)


    # TODO 6: Define print_results function within the file print_results.py
    # Once the print_results function has been defined replace 'None' 
    # in the function call with in_arg.arch  Once you have done the 
    # replacements your function call should look like this: 
    #      print_results(results, results_stats, in_arg.arch, True, True)
    # Prints summary results, incorrect classifications of dogs (if requested)
    # and incorrectly classified breeds (if requested)
   # print_results(results, results_stats, None, True, True)
    
   
    

# Call to main function to run the program
if __name__ == "__main__":
    main()
