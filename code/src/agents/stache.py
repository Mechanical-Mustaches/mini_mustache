import mechanical_mustaches as mm

class Stache(mm.Agent):
    def __init__(self,
                 name: str,
                 l_pin: int,
                 l_min: int,
                 l_max: int,
                 r_pin: int,
                 r_min: int,
                 r_max: int):
        self.stachel = mm.Servo(pin=l_pin, name=stachel, min=l_min, max=l_max)
        self.stacher = mm.Servo(pin=r_pin, name=stacher, min=r_min, max=r_max)
        self.state = 'sleeping'
        self.timmy = mm.Timer()
        self.auto = mm.Auto

    
    def check(self):
        states = {
            'sleeping': sleeping(),
            'dancing': self.auto.check()
            }
        
        states[self.state]()
    
    #-------------------------------------------------------------

    def wiggle(self, pos: float) -> None:
        self.stachel.set(pos)
        self.stacher.set(-pos)
        
    def twist(self, pos: float) -> None:
        self.stachel.set(pos)
        self.stacher.set(pos)
        
    #-------------------------------------------------------------

    def sleep(self):
        self.twist(0)
        self.state = 'sleeping'
        
    def sleeping(self):
        pass
    
    #-------------------------------------------------------------

    def dance(self):
        tiny_dancer = [
            lambda: self.twist(.75),
            lambda: self.timmy.wait(1),
            lambda: self.twist(-.75),
            lambda: self.timmy.wait(1),
            lambda: self.twist(.75),
            lambda: self.timmy.wait(1),
            lambda: self.twist(-.75),
            lambda: self.timmy.wait(1),
            lambda: self.sleep()
            ]
        self.auto.run(tiny_dancer)
        self.state = 'dancing'
    

        
