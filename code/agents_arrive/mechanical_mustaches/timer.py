import utime

class Timer():
    """
    ~ reset
    ~ read (how many ms its been)
    
    abs time
    the mystery thing??????
    current time
    """

    
    def __init__(self, name='timmy'):
        self.name = name
        self.lil_sam = 0 # little sammy setpoint :)
    
    def reset(self) -> None:
        self.lil_sam = utime.ticks_ms()
        # print(f'reset to {self.lil_sam}')
        
    
    def read(self) -> float:
        now = utime.ticks_ms()
        store = utime.ticks_diff(now, self.lil_sam)
        # print(f'time is {store / 1000}')
        return store / 1000 
        
    

