from tempclass import *

class Fahrenheit(Temperature):

    def __init__(self, temperature):
        Temperature.__init__(self, temperature)

    def __str__(self):

        return str(self.getTemperature()) + ' F'
    
    def __repr__(self):

        return self.__str__()
    
    def aboveFreezing(self):
        '''Return True if the temperature is above the freezing point'''
        if self.getTemperature() >= 32:
            return True
        else:
            return False

    def convertToFahren(self):
        '''Return a new temperature object that has been converted to degrees Fahrenheit'''
        fahrenheit = Fahrenheit(self.getTemperature())
        return fahrenheit

    def convertToCelsius(self):
        '''Return a new temperature object that has been converted to degrees Celsius'''
        fahrenheit = self.getTemperature()
        celsius = Celsius(round((fahrenheit - 32) * (5/9)))
        return celsius

    def convertToKelvin(self):
        '''Return a new temperature object that has beeen converted to degrees Kelvin'''
        fahrenheit = self.getTemperature()
        kelvin = Kelvin(round((fahrenheit - 32) * (5/9) + 273.15))
        return kelvin
    
class Celsius(Temperature):

    def __init__(self, temperature):
        Temperature.__init__(self, temperature)

    def __str__(self):

        return str(self.getTemperature()) + ' C'
    
    def __repr__(self):

        return self.__str__()

    def aboveFreezing(self):
        '''Return True if the temperature is above the freezing point'''
        if self.getTemperature() >= 0:
            return True
        else:
            return False

    def convertToFahren(self):
        '''Return a new temperature object that has been converted to degrees Fahrenheit'''
        celsius = self.getTemperature()
        fahrenheit = Fahrenheit(round((celsius * (9/5)) + 32))
        return fahrenheit

    def convertToCelsius(self):
        '''Return a new temperature object that has been converted to degrees Celsius'''
        celsius = Celsius(self.getTemperature())
        return celsius

    def convertToKelvin(self):
        '''Return a new temperature object that has beeen converted to degrees Kelvin'''
        celsius = self.getTemperature()
        kelvin = Kelvin(round(celsius + 273.15))
        return kelvin


class Kelvin(Temperature):
    
    def __init__(self, temperature):
        Temperature.__init__(self, temperature)

    def __str__(self):

        return str(self.getTemperature()) + ' K'
    
    def __repr__(self):

        return self.__str__()

    def aboveFreezing(self):
        '''Return True if the temperature is above the freezing point'''
        if self.getTemperature() >= 273:
            return True
        else:
            return False

    def convertToFahren(self):
        '''Return a new temperature object that has been converted to degrees Fahrenheit'''
        kelvin = self.getTemperature()
        fahrenheit = Fahrenheit(round((kelvin - 273.15) * (9/5) + 32))
        return fahrenheit

    def convertToCelsius(self):
        '''Return a new temperature object that has been converted to degrees Celsius'''
        kelvin = self.getTemperature()
        celsius = Celsius(round(kelvin - 273.1))
        return celsius

    def convertToKelvin(self):
        '''Return a new temperature object that has beeen converted to degrees Kelvin'''
        kelvin = Kelvin(self.getTemperature())
        return kelvin
