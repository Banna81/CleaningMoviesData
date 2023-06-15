# 'dataset' holds the input data for this script
# clean power bi data 
import pandas as pd

dataset.loc[((dataset.worldwide_gross.isnull()) & (dataset.genre == 'Action')) , 'worldwide_gross'] = 522182000
dataset.loc[((dataset.worldwide_gross.isnull()) & (dataset.genre == 'Adventure')) , 'worldwide_gross'] = 48313000
dataset.loc[((dataset.worldwide_gross.isnull()) & (dataset.genre == 'Thriller/Suspense')) , 'worldwide_gross'] = 3859444018

dataset.loc[((dataset.domestic_gross.isnull()) & (dataset.genre == 'Action')) , 'domestic_gross'] = 184934250
dataset.loc[((dataset.domestic_gross.isnull()) & (dataset.genre == 'Adventure')) , 'domestic_gross'] = 181137860
dataset.loc[((dataset.domestic_gross.isnull()) & (dataset.genre == 'Thriller/Suspense')) , 'domestic_gross'] = 148418869
dataset.loc[((dataset.domestic_gross.isnull()) & (dataset.genre == 'Drama')) , 'domestic_gross'] = 128897493


df.loc[((df.pclass == 1) & (df.sex == 'male') & (df.age.isnull())) , 'age'] = df.loc[((df.pclass == 1) & (df.sex == 'male') ) , 'age'].mean()
