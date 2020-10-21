import pandas
import scipy
import matplotlib.pyplot as plt

def get_data_from_webpage(url):
    # This returns a list of dataframes
    # if there are multiple tables in html, we would need multiple dataframes
    # If there is one table in html, we only need one
    url = thermo.pressbooks.com/chapter/saturation-properties-temperature-table
    #syntax error on anything other than above
    t_table = pandas.read_html(url, header=0)
    # Element 0 is the DataFrame we want?  how does he know?
    #which table is correct on webpage?
    return t_table[0]
    print(t_table[0])

userInput = str(input('Enter temperature in degrees C:').upper())
#input string to pass in temp to get user output

#call to csv file to grab column for each?  need to designate 2nd row cell?  how?
#what file directory?
pressureMpa = pandas.read_csv("assign8temp.csv")
volumeVf = pandas.read_csv("assign8temp.csv")
energyUf = pandas.read_csv("assign8temp.csv")
enthalpyHf = pandas.read_csv("assign8temp.csv")
enthropySf = pandas.read_csv("assign8temp.csv")
#print(???)

pressureMpa.describe()
volumeVf.describe()
energyUf.describe()
enthalpyHf.describe()
enthropySf.describe()
#data frame

"""
loc based on labels
iloc based on locations (indexes)
"""

pressureMpa.head()
volumeVf.head()
energyUf.head()
enthalpyHf.head()
enthropySf.head()
#data frame?

pressureMpa = MPa.data.iloc[: ,25]

aPressure = MPa.data.iloc[[25], [2]]
# number in bracket?  don't know what that does yet.
# need to do one of these for each othe the above?

plt.scatter(MPa)
print(MPa)










