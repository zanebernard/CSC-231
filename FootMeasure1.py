class FootMeasure(object):

    def __init__(self, feet = 0, inches = 0):
        """Initializes the FootMeasure object."""
        
        self.__feet = feet
        self.__inches = inches

    def __repr__(self):

        if self.__inches < 12 and self.__inches > 0:
            return str(self.__feet) + 'ft. ' + str(self.__inches) + 'in.'

        elif self.__inches >=12:
            self.format()
            return str(self.__feet) + 'ft. ' + str(self.__inches) + 'in.'
        
        else:
            return str(self.__feet) + 'ft.'

    def __str__(self):

        return self.__repr__()

    def format(self):
        """Reduces the inches, sets new feet and inches. """
        temp_feet = self.getFeet()
        temp_inches = self.getInches()

        if temp_inches < 12 and temp_inches > 0:
            self.setFeet(temp_feet)
            self.setInches(temp_inches)

        else:
            temp_feet = temp_inches//12
            temp_inches = temp_inches - (temp_feet * 12)

            self.setFeet(temp_feet)
            self.setInches(temp_inches)

    def getFeet(self):
        """Returns the feet measure."""

        return self.__feet

    def getInches(self):
        """Returns the inches measure."""

        return self.__inches

    def setFeet(self, value):
        """Sets the feet measure of FootMeasure object."""

        self.__feet = value

    def setInches(self, value):
        """Sets the inches of FootMeasure object."""

        self.__inches = value

    def copy(self):
        copy_measure = FootMeasure(self.__feet, self.__inches)
        return copy_measure
    
    def __add__(self, other):
        """Returns the resulting addition of self and other."""

        new_feet = self.__feet + other.getFeet()
        new_inches = self.__inches + other.getInches()

        new_measure = FootMeasure(new_feet, new_inches)
        return new_measure

    def __eq__(self, other):
        """Returns True if self is the same length as other.
        Otherwise, returns False.
        """

        temp_self = self.copy()
        temp_other = other.copy()

        temp_self.format()
        temp_other.format()


        return temp_self.getFeet() == temp_other.getFeet() and \
            temp_self.getInches() == temp_other.getInches()

    def __ne__(self, other):
        """Returns True if self is not the same length as other.
        Otherwse, returns False.
        """

        return not self.__eq__(other)   #if eq returns True then ne returns False

    def __lt__(self, other):
        """Returns True if self is shorter than other."""

        temp_self = self.copy()
        temp_other = other.copy()
        temp_self.format()
        temp_other.format()

        return temp_self.getInches() < temp_other.getInches()

    def __le__(self, other):
        
        if self == other or self < other:
            return True
        else:
            return False

    def __gt__(self, other):
        
        if not (self<=other):
            return True
        else:
            return False
        
    def __ge__(self, other):
        if not (self<other):
            return True
        else:
            return False
