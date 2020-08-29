# Python Script to Rename Files in batch
# This Script will retain the Extension of the Files
# Author : wh0am1
# GitHub : https://github.com/wh0th3h3llam1


from os import listdir, getcwd, chdir, rename
from os.path import isfile, join, splitext


def get_files():

	path = input("Enter Full Path of Folder (Default is Current Directory): ")
	if path == '':
		print("[INFO] Path is Empty")
		print("[INFO] Using Current Directory as Path")
		path = getcwd()

	else:
		print("[INFO] Changing Path to " + path + "...")

	try:
		chdir(path)
	except Exception as e:
		print("[ERROR] Error Changing Path : ")
		print(e)
		exit(1)


	files = [f for f in listdir(path) if isfile(join(path, f))]
	if len(files) == 0:
		print("No Files Found.")
		exit()

	print("Collecting All the Files...")
	print("{0} Files Found".format(len(files)))
	return files


def rename_files(files):
	i = 0
	count = 0

	print('\n\tTYPE A RENAME PATTERN')
	print("[INFO] Example : my_file_* : ")
	print("[INFO] Example : my_file_*_new : ")
	print("[INFO] If '*' is not present, numbers will be appended at the end of the file name")
	print()
	rename_pattern = input("Enter a Rename Pattern : ")
	i = int(input("Counting should start from (Default is 0): "))

	try:
		flag = 1
		mid = rename_pattern.index('*')
		before_mid = rename_pattern[:mid]
		after_mid = rename_pattern[mid+1:]
		print("[INFO] Asterisk Found.")
		print("[INFO] Files will be renamed as ", end='')
		print("{0}{1}{2}".format(before_mid, str(i), after_mid), end='\t')
		print("{0}{1}{2}".format(before_mid, str(i + 1), after_mid))

	except :
		flag = 0
		print("[INFO] No Asterisk Found.")
		print("[INFO] Numbers will be appended at the end of the file name.")

	print()
	x = input("Press any key to continue...")
	try:
		for file in files:

			# Get File Extension
			name, extension = splitext(file)[0], splitext(file)[1]
			# print("Name : " + file + "\t" + "Extension :" + extension)

			print(name + extension + " renamed to --> ", end='')
			if flag == 1:
				rename(file, before_mid + str(i) + after_mid + extension)
				print(before_mid + str(i) + after_mid + extension)

			else:
				rename(file, rename_pattern + str(i) + extension)
				print(str(i) + extension)

			count += 1
			i += 1

	except Exception as e:
		print("Can't Rename the Files...")
		print(e)
		exit(1)

	print("\n[INFO] Successfully Renamed " + str(count) + " Files")


def main():
	files = get_files()

	rename_files(files)


if __name__ == "__main__":
	main()


#wh0am1
