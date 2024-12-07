# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WYEV0Fb4dFX1kHFYslSlqALbTM3FEZJB
"""



import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

"""**bold text**import data"""

data = pd.read_csv('country_wise_latest.csv')

data.head()

data.columns

data.tail()

data.describe()

"""CHECK FOR NULL VALUES"""

data.isnull().sum()

"""# Relating variables with scatter plots"""

sns.relplot(x="Confirmed", y="Recovered", data=data)

sns.pairplot(data)

h=data.groupby('Country/Region')['Deaths'].sum().nlargest(10)
h



fig, ax = plt.subplots()
ax.bar(h.index, h.values)
ax.set_xlabel('country')
ax.set_ylabel('deaths')
ax.set_title('deaths_by_country')
plt.xticks(rotation=45)
plt.show()

h1=data.groupby('Country/Region')['Deaths'].sum().nsmallest(10)
h1

fig, ax = plt.subplots()
ax.bar(h1.index, h1.values)
ax.set_xlabel('country')
ax.set_ylabel('deaths')
ax.set_title('deaths_by_country')
plt.xticks(rotation=45)
plt.show()

"""#grouping 1 week change by sum of deaths"""

f=data.groupby('1 week change')['Deaths'].sum(20)
f

"""#extracting coloums of cases and deaths by sum"""

e=data[['Confirmed','Deaths']].sum()
e

#bar graph for total cases vs total deaths
plt.bar(e.index, e.values)
plt.xlabel('stats')
plt.ylabel('Values')
plt.title('Case vs Deaths')
plt.show()



"""Top 10 countries with highest number of COVID_19 Cases registered"""

grp_cnt=data.groupby("Country/Region").agg('sum').sort_values("Confirmed", ascending=False).reset_index().head(10)[["Country/Region",'Confirmed','Deaths']]
grp_cnt

# @title Deaths

from matplotlib import pyplot as plt
grp_cnt['Deaths'].plot(kind='hist', bins=20, title='Deaths')
plt.gca().spines[['top', 'right',]].set_visible(False)

plt.figure(figsize=(10, 6))
cases=sns.barplot(data.groupby("Country/Region").agg("sum").sort_values("Confirmed",ascending=False).head(10).reset_index(),x="Country/Region",y='Confirmed')
#plt.ticklabel_format(style="plain",axis="y")
plt.bar_label(cases.containers[0],fmt="%.f")
plt.xticks(rotation=30)
plt.xlabel('Country',fontsize=16)
plt.ylabel("Number of cases registered",fontsize=16)
plt.title("Countries with highest number of cases registered",fontsize=20)
plt.show()

"""Who region with highest number of COVID_19 Cases registered"""

data.groupby("WHO Region").agg("sum").sort_values("Deaths",ascending=False).head().reset_index()[["WHO Region",'Deaths']]

plt.figure(figsize=(10, 6))
br=sns.barplot(data.groupby("WHO Region").agg("sum").sort_values("Deaths",ascending=False).head().reset_index(),x="WHO Region",y='Deaths')
plt.bar_label(br.containers[0],fmt="%.f")
plt.xticks(rotation=45)
plt.xlabel("Region",fontsize=16)
plt.ylabel("Deaths",fontsize=16)
plt.title("Who region with Highest number of deaths",fontsize=20)
plt.show()