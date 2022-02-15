# TODO:generate json for web visualization
import json
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import re
import seaborn as sns
dir = "C:/Users/YH/Documents/Code/python/IC/IC_DSI_Project/Project_salary/web/json/demo2.json"
wdir1 = "C:/Users/YH/Documents/Code/python/IC/IC_DSI_Project/Project_salary/web/json/job.json"
wdir2 = "C:/Users/YH/Documents/Code/python/IC/IC_DSI_Project/Project_salary/web/json/job_avg.json"
wdir3 = "C:/Users/YH/Documents/Code/python/IC/IC_DSI_Project/Project_salary/web/json/company.json"
with open(dir, 'r', encoding='utf-8') as LoadF:
    LoadDict = json.load(LoadF)

# TODO:
AbbMapping = {'WV': 'West Virginia', 'PR': 'Puerto Rico', 'HI': 'Hawaii', 'IA': 'Iowa', 'IL': 'Illinois', 'KS': 'Kansas', 'MA': 'Massachusetts', 'AL': 'Alabama', 'NY': 'New York', 'CO': 'Colorado', 'MT': 'Montana', 'NM': 'New Mexico', 'OK': 'Oklahoma', 'SD': 'South Dakota', 'VA': 'Virginia', 'GA': 'Georgia', 'DE': 'Delaware', 'ID': 'Idaho', 'KY': 'Kentucky', 'MI': 'Michigan', 'NV': 'Nevada', 'NC': 'North Carolina', 'NE': 'Nebraska', 'AK': 'Alaska', 'CA': 'California', 'OR': 'Oregon', 'TN': 'Tennessee',
              'WA': 'Washington', 'IN': 'Indiana', 'ME': 'Maine', 'MS': 'Mississippi', 'NH': 'New Hampshire', 'LA': 'Louisiana', 'MN': 'Minnesota', 'OH': 'Ohio', 'AZ': 'Arizona', 'CT': 'Connecticut', 'PA': 'Pennsylvania', 'TX': 'Texas', 'FL': 'Florida', 'MD': 'Maryland', 'MO': 'Missouri', 'NJ': 'New Jersey', 'SC': 'South Carolina', 'VT': 'Vermont', 'AR': 'Arkansas', 'RI': 'Rhode Island', 'ND': 'North Dakota', 'UT': 'Utah', 'WY': 'Wyoming', 'WI': 'Wisconsin', 'DC': 'District of Columbia'}
DataDir = "C:/Users/YH/Documents/Code/python/IC/IC_DSI_Project/Project_salary/data/data_cleaned_2021.csv"
df = pd.read_csv(DataDir)


# df_loc = df['Job Location']
# # DfLocFull = [AbbMapping.get(i.split(', ')[1]) for i in df_loc]
# DfLocFull = [AbbMapping.get(i) for i in df_loc]
# JobLocCnt = {}
# for key, value in AbbMapping.items():
#     JobLocCnt[value] = 0
# for i in DfLocFull:
#     JobLocCnt[i] = JobLocCnt.get(i, 0) + 1
# wdf1 = LoadDict
# for unit in wdf1["features"]:
#     unit["properties"]["density"] = JobLocCnt[unit["properties"]["name"]]
# # with open(wdir1, 'w', encoding='utf-8') as f:
# #     json.dump(wdf1, f, ensure_ascii=True)
# DfSaLoc = df.iloc[:, [19, 21]]
# for i in range(0, DfSaLoc.shape[0]):
#     DfSaLoc.iloc[i, DfSaLoc.columns.get_loc(
#         "Job Location")] = AbbMapping[DfSaLoc.iloc[i, DfSaLoc.columns.get_loc("Job Location")]]
# AvgSalary = {value: 0 for key, value in AbbMapping.items()}
# for index, row in DfSaLoc.iterrows():
#     AvgSalary[row["Job Location"]] += row["Avg Salary(K)"]
# for key, value in AvgSalary.items():
#     if(JobLocCnt[key]):
#         AvgSalary[key] /= JobLocCnt[key]
# wdf2 = LoadDict
# for unit in wdf1["features"]:
#     unit["properties"]["density"] = AvgSalary[unit["properties"]["name"]]
# # with open(wdir2, 'w', encoding='utf-8') as f:
# #     json.dump(wdf2, f, ensure_ascii=True)

# df_cmloc = df['Location']
# DfLocFull = [AbbMapping.get(i.split(', ')[1]) for i in df_cmloc]
# # DfLocFull = [AbbMapping.get(i) for i in df_loc]
# CompanyCnt = {}
# for key, value in AbbMapping.items():
#     CompanyCnt[value] = 0
# for i in DfLocFull:
#     CompanyCnt[i] = CompanyCnt.get(i, 0) + 1
# wdf3 = LoadDict
# for unit in wdf3["features"]:
#     unit["properties"]["density"] = CompanyCnt[unit["properties"]["name"]]
# with open(wdir3, 'w', encoding='utf-8') as f:
#     json.dump(wdf3, f, ensure_ascii=True)
