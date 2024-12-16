class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.model = __model
        self.engine_power = __engine_power
        self.color = __color


    def get_model(self):
        print(f'Модель: {self.model}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.engine_power}')

    def get_color(self):
        print(f'Цвет: {self.color}')

    def print_info(self):
        print(f'Model: {self.model}\n'
              f'Мощность двигателя: {self.engine_power}\n'
              f'Цвет: {self.color}\n\n'
              f'Владелец: {self.owner}\n'
              )

    def set_color(self, new_color):
        self.new_color = new_color.lower()
        if self.new_color in self.__COLOR_VARIANTS:
            print(f'Новый цвет: {new_color}')
        else:
            print(f'Нельзя сменить цвет на {self.new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()
vehicle1.set_color('Green')

vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

vehicle1.print_info()