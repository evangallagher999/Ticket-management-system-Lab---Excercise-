#interface class 
from abc import ABC,abstractmethod

class IData(ABC): # will be implemented by child classes.
    @abstractmethod # decorator to declare this interface. 
    def getObjectData(self):
        pass


    