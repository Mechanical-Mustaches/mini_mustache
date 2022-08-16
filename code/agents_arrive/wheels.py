import mechanical_mustaches as mm



class Wheels(mm.Agent):
    def __init__(self, name: str, louie: dict , roger: dict):
        super().__init__(name)
        self.name = name
        self.louie = mm.Motor(**louie)
        self.roger = mm.Motor(**roger)

        print("{} has rolledddddddd on in".format(self.name))   

    def move(self, left, right):
        
        self.louie.set(left)
        self.roger.set(right)
        
    def stop(self):
        
        self.louie.set(0)
        self.roger.set(0)
        
    def check(self):
        pass