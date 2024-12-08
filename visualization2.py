import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\OSHITH\OneDrive - University of Kelaniya\Desktop\lirneasia\monthlySmartData.csv")
df['YearMonth'] = pd.to_datetime(df['YearMonth'], format='%Y-%m')

df = df.rename(columns={
    'TR1_TOTAL_IMPORT (kWh)_exact': 'Day Time Energy (kWh)',
    'TR2_TOTAL_IMPORT (kWh)_exact': 'Peak Time Energy (kWh)',
    'TR3_TOTAL_IMPORT (kWh)_exact': 'Off-Peak Time Energy (kWh)'
})

columnsToPlot = ['Day Time Energy (kWh)', 'Peak Time Energy (kWh)', 'Off-Peak Time Energy (kWh)']
monthlySummary = df.groupby('YearMonth')[columnsToPlot].sum()

customColors = ['#FF8000', '#4C1F7A', '#219B9D']

ax = monthlySummary.plot(kind='area', stacked=True, figsize=(10, 6), color=customColors)
plt.title('Cumulative Energy Consumption per Transformer Over Time (Smart-Meter)')
plt.xlabel('Month')
plt.ylabel('Energy (kWh)')
plt.xticks(rotation=45)
plt.tight_layout()

ax.legend(title='Time Periods')

plt.show()
