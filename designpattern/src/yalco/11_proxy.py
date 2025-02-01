from abc import ABC, abstractmethod

class Image(ABC):
    def display(self):
        ...
    def get_file_name(self)->str:
        ...
    
    
class RealImage(Image):
    __file_name:str
    
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__load_from_disk()

    def __load_from_disk(self):
        print(f"loading... {self.__file_name}") 

    def display(self):
        print("Displaying")
    
    def get_file_name(self):
        return self.__file_name

class ProxyImage(Image):
    __real_image:RealImage
    __file_name:str

    def __init__(self, file_name:str):
        self.__file_name = file_name
    
    def display(self):
        if self.__real_image is None:
            self.__real_image = RealImage
        self.__real_image.display()
    
    def get_file_name(self):
        return self.__file_name
    
    def get_file_extension(self):
        last_idx = self.__file_name.rfind('.')
        if last_idx == -1:
            return ''
        return self.__file_name[last_idx+1]
