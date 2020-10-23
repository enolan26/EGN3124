from pandas.io.html import read_html

page = 'https://thermo.pressbooks.com/chapter/saturation-properties-temperature-table/'
site_content = read_html(page,  attrs={"class":"site_content"})
print("extracted {num} site_content".format(num=len(site_content)))