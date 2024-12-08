import sys
import os
from PIL import Image

current_dir=os.getcwd()
from_Path_folder=sys.argv[1]
to_Path_Folder=sys.argv[2]
for i in os.listdir(from_Path_folder):
    old_image=Image.open(f'{current_dir}/{from_Path_folder}//{i}')
    new_image=old_image.resize((1920,1280))
    new_image.save(f"{current_dir}/{to_Path_Folder}/{i.split('.')[0]}.jpg",'jpg')
    new_image.show()