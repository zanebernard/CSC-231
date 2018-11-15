#import classfile multitemp (celcius, kelvin, farhen)
from multitempclass import *

#create a list of objects that are different temperature types
temps = [Fahrenheit(75), Celsius(40), Kelvin(320), Kelvin(350), Fahrenheit(45), Celsius(27)]

print('------ Temperatures in Fahrenheit, Celsius and Kelvin------------')
for item in temps:
    if item.aboveFreezing():
        print(str(item), 'is above freezing.')
    else:
        print(str(item), 'is below freezing.')
print('------ All temperatures in Fahrenheit------------')
fahren_list = []
for item in temps:
    fahren_list.append(item.convertToFahren())

for temp in fahren_list:
    if temp.aboveFreezing():
        print(str(temp), 'is above freezing.')
    else:
        print(str(temp), 'is below freezing.')

print('------ All temperatures in Celsius------------')
celsius_list = []
for item in temps:
    celsius_list.append(item.convertToCelsius())

for temp in celsius_list:
    if temp.aboveFreezing():
        print(str(temp), 'is above freezing.')
    else:
        print(str(temp), 'is below freezing.')

print('------ All temperatures in Kelvin------------')
kelvin_list = []
for item in temps:
    kelvin_list.append(item.convertToKelvin())

for temp in kelvin_list:
    if temp.aboveFreezing():
        print(str(temp), 'is above freezing.')
    else:
        print(str(temp), 'is below freezing.')

