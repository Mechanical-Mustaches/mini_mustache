import uasyncio as asyncio
from collections import OrderedDict


from mechanical_mustaches.auto import Auto
import mechanical_mustaches.motor
from mechanical_mustaches.stache_station import FakeStation



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
        self.state = None

    def __str__(self):
        return f"nice to meet you comrade I am {self.name}, I am a {self.__class__.__name__}"

    def check(self):
        pass
        # print(f'{self.name} is working')

    def test(self):
        pass

    def report(self):
        return self.state

    def __call__(self, *args, **kwargs):
        if args:
            return f"you want an argument? I'll tell you where you can stick your {args}"
        elif kwargs:
            return f"I love kwargs <3, thank you for the {kwargs}"
        else:
            return f"ring ring hello this is {self.name}, who's there"

    def __repr__(self):
        return f'OG_{self.name}'


class CEO:
    def __init__(self, name):
        self.name = name
        self.agents = OrderedDict()
        self.state = 'disabled'  # auto, test, disabled
        self.autos = []
        self.the_report = []
        self.ss = FakeStation  # stache station

    def talk(self):
        print(f'hello i am {self.name.upper()} nice to meet you {self.agents}')

    def add_agent(self, name: str, agent: Agent):
        outputs = (mechanical_mustaches.motor.Motor)
        self.agents.update({name: {'self': agent, 'outputs': {}}})
        # for out, value in agent.__dict__.items():  # (name, value) = (k, v) --> (key, value)
        #         print(out, value)
        #         if isinstance(value, outputs):
        #             print(f"found name:{out} and value:{value}")
        #             self.agents[name]['outputs'][name] = value

    async def check(self):  # This is the teleopPeriodic function
        for agent in self.agents.values():
            agent['self'].check()
            await asyncio.sleep_ms(0)

    async def test(self):
        for agent in self.agents.values():
            agent['self'].test()
            await asyncio.sleep_ms(0)

    async def auto_check(self):
        for auto in self.autos:
            auto['self'].check()
        await asyncio.sleep_ms(0)

    def run(self, robot):
        self.robot = robot
        self.robot.robotInit()
        self.robot.disabledInit()
        self.find_outputs()
        self.post('BOOT COMPLETE')
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
            self.ss.check()
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

    def make_report(self):
        for name, agent in self.agents.items():
            self.the_report.append([f'{name}_state', agent['self']])
            for o_name, output in agent['outputs'].items():
                self.the_report.append([f'{name}_{o_name}_state', output])

    def report(self):
        return {k:v.report() for k,v in self.the_report}

    def find_outputs(self):
        outputs = (mechanical_mustaches.motor.Motor)
        for name, agent in self.agents.items():
            this_agent = agent["self"]
            for this_name, value in this_agent.__dict__.items():  # (name, value) = (k, v) --> (key, value)
                # print(this_name, value)
                if isinstance(value, outputs):
                    # print(f"found name:{this_name} and value:{value}")
                    self.agents[this_agent.name]['outputs'][this_name] = value
                    
    def set_LCD(self, lcd):
        self.lcd = lcd
    
    def post(self, the_post: str):
        self.lcd.print(the_post)
        print(the_post)


m = CEO('m')

if __name__ == '__main__':
    print('agent')

