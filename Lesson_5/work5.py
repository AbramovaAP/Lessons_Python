import pandas as pd

#читаем
df = pd.read_csv('sample_data/california_housing_train.csv')

df.head(n = 10)

df.tail(n = 2)

df.shape # Вывод будет в формате (количество строк, количество столбцов)

df.isnull()

df.isnull().sum()

df.dtypes

df.columns

df['latitude']

print(df['latitude'])
print(df['population'])

df[['latitude', 'population']]

df[df['housing_median_age'] < 20]

df[(df['housing_median_age'] > 20) & (df['total_rooms'] > 2000)]

df[df['housing_median_age'] < 20]['total_rooms']
# или (если необходимо вывести 2 и более столбцов
df[(df['housing_median_age'] > 20) & (df['total_rooms'] > 2000)] [['total_bedrooms', 'total_rooms']]

print(df['population'].max()) # находим максимальное значение в столбце 'population'

print(df['population'].min())

print(df['population'].mean())

print(df['population'].sum())

# находим среднее значение двух столбцов 'population' и 'total_rooms'
df[['population', 'total_rooms']].median()

df.describe()



import seaborn as sns

sns.scatterplot(data=df, x="longitude", y="latitude")

sns.scatterplot(data=df, x="households", y="population", hue="total_rooms")

sns.scatterplot(data=df, x="households", y="population", hue="total_rooms", size = 10)

cols = ['population', 'median_income', 'housing_median_age',
'median_house_value']
g = sns.PairGrid(df[cols])
g.map(sns.scatterplot)

sns.relplot(x="latitude", y="median_house_value", kind="line", data=df)

sns.relplot(x = 'longitude', y = 'median_house_value', kind = 'line', data = df)

sns.scatterplot(data=df, x="latitude", y="longitude", hue="median_house_value")

sns.histplot(data=df, x="median_income")

sns.histplot(data = df, x = 'housing_median_age')

sns.histplot(data=df[df['housing_median_age']>50], x="median_income")

df.loc[df['housing_median_age'] <= 20, 'housing_median_age']

df.loc[df['housing_median_age'] <= 20, 'age_group'] = 'Молодые'
df.loc[(df['housing_median_age'] > 20) & (df['housing_median_age'] <= 50), 'age_group'] = 'Ср. возраст'
df.loc[df['housing_median_age'] > 50, 'age_group'] = 'Пожилые'

df.columns

df.head()

df.groupby('age_group')['median_income'].mean().plot(kind='bar')

df.loc[df['median_income'] > 6, 'income_group'] = 'rich'
df.loc[df['median_income'] < 6, 'income_group'] = 'everyone_else'

df.columns

df.head()

sns.displot(df, x="median_house_value", hue="income_group")
