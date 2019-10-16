# Python Script to Batch Rename Files
# This Code will Retain the Extension of the Files
# Author : wh0am1
# GitHub : https://github.com/wh0th3h3llam1


import os
from os import listdir
from os.path import isfile, join, splitext


def get_files():
	path = input("Enter Full Path for the Files to be Renamed : ")

	print("Changing Path to " + path + "...")

	try:
		os.chdir(path)
	except Exception as e:
		print("Error Changing Path : ")
		print(e)
		exit(1)


	files = [f for f in listdir(path) if isfile(join(path, f))]
	if len(files) == 0:
		print("No Files Found.")
		exit()

	print("Collecting All the Files...")

	return files


def rename_files(files):
	i = 0
	count = 0

	rename_sequence = input("Enter a Rename Sequence: ")
	i = int(input("Counting should start from : "))

	try:
		for file in files:

			# Get File Extension
			extension = splitext(file)[1]
			print("Name : " + file + "\t" + "Extension :" + extension)
			os.rename(file, rename_sequence + str(i) + extension)

			count += 1
			i += 1

	except Exception as e:
		print("Can't Rename the Files...")
		print(e)
		exit(1)

	print("Successfully Renamed " + str(count) + " Files")


def main():
	files = get_files()

	rename_files(files)


if __name__ == "__main__":
	main()
