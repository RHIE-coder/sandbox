from configparser import ConfigParser
from testmo_automation import resovler

__ini_file = (resovler.get_project_path() / ".testmo.ini").resolve()

def ini_path():     
    return __ini_file

def load_ini_config():
    __config = ConfigParser()
    __config.read(__ini_file)
    return __config

def get_ini_struct():
    info = dict()
    config = load_ini_config()
    sections = config.sections()
    for section in sections:
        info[section] = list(config[section].keys())
    return info

class TestmoUrlBuilder:

    def __init__(self, workspace_name:str):
        self.__workspace_name = workspace_name
        self.__origin = f"https://{self.__workspace_name}.testmo.net"
        self.__repo_num = None
        self.__group_id = None
        self.__case_id = None

    def home(self):
        return self.__origin

    def repo(self, num:int):
        self.__repo_num = num
        self.__group_id = None
        self.__case_id = None
        return self
    
    def group(self, id:int):
        self.__group_id = id
        self.__case_id = None
        return self
    
    def case(self, id:int):
        self.__case_id = id
        return self
    
    def build_url(self):
        url = self.__origin

        if self.__repo_num is None:
            return url
        
        url = f"{url}/repositories/{self.__repo_num}"

        if self.__group_id is None:
            return url
        
        url = f"{url}?group_id={self.__group_id}"

        if self.__case_id is None:
            return url
        
        return f"{url}&case_id={self.__case_id}"