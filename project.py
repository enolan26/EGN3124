import numpy as np
import pandas as pd

#create csv file for cosine and import
df = pd.read_csv (r'C:\Users\ebnol\Documents\School 2020\Prog For Engineering\Excel Files\Cosine.csv')
print (df)

t = str(input('Enter nominal torque value and unit:').upper())
rt = str(input('Enter measured running torque and unit:').upper())
L = str(input('Enter length of extension in inches:').upper())
Lw =str(input('Enter length of torque wrench in inches:')).upper()
cos = str(input('Enter cosine decimal equivalent for angle from imported data array').upper())
AT = (t*L)/(Lx + LW) + rt
ATA = (t*L)/(LW +L*(cos)) + rt

while continue_yn=='y':
     if question == 'ask':
          question = input('Are you using a crowsfoot and or an extension (Y, N)?').upper()
    
     if question == 'Y':
          t = float(input("Enter nominal torque value in inch-lbs: "))
          rt = float(input("Enter measured running torque in inch-lbs: "))
          L  = float(input("Enter Length of extensions in inches enter 0 if extension is not used: "))
          LW = float(input("Enter Length of toqure wrench in inches: "))
          cos = float(input("Enter cosine decimal equivalent for angle from imported data array enter 0 for 90 and 270 degrees: "))
          print()
          ata = (t*L)/(LW +L*(cos)) + rt
          print(f'Round up to whole number and set torque wrench to: {ata:.2f}')
        
        
continue_yn = input('Would you like enter new data? (Y, N)?').lower()

if question == 'N':
     
     t = float(input("Enter nominal torque value in inch-lbs: "))
     rt = float(input("Enter measured running torque in inch-lbs: "))
     print()          
     torque = t + rt
     print(torque = t + rt)

continue_yn = input('Would you like enter new data? (Y, N)?').lower()

     elif question == 'N': 
          print("Values will print in array.")
          
          break
          

def calculateTwithext(t, rt, L, Lw):
     #AT = adjusted torque
     AT = (t*L)/(Lx + LW)

def calculateTwithangle(t, rt, L, Lw, cos):
     #ATA = adjusted torque with angle
     #find correct formula
     ATA = (t*L)/(LW +L*(cos))

# while loop to enter more than one value.
#print table with computed values.
