import pandas as pd
import numpy as np

#headers are genres of the elements in a column
headers = ["EWRB_ID", "Property-Type", "Organization", "Address", "Region", "Postal-Code", "Total-Indoor-Space-(sqft)", "Weekly-Average-Operating-Hours", "Annual-Electricity_Quantity-(kWh)", "Annual-NaturalGas_Quantity-(m3)", "Annual-GHG-Emissions-(kgCO2e)", "Energy-Intensity-(ekWh/sqft)", "Ener_Star_Certs"]
df = pd.read_excel(r'database\data.xlsx', names=headers) #fetch the database in the form of excel file
df.replace("?", np.nan, inplace = True) #replace missing data with NAN
#change the unit of a column for better presentation
df["Annual-Electricity_Quantity-(MWh)"] = df["Annual-Electricity_Quantity-(kWh)"]/1000 
df[["Annual-Electricity_Quantity-(MWh)"]] = df[["Annual-Electricity_Quantity-(MWh)"]].astype("int")
#assume the desired data we want are EWRB_ID, Annual-Electricity-Quantity(MWh), and Address
df.sort_values(by="EWRB_ID", ascending=True, inplace=True) #sort the database by EWRB_ID(example)
###shovel desired data to a new dataframe###
d = {"EWRB_ID": [], "AEQ(Mwh)":[], "Address":[]}
for i in range(len(df.index)):
    d["EWRB_ID"].append(df["EWRB_ID"][i])
    d["AEQ(Mwh)"].append(df["Annual-Electricity_Quantity-(MWh)"][i])
    d["Address"].append(df["Address"][i])

df_new = pd.DataFrame(data=d)
df_new.to_csv('database.csv', sep='\t') #store the new dataframe with the desired data to a csv file