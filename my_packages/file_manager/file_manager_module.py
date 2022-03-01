import io
import os
import shutil
import pathlib

class FileManagerModule:

    __working_directory = None

    ## Constructor
    def __init__(self , working_directory = '') ->None:
        self.__working_directory = f"{pathlib.Path.cwd()}/{working_directory}"
        pass
    
    @property
    def working_directory(self):
        return self.__working_directory

    def dirExist(self , dirPath = None):

        fullDir = self.__working_directory
        
        if dirPath != None:
            fullDir = f"{self.__working_directory}/{fullDir}"

        return os.path.exists(dirPath)

    def dirCreate(self , dirPath , permission = 775):
      
        dirPath = f"{self.__working_directory}/{dirPath}"

        if self.dirExist(dirPath) == False:
            os.makedirs(dirPath, permission)
            
        return self.dirExist(dirPath)

    def dirRemove(self , dirPath):

        dirPath = f"{self.__working_directory}/{dirPath}"
        
        if self.dirExist(dirPath) == True:
            shutil.rmtree(dirPath)
        
        return self.dirExist(dirPath) == False

    def dirCopy(self , originDirPath,destinyDirPath):
        
        originDirPath = f"{self.__working_directory}/{originDirPath}"
        
        destinyDirPath = f"{self.__working_directory}/{destinyDirPath}"
        
        shutil.copytree(originDirPath,destinyDirPath)

    def dirGetContent(self , dirPath):
        
        content = []
       
        dirPath = f"{self.__working_directory}/{dirPath}"
       
        if self.dirExist(dirPath):
            content = os.listdir(dirPath)

        return content

    def fileExist(self , file_path):
        file_path = f"{self.__working_directory}/{file_path}"
        return os.path.isfile(file_path)

    def fileWrite(self , path,txt):
        
        path = f"{self.__working_directory}/{path}"

        result = True

        try:
            fileManager = io.open(path, "a")
            fileManager.write(txt)
            fileManager.close()
        except:
            result = False    
        
        return result

    def fileGetContent(self , path , asList = False):

        path = f"{self.__working_directory}/{path}"

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
       
        origin_path = f"{self.__working_directory}/{origin_path}"
        destiny_path = f"{self.__working_directory}/{destiny_path}"

        if self.fileExist(origin_path) == True:
            shutil.copyfile(origin_path , destiny_path)

    def fileRename(self , origin_path,destiny_path):
     
        origin_path = f"{self.__working_directory}/{origin_path}"
     
        destiny_path = f"{self.__working_directory}/{destiny_path}"
        
        if self.fileExist(origin_path) == True:
            shutil.move(origin_path , destiny_path)    
            
    def fileRemove(self , path):

        path = f"{self.__working_directory}/{path}"
      
        if self.fileExist(path) == True:
            os.remove(path)
        
        return self.fileExist(path) == False


        
