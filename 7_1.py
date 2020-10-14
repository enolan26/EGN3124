from pint import UnitRegistry
ureg = UnitRegistry()
from scipy.constants import convert_temperature

# p = float(input('Enter Pressure with a space and unit (ATM, inHG, PSI): ').upper())
# v = float(input('Volume (liters):'))
# n = 1
# r = .0821
# t = float(input('Enter Temperature with a space and unit (C,F,K): ').upper())
# v = n * .0821 * t / p

print("Unit Converter");
print();

temperature = str(input('Enter Temperature with a space and unit (C,F,K): ').upper())

pressure = str(input('Enter Pressure with a space and unit (ATM, inHG, PSI): ').upper())

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

def get_pressure():
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

def calc_v():
    p = (P)
    n = 1
    r = .0821
    t = (T)

    v = n * .0821 * t / p
    print()
    print(f'Volume in Liters: {v:.2f}')
