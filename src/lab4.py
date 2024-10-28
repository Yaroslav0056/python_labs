class Chainsaw:
    # 3. Приватні поля
    def __init__(self, name=None, power=None, chain_speed=None):
        # 2, 7. Конструктор з ініціалізацією полів
        self.__name = name
        self.__power = power
        self.__chain_speed = chain_speed

        # 6. Публічні поля
        self.weight = 0  # числове значення
        self.material = ""  # строкове значення

    # 4. Методи доступу до приватних полів (геттери та сеттери)
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

    # 5. Перевизначення методів __str__ та __repr__
    def __str__(self):
        return f"Chainsaw(name={self.__name}, power={self.__power}, chain_speed={self.__chain_speed})"

    def __repr__(self):
        return f"Chainsaw('{self.__name}', {self.__power}, {self.__chain_speed})"

    # 8. Деструктор
    def __del__(self):
        print(f"Chainsaw '{self.__name}' has been deleted")

# 9. Ініціалізація об'єктів
chainsaw1 = Chainsaw("Stihl MS 180", 1500, 9000)
chainsaw2 = Chainsaw("Husqvarna 120", 1600, 8500)
chainsaw3 = Chainsaw("Makita UC4051A", 1800, 9200)

# Виведення значень всіх полів для кожного об'єкта
print(chainsaw1)
print(chainsaw2)
print(chainsaw3)
