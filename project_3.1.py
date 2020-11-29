import numpy as np
import pandas as pd
import matplotlib as mp
import matplotlib.pyplot as plt

def calculateplot(torque):

     plt.xlabel("Number of Bolts")
     plt.ylabel("Torque)")
     plt.title('Final torque including running torque.')
     plt.scatter(torque, color='blue')
     plt.show()

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
torque = []
numberbolts = [count]
print()
while continue_yn=='y':
     if question == 'ask':
          question = input('Are you using a crowsfoot, extension or both (Y, N)?').upper()
          print()
    
     if question == 'Y':
          t = float(input("Enter nominal torque value in inch-lbs: "))
          rt = float(input("Enter measured running torque in inch-lbs: "))
          lw  = float(input("Enter Length of extension in inches if used.  Angle of 180 on extension or crowsfoot will need to be entered as extension length: "))
          l = float(input("Enter Length of toqure wrench in inches: "))
          cos = float(input("Enter cosine decimal equivalent for angle up to 90 degrees if angle needed.  Consider 180 as zero degrees and work back to 89 degrees. Use zero for 90 and 270 degrees: "))
                    
          if cos==0:
               ata = ((t+rt)*l)/(lw+l)
          else:
               ata = ((t+rt)*l)/((lw+l)*cos)
          nm1 = ata * .113
          ftlb1 = ata/12
          torque.append(ata)
          numberbolts.append(print(count)
          
          print(f'Round up to whole number and set torque wrench to: {ata:.2f} in-lbs')
          print(f'Round up to whole number and set torque wrench to: {nm1:.2f} Nm')
          print(f'Round up to whole number and set torque wrench to: {ftlb1:.2f} ft-lbs')
          print()

          continue_yn = input('Would you like enter new data? (Y, N)?').lower()
          

     elif question == 'N':
     
          t = float(input("Enter nominal torque value in inch-lbs: "))
          rt = float(input("Enter measured running torque in inch-lbs: "))
          print()          
          nt = t + rt
          nm2 = nt * .113
          ftlb2 = nt/12
          torque.append(nt)
          numberbolts.append(print(count)
          print(f'Set torque wrench to: {nt:.2f} in-lbs')
          print(f'Set torque wrench to: {nm2:.2f} Nm')
          print(f'Set torque wrench to: {ftlb2:.2f} ft-lbs')
          
          print() 
     
          continue_yn = input('Would you like enter new data? (Y, N)?').lower()

          continue_yn = input('Would you like enter new data? (Y, N)?').lower()
          print()
          if continue_yn == 'N':

               break
          
          print()
     elif continue_yn == "y":
          question = 'ask'
          print()



count =0
while x != y:
     count +=1
     print(count)