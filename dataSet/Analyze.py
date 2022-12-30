import datetime

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv ("dataSet/testAAPL_afterSplits.csv")
my = datetime.datetime(1980,12,12)
df['Date']= (df['Date'])
df["DateFloat"] = (pd.to_datetime (df["Date"])-my)
df["DateFloat"] = df["DateFloat"].dt.days
# performance = pd.DataFrame(dict(install_date = 1980-12-12))
# performance.dtypes
# round(performance['Date'].dt.days/30, 2)
df["Log"] = np.log(df["afterSplit"])
plt.scatter(x=df["Date"], y=df["Log"], color='green', alpha=0.3)
plt.xlabel("Date")
plt.ylabel("Closing price")
plt.savefig("Change in closing value by date.png")
plt.cla()
plt.clf()



sns.set(rc={'figure.figsize':(50,30)})
sns.lmplot(x="DateFloat", y="Log", fit_reg=True, palette="PuOr", data=df, line_kws={"color": "red"})
plt.savefig("Сумарна генерація в залежності від протяжності дня2.png")
plt.cla()
plt.clf()

from tabulate import tabulate
#df_for_days = df.groupby('Data').sum()
#df_for_days["afterSplit"] = df.groupby('Data').mean()["afterSplit"]
# print(df_for_days.columns)
print(tabulate(df, headers='keys', tablefmt='psql'))

corr = df.corr()
print(tabulate(corr, headers='keys', tablefmt='psql'))

plt.figure(figsize=(20, 15))
mask = np.zeros_like(corr)
triangle_indices = np.triu_indices_from(mask)
mask[triangle_indices] = True
sns.heatmap(corr, mask=mask, annot=True, annot_kws={"size":17})
sns.set_style("white")
plt.xticks(fontsize=17)
plt.savefig("hitmap.png")
# Corelation close - aftersplit
# Corel log aftersplit
# print ("*"*100)
# print(df["afterSplit"].corr())
print ("*"*100)
print(df.corr())








from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#
#
# def analyze(df: pd.DataFrame = None):
#     df = df or pd.read_csv('data_aver.csv', sep=";")


    # print(df.head(50))
    # print(pd.isnull(df).any())  # аналіз пропуски
    # print(df.info())
    # print(df.describe())
    # print(df.columns)

    # plt.hist(df["genaration"], bins=50, ec='black', color='green')
    # plt.xlabel("gen")
    # plt.ylabel("in 30 sec")
    # plt.savefig("1.png")
    # plt.show()
    #
    #


# plt.figure(figsize=(20, 15))
# plt.scatter(x=(183 + df["day_float"])%365, y=df["genaration"], color='green', alpha=0.3)
# plt.xlabel("days of year")
# plt.ylabel("generation")
# plt.savefig("Генерація за кожну годину на протязі року.png")
# plt.cla()
# plt.clf()



# plt.figure(figsize=(20, 15))
# # plt.scatter(x=df['sunDuration_float'], y=df["genaration"], color='green', alpha=0.3)
# plt.xlabel("sun duration")
# plt.ylabel("sum generation")
# sns.lmplot(x="sunDuration_float", y="genaration", fit_reg=True, palette="PuOr", data=df, line_kws={"color":"red"})
# plt.savefig("sun duration - sum generation.png")
# plt.cla()
# plt.clf()





# plt.figure(figsize=(20, 15))
# plt.scatter(x=df_for_days["sunDuration_float"], y=df_for_days["genaration"], color='green', alpha=0.7)
# plt.xlabel("days of year")
# plt.ylabel("generation")
# plt.savefig("Сумарна генерація в залежності від протяжності дня.png")
# plt.cla()
# plt.clf()
#
# plt.figure(figsize=(20, 15))
# sns.set(rc={'figure.figsize':(50,30)})
# sns.lmplot(x="sunDuration_float", y="genaration", fit_reg=True, palette="PuOr", data=df_for_days, line_kws={"color": "red"})
# plt.savefig("Сумарна генерація в залежності від протяжності дня2.png")
# plt.cla()
# plt.clf()
#
#
# plt.figure(figsize=(20, 15))
# plt.scatter(x=(183 + df_for_days.index) % 365, y=df_for_days["genaration"], color='green', alpha=0.7)
# plt.xlabel("days of year")
# plt.ylabel("generation")
# plt.savefig("Генерація за кожну годину на протязі року(sum of day).png")
# plt.cla()
# plt.clf()
#
#
#
#
#
#
#

