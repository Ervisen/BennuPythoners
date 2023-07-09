from math import pi

def area(r):
    areaC = pi*(r**2)
    return areaC
valores = [1, 3, 0, -1, -3, 2+3j, True, 'Hola']

for v in valores:
    areaCalcualda =area(v)
    print('Para el valor', v, 'el área es', areaCalcualda)