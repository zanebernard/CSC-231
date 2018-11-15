# Fraction Class

class Fraction(object):

    def __init__(self, numerator, denominator):
        self.validateInput(numerator, denominator)
        self.__numerator = numerator
        self.__denominator = denominator
        self.reduce()

    def validateInput(self,numerator, denominator):
        if type(numerator) != type(int()) or type(denominator)!= type(int()):
            raise TypeError("Only Integer Values Accepted")
        if denominator == 0:
            raise ValueError('Invalid Denominator: Divide by Zero Error')

    def __str__(self):
        return str(self.__numerator) + '/' + str(self.__denominator)

    def __repr__(self):
        return str(self.__numerator) + '/' + str(self.__denominator)

    def getNumerator(self):
        return self.__numerator

    def getDenominator(self):
        return self.__denominator

    def get(self):
        return (self.getNumerator(), self.getDenominator())

    def setNumerator(self, value):
        self.__numerator = value

    def setDenominator(self, value):
        if value == 0:
            raise ValueError('Divide by Zero Error')

        self.__denominator = value

    def set(self, numer, denom):
        self.setNumerator(numer)
        self.setDenominator(denom)

    def reduce(self):
        gcd = self.__calcGCD()
        self.__numerator = self.__numerator // gcd
        self.__denominator = self.__denominator // gcd

    def __calcGCD(self):
        a = max(abs(self.__numerator), abs(self.__denominator))
        b = min(abs(self.__numerator), abs(self.__denominator))

        while b != 0:
            temp = b
            b = a % b
            a = temp

        return a

    def __adjust(self, factor):
        self.setNumerator(self.getNumerator() * factor)
        self.setDenominator(self.getDenominator() * factor)

    def copy(self):
        new_frac = Fraction(self.__numerator, self.__denominator)
        return new_frac

    def __neg__(self):
        return Fraction(-self.__numerator, self.__denominator)

    def __add__(self, rfraction):
        numer = self.__numerator * rfraction.getDenominator() + \
                rfraction.getNumerator() * self.__denominator

        denom = self.__denominator * rfraction.getDenominator()

        resultFrac = Fraction(numer, denom)
        resultFrac.reduce()

        return resultFrac

    def __sub__(self, rfraction):

        return self + (-rfraction)

    def __mul__(self, rfraction):
        numer = self.__numerator * rfraction.getNumerator()
        denom = self.__denominator * rfraction.getDenominator()

        resultFrac = Fraction(numer, denom)
        resultFrac.reduce()

        return resultFrac

    def __eq__(self, rfraction):
        temp_frac1 = self.copy()
        temp_frac2 = rfraction.copy()
        temp_frac1.reduce()
        temp_frac2.reduce()

        if temp_frac1.getNumerator() == temp_frac2.getNumerator() and \
                temp_frac1.getDenominator() == temp_frac2.getDenominator():
            return True
        else:
            return False

    def __neq__(self, rfraction):
        return not self.__eq__(rfraction)

    def __lt__(self, rfraction):
        lessthan = False

        temp_frac1 = self.copy()
        temp_frac2 = rfraction.copy()

        temp_frac1.__adjust(temp_frac2.getDenominator())
        temp_frac2.__adjust(temp_frac1.getDenominator())

        if temp_frac1.getNumerator() < temp_frac2.getNumerator():
            lessthan = True

        return lessthan

    def __le__(self, rfraction):
        if self == rfraction or self < rfraction:
            return True
        else:
            return False

    def __gt__(self, rfraction):
        if not (self <= rfraction):
            return True
        else:
            return False

    def __ge__(self, rfraction):
        if not (self < rfraction):
            return True
        else:
            return False


