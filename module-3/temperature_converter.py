class TemperatureConverter:
    _temperature = 0

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value

    def __init__(self, temperature):
        self.temperature = temperature

    def to_c(self):
        return self.f_to_c(self.temperature)

    def to_f(self):
        return self.c_to_f(self.temperature)

    @staticmethod
    def c_to_f(celsius):
        return celsius * 9 / 5 + 32

    @staticmethod
    def f_to_c(fahrenheit):
        return (fahrenheit - 32) * 5/9


