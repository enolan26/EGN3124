import pandas as pd

url=r'https://thermo.pressbooks.com/chapter/saturation-properties-temperature-table/'
t_table = pd.read_html(url, header=0)
print(t_table)

userInput = str(input('Enter temperature in degrees C:').upper())

