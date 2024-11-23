import pandas as pd
df = pd.read_csv('DataAnalyst.csv')
df.dropna()
print(df.info())
# Заробітна плата == Рейтинг

print(df["Job Description"])

# print(df.groupby(by = 'Rating')['Job Title'])

