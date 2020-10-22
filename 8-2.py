import pandas
import scipy
import matplotlib.pyplot as plt
import pylint

def get_data_from_webpage(url):
    pandas.read_html('https://thermo.pressbooks.com/chapter/saturation-properties-temperature-table/')
    print(pandas.read_html('https://thermo.pressbooks.com/chapter/saturation-properties-temperature-table/'))
    #will not display
    separate = pandas.read_html('https://thermo.pressbooks.com/chapter/saturation-properties-temperature-table/')
    pandas.concat([separate[0],separate[11]])
    #return pandas.concat([separate[0],separate[11]])
    #print(pandas.concat([separate[0],separate[11]]))