# TODO:generate json for web visualization
import json
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import re
dir = "C:/Users/YH/Documents/Code/python/IC/IC_DSI_Project/Project_salary/web/json/demo2.json"
wdir1 = "C:/Users/YH/Documents/Code/python/IC/IC_DSI_Project/Project_salary/web/json/job.json"
wdir2 = "C:/Users/YH/Documents/Code/python/IC/IC_DSI_Project/Project_salary/web/json/job_avg.json"
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


def regex(row, symbol):
    ans = 1
    if re.search(symbol, row['Job Description']) is None:
        ans = 0
    return ans


df["writing"] = df.apply(
    regex, axis=1, args=("writ",))
df["analysing"] = df.apply(
    regex, axis=1, args=("analy",))
df["communicating"] = df.apply(
    regex, axis=1, args=("communicat",))
df["collaborating"] = df.apply(
    regex, axis=1, args=("(collaborat)|(teamwork)",))
df["innovating"] = df.apply(
    regex, axis=1, args=("(innovat)|(creat)",))
df["experience"] = df.apply(
    regex, axis=1, args=("experience",))
df["troubleshooting"] = df.apply(
    regex, axis=1, args=("(troubleshoot)|(problem-solving)",))
df["presenting"] = df.apply(
    regex, axis=1, args=("present",))
df["managing"] = df.apply(
    regex, axis=1, args=("management",))
df3 = df.iloc[:, [19, 42, 43, 44, 45, 46, 47, 48, 49, 50]]
pd.set_option('display.max_columns', 1000)
pd.set_option('display.max_rows', 1000)
pd.set_option('display.width', 1000)
print(df3)
# print(re.search("abc","ioabcde"))
