import pandas as pd

x = pd.read_csv('/Users/mayank/Documents/Online Political Polarization/Followers1/userfollowing.csv')

counts = x['following'].value_counts()

res = x[~x['following'].isin(counts[counts < 3].index)]

res.to_csv(f'/Users/mayank/Documents/Online Political Polarization/Followers1/userfollow.csv',index=False)
