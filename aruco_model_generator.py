#!/usr/bin/env python

import os
from pathlib import Path
import shutil

for x in range(250):
    print(x)
    
    for subdir, dirs, files in os.walk("aruco_code_base"):
        for filename in files:
            filepath = subdir + os.sep + filename

            copy_subdir = subdir.replace("base", str(x).zfill(3))
            content = Path(filepath).read_text()
            copy_content = content.replace("{xxx}", str(x).zfill(3))
            copy_filename = filename.replace("{xxx}", str(x).zfill(3))

            print (os.path.join(copy_subdir, copy_filename))
            Path(copy_subdir).mkdir(parents = True, exist_ok = True)
            Path(copy_subdir + os.sep + copy_filename).write_text(copy_content)

    copy_subdir = "aruco_code_" + str(x).zfill(3) + os.sep + "materials" + os.sep + "textures"
    Path(copy_subdir).mkdir(parents = True, exist_ok = True)
    shutil.copyfile("aruco_code_images" + os.sep + str(x).zfill(5) + ".png", copy_subdir + os.sep + str(x).zfill(5) + ".png")
    
