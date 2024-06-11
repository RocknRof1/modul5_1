class House:
    def __init__(self, name, floor):
        self.name = name
        self.number_or_floor = floor
        
    def go_to(self, new_floor):
        if new_floor <= self.number_or_floor:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print('Такого этажа не существует')


h1 = House('ЖК Лесная тропа', 7)
h2 = House('Урицкого сити', 10)
h1.go_to(5)
h2.go_to(11)