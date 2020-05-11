# -*- coding: utf-8 -*-
"""
Created on Sun May 10 19:20:03 2020

@author: Lars Krüger
"""


with open('dognames.txt') as f:
        dog_name_list = [line for line in f]
for i in range(len(dog_name_list)):
    dog_name_list[i]=dog_name_list[i].strip("\n")
    print(dog_name_list)
    print(type(dog_name_list))
    print(len(dog_name_list))
    dog_name_set = set(dog_name_list)
    pet_label = str("basenji")
    pet_label_set = {pet_label}
    print("Pet Set", pet_label_set)
    print("Dog Set", dog_name_set)
    enthalten = pet_label_set.issubset(dog_name_set)
    if enthalten == True:
        print("enthalten")
    else:
        print("{} ist nicht enthalten".format(pet_label))