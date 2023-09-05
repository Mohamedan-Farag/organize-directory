import os
import shutil
import sys

 
current_dir = os.getcwd()

for name_of_file in os.listdir(current_dir):
    if name_of_file.endswith((".png" , "jpg","jpeg","gif")):
        if not os.path.exists("Images"):
            os.mkdir("Images")
        shutil.move(name_of_file, "Images")
        print("Image moved successfully")


for name_of_file in os.listdir(current_dir):
    if name_of_file.endswith((".mp4" , ".mkv",".avi",".flv")):
        if not os.path.exists("Videos"):
            os.mkdir("Videos")
        shutil.move(name_of_file, "Videos")
        print("Video moved successfully")


for name_of_file in os.listdir(current_dir):
    if name_of_file.endswith((".pdf" , ".docx",".doc",".txt")):
        if not os.path.exists("Documents"):
            os.mkdir("Documents")
        shutil.move(name_of_file, "Documents")
        print("Document moved successfully")

for name_of_file in os.listdir(current_dir):
    if name_of_file.endswith((".zip" , ".rar",".tar",".gz")):
        if not os.path.exists("Archives"):
            os.mkdir("Archives")
        shutil.move(name_of_file, "Archives")
        print("Archives moved successfully")

print("All files are organized successfully")

