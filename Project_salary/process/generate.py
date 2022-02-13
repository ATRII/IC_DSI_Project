# TODO:generate json for web visualization
import json
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)

dir = "C:/Users/YH/Documents/Code/python/IC/IC_DSI_Project/Project_salary/web/json/demo2.json"
wdir1 = "C:/Users/YH/Documents/Code/python/IC/IC_DSI_Project/Project_salary/web/json/job.json"
wdir2 = "C:/Users/YH/Documents/Code/python/IC/IC_DSI_Project/Project_salary/web/json/job_avg.json"
with open(dir, 'r', encoding='utf-8') as load_f:
    load_dict = json.load(load_f)


# TODO:
abb_mapping = {'WV': 'West Virginia', 'PR': 'Puerto Rico', 'HI': 'Hawaii', 'IA': 'Iowa', 'IL': 'Illinois', 'KS': 'Kansas', 'MA': 'Massachusetts', 'AL': 'Alabama', 'NY': 'New York', 'CO': 'Colorado', 'MT': 'Montana', 'NM': 'New Mexico', 'OK': 'Oklahoma', 'SD': 'South Dakota', 'VA': 'Virginia', 'GA': 'Georgia', 'DE': 'Delaware', 'ID': 'Idaho', 'KY': 'Kentucky', 'MI': 'Michigan', 'NV': 'Nevada', 'NC': 'North Carolina', 'NE': 'Nebraska', 'AK': 'Alaska', 'CA': 'California', 'OR': 'Oregon', 'TN': 'Tennessee',
               'WA': 'Washington', 'IN': 'Indiana', 'ME': 'Maine', 'MS': 'Mississippi', 'NH': 'New Hampshire', 'LA': 'Louisiana', 'MN': 'Minnesota', 'OH': 'Ohio', 'AZ': 'Arizona', 'CT': 'Connecticut', 'PA': 'Pennsylvania', 'TX': 'Texas', 'FL': 'Florida', 'MD': 'Maryland', 'MO': 'Missouri', 'NJ': 'New Jersey', 'SC': 'South Carolina', 'VT': 'Vermont', 'AR': 'Arkansas', 'RI': 'Rhode Island', 'ND': 'North Dakota', 'UT': 'Utah', 'WY': 'Wyoming', 'WI': 'Wisconsin', 'DC': 'District of Columbia'}
data_dir = "C:/Users/YH/Documents/Code/python/IC/IC_DSI_Project/Project_salary/data/data_cleaned_2021.csv"
df = pd.read_csv(data_dir)
df_loc = df['Job Location']
# df_loc_full = [abb_mapping.get(i.split(', ')[1]) for i in df_loc]
df_loc_full = [abb_mapping.get(i) for i in df_loc]
job_loc_cnt = {}
for key, value in abb_mapping.items():
    job_loc_cnt[value] = 0
for i in df_loc_full:
    job_loc_cnt[i] = job_loc_cnt.get(i, 0) + 1
wdf1 = load_dict
for unit in wdf1["features"]:
    unit["properties"]["density"] = job_loc_cnt[unit["properties"]["name"]]
# with open(wdir1, 'w', encoding='utf-8') as f:
#     json.dump(wdf1, f, ensure_ascii=True)
df_sa_loc = df.iloc[:, [19, 21]]
for i in range(0, df_sa_loc.shape[0]):
    df_sa_loc.iloc[i, df_sa_loc.columns.get_loc("Job Location")] = abb_mapping[df_sa_loc.iloc[i, df_sa_loc.columns.get_loc("Job Location")]]
avg_salary = {value: 0 for key, value in abb_mapping.items()}
for index, row in df_sa_loc.iterrows():
    avg_salary[row["Job Location"]] += row["Avg Salary(K)"]
for key, value in avg_salary.items():
    if(job_loc_cnt[key]):
        avg_salary[key] /= job_loc_cnt[key]
wdf2 = load_dict
for unit in wdf1["features"]:
    unit["properties"]["density"] = avg_salary[unit["properties"]["name"]]
with open(wdir2, 'w', encoding='utf-8') as f:
    json.dump(wdf2, f, ensure_ascii=True)
