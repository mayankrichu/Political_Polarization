from datetime import datetime
import twint
import nest_asyncio
nest_asyncio.apply()

#hashtags= ["#ChowkidaarChorHai", "#BloodLessEid", "intolerant india", "tolerant india", "islamophobia in india", "hindhuphobia in india"]
hashtags = ["#IRejectCAA", "#ISupportCAA"]
if __name__ == "__main__":
    for i in hashtags:
        output_file= f'/Users/mayank/Documents/Online Political Polarization/Tweets/{i}.csv'

        config = twint.Config()
        config.Search= f'{i}'
        config.Lang = "en"
        config.Resume = output_file
        config.Since = str(datetime(2015,1,14))
        config.Until = str(datetime(2020,1,14))
        config.Store_csv= True
        config.Output = output_file
        twint.run.Search(config)