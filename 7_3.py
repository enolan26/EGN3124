

#P = float(input(P)
#n = 1
#r = .0821
#T = float(input(T)

from scipy.constants import convert_temperature
from pint import UnitRegistry
ureg = UnitRegistry()
Q = ureg.Quantity

print("Unit Converter")
print()

# pressure = []
# volume = []
# n = 1
# T = []

def calculateVolume(P, T):
    n = 1 * ureg.mole
    R = Q(0.0821, 'L*atm/(mole*K)') # Universal Gas Constant on atm.L/(mol.K)
    V = (n*R*T)/P

    return V

temp = str(input('Enter Temperature with a space and unit (C,F,K): ').upper())
if temp[-1] == 'F':
    temp = int(temp[:-1])
    T = Q(temp, ureg.degF)
    # print(T)

elif temp[-1] == 'C':
    temp = int(temp[:-1])
    T = Q(temp,ureg.degree_Celsius)
    # print(T)

elif (temp[-1] == 'K' or len(temp.split(' ')) == 1):
    if len(temp.split(' ')) == 1:
        temp = int(temp[:-2])
        T = Q(temp, ureg.kelvin)
        # print(T)

else:
    T = int(temp[:-1])
    # print(T)

pressure = str(input('Enter Pressure with a space and unit (ATM, inHG, PSI): ').upper())

if pressure.split()[1] == 'PSI':
    pressure = int(pressure[:-3])
    P = pressure * ureg.psi
    # print(P.to(ureg.atm))
    P.to(ureg.atm)

elif pressure.split()[1] == 'INHG':
    pressure = int(pressure[:-4])
    #split removes unit by designating position in input -4 indicates position
    P = pressure * ureg.inHg
    #print(P.to(ureg.atm))
    P.to(ureg.atm)

elif pressure.split()[1] == 'ATM':
    pressure = int(pressure[:-3])
    P = pressure

# print()
print(f'Volume is {V:.2f} in Liters')