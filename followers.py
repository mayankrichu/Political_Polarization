import tweepy
import time
import pandas as pd
consumer_key ='KfxnhAYl7jSML89fu8iiP9zVs'
consumer_secret='4goum4qn2kjk0QRqmyQ93CKY7ccdkXchG4x884EirVkRyXbOFM'
access_token='1240207427561123840-dAnWqF3eqIMCwW7DTN1HrZpuiQwBYb'
access_token_secret='7YNuVSlf3jr6To7HMeARbuG7Y7cTBWvv0detnXayUnzc0'

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)



persons= ['DeShobhaa','mynameswatik','drusawasthi','netshrink','SattarFarooqui','Kaviraj_AFC','ipsvipul_','KPCentralDiv','UmmeSumbulaZuha','FaaridZaeem','sairamogirala', 'parimalaloke', 'libertariandesi', 'Sanjay_Dixit', 'RiseofBurnol', 'TheSkandar','IAnnapurnna','MahaveerVJ','shruttitandon','Sweet_Honeygal' ]



if(api.verify_credentials):
    print ('We successfully logged in')

list= []

for i in persons:
    ids = []
    for page in tweepy.Cursor(api.friends_ids, screen_name=i).pages():
        print(page)
        ids.extend(page)
        person_id = api.get_user(i)
        screen_id = person_id.id

        time.sleep(60)


    #username=[]
    #for j in page:
        #user = api.get_user(j)
        #screen_name = user.screen_name
        #username.append(screen_name)
    #print(username)
    df = pd.DataFrame(ids)
    df.to_csv(f'/Users/mayank/Documents/Online Political Polarization/Followers1/{screen_id}.csv',index=False)
    print(len(ids))
