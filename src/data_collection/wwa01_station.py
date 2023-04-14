'''
### Get all available data from Bogus Basin Site WWA01 from MesoWest

https://mesowest.utah.edu/cgi-bin/droman/meso_base_dyn.cgi?stn=WWA01

using: https://developers.synopticdata.com/mesonet/v2/stations/timeseries/
'''

import requests
import pandas as pd
import pickle
from os.path import join

token = '0191c61bf7914bd49b8bd7a98abb9469'
stid = 'WWA01'
start = '202010010000'
end = '202206010000'
call = f'https://api.synopticdata.com/v2/stations/timeseries?stid={stid}&start={start}&end={end}&token={token}&output=json'

r = requests.get(call)
j = r.json()

hdr = pd.json_normalize(j, 'STATION')
units = j['UNITS']
df = pd.DataFrame.from_dict(j['STATION'][0]['OBSERVATIONS'])
df.loc[:, 'date_time'] = pd.to_datetime(df.date_time)
df = df.set_index('date_time')
for col in df.columns:
    try:
        df.loc[:,col] = df.loc[:,col].astype(float)
    except:
        pass
df.attrs['units'] = units
df.attrs['hdr'] = hdr

data_dir = '/Users/zachkeskinen/Documents/temp/data'
with open(join(data_dir, 'wx', 'wwa01.pkl'), 'wb') as f:
    pickle.dump(df, f)

data.to_parquet('../../data/wx/wwa01.parq')