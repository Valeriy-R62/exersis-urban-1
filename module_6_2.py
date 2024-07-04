class Vehicle:
    __COLOR_VARIANTS = ('blue', 'red', 'black', 'white', 'green')

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = "Fedos"
        self.__model = "Toyota Mark II"
        self.__engine_power = 500
        self.__color = "blue"

    def get_model(self):
        return f"модель: {self.__model}"

    def get_horsepower(self):
        return f"мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"цвет: {self.__color}"

    def print_info(self):
        print(f"Модель:{self.__model}\nМощность двигателя: {self.__engine_power}\n"
              f"Цвет:{self.__color}\nВладелец {self.owner}")

    def set_color(self, new_color):
        self.new_color = "blue"
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f"Невозможно покрасить в {new_color}")

    def set_name(self, owner):
        self.owner = owner


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('owner', '_Vehicle__model', '_Vehicle__engine_power', '_Vehicle__color')
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.set_name("Vasyok")
vehicle1.print_info()