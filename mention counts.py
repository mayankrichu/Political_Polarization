import pandas as pd
import re
import numpy as np
persons= ['DeShobhaa','mynameswatik','drusawasthi','netshrink','SattarFarooqui','Kaviraj_AFC','ipsvipul_','KPCentralDiv','UmmeSumbulaZuha','FaaridZaeem','sairamogirala', 'parimalaloke', 'libertariandesi', 'Sanjay_Dixit', 'RiseofBurnol', 'TheSkandar','IAnnapurnna','MahaveerVJ','shruttitandon','Sweet_Honeygal' ]


def count_mention(file):
    x=[]
    table=[]
    wordcount=[]
    for i in range(0, len(tweets)):
        z= tweets.iloc[i]

        match=re.findall(r"(@[a-zA-Z0-9]*)\s", z[0])
        for j in match:
            if j in table:
                count=table.index(j)
                wordcount[count]+=1
            else:
                table.append(j)
                wordcount.append(1)

    data=pd.DataFrame({'mentions':table,'count':wordcount})

    return data

dataframe_list=[]
for i in range(0,len(persons)):
    tweets = pd.read_csv(f'/Users/mayank/Desktop/Tweets/{persons[i]}.csv', sep='delimiter', header=None)
    p = count_mention(tweets)
    df=pd.DataFrame(p)
    df.to_csv(f'/Users/mayank/Desktop/Tweets/mentions/{persons[i]}.csv')
    dataframe_list.append(p)

'''
jaccardcoefficient =[]
count=0
for j in range(0, len(dataframe_list)):
    for k in range(0, len(dataframe_list)):
        x=np.where((dataframe_list[j]['mentions']==dataframe_list[k]['mentions']), dataframe_list[j]['count'],0)
        print(x)

  '''

