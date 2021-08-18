#%% import dependencies
import pandas
from matplotlib import pyplot
import numpy
import os
import datetime

# %% load datasets


#dfLV = pandas.read_csv(os.path.join(os.path.dirname(__file__), "data\covid_19stats_LV.csv"), delimiter=";", encoding="UTF8")
#dfLV = pandas.read_csv("D:\Course\DA-FInal\data\covid_19_stats_LV.csv", delimiter=";", encoding="UTF8")

dfLV = pandas.read_csv(".\data\covid_19_stats_LV.csv", delimiter=";", encoding="UTF8")
dfLT = pandas.read_csv(".\data\COVID19_stats_LT.csv", delimiter=",", encoding="UTF8")



columnsToDrop = ["TestuSkaits","Ipatsvars","IzarstetoPacientuSkaits","ApstiprinatiVecGr_0-9Gadi","ApstiprinatiVecGr_10-19Gadi","ApstiprinatiVecGr_20-29Gadi","ApstiprinatiVecGr_30-39Gadi","ApstiprinatiVecGr_40-49Gadi","ApstiprinatiVecGr_50-59Gadi","ApstiprinatiVecGr_60-69Gadi","ApstiprinatiVecGr_70GadiUnVairak","ApstiprinatiVecGr_70-79Gadi","ApstiprinatiVecGr_80GadiUnVairak","14DienuKumulativaSaslimstibaUz100000Iedzivotaju", "ApstCOVID19InfSk_NevakcVakcNepab", "ApstCOVID19InfSk_Vakc"]

#remove columns
dfLV.drop(columnsToDrop, 1, inplace=True)

dfLV.rename(columns={"ApstiprinataCOVID19InfekcijaSkaits": "NewInfections",
                "MirusoPersonuSkaits": "Deaths",
                "Datums": "DateValue",
                "IzveselojusosSkaits": "Recovered"}, inplace=True)

# %%
dfLV["DateValue"] = dfLV["DateValue"].apply(lambda x: datetime.datetime.strptime(x, "%Y.%m.%d."), result_type='broadcast')

#datetime.datetime.strptime("2020.03.02.", "%Y.%m.%d.")
# %% clean LT dataset

# %% Add forecasted range

# %% Visualize
