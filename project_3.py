import numpy as np
import pandas as pd

#create csv file for cosine and import
df = pd.read_csv (r'C:\Users\ebnol\Documents\School 2020\Prog For Engineering\Excel Files\Cosine.csv')
print (df)

# t = str(input('Enter nominal torque value and unit:').upper())
# rt = str(input('Enter measured running torque and unit:').upper())
# L = str(input('Enter length of extension in inches:').upper())
# lw =str(input('Enter length of torque wrench in inches:')).upper()
# cos = str(input('Enter cosine decimal equivalent for angle from imported data array').upper())
# AT = (t*L)/(L + lw) + rt
# ATA = (t*L)/(lw +L*(cos)) + rt
continue_yn = 'y'
question = 'ask'

print()
while continue_yn=='y':
     if question == 'ask':
          question = input('Are you using a crowsfoot, extension or both (Y, N)?').upper()
    
     if question == 'Y':
          t = float(input("Enter nominal torque value in inch-lbs: "))
          rt = float(input("Enter measured running torque in inch-lbs: "))
          lw  = float(input("Enter Length of extensions in inches if used, angle of 180 needs added length of crows foot: "))
          l = float(input("Enter Length of toqure wrench in inches: "))
          cos = float(input("Enter cosine decimal equivalent for angle up to 90 degrees.  Use zero for 90 and 270.  Use Zero for 180 and input extension length: "))
          print()
          
          if cos==0:
               ata = ((t+rt)*l)/(lw+l)
          else:
               ata = ((t+rt)*l)/((lw+l)*cos)
          print()
          print(f'Round up to whole number and set torque wrench to: {ata:.2f} in-lbs')
          print()
          
     if continue_yn == "y":
          question = input('Are you using a crowsfoot, extension or both (Y, N)?').upper()

     if question == 'N':
     
          t = float(input("Enter nominal torque value in inch-lbs: "))
          rt = float(input("Enter measured running torque in inch-lbs: "))
          print()          
          nt = t + rt
          print(f'Set torque wrench to: {nt:.2f} in-lbs')
          print() 

if continue_yn == "y":
     print()
     question = input('Are you using a crowsfoot, extension or both (Y, N)?').upper()
          

# runs = (f'Round up to whole number and set torque wrench to: {ata:.2f} in-lbs', f'Set torque wrench to: {nt:.2f} in-lbs')

# results = []
# for i in range(runs):
#      results.append(runs(100))
#      np.hstack(results)