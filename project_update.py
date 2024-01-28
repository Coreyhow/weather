## Final Project Code Merging the Data Sets ## 

## Imports ## 
import pandas as pd

## Filepath and CSVs ## 
energy_rate = 'energy_rate.csv'
new_income = 'new_income.csv'
monthly_energy = 'monthly_tx_energy.csv'
avg_temp = 'Avg_Month_Temp.csv'

filepath = '/Users/corey/Downloads/'

## Reading the CSVs ## 
energy_rate_path = filepath + energy_rate
df_enrate = pd.read_csv(energy_rate_path, delimiter=',')
tx_income_path = filepath + new_income
df_income = pd.read_csv(tx_income_path, delimiter='|')
monthly_energy_path = filepath + monthly_energy
df_mont_energy = pd.read_csv(monthly_energy_path, delimiter=',')
temp_path = filepath + avg_temp
df_avg_temp = pd.read_csv(temp_path, delimiter=',')


## Merging the Data ## 
df_enrate["Month"][df_enrate["Month"]=="January"]="Jan"
df_enrate["Month"][df_enrate["Month"]=="February"]="Feb"
df_enrate["Month"][df_enrate["Month"]=="March"]="Mar"
df_enrate["Month"][df_enrate["Month"]=="April"]="Apr"
df_enrate["Month"][df_enrate["Month"]=="May"]="May"
df_enrate["Month"][df_enrate["Month"]=="June"]="June"
df_enrate["Month"][df_enrate["Month"]=="July"]="July"
df_enrate["Month"][df_enrate["Month"]=="August"]="Aug"
df_enrate["Month"][df_enrate["Month"]=="September"]="Sept"
df_enrate["Month"][df_enrate["Month"]=="October"]="Oct"
df_enrate["Month"][df_enrate["Month"]=="November"]="Nov"
df_enrate["Month"][df_enrate["Month"]=="December"]="Dec"

df_mont_energy["Month"][df_mont_energy["Month"]=="January"]="Jan"
df_mont_energy["Month"][df_mont_energy["Month"]=="February"]="Feb"
df_mont_energy["Month"][df_mont_energy["Month"]=="March"]="Mar"
df_mont_energy["Month"][df_mont_energy["Month"]=="April"]="Apr"
df_mont_energy["Month"][df_mont_energy["Month"]=="May"]="May"
df_mont_energy["Month"][df_mont_energy["Month"]=="June"]="June"
df_mont_energy["Month"][df_mont_energy["Month"]=="July"]="July"
df_mont_energy["Month"][df_mont_energy["Month"]=="August"]="Aug"
df_mont_energy["Month"][df_mont_energy["Month"]=="September"]="Sept"
df_mont_energy["Month"][df_mont_energy["Month"]=="October"]="Oct"
df_mont_energy["Month"][df_mont_energy["Month"]=="November"]="Nov"
df_mont_energy["Month"][df_mont_energy["Month"]=="December"]="Dec"

df_income_energy_merge = df_income.merge(df_enrate, how='inner', on=['Month', 'Year'])
df=df_enrate.merge(df_mont_energy,how="inner",on=['Month','Year'])
df_merge_2 = df_income_energy_merge.merge(df_mont_energy, how='inner', on=['Month', 'Year',])
df_merge_all = df_avg_temp.merge(df_merge_2, how='inner', on=['Month', 'Year','City'])

df_merge_all["Energy Cost"]= df_merge_all["Energy Consumption"]*1000000*df_merge_all["Energy Rate"]/100000000
df_merge_all.dtypes
df_merge_all["Energy Consumption"]=df_merge_all["Energy Consumption"].str.replace(',','')
df_merge_all["Energy Consumption"]=df_merge_all["Energy Consumption"].astype(float)
df_merge_all.drop(labels=["Unnamed: 3","Unnamed: 4","Unnamed: 5","Unnamed: 6","Unnamed: 7","Unnamed: 8","Unnamed: 9","Unnamed: 10","Unnamed: 11","Unnamed: 12","Unnamed: 13","Unnamed: 14"],axis=1,inplace=True)






