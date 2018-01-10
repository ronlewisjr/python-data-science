import pandas as pd

df = pd.read_csv('supplies.csv')

# add a new column called total = units * unit price
df['Total'] = df.Units * df['Unit Price']

# show the mean, sum for each rep per region
df.groupby(['Region', 'Rep'])['Total'].agg(['mean', 'sum', 'count'])

# total sold per region
regions = df.groupby(['Region'])['Total'].agg(['sum']).reset_index()
reps = df.groupby(['Region'])['Rep'].unique().to_frame().reset_index()
merged = reps.merge(regions, on='Region').set_index('Region')
merged['count'] = merged.apply(lambda row: len(row['Rep']), axis=1)
merged['normalized'] = merged['sum'] / merged['count']