import sys
import os
from PIL import Image

from_Path_folder=sys.argv[1]
to_Path_Folder=sys.argv[2]
for i in os.listdir(from_Path_folder):
	if os.path.isdir(to_Path_Folder):
		i.save(f"{i}.png",'png')
