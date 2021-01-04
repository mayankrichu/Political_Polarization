import twint
import nest_asyncio
nest_asyncio.apply()
import pandas

# Configure
username= ['DeShobhaa','mynameswatik','drusawasthi','netshrink','SattarFarooqui','Kaviraj_AFC','ipsvipul_','KPCentralDiv','UmmeSumbulaZuha','FaaridZaeem','sairamogirala', 'parimalaloke', 'libertariandesi', 'Sanjay_Dixit', 'RiseofBurnol', 'TheSkandar','IAnnapurnna','MahaveerVJ','shruttitandon','Sweet_Honeygal' ]
for i in username:
    c = twint.Config()
    c.Username = i
    c.store_csv = True
    c.Output = f"/Users/mayank/Desktop/Tweets/{i}.csv"
    print("successul")
    twint.run.Search(c)

