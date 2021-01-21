
import pandas as pd
import re

tweets3 = pd.read_csv(f'/Users/mayank/Documents/Online Political Polarization/Followers1/userfollow.csv')

tweets3['following'] = tweets3['following'].astype(str).str[1:]
tweets3['person_name'] = tweets3['person_name'].astype(str).str[1:]




following_weights = (
    tweets3.groupby(["person_name", "following"])
    .size()
    .reset_index()
    .rename(columns={"person_name": "source", "following": "target", 0: "mention_weights"}))

print("N Mentions:", len(following_weights))


all_nodes = set(following_weights['source'].drop_duplicates()) | set(following_weights['target'].drop_duplicates())
all_nodes = sorted(list(all_nodes))
node_map = dict(enumerate(all_nodes))
node_map_inv = {v : k for k, v in node_map.items()}

following_weights['source_id'] = following_weights['source'].map(node_map_inv)
following_weights['target_id'] = following_weights['target'].map(node_map_inv)


nodes = pd.DataFrame(list(node_map.items()), columns=['index', 'username'])
nodes.to_csv(f'/Users/mayank/Documents/Online Political Polarization/Followers1/nodes.csv')
following_weights.to_csv(f'/Users/mayank/Documents/Online Political Polarization/Followers1/edge_weights.csv')

