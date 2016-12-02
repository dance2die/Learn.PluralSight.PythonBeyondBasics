class TemperatureConverter:
    @staticmethod
    def c_to_f(celsius):
        return celsius * 9 / 5 + 32

    @staticmethod
    def f_to_c(fahrenheit):
        return (fahrenheit - 32) * 5/9


