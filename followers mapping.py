import os
import pandas as pd


person_name = []
following = []

for file in os.listdir("/Users/mayank/Documents/Online Political Polarization/Followers1"):

    person_id = file[:-4]
    x=pd.read_csv(f'/Users/mayank/Documents/Online Political Polarization/Followers1/{file}')
    print(file)
    x = x.iloc[:, 0]
    #df = pd.DataFrame(columns=['person_name','following'])
    for i in range(0,len(x)):
        person_name.append(person_id)
        following.append(x[i])

df = pd.DataFrame({'person_name' : person_name, 'following' : following})
df.to_csv(f'/Users/mayank/Documents/Online Political Polarization/Followers1/user-following.csv',index=False)
