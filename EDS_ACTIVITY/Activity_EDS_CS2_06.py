import pandas as pd 
import numpy as np 

df = pd.read_csv('FIFA22_official_data.csv')
print(df)

# 1. Display the number of rows and columns in the dataset
df.shape

# 2. Show the first 5 rows of the dataset
df.head()

# 3. Get basic information about the dataset (column types, nulls)
df.info()

# 4. Find the number of missing values in each column
df.isnull().sum()

# 5. Get the list of unique nationalities in the dataset
df['Nationality'].unique()

# 6. Count how many players are from Argentina
df[df['Nationality'] == 'Argentina'].shape[0]

# 7. Find the average age of all players
df['Age'].mean()

# 8. Get the maximum and minimum overall ratings
df['Overall'].max(), df['Overall'].min()

# 9. Find the player(s) with the highest overall rating
df[df['Overall'] == df['Overall'].max()][['Name', 'Overall']]

# 10. List top 5 clubs with the most players
df['Club'].value_counts().head(5)

# 11. Find the average potential of players from Brazil
df[df['Nationality'] == 'Brazil']['Potential'].mean()

# 12. Find how many left-footed players are in the dataset
df[df['Preferred Foot'] == 'Left'].shape[0]

# 13. Count players whose wage is more than €100K (strip € and K/M first)
df['Wage_EUR'] = df['Wage'].str.replace('€', '').str.replace('K', 'e3').str.replace('M', 'e6').map(eval)
df[df['Wage_EUR'] > 100000].shape[0]

# 14. Find top 5 players with the highest shooting skill
df[['Name', 'Finishing']].sort_values(by='Finishing', ascending=False).head(5)

# 15. List the number of players in each age group (use value_counts)
df['Age'].value_counts().sort_index()

# 16. Get average strength by nationality (top 5 only)
df.groupby('Nationality')['Strength'].mean().sort_values(ascending=False).head(5)

# 17. Check how many unique clubs are in the dataset
df['Club'].nunique()

# 18. Find all players whose name starts with 'L'
df[df['Name'].str.startswith('L')][['Name']]

# 19. Find players who play for FC Barcelona
df[df['Club'] == 'FC Barcelona'][['Name', 'Club']]

# 20. Count players with jersey number 10
(df['Jersey Number'] == 10).sum()