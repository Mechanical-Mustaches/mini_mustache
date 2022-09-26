from machine import Pin, PWM
import utime

class Motor:
    def __init__(self, f_pin, r_pin, freq, name):
        
        self.name = name
        self.f_pin = f_pin
        self.r_pin = r_pin
        self.freq = freq
        self.f = PWM(Pin(f_pin), freq=freq)
        self.r = PWM(Pin(r_pin), freq=freq)
                 
        utime.sleep_ms(10)
        self.f.duty(0)
        self.r.duty(0)
        
        print("{} has entered the arena".format(self.name))
         
    def intro(self):
        print("My name is {}, my forward pin is {}, my reverse pin is {}, and my frequency is {}. Also mint chocolate chip is the best ice cream flavor.".format(self.name, self.f_pin, self.r_pin, self.freq))

    # + Speed move forward
    # - Speed move backward
    def set(self, speed):
        """
        Range is -1023 <---> 1023 for Speed
        """
        if speed > 0:
            self.f.duty(speed)  # forward pin
            self.r.duty(0)  # reverse pin
        elif speed < 0:
            self.f.duty(0)
            self.r.duty(abs(speed))
        else:
            self.f.duty(0)
            self.r.duty(0)

    def set_raw(self, speed):
        """
        Range is -1023 <---> 1023 for Speed
        """
        if speed > 0:
            self.f.duty(speed)  # forward pin
            self.r.duty(0)  # reverse pin
        elif speed < 0:
            self.f.duty(0)
            self.r.duty(abs(speed))
        else:
            self.f.duty(0)
            self.r.duty(0)

    def rez(self):
        return f'f:{self.f.duty()}, r:{self.r.duty()}'