
import math
import pandas
import numpy as np
print( np.random.rand(3,4))

class person():
    "hello person"
    def __init__(self, name="", id= ""):
        self.sName = name
        self.nID = id
    
    def desc(self):
        print("my name is", self.sName, "id=", self.nID)

    def doRun(self, ntye,sStr):
        print(self.sName, ntye, sStr)


#print(dir(math))
#print(person.__doc__)

p1= person("gwg","123")
p1.desc()
