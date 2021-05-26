import random

class Obj:
    def __init__(self, name):
        self.name = name

class ObjRandom(Obj):
    def __init__(self, name):
        super().__init__(name)
    
    def move(self):
        return random.choice([(0,1),(0,-1),(1,0),(-1,0)])
