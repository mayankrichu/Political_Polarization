from Tweetsmention import hashtags


def mention(person):
    x=[]
    table=[]
    wordcount=[]
    for i in range(0, len(person)):
        z= person.iloc[i]
        match=re.findall(r"(@[a-zA-Z0-9]*)\s", z[0])
        for j in match:
                
                count=table.index(j)
                wordcount[count]+=1
            else:
                table.append(j)
                wordcount.append(1)

    data=pd.DataFrame({'mentions':table,'count':wordcount})

    return data



for i in range(0,len(hashtags)):
    tweets = pd.read_csv(f'/Users/mayank/Desktop/Tweets/{persons[i]}.csv')
    p = mention(tweets)
    df=pd.DataFrame(p)
    df.to_csv(f'/Users/mayank/Desktop/Tweets/mentions/{persons[i]}.csv')
    dataframe_list.append(p)