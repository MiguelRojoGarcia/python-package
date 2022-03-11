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

    def dirExist(self , dir_path):
        return os.path.exists(dir_path)

    def dirCreate(self , dir_path , permission = 775):
      
        dir_path = f"{self.__working_directory}/{dir_path}"

        if self.dirExist(dir_path) == False:
            os.makedirs(dir_path, permission)
            
        return self.dirExist(dir_path)

    def dirRemove(self , dir_path):

        dir_path = f"{self.__working_directory}/{dir_path}"
        
        if self.dirExist(dir_path) == True:
            shutil.rmtree(dir_path)
        
        return self.dirExist(dir_path) == False

    def dirCopy(self , origindir_path,destinydir_path):
        
        origindir_path = f"{self.__working_directory}/{origindir_path}"
        
        destinydir_path = f"{self.__working_directory}/{destinydir_path}"
        
        shutil.copytree(origindir_path,destinydir_path)

    def dirGetContent(self , dir_path = None):
        
        content = []

        if dir_path != None:
            dir_path = f"{self.__working_directory}/{dir_path}"
        else:
            dir_path = f"{self.__working_directory}"

        if self.dirExist(dir_path):
            content = os.listdir(dir_path)

        return content

    def fileExist(self , file_path , use_working_directory = True):

        if use_working_directory == True:
            file_path = f"{self.__working_directory}/{file_path}"
        
        return os.path.isfile(file_path)

    def fileWrite(self , path,txt):
        
        path = f"{self.__working_directory}/{path}"

        result = True

        try:
            file_handler = io.open(path, "a")
            file_handler.write(txt)
            file_handler.close()
        except:
            result = False    
        
        return result

    def fileGetContent(self , path , as_list = False):

        path = f"{self.__working_directory}/{path}"

        file_content = None

        try:

            file_handler = io.open(path, "r")

            if as_list == True:
                file_content=file_handler.readlines()
            else:
                file_content=file_handler.read()
            
            file_handler.close()

        except:
            file_content = None    
        
        return file_content

    def fileCopy(self,origin_path,destiny_path):
        
        origin_path = f"{self.__working_directory}/{origin_path}"
        destiny_path = f"{self.__working_directory}/{destiny_path}"

        if self.fileExist(origin_path , False) == True:
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


        
