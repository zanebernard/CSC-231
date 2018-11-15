class Money(object):

    def __init__(self, dollars = 0, cents = 0):
        """Initializes two integers into two private variables (__dollars, __cents).
        Inputs are validated and formatted.
        """

        self.validate_input(dollars, cents)   #makes sure the inputs are two positive integers
        self.__dollars = dollars
        self.__cents = cents
        self.format()

    def validate_input(self, dollars, cents):
        """Validates that dollars and cents are positive integers.
        Raises a TypeError or ValueError.
        """
        
        if type(dollars) != type(int()) or type(cents) != type(int()):
            raise TypeError("Only Integer Values.")     #raises a TypeError when the type is not an integer
        if dollars < 0 or cents < 0:
            raise ValueError('Only Positive Values.')   #raises a ValueError when values are negative

    def format(self):
        """Formats variables dollars and cents to be displayed as a dollar amount.
        """
        
        temp_dollars = self.getDollars()    #gets dollars and cents to be used in operation
        temp_cents = self.getCents()

        if temp_cents > 99:         
            temp_cents = temp_cents % 100   #returns a positive, 2 digit integer that is left over from carrying to dollars
                                            #e.g. 234 -> 234 % 100 = 34
        self.setDollars(int(temp_dollars + self.__cents//100))  #returns dollars plus any carried over cents
        self.setCents(float(temp_cents/100))                    #e.g. 2 dollars and 234 cents -> 2 + (234//100) = 4
        
    def __str__(self):
        """Displays object in print function."""
        
        dollar_cents = self.__dollars + self.__cents            
        return '$ ' + str('{0:.2f}'.format(dollar_cents))
                          
    def __repr__(self):
        """Displays object in python shell. See __str__"""
        
        return self.__str__()
    
    def __add__(self, other):
        """Adds the total of self and other and returns the sum.
        Returns the sum as a new Money object."""

        add_cents = int(self.__cents*100 + other.__cents*100)
        add_dollars = int(self.__dollars + other.__dollars)
        
        total_sum = Money(add_dollars, add_cents)   #creates new Money object
                                                    #allows the sum to be utilized further
        return total_sum
        
    def get(self):
        """Gets the whole Money object. Returns dollars and cents as one floating point number.
        """

        return float(self.getDollars()) + float(self.getCents())
    def getDollars(self):
        """Returns value of dollars."""

        return self.__dollars

    def getCents(self):
        """Returns value of cents."""

        return self.__cents

    def setDollars(self, value):
        """Sets the value that is passed to dollars."""
        
        self.__dollars = value

    def setCents(self, value):
        """Setsthe value that is passed to cents.""" 

        self.__cents = value
        
    def getCanadian(self):
        """Converts USD to Canadian dollar. Takes no arguments.
        Returns converted currency as a new object
        """
        
        CAD_dollars = int(self.get() * 1.30)    #gets whole number, multiplies by conversion, and makes an int()
                                                #without the int(), CAD_dollars would not pass through __init__ validation
        if CAD_dollars == 0:        #for "divide by zero" cases
            CAD_cents = int((self.get() * 1.30)*100)    #when CAD_dollars is 0, cents is the only number
        else:
            CAD_cents = int(((self.get() * 1.30) % CAD_dollars)*100)    #gets the remainder of the conversion
                                                                        #multiplied by 100 to make it a whole number
                                                                        
        canada_convert = Money(CAD_dollars, CAD_cents)  #both variables, as positive whole integers, are created into a new object

        return canada_convert
    def getEuro(self):
        """Converts USD into Euro. Takes no arguments.
        Returns converted currency as a new object
        """
                                                        #see getCanandian() for same process
        EUR_dollars = int(self.get() * 0.87)
        if EUR_dollars == 0:
            EUR_cents = int((self.get() * 0.87)*100)
        else:
            EUR_cents = int(((self.get() * 0.87) % EUR_dollars)*100)

        euro_convert = Money(EUR_dollars, EUR_cents)

        return euro_convert
    
    def getColoPeso(self):
        """Converts USD into Colombian Peso. Takes no arguments.
        Returns converted currency as a new object
        """
                                                        #see getCanandian() for same process
        COP_dollars = int(self.get() * 3102.50)
        
        if COP_dollars == 0:
            COP_cents = int((self.get() * 3102.50)*100)
        else:
            COP_cents = int(((self.get() * 3102.50) % COP_dollars)*100)

        colombia_convert = Money(COP_dollars, COP_cents)

        return colombia_convert
