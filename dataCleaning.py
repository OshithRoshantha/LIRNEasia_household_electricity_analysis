import pandas as pd
import os

csv_dir = r"C:\Users\OSHITH\OneDrive - University of Kelaniya\Desktop\lirneasia\EC_2\smart_data"
csv_files = [os.path.join(csv_dir, f"file{num}.csv") for num in range(5, 101, 5)]
output_file = os.path.join(csv_dir, "combinedSmartData.csv")

combined_df = pd.DataFrame()

for file in csv_files:
    try:
        print(f"Processing file: {file}")
        df = pd.read_csv(file)
        combined_df = pd.concat([combined_df, df], ignore_index=True)
    except FileNotFoundError:
        print(f"File not found: {file}. Skipping...")
    except Exception as e:
        print(f"Error processing {file}: {e}")
        
missing_values = combined_df.isnull().sum()
print(missing_values)

dfCleaned = combined_df.dropna()
dfCleaned.to_csv(r"C:\Users\OSHITH\OneDrive - University of Kelaniya\Desktop\lirneasia\cleanedSmartData.csv", index=False)