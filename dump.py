import os
import shutil

dump = 'D:/zz/Med-imgs/Dump'
main_dir = 'D:/zz/Med-imgs/All'

for root, subdirs, files in os.walk(main_dir):
    for file in files:
        if file[-3:] == 'jpg':
            path = os.path.join(root,file)
            shutil.copy(path, dump)
            print(path)
