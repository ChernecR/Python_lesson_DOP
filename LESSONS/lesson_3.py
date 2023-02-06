class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def main_info(self):
        print(f'привет меня зовут { self.name}'
              f'и мой возрfст {self.age}')
nataly = Human("Наталья", 18)
nataly.main_info()