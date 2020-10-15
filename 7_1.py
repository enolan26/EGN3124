P = float(P)
V = float(input('Volume (liters):'))
n = 1
r = .0821
T = float(input(T)

from pint import UnitRegistry
ureg = UnitRegistry()
from scipy.constants import convert_temperature

print("Unit Converter")
print()

temperature = str(input('Enter Temperature with a space and unit (C,F,K): ').upper())

pressure = str(input('Enter Pressure with a space and unit (ATM, inHG, PSI): ').upper())

def CalculateVolume(P, n, T):

    R = 0.0821 # Universal Gas Constant on atm.L/(mol.K)
    n = 1
    V = (n*R*T)/P

    return V
    print((n*R*T)/P{:.2f})
    

def get_temp(temperature):
    if temp[-1] == 'F':
        temp = int(temp[:-1])
        T = convert_temperature(temp, 'Fahrenheit', 'Kelvin')
        print(T)
    
    elif temp[-1] == 'C':
        temp = int(temp[:-1])
        T = convert_temperature(temp, 'Celsius', 'Kelvin')
        print(T)

    elif (temp[-1] == 'K' or len(temp.split(' ')) == 1):
        if len(temp.split(' ')) == 1:
            T = int(temp)
            print(T)

    else:
        T = int(temp[:-1])
        print(T)

    return T

def get_pressure(pressure):
    if pressure.split()[1] == 'PSI':
        pressure = int(pressure[:-3])
        P = pressure * ureg.psi
        print(P.to(ureg.atm))

    elif pressure.split()[1] == 'INHG':
        pressure = int(pressure[:-4])
        P = pressure * ureg.inHg
        print(P.to(ureg.atm))

    elif pressure.split()[1] == 'ATM':
        pressure = int(pressure[:-3])
        P = pressure * ureg.atm
        print(P.to(ureg.atm))

    return P
