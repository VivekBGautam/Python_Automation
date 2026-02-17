# Whrite the automation script to print the file name with extention .txt

import sys
import os

def DirectoryFileSearch(DirName,Fileextention):
    Ret = False

    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("There is no such directry")
        return

    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("There is no not directry")
        return
    
    for FolderName, SubFolderName, FileName in os.walk(DirName):        # To walk/Scan directry 
        for File in FileName:
            if(File.split(".")[1] == Fileextention):      # to check file extention 
                print("File Name : ", File)
    

def main():
    Border = "_"*60
    print(Border)
    print("-----------------Vivek Directory Automation-----------------")
    print(Border)

    if(len(sys.argv) != 3):
        print("Invalid number of argument")
        print("Please specify the name of directory and file extention")
        return
    
    DirectoryFileSearch(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
    main()