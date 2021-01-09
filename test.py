
import pandas as pd
import re



tweets = pd.read_csv(f'/Users/mayank/Documents/Online Political Polarization/Tweets/#CrackerBan.csv',skiprows=1, sep=',', header=None)

username=[]
mention=[]
def user_name(row):
    username = tweets.iloc[row][7]
    return username

def mentions(row):

    tweet = tweets.iloc[row][10]
    match = re.findall(r"(@[a-zA-Z0-9]*)\s", tweet)

    return match



for i in range(0, len(tweets)):
    if("scroll" in tweets.iloc[i][0]):
        continue
    x = user_name(i)
    y = mentions(i)
    username.append(x)
    mention.append(y)

data = pd.DataFrame({'username': username, 'mentions': mention})

data = data[data.astype(str)['mentions'] != '[]']

data= data.reset_index()


s = data.apply(lambda x: pd.Series(x['mentions']),axis=1).stack().reset_index(level=1, drop=True)

#data = pd.DataFrame({col: data['username'].map(data['mentions']) for col in data})

s.name='mentions'

data = data.drop('mentions', axis=1).join(s)

data=data[['username','mentions']]

print(data)
print(len(data))

