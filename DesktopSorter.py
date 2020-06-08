#!/usr/bin/env python3
import os
import shutil
import pathlib
import time
import sys

# makes Sorting Folder is one does not exist
sortDir = os.path.expanduser('~/Desktop/SortFolder')
if not os.path.exists(sortDir):
    os.mkdir(sortDir)
    # Initialises watchman to watch for sortFile directory changes
    os.system('watchman -- trigger ~/Desktop/SortFolder pictureSort -- python3 ~/Desktop/picSorter.py')

# Makes Pictures Directory if one does not exist
picDir = os.path.expanduser("~/Documents/Pictures")
if not os.path.exists(picDir):
    os.mkdir(picDir)

# Enter Sorting Drirectory
os.chdir(sortDir)

# Retreiving all files within Sorting Directory
sortDirContents = os.listdir()

for file in sortDirContents:

    # Retrieves month and year of file in the format
    fileYear = time.strftime('%Y', time.localtime(os.path.getmtime(sortDir + '/' + file)))
    fileMonth = time.strftime('%m', time.localtime(os.path.getmtime(sortDir + '/' + file)))
    # Converts months and years into PATH
    dateDir = picDir + '/' + fileYear + '/' + fileMonth

    # Creates month and year directories if none exist
    os.makedirs(dateDir, exist_ok = True)

    # Moves file to the relevent subdirectory
    try:
        shutil.move(file, dateDir)
    except:
        pass
