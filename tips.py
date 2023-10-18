import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Загрузка данных
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

# 1) Гистограмма total_bill
plt.figure(figsize=(10, 6))
sns.histplot(df['total_bill'], bins=30, kde=True)
plt.title('Гистограмма total_bill')
plt.show()

# 2) Scatterplot между total_bill и tip
plt.figure(figsize=(10, 6))
sns.scatterplot(x='total_bill', y='tip', data=df)
plt.title('Связь между total_bill и tip')
plt.show()

# 3) График связывающий total_bill, tip, и size
plt.figure(figsize=(10, 6))
sns.scatterplot(x='total_bill', y='tip', hue='size', data=df, palette='viridis', size='size', sizes=(20,200))
plt.title('Связь между total_bill, tip и size')
plt.show()

# 4) Связь между днем недели и размером счета
plt.figure(figsize=(10, 6))
sns.boxplot(x='day', y='total_bill', data=df)
plt.title('Связь между днем недели и размером счета')
plt.show()

# 5) Scatter plot с днем недели по оси y, чаевыми по оси x, и цветом по полу
plt.figure(figsize=(10, 6))
sns.scatterplot(x='tip', y='day', hue='sex', data=df)
plt.title('Чаевые в зависимости от дня недели и пола')
plt.show()

# 6) Box plot с суммой всех счетов за каждый день, разбивая по time (Dinner/Lunch)
plt.figure(figsize=(10, 6))
sns.boxplot(x='day', y='total_bill', hue='time', data=df)
plt.title('Сумма счетов по дням и времени')
plt.show()

# 7) Две гистограммы чаевых на обед и ланч рядом
plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
sns.histplot(df[df['time'] == 'Lunch']['tip'], bins=30, kde=True, color='blue')
plt.title('Чаевые на Lunch')
plt.subplot(1, 2, 2)
sns.histplot(df[df['time'] == 'Dinner']['tip'], bins=30, kde=True, color='red')
plt.title('Чаевые на Dinner')
plt.tight_layout()
plt.show()

# 8) Два scatterplots для мужчин и женщин, с разбивкой по курящим/некурящим
plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
sns.scatterplot(x='total_bill', y='tip', hue='smoker', data=df[df['sex'] == 'Male'])
plt.title('Мужчины: total_bill vs tip')
plt.subplot(1, 2, 2)
sns.scatterplot(x='total_bill', y='tip', hue='smoker', data=df[df['sex'] == 'Female'])
plt.title('Женщины: total_bill vs tip')
plt.tight_layout()
plt.show()
