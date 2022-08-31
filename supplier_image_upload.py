#! /usr/bin/env python3
import requests
import os

url = "http://localhost/upload/"

# create list of all .jpeg files in folder
path = "/home/student-04-fc56b350ba3e/supplier-data/images"
list_images = []
for _,_, files in os.walk(path):
  for name in files:
    #  Want to exlude hidden files AND only include .jpeg files
    if not name.startswith(".") and name.endswith(".jpeg"):
      list_images.append(name)

#  Go through list of files and post to url.
#  Use 'rb' for read, binary (for images)
for image in list_images:
  image_path = path + "/" + image
  with open(image_path, 'rb') as opened:
    r = requests.post(url, files={'file': opened})