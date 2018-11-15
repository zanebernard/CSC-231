class Temperature(object):

    def __init__(self, temperature):
        self.__temperature = temperature

    def getTemperature(self):
        return self.__temperature

    def __str__(self):
        '''Should return a string in the form of "75 degrees Farenheit"'''
        raise NotImplementedError('Method __str__ not implemented')

    def __repr__(self):
        '''Do the same thing as __str__'''
        raise NotImplementedError('Method __repr__ not implemented')

    def aboveFreezing(self):
        '''Return True if the temperature is above the freezing point'''
        raise NotImplementedError('Method aboveFreezing not implemented')

    def convertToFahren(self):
        '''Return a new temperature object that has been converted to degrees Fahrenheit'''
        raise NotImplementedError('Method convertToFahren not implemented')

    def convertToCelsius(self):
        '''Return a new temperature object that has been converted to degrees Celsius'''
        raise NotImplementedError('Method convertToCelsius not implemented')

    def convertToKelvin(self):
        '''Return a new temperature object that has beeen converted to degrees Kelvin'''
        raise NotImplementedError('Method convertToKelvin not implemented')
