# Python Script to Batch Rename Files
# This Code will ONLY Rename JPG and MOV Files
# Author : wh0am1
# GitHub : https://github.com/wh0th3h3llam1


import os
from os import listdir
from os.path import isfile, join

# path = "C:\\Users\\Aarsh\\Documents\\Pics\\"
path = input("Enter Full Path for the Files to be Renamed : ")

print("Changing Path to " + path)

try:
	os.chdir(path)
except Exception as e:
	print("Error Changing Path")
	print(e)
	exit(1)

print("Collecting All the Files...")


files = [f for f in listdir(path) if isfile(join(path, f))]
if len(files) == 0:
	print("No Files Found.")
	exit()


i = 1290

try:
	for file in files:
		if file.endswith('.JPG'):
			os.rename(file, "DSC_" + str(i) + '.JPG')
		if file.endswith('.MOV'):
			os.rename(file, "DSC_" + str(i) + '.MOV')
		i = i + 1
except Exception as e:
	print("Can't Rename the Files " + e)




# for r, d, f in os.walk(path):
# 			print(file)