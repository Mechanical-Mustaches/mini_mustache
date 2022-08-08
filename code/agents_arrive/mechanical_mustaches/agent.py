
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

    def chk(self):
        pass
        # print(f'{self.name} is working')

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

    def talk(self):
        print(f'hello i am {self.name.upper()} nice to meet you {self.agents}')

    def add_agent(self, name: str, agent: Agent):
        self.agents[name] = agent
#         self.agents[name].update(**{'outputs': {}})

    def chk(self): # This is the teleopPeriodic function
        for agent in self.agents.values():
            agent.chk()


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