import pandas as pd
df = pd.read_csv('kclt.csv')
df['date'] = pd.to_datetime(df.date)
df[(df.actual_mean_temp < 20) | (df.actual_mean_temp > 86)].date
df[(df.actual_mean_temp < 20) | (df.actual_mean_temp > 86)
   ][['date', 'actual_mean_temp']]
df.date[0].year
df[df.date > '2015-06-01'].date.head(2)