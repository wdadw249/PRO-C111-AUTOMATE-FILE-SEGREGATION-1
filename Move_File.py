import shutil
import os

#This is the path where I am going to copy the file
from_dir = "C:/Users/Sayed/Downloads"
#This is the destination where I will be pasting the file
to_dir = "C:/Users/Sayed/Documents/Document_Files"
list_of_files = os.listdir(from_dir)

print()
for i in list_of_files:
    name, ext = os.path.splitext(i)
    source_file = os.path.join(from_dir, i)
    if ext == ".pdf":
        #I'am not going to cut, I am just going to copy it
        shutil.copy(source_file, to_dir)
        print(f"!! The file {name} has been pasted in the destination since it was a .pdf file")
    else:
        print(f"@@ The file {name} didn't get pasted since it wasnt a .pdf file")
print()
print(os.listdir(to_dir))
