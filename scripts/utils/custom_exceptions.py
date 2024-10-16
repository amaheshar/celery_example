import fastapi 

class CustomException(Exception):
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        