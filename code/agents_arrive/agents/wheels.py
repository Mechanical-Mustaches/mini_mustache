import mechanical_mustaches as mm



class Wheels(mm.Agent):
    def __init__(self, name: str, louie: dict , roger: dict):
        super().__init__(name)
        self.name = name
        self.louie = mm.Motor(**louie)
        self.roger = mm.Motor(**roger)
        print("{} has rolledddddddd on in".format(self.name))

    def tankdrive(self, left, right):
        
        self.louie.set(left)
        self.roger.set(right)
        
    def stop(self):
        
        self.louie.set(0)
        self.roger.set(0)
        
    def check(self):
        pass
    
    
    def drive(self, speed: float, turn: float):
        """speed and turn take arguments from -1 to 1"""
        
        wheels = [speed + turn, speed - turn]
        
        for wheel in wheels:
            if wheel > 1:
                wheel = 1
            if wheel < -1:
                wheel = -1
        print(wheels)
        self.louie.set(wheels[0])
        self.roger.set(wheels[1])
        
            
        
        
