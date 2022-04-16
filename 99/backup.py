import os
import shutil

soure = input("inupt source")
palce = input("enter place")

soure = soure + "/"
palce = palce + "/"

list_of_files = os.listdir(soure)

for i in list_of_files:
    shutil.copy((soure + i), palce)