class Vehicle:
    def __init__(self, owner, __model, __color,__engine_power):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    __COLOR_VARIANTS = ['серобуромалиновый', 'зачетный', 'черный', 'красненький', 'противный']

    def get_model(self):
        print(f'Модель: {self.__model}')
    def get_horsepower(self):
        print(f'Мощность двигателя:{self.__engine_power}')
    def get_color(self):
        print(f'Цвет:{self.__color}')
    def print_info(self):
        print(f'Модель:{self.__model}\nМощность двигателя:{self.__engine_power}'
              f'\nЦвет:{self.__color}\nВладелец:{self.owner}')
    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}\n')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'синий', 500)

# Изначальные свойства
vehicle1.print_info()
# # Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('РОЗОВЫЙ')
vehicle1.set_color('ЧЕРНЫЙ')
vehicle1.owner = 'Vasyok'
# # Проверяем что поменялось
vehicle1.print_info()