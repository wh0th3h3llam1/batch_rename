import os

path = "C:\\Users\\Aarsh\\Documents\\Pics - Copy"

os.chdir(path)

files = os.listdir(path)

i = 1

try:
	for file in files:
		if file.endswith('.JPG'):
			os.rename(file, "DSC_" + str(i) + '.JPG')
		if file.endswith('.MOV'):
			os.rename(file, "DSC_" + str(i) + '.MOV')
		i = i + 1
except Exception as e:
	print("Can't Rename the Files " + e)