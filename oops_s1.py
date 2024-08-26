"""name = "lion"
color = "yellow"
_name = "dove"
_color = "white"
print(name)
print(color)
print(_name)
print(_color)
"""
class object:
    def __init__(self,name):
        self.name = name

class animal(object):
    pass

animal1 = animal("lion")
animal2 = animal("tiger")
print(animal1.name)
print(animal2.name)