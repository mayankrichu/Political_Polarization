
import pandas as pd
import re

#tweets1 = pd.read_csv(f'/Users/mayank/Documents/Online Political Polarization/Tweets/islamophobia in india.csv',skiprows=1, sep=',', header=None)


#tweets2 = pd.read_csv(f'/Users/mayank/Documents/Online Political Polarization/Tweets/#BloodLessEid.csv',skiprows=1, sep=',', header=None)

#tweets3 = pd.read_csv(f'/Users/mayank/Documents/Online Political Polarization/Tweets/#CrackerBan.csv',skiprows=1, sep=',', header=None)
#tweets4 = pd.read_csv(f'/Users/mayank/Documents/Online Political Polarization/Tweets/tolerant india.csv',skiprows=1, sep=',', header=None)
#tweets5 = pd.read_csv(f'/Users/mayank/Documents/Online Political Polarization/Tweets/intolerant india.csv',skiprows=2, sep=',', header=None)
#tweets2 = pd.read_csv(f'/Users/mayank/Documents/Online Political Polarization/Tweets/CrackerBan.csv',skiprows=1, sep=',', header=None)
tweets3 = pd.read_csv(f'/Users/mayank/Documents/Online Political Polarization/Tweets/#BloodLessEid.csv',skiprows=1, sep=',', header=None)


#HappyBirthdayPappu
frames = [tweets3]
tweets = pd.concat(frames)
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



data['mentions'] = data['mentions'].astype(str).str[1:]

unique_users = set(data["username"].drop_duplicates())

mention_df = data[
    (data["mentions"].isin(unique_users)) & (data["username"] != data["mentions"])
]
#print(len(mention_df))


mention_weights = (
    mention_df.groupby(["username", "mentions"])
    .size()
    .reset_index()
    .rename(columns={"username": "source", "mentions": "target", 0: "mention_weights"}))

print("N Mentions:", len(mention_weights))


all_nodes = set(mention_weights['source'].drop_duplicates()) | set(mention_weights['target'].drop_duplicates())
all_nodes = sorted(list(all_nodes))
node_map = dict(enumerate(all_nodes))
node_map_inv = {v : k for k, v in node_map.items()}

mention_weights['source_id'] = mention_weights['source'].map(node_map_inv)
mention_weights['target_id'] = mention_weights['target'].map(node_map_inv)


nodes = pd.DataFrame(list(node_map.items()), columns=['index', 'username'])
nodes.to_csv(f'/Users/mayank/Documents/Online Political Polarization/Tweets/nodes.csv')
mention_weights.to_csv(f'/Users/mayank/Documents/Online Political Polarization/Tweets/edge_weights.csv')