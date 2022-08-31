#! /usr/bin/env python3

import os
import requests

# create list of files for the descriptions
path = "/home/student-04-f30c05e8e3ff/supplier-data/descriptions"
list_descriptions = []
for _,_, files in os.walk(path):
  for name in files:
    #  Want to exlude hidden files AND only include .txt files
    if not name.startswith(".") and name.endswith(".txt"):
      list_descriptions.append(name)

# for every file, open file, create a dictionary with info.
# {"name": "string", "weight": "int", "description": "string", "image_name": "string"
list_dict = []
for file in list_descriptions:
  with open(path + "/" + file, 'r') as opened:
    lines = opened.readlines()
    descriptions_dict = {}
    descriptions_dict["name"] = lines[0].strip("\n")
    descriptions_dict["weight"] = int(lines[1].strip("lbs \n"))
    descriptions_dict["description"] = lines[2].strip("\n")
    descriptions_dict["image_name"] = file.strip(".txt") + ".jpeg"
    list_dict.append(descriptions_dict)

# post dictionary to url
url = "http://35.202.26.82/fruits/"
for dict in list_dict:
  data = dict
  r = requests.post(url, data = data)