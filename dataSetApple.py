import pandas as pd
import numpy as np
import datetime
import scipy
# dataYahoo = pd.read_csv ("C:\Users\PC\PycharmProjects\pythonProject4\dataSet\AAPL.csv")
dataYahoo = pd.read_csv ("dataSet/AAPL.csv")
dataYahooDividents = pd.read_csv ('dataSet/AAPL_Dividents.csv',sep = ",")
dataYahooStockSplits = pd.read_csv ('dataSet/AAPL_Stock_Splits.csv')
#dataYahooDividents = pd.read_csv ('dataSet/AAPL_Dividents.csv',sep = ",")
print(dataYahoo.head())
print(dataYahooDividents.head())
print(dataYahooStockSplits.head())
dataCommon = pd.merge (dataYahoo,dataYahooDividents, on="Date", how="outer")
dataCommon = dataCommon.interpolate(method="cubic")
dataCommon = dataCommon.fillna(method="ffill").fillna(method="backfill")
dataCommon = pd.merge (dataCommon,dataYahooStockSplits, on="Date", how="outer")

print(dataCommon)
pd.set_option ("display.max_rows", dataCommon.shape[0]+1)
pd.set_option ("display.max_columns", dataCommon.shape[0]+1)


# Додаємо float дату і час
#def date_time_to_float(val): return np.float64(
    #(val - datetime(2019, 7, 2)).days + (val.hour * 60 + val.minute / (60 * 24)))




#def time_to_float(val): return np.float64(val.hour + val.minute / 60)


#dataConsolidated["date_time_float"] = dataConsolidated['date_time'].apply(lambda val: date_time_to_float(val))
#dataConsolidated["time_float"] = dataConsolidated['time'].apply(lambda val: time_to_float(val))

# dataConsolidated["sunrise_float"] = dataConsolidated['sunrise'].apply(lambda val: time_to_float(val))
# dataConsolidated["sunset_float"] = dataConsolidated['sunset'].apply(lambda val: time_to_float(val))
# dataConsolidated["sunDuration_float"] = dataConsolidated['sunDuration'].apply(lambda val: time_to_float(val))

print(dataCommon.tail(100))

print(dataCommon.tail(100))

# dataCommon = dataCommon.fillna(method="ffill").fillna(method="backfill")
dataCommon = dataCommon.fillna(method="ffill").fillna(value=1)
#  додали 1

dataCommon.to_csv("dataSet/testAAPL.csv")

dataCommon["afterSplit"] = dataCommon["Close"]/dataCommon["Stock Splits"]

dataCommon.to_csv("dataSet/testAAPL_afterSplits.csv")
def Date(val): return np.float64((val - datetime(1980,12,12).date()).days)
dataCommon["Date"] = dataCommon["Date"].apply(lambda val: Date(val))