import json
import pandas as pd
import matplotlib.pyplot as plt

with open('agri area.json') as json_file:
    data = json.load(json_file)

years=[]
area=[]

years1=[]
area1=[]

for i in data:
    for j in i:
        if i[j]=='India':
            years.append(i["YEAR"])
            area.append(float(i['VALUE']))
        elif i[j]=='Australia':
            years1.append(i["YEAR"])
            area1.append(float(i['VALUE']))
            
years=years[-6:]
area=area[-6:]

years1=years1[-6:]
area1=area1[-6:]
            
plt.plot(area1, years1,label='Australia')     
plt.plot(area, years,label='India')

plt.legend()
plt.xlabel('Agricultural Area %')
plt.ylabel('Years')
            
