import numpy as np
import pandas as pd
from pandas.io.sql import table_exists

#create csv file for cosine and import
#url=r'https://www.grc.nasa.gov/WWW/K-12/airplane/tablcos.html'
#t_table = pd.read_html(url, header=1)
#t_table = t_table[0]

#cols = t_table.columns
#t_table = t_table.rename({'Angle': 'sinA'}, axis=1)
#t_table = t_table.drop(columns=['Angle', 'cosA', 'Angle', 'cosA', 'Angle', 'cosA', 'Angle', 'cosA'])
#print(t_table)
#print()

while continue_yn=='y':
    
    if question == 'ask':
        question = input('Are you using a crowsfoot and or ann extension (Y, N)?').upper()
    
    if question == 'Y':
              
        t = float(input("Enter nominal torque value in inch-lbs: "))
        
        rt = float(input("Enter measured running torque in inch-lbs: "))
        
        L  = float(input("Enter Length of extensions in inches: "))
        
        LW = float(input("Enter Length of toqure wrench in inches: "))

        cos = float(input("Enter cosine decimal equivalent for angle from imported data array: "))
        
        print()
        
        ata = (t*L)/(LW +L*(cos)) + rt
  
        print(f'Set torque wrench to: {ata:.2f}')
        
        
        continue_yn = input('Would you like enter new data? (Y, N)?').lower()

     elif question == 'N': 

          t = float(input("Enter nominal torque value in inch-lbs: "))
          rt = float(input("Enter measured running torque in inch-lbs: "))
          print()
          torque = t + rt
          print(torque = t + rt)
          continue_yn = input('Would you like enter new data? (Y, N)?').lower()
        


t = str(input('Enter nominal torque value and unit:').upper())
rt = str(input('Enter measured running torque and unit:').upper())
#is an extension being used? prompt next string need if statement if yes.  Y/N
L = str(input('Enter length of extension in inches:').upper())
Lw =str(input('Enter length of torque wrench in inches:')).upper()
#is a crowsfoot being used?  y/n prompt next string elif or and statement
cos = str(input('Enter cosine decimal equivalent for angle from imported data array').upper())
AT = (t*L)/(Lx + LW) + rt
ATA = (t*L)/(LW +L*(cos)) + rt

def calculateTwithext(t, rt, L, Lw):
     #AT = adjusted torque
     AT = (t*L)/(Lx + LW)

def calculateTwithangle(t, rt, L, Lw, cos):
     #ATA = adjusted torque with angle
     #find correct formula
     ATA = (t*L)/(LW +L*(cos))

# while loop to enter more than one value.
#print table with computed values.
