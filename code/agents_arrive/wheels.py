import mechanical_mustaches as mm



class Wheels(mm.Agent):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.louie = mm.Motor(f_pin=12, r_pin=26, freq=20000, name='louie')
        self.roger = mm.Motor(f_pin=25, r_pin=33, freq=20000, name='roger')

        print("{} has rolledddddddd on in".format(self.name))   

    def move(self, left, right):
        
        self.louie.set(left)
        self.roger.set(right)
        
    def stop(self):
        
        self.louie.set(0)
        self.roger.set(0)