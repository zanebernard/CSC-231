#from Fraction import Fraction as Frac
import Fraction
from MixedFraction import *

#frac1 = Frac(4,5)
frac1 = Fraction.Fraction(5,10)
frac2 = Fraction.Fraction(7,8)

frac3 = frac1.copy()

print(frac1)
print(frac3)

result = frac2 - frac1
print(result)
result = frac2 + frac1
print(result)
result = - frac1
print(result)
result = frac2 * frac1
print(result)
print(frac1 < frac2)
print(frac1 <= frac2)
print(frac1 == frac2)
print(frac1 != frac2)
print(frac1 > frac2)
print(frac1 >= frac2)
