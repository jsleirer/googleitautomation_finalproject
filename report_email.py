#!/usr/bin/env python3

import os
import reports
from datetime import date
import emails
import sys

# Need Title to include today's date
# Processed Update on Month Day, Year"
today = date.today().strftime("%B %d, %Y")
title = "Processed update on " + today
#info = " "
attachment = "/tmp/processed.pdf"

# create list of files for the descriptions
path = "/home/student-04-f30c05e8e3ff/supplier-data/descriptions"
list_descriptions = []
for _,_, files in os.walk(path):
  for name in files:
    #  Want to exlude hidden files AND only include .txt files
    if not name.startswith(".") and name.endswith(".txt"):
      list_descriptions.append(name)

# for every file, open file, create a dictionary with info.
# {"name": "string", "weight": "int", "description": "string", "image_name": "s$
list_dict = []
for file in list_descriptions:
  with open(path + "/" + file, 'r') as opened:
    lines = opened.readlines()
    descriptions_dict = {}
    descriptions_dict["name"] = lines[0].strip("\n")
    descriptions_dict["weight"] = lines[1].strip("\n")
    list_dict.append(descriptions_dict)

# Need to read in dictionary values as a list.
# Loop through list of dictionaries
# Append to list key, value, <br/>
new_list = []
for item in list_dict:
  new_list.append("name: " + item["name"])
  new_list.append("weight: " + item["weight"])
  new_list.append("<br/>")

info = "<br/>".join(new_list)
From = "automation@example.com"
To = "student-04-f30c05e8e3ff@example.com"
Subject = "Upload Completed - Online Fruit Store"
Body = "All fruits are uploaded to our website successfully. A detailed list is$
Attachment = "/tmp/processed.pdf"


def main(argv):
  reports.generate_report(attachment, title, info)
  message = emails.generate_email(From, To, Subject, Body, Attachment)
  emails.send_email(message)

if __name__ == "__main__":
  main(sys.argv)