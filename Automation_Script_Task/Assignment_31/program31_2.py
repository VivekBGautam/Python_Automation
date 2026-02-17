# Whrite the automation script which accept directry name and first file extention
#  and anf chenge first file extention by secnd file extention 

import sys
import os

def DirectoryFileSearch(DirName,SorceFileExt,ChengeFileExt):
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
            BaseName, Ext = os.path.splitext(File)
            Ext = Ext.lstrip(".")      # To remove dot
            if(Ext == SorceFileExt):      # to check file extention 
                OldFilePath = os.path.join(FolderName, File)
                NewFileName = BaseName + "." + ChengeFileExt
                NewFilePath = os.path.join(FolderName, NewFileName)

                os.rename(OldFilePath, NewFilePath)

                print(f"Renamed: {File} -> {NewFileName}")
    
def main():
    Border = "_"*60
    print(Border)
    print("-----------------Vivek Directory Automation-----------------")
    print(Border)

    if(len(sys.argv) != 4):
        print("Invalid number of argument")
        print("Please specify the name of directory")
        print("and file extention of source and to chenge file extention")
        print("Give input in this format : Filename.py DirName firstExtention  Second extention")
        return
    
    DirectoryFileSearch(sys.argv[1],sys.argv[2],sys.argv[3])

if __name__ == "__main__":
    main()