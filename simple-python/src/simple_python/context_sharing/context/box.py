import importlib

class LazyBox:
    def __init__(self):
        self.__targets = list()
    
    def add(self, module_location, target):
        self.__targets.append(dict(
            module_location = module_location,
            target = target,
        ))
    
    def dynamic_import(self, module_path, object_name):
        module = importlib.import_module(module_path)
        obj = getattr(module, object_name)
        return obj

    def check(self):
        return self.__targets
    
    def parse(self):
        for i in range(len(self.__targets)):
            item = self.__targets[i]
            obj = self.dynamic_import(item["module_location"], item["target"])
            self.__targets[i]["object"] = obj
    
    def inject(self):
        for i in range(len(self.__targets)):
            item = self.__targets[i]
            print(item["object"].deps)
            self.__targets[i]["object"]
            
    def size(self):
        return len(self.__targets)
    

lazy = LazyBox()

print("*"*35)
print("context/box.py --> call/import")
print("*"*35)