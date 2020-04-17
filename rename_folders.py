#!/usr/bin/python3
import os, sys




#Function to display all the name od the folders in a given directory
def listdirs(folder):
    return [d for d in os.listdir(folder) if os.path.isdir(os.path.join(folder, d))]


# loop 
#  Call the function and rename each folder add a prefix to the name
for file in listdirs(sys.argv[1]):
	os.rename(path + file, (path + prefix + file))
	print (sys.argv[1] + sys.argv[2] + file)



#  Execute the script python3 rename_folders.py arg1 arg2   



 
