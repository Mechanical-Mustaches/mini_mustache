import uasyncio as asyncio
from mechanical_mustaches.auto import Auto

class Agent:
    """
    Agent's Manifesto
    1) An agent is in charge of their own destiny
    2) An Agent does not touch another Agent's variables (it is considered rude!)
    3) ALL agents must report to M, pronto!
    """


    def __init__(self, name, **nomnom):
        self.name = name
        m.add_agent(name, self)  # add self to m's dictionary

    def __str__(self):
        return f"nice to meet you comrade I am {self.name}, I am a {self.__class__.__name__}"

    def check(self):
        pass
        # print(f'{self.name} is working')
        
    def test(self):
        pass

    def rez(self):
        print(vars(self))

    def __call__(self, *args):
        if not args:
            print(f"ring ring hello this is {self.name}, who's there")
        else:
            print(f'so thoughtful you brought me a {args[0]}')

    def __repr__(self):
        return f'OG_{self.name}'

    


class CEO:
    def __init__(self, name):
        self.name = name
        self.agents = {}
        self.state = 'disabled' # auto, test, disabled
        self.autos = []

    def talk(self):
        print(f'hello i am {self.name.upper()} nice to meet you {self.agents}')

    def add_agent(self, name: str, agent: Agent):
        self.agents[name] = agent
#         self.agents[name].update(**{'outputs': {}})

    async def check(self): # This is the teleopPeriodic function
        for agent in self.agents.values():
            agent.check()
            await asyncio.sleep_ms(0)
            
    async def test(self):
        for agent in self.agents.values():
            agent.test()
            await asyncio.sleep_ms(0)
    
    async def auto_check(self):
        for auto in self.autos:
            auto.check()
        await asyncio.sleep_ms(0)
            
    def run(self, robot):
        self.robot = robot
        loop = asyncio.get_event_loop()
        loop.create_task(self.loop())
        loop.run_forever()
                
    async def loop(self):
        while True:
            if self.state == 'teleop':  # auto, test, disabled
                await self.robot.teleopPeriodic()
                await self.robot.robotPeriodic()
            elif self.state == 'auto':
                await self.robot.autonomousPeriodic()
                await self.robot.robotPeriodic()
            elif self.state == 'test':
                await self.robot.testPeriodic()
                await self.robot.robotPeriodic()
            elif self.state == 'disabled':
                await self.robot.disabledPeriodic()
                await self.robot.robotPeriodic()
            await asyncio.sleep_ms(20)
            
                
    def add_auto(self, playbook: list, **kwargs):
        archie = Auto(**kwargs)
        self.autos.append(archie)
        archie.run(playbook, start=False)
        
        
    def retire(self, target):
        print(f"I'm sorry {target} it is time to die!")
        for i in range(len(self.autos)):
            if self.autos[i].name == target:
                self.autos.remove(i)
        
        
    def change_state(self, state):
        print(f'changing state to {state}')
        if state == 'disabled':
            self.robot.disabledInit()
        elif state == 'auto':
            self.autos.clear()
            self.robot.autonomousInit()
        elif state == 'test':
            self.robot.testInit()
        elif state == 'teleop':
            self.robot.teleopInit()
        
        self.state = state
        
        

#     def rez(self):
#         for agent in self.agents.values():
#             agent['self'].rez()

#     def find_outputs(self):
#         outputs = (MM_Motor, MM_Output)
#         for agent in self.agents.values():
#             this_agent = agent["self"]
#             for name, value in vars(this_agent).items():  # (name, value) = (k, v) --> (key, value)
#                 # print(name, value)
#                 if isinstance(value, outputs):
#                     print(f"found {name = } and {value = }")
#                     self.agents[this_agent.name]['outputs'][name] = value
# 

m = CEO('m')

if __name__ == '__main__':
    print('agent')