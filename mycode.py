import numpy as np
import pandas as pd
import os

# create a sample DataFrame with column names
data = {'Name':['Alice', 'Bob', 'Charlie'],
        'Age':[25, 30, 35],
        'City':['New York', 'Los Angels', 'Chicago']
        }

df = pd.DataFrame(data)


# Ensure the 'data' directory exits at the root level
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

# Define the file path
file_path = os.path.join(data_dir, 'sample_data.csv')

# save the DataFrame to a CSV file, including columns names
df.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")

