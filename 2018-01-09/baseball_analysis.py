import pandas as pd
import morestats as m

df = pd.read_csv('baseball.csv')

# find average height, weight, age for all players using morestats
avg_height = m.mean(df.Height)
avg_weight = m.mean(df.Weight)
avg_age = m.mean(df.Age)

# group by team name and show mean height, weight, age
teams = df.groupby(['Team']).mean()

# find aggregate stats for Arizona
arizona = teams.loc['ARZ']

# find team with highest average height
tallest_team = teams.idxmax()['Height']

# find a subset of the data
subset = teams.loc['BAL':'CLE', 'Height':'Weight']