#! /usr/bin/env python3

from PIL import Image
import os

#/home/student-04-fc56b350ba3e
path = "/home/student-04-fc56b350ba3e/supplier-data/images"

list_images = []
for _,_, files in os.walk(path):
  for name in files:
    #  Want to exlude hidden files AND only include .tiff files
    if not name.startswith(".") and name.endswith(".tiff"):
      list_images.append(name)

print(list_images)
# resizes a list of images to (600x400) and converts them to jpg.
# saves new images in same folder as found.
for image in list_images:
    im = Image.open(path+"/"+image)
    new_image = image.strip(".tiff") + ".jpeg"
    im.convert('RGB').resize((600,400)).save(path + "/" +  new_image, "JPEG")