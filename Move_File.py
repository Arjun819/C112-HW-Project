import os # importing os module
import shutil # importing shutil module

from_dir = "C:/Users/Aashima Bandiwadekar/Downloads" # Source File
to_dir = "C:/Users/Aashima Bandiwadekar/Downloads/Document_File" # Destination File

list_files = os.listdir(from_dir) # creating a function listdir() to create a list of all files in the destination file
print(list_files) # prints all the files in the destination path

for file in list_files: # for loop used to check all the files present in the destination path
    name,extension = os.path.splitext(file) #  splitext() function would split the file into it's name and his extension
    print("Name of "+file +" is "+name)
    print("Extension of "+file +" is "+extension)
    
    if(extension == ""): # if the extension is blank then skip this file and continue to the next file
        continue # used to skip this file and move to next file
    if(extension in [".txt",".doc",".docx",".pdf"]): # if the extensionn matched the extension present in documents
        path1 = from_dir + "/" + file # source path
        path2 = to_dir + "/" + "Document_Files" # destination path
        path3 = to_dir + "/" + "Document_Files" + "/" + file # final path

        if(os.path.exists(path2)): # if path2 or destination path existed 
            shutil.move(path1,path3) # it will move the file to the final path
            print("Moving")
        else: # if path2 or destination path did not exists
            os.makedirs(path2) # it created a new directory to the destination path
            shutil.move(path1,path3) # it will move the file to the final path
            print("Moving")
