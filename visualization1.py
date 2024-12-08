import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\OSHITH\OneDrive - University of Kelaniya\Desktop\lirneasia\monthlySmartData.csv")

df['YearMonth'] = pd.to_datetime(df['YearMonth'], format='%Y-%m')

monthlySummary = df.groupby('YearMonth')[['TOTAL_IMPORT (kWh)_exact', 'TOTAL_EXPORT (kWh)_exact']].sum()

plt.figure(figsize=(10, 6))
plt.plot(monthlySummary.index, monthlySummary['TOTAL_IMPORT (kWh)_exact'], label='Total Import (kWh)', color='#FF8000', marker='o')
plt.plot(monthlySummary.index, monthlySummary['TOTAL_EXPORT (kWh)_exact'], label='Total Export (kWh)', color='#4C1F7A', marker='o')

plt.title('Total Import and Export (kWh) Over Time (Smart-Meter)', fontsize=14)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Energy (kWh)', fontsize=12)
plt.xticks(rotation=45)
plt.legend()

plt.tight_layout()
plt.show()

