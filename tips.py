import math

import pandas as pd
import numpy as np
import streamlit as st

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

path = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'

tips = pd.read_csv(path)

st.write("""
         
#         Исследование по чаевым
         
""")
         
fig1, ax1 = plt.subplots()
sns.histplot(data=tips['total_bill'], bins=10) 
plt.xlabel("Total Bill")
plt.ylabel("Count")
plt.title("Histogram of Total Bill")
st.pyplot(fig1)

fig2, ax2 = plt.subplots()
sns.scatterplot(data=tips, x="total_bill", y="tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.title("Scatterplot of Total Bill vs. Tip")
st.pyplot(fig2)

fig3, ax3 = plt.subplots()
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="size")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.title("Scatterplot of Total Bill, Tip, and Size")
plt.legend(title="Size")
st.pyplot(fig3)

fig4, ax4 = plt.subplots()
sns.barplot(data=tips, x="day", y="total_bill", errorbar=None)
plt.xlabel("Day of the Week")
plt.ylabel("Average Total Bill")
plt.title("Average Total Bill by Day of the Week")
st.pyplot(fig4)

fig5, ax5 = plt.subplots()
sns.scatterplot(x="tip", y="day", hue="sex", data=tips, palette={"Male": "b", "Female": "r"}, s=100)
plt.xlabel("Чаевые")
plt.ylabel("День недели")
plt.title("Scatter Plot с днем недели, чаевыми и полом")
st.pyplot(fig5)

fig6, ax6 = plt.subplots()
sns.boxplot(x="day", y="total_bill", hue="time", data=tips, palette="coolwarm")
plt.xlabel("День")
plt.ylabel("Общий счет")
plt.title("Box Plot общего счета по дням и времени приема пищи")
st.pyplot(fig6)

fig7, ax7 = plt.subplots()
plt.subplot(1, 2, 1)
sns.histplot(data=tips[tips['time'] == 'Lunch'], x='tip', kde=True, color='blue')
plt.title("Гистограмма чаевых на обед")
plt.xlabel("Чаевые")
plt.ylabel("Частота")
plt.subplot(1, 2, 2)
sns.histplot(data=tips[tips['time'] == 'Dinner'], x='tip', kde=True, color='green')
plt.title("Гистограмма чаевых на ужин")
plt.xlabel("Чаевые")
plt.ylabel("Частота")
plt.tight_layout()
st.pyplot(fig7)

fig8, ax8 = plt.subplots()
plt.subplot(1, 2, 1)
sns.scatterplot(data=tips[tips['sex'] == 'Male'], x='total_bill', y='tip', hue='smoker', palette='Set1')
plt.title("Scatter plot для мужчин")
plt.xlabel("Размер счета")
plt.ylabel("Чаевые")
plt.subplot(1, 2, 2)
sns.scatterplot(data=tips[tips['sex'] == 'Female'], x='total_bill', y='tip', hue='smoker', palette='Set1')
plt.title("Scatter plot для женщин")
plt.xlabel("Размер счета")
plt.ylabel("Чаевые")
plt.tight_layout()
st.pyplot(fig8)
