class Chainsaw:
    def __init__(self, name=None, power=None, chain_speed=None):
        self.__name = name
        self.__power = power
        self.__chain_speed = chain_speed

        self.weight = 0  
        self.material = ""  

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_power(self):
        return self.__power

    def set_power(self, power):
        self.__power = power

    def get_chain_speed(self):
        return self.__chain_speed

    def set_chain_speed(self, chain_speed):
        self.__chain_speed = chain_speed

    def __str__(self):
        return f"Chainsaw(name={self.__name}, power={self.__power}, chain_speed={self.__chain_speed})"

    def __repr__(self):
        return f"Chainsaw('{self.__name}', {self.__power}, {self.__chain_speed})"

    def __del__(self):
        print(f"Chainsaw '{self.__name}' has been deleted")

chainsaw1 = Chainsaw("Stihl MS 180", 1500, 9000)
chainsaw2 = Chainsaw("Husqvarna 120", 1600, 8500)
chainsaw3 = Chainsaw("Makita UC4051A", 1800, 9200)

print(chainsaw1)
print(chainsaw2)
print(chainsaw3)
