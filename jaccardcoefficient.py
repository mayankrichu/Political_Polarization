import pandas as pd

import numpy as np
persons= ['DeShobhaa','mynameswatik','drusawasthi','netshrink','SattarFarooqui','Kaviraj_AFC','ipsvipul_','KPCentralDiv','UmmeSumbulaZuha','FaaridZaeem','sairamogirala', 'parimalaloke', 'libertariandesi', 'Sanjay_Dixit', 'RiseofBurnol', 'TheSkandar','IAnnapurnna','MahaveerVJ','shruttitandon','Sweet_Honeygal' ]

'''merge_data=[]
for i in range(0,len(persons)):
    file = pd.read_csv(f'/Users/mayank/Desktop/Tweets/mentions/{persons[i]}.csv')
    merge_data.append(file)'''
count=1
for i in range(0,20):
    file = pd.read_csv(f'/Users/mayank/Desktop/Tweets/mentions/{persons[i]}.csv')

    for j in range(0, 20):

        file1 = pd.read_csv(f'/Users/mayank/Desktop/Tweets/mentions/{persons[j]}.csv')
        c=pd.merge(file,file1, how='outer', indicator=True, on='mentions')
        d = c.loc[c['_merge'] == 'left_only', ['mentions','count_x']]
        e = c.loc[c['_merge'] == 'right_only', ['mentions','count_y']]
        sum=d['count_x'].sum()+e['count_y'].sum()


        x=file.merge(file1, on='mentions')

        minimum=x[["count_x", "count_y"]].min(axis=1)
        maximum=x[["count_x", "count_y"]].max(axis=1)
        sum=(file['count'].sum()+file1['count'].sum())
        minimumsum=(minimum.sum())
        maximumsum=(maximum.sum())
        totalsum=maximumsum+sum

        print(f"between{i}*****{persons[i]}and******* {j}{persons[j]}")
        jaccardc=minimumsum/totalsum

        print(jaccardc)
