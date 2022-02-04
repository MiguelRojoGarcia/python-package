import io
import os
import shutil
import pathlib

class FileManagerModule:

    ## Constructor
    def __init__(self) ->None:
        pass

    def getRootPath(self):
        return pathlib.Path.cwd()

    def dirExist(self , dirPath):
        return os.path.isdir(dirPath)

    def dirCreate(self , dirPath):
        if self.dirExist(dirPath) == False:
            os.mkdir(dirPath)

    def dirRemove(self , dirPath):
        if self.dirExist(dirPath) == True:
            shutil.rmtree(dirPath)

    def dirCopy(self , originDirPath,destinyDirPath):
        shutil.copytree(originDirPath,destinyDirPath)

    def dirGetContent(self , dirPath):
        content = []
        
        if self.dirExist(dirPath):
            content = os.listdir(dirPath)

        return content

    def fileExist(self , file_path):
        return os.path.isfile(file_path)

    def fileWrite(self , path,txt):

        result = True

        try:
            fileManager = io.open(path, "a+")
            fileManager.write(txt)
            fileManager.close()
        except:
            result = False    
        
        return result

    def fileGetContent(self , path , asList = False):

        file_content = None

        try:

            fileManager = io.open(path, "r")

            if asList == True:
                file_content=fileManager.readlines()
            else:
                file_content=fileManager.read()
            
            fileManager.close()

        except:
            file_content = None    
        
        return file_content

    def fileCopy(self,origin_path,destiny_path):

        if self.fileExist(origin_path) == True:
            shutil.copyfile(origin_path , destiny_path)

    def fileRename(self , origin_path,destiny_path):

        if self.fileExist(origin_path) == True:
            shutil.move(origin_path , destiny_path)    
            
    def fileRemove(self , path):
        if self.fileExist(path):
            os.remove(path)
        

        
