"""
Create a class:

class Temperature:
    ...

It should:

Store an internal temperature in Celsius as _celsius.
Provide a celsius property for reading and changing the temperature.
Reject temperatures below -273.15 °C because that would violate the intended valid range.
Provide a read-only fahrenheit property that calculates the equivalent Fahrenheit temperature."""

class Temperature:


    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, temperature):
        if temperature < -273.15:
            raise ValueError("Temp cannot be less than -273.15")

        self._celsius = temperature 

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32
                
temp = Temperature(25)

print(temp.celsius)      # 25
print(temp.fahrenheit)   # 77.0

temp.celsius = 30

print(temp.fahrenheit) 