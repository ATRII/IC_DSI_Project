# TODO:generate json for web visualization
import json
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)

dir = "C:/Users/YH/Documents/Code/python/IC/IC_DSI_Project/Project_salary/web/json/demo2.json"
with open(dir, 'r', encoding='utf-8') as load_f:
    load_dict = json.load(load_f)

# with open(dir, 'w', encoding='utf-8') as f:
# json.dump(load_dict, f, ensure_ascii=False)
# TODO:
abb_mapping = {'HI': 'Hawaii', 'IA': 'Iowa', 'IL': 'Illinois', 'KS': 'Kansas', 'MA': 'Massachusetts', 'AL': 'Alabama', 'NY': 'New York', 'CO': 'Colorado', 'MT': 'Montana', 'NM': 'New Mexico', 'OK': 'Oklahoma', 'SD': 'South Dakota', 'VA': 'Virginia', 'GA': 'Georgia', 'DE': 'Delaware', 'ID': 'Idaho', 'KY': 'Kentucky', 'MI': 'Michigan', 'NV': 'Nevada', 'NC': 'North Carolina', 'NE': 'Nebraska', 'AK': 'Alaska', 'CA': 'California', 'OR': 'Oregon', 'TN': 'Tennessee',
               'WA': 'Washington', 'IN': 'Indiana', 'ME': 'Maine', 'MS': 'Mississippi', 'NH': 'New Hampshire', 'LA': 'Louisiana', 'MN': 'Minnesota', 'OH': 'Ohio', 'AZ': 'Arizona', 'CT': 'Connecticut', 'PA': 'Pennsylvania', 'TX': 'Texas', 'FL': 'Florida', 'MD': 'Maryland', 'MO': 'Missouri', 'NJ': 'New Jersey', 'SC': 'South Carolina', 'VT': 'Vermont', 'AR': 'Arkansas', 'RI': 'Rhode Island', 'ND': 'North Dakota', 'UT': 'Utah', 'WY': 'Wyoming', 'WI': 'Wisconsin', 'DC': 'Dist. of Columbia'}
data_dir = "C:/Users/YH/Documents/Code/python/IC/IC_DSI_Project/Project_salary/data/data_cleaned_2021.csv"
df = pd.read_csv(data_dir)
df_location = df['Location']
df_location_full = [abb_mapping.get(i.split(', ')[1]) for i in df_location]

print(df_location_full)
