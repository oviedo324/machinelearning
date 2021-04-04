import warnings
warnings.simplefilter('ignore', FutureWarning)

# Importa la libreria pandas
from pandas import *

# Importa matplot
import matplotlib.pyplot as plt


data = read_excel('API_SP.POP.TOTL_DS2_en_excel_v2_2163395.xls', sheet_name=0, skiprows=3)
data
print (data)
wait = input("PRESS ENTER TO CONTINUE.")


#en este dataframe se van mostrar las columnas que vamos a ir agregando de la variable data
dfp = DataFrame()
dfp


#dfp['nombre que va tener la coloumna'] = data['nombre de la columna donde se van a copiar los datos']
dfp['Country Name'] = data['Country Name']
dfp
print (dfp)
wait = input("PRESS ENTER TO CONTINUE.")


#dfp['nombre que va tener la coloumna'] = data['nombre de la columna donde se van a copiar los datos']
dfp['Population'] = data['2018']
dfp
print (dfp)
wait = input("PRESS ENTER TO CONTINUE.")





# Lee los datos desde archivo excel
# data = read_excel('GDP_TOT_2018_ALL.xls', sheet_name=0, skiprows=3)

# Descarga la información directamente desde el sitio web
#con el comando sheet_name, seleccionamos la hoja del excel que vamos a trabajar
#con el comando skiprows, indicamos cuando saltos vamos a hacer y desde ese punto mostrar la informacion

#data = read_excel('http://api.worldbank.org/v2/en/indicator/NY.GDP.MKTP.CD?downloadformat=excel', sheet_name=0, skiprows=3)
data = read_excel('API_NY.GDP.MKTP.CD_DS2_en_excel_v2_2163433.xls', sheet_name=0, skiprows=3)
data
print(data)
wait = input("PRESS ENTER TO CONTINUE.")


dfg = DataFrame()
dfg


dfg['Country Name'] = data['Country Name']
dfg


dfg['GDP'] = data['2018']
dfg
print (dfg)
wait = input("PRESS ENTER TO CONTINUE.")



dfm = merge(dfp,dfg,on='Country Name')
dfm
print (dfm)
wait = input("PRESS ENTER TO CONTINUE.")



ip = round(dfm['GDP']/dfm['Population'],2)
dfm['GDP per capita'] = ip
dfm
print(dfm)
wait = input("PRESS ENTER TO CONTINUE.")



dfm['Population'] = round(dfm['Population'] / 100, 2)
dfm
print (dfm)
wait = input("PRESS ENTER TO CONTINUE.")


dfm['GDP'] = round(dfm['GDP'] / 1000000, 2)
dfm
print (dfm)
wait = input("PRESS ENTER TO CONTINUE.")


dfm = dfm.fillna(value=0)
dfm
print (dfm)
wait = input("PRESS ENTER TO CONTINUE.")



dfm.set_index('Country Name',inplace=True)


dff = dfm.drop(['World',
'High income',
'OECD members',
'Post-demographic dividend',
'IDA & IBRD total',
'Low & middle income',
'Middle income',
'IBRD only',
'East Asia & Pacific',
'Upper middle income',
'Europe & Central Asia',
'North America',
'Late-demographic dividend',
'European Union',
'East Asia & Pacific (excluding high income)',
'East Asia & Pacific (IDA & IBRD countries)',
'Euro area',
'Early-demographic dividend',
'Lower middle income',
'Latin America & Caribbean',
'Latin America & Caribbean (excluding high income)',
'Europe & Central Asia (IDA & IBRD countries)',
'Middle East & North Africa',
'South Asia',
'South Asia (IDA & IBRD)',
'Europe & Central Asia (excluding high income)',
'Arab World',
'IDA total',
'Latin America & the Caribbean (IDA & IBRD countries)',
'Sub-Saharan Africa (IDA & IBRD countries)',
'Sub-Saharan Africa',
'Sub-Saharan Africa (excluding high income)',
'Central Europe and the Baltics',
'Pre-demographic dividend',
'IDA only',
'Least developed countries: UN classification',
'IDA blend',
'Fragile and conflict affected situations',
'Heavily indebted poor countries (HIPC)',
'Low income',
'Small states',
'Other small states'])

# Top 10 
dff.sort_values('GDP',ascending=False).head(10)


ax = dff.sort_values('GDP',ascending=False).head(10).plot.bar()
plt.show()

# Resumen estadística 
print (dff.describe())
wait = input("PRESS ENTER TO CONTINUE.")