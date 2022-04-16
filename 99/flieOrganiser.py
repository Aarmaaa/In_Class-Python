import os
import shutil

path = input("Enter the name of the folder to be sorted: ")

list_of_files = os.listdir()

for i in list_of_files:
    name, ext = os.path.splitext(i)
    #To store all the extension types as a list
    ext = ext[1:]
    #If it is a directory (folder)
    if ext == "":
        continue
    #Checking if a folder with ext exists
    if os.path.exists(path + "/" + ext):
        shutil.move(path+"/"+ i, path+ "/" + ext + "/" +i)
    else :
        os.makedirs(path + "/" + ext)
        shutil.move(path + "/" + i , path + "/" + ext + "/" + i )

