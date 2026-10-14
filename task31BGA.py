class Temperature:
    def __init__(self, celsius: float = 0.0):
        self._celsius = float(celsius)

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float):
        self._celsius = float(value)

    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value: float):
        self._celsius = (float(value) - 32) * 5 / 9

    @property
    def kelvin(self) -> float:
        return self._celsius + 273.15

    @kelvin.setter
    def kelvin(self, value: float):
        self._celsius = float(value) - 273.15



t = Temperature(25)
print(f"{t.celsius}C, {t.fahrenheit}F, {t.kelvin}K")  
t.fahrenheit = 32
print(f"После установки 32F: {t.celsius}C") 
