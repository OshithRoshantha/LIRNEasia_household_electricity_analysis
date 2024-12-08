import pandas as pd

df = pd.read_csv(r"C:\Users\OSHITH\OneDrive - University of Kelaniya\Desktop\lirneasia\EC_2\smart_data\cleanedSmartData.csv")

df['DATE'] = pd.to_datetime(df['DATE'])
df['YearMonth'] = df['DATE'].dt.to_period('M')

dfMonthly = df.groupby(['household_ID', 'YearMonth']).agg({
    'TOTAL_IMPORT (kWh)': 'max',
    'TOTAL_EXPORT (kWh)': 'max',
    'TOTAL_IMPORT - PV1 (kWh)': 'max',
    'TOTAL_EXPORT - PV1 (kWh)': 'max',
    'TR1_TOTAL_IMPORT (kWh)': 'max',
    'TR2_TOTAL_IMPORT (kWh)': 'max',
    'TR3_TOTAL_IMPORT (kWh)': 'max',
    'TR1_TOTAL_EXPORT (kWh)': 'max',
    'TR2_TOTAL_EXPORT (kWh)': 'max',
    'TR3_TOTAL_EXPORT (kWh)': 'max',
    'PHASE_A_CURRENT (A)': 'mean',
    'PHASE_A_VOLTAGE (V)': 'mean',
    'FREQUENCY (Hz)': 'mean',
}).reset_index()

cumulative_columns = [
    'TOTAL_IMPORT (kWh)', 'TOTAL_EXPORT (kWh)', 'TOTAL_IMPORT - PV1 (kWh)',
    'TOTAL_EXPORT - PV1 (kWh)', 'TR1_TOTAL_IMPORT (kWh)', 'TR2_TOTAL_IMPORT (kWh)',
    'TR3_TOTAL_IMPORT (kWh)', 'TR1_TOTAL_EXPORT (kWh)', 'TR2_TOTAL_EXPORT (kWh)', 'TR3_TOTAL_EXPORT (kWh)'
]
for col in cumulative_columns:
    dfMonthly[col + '_exact'] = dfMonthly.groupby('household_ID')[col].diff().fillna(dfMonthly[col])

dfMonthly = dfMonthly.drop(columns=cumulative_columns)
print(dfMonthly.head())
dfMonthly.to_csv(r"C:\Users\OSHITH\OneDrive - University of Kelaniya\Desktop\lirneasia\monthlySmartData.csv", index=False)
