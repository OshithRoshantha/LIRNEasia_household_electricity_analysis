import pandas as pd

df = pd.read_csv(r"C:\Users\OSHITH\OneDrive - University of Kelaniya\Desktop\lirneasia\EC_2\smart_data\cleanedSmartData.csv")
householdInfo = pd.read_csv(r"C:\Users\OSHITH\OneDrive - University of Kelaniya\Desktop\lirneasia\EC_1\w1_household_information_and_history.csv")

df['DATE'] = pd.to_datetime(df['DATE'])
df['YearMonth'] = df['DATE'].dt.to_period('M')

dfMonthly = df.groupby(['household_ID', 'YearMonth']).agg({
    'TOTAL_IMPORT (kWh)': 'max'
}).reset_index()

dfMonthly['TOTAL_IMPORT (kWh)'] = dfMonthly.groupby('household_ID')['TOTAL_IMPORT (kWh)'].diff().fillna(dfMonthly['TOTAL_IMPORT (kWh)'])

dfAvgImport = dfMonthly.groupby('household_ID')['TOTAL_IMPORT (kWh)'].mean().reset_index()

dfCombined = pd.merge(dfAvgImport, householdInfo, on='household_ID', how='inner')

dfCombined.to_csv(r"C:\Users\OSHITH\OneDrive - University of Kelaniya\Desktop\lirneasia\houseConsumption.csv", index=False)
