#Top
class Light():
    def __init__(self):
        self.stat = 'green'

class Create_section():
    def __init__(self,num_light):
        self.num_lights = num_light
        for i in range(self.num_lights):
            Light()