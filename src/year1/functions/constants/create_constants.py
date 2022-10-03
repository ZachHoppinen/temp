import pickle
from os.path import expanduser, join

sensor_heights = {'air_temp_1':2.0, 
'soil_temp_4': -0.05, 
'soil_temp_3':-0.1, 
'soil_temp_2':-0.15, 
'soil_temp_1':-0.15, 
'air_temp_2':0, 
'air_temp_3':0.05, 
'air_temp_4':0.1, 
'air_temp_5':0.15, 
'air_temp_6':0.2, 
'air_temp_7':0.25, 
'air_temp_8':0.3, 
'air_temp_9':0.35, 
'air_temp_10':0.4, 
'air_temp_11':0.45, 
'air_temp_12':0.5, 
'air_temp_13':0.55, 
'air_temp_14':0.6,
'air_temp_15':0.65,
'air_temp_16':0.7,
'air_temp_17':0.75,
'air_temp_18':0.8,
'air_temp_19':0.85,
'air_temp_20':0.9,
'air_temp_21':0.95,
'air_temp_22':1,
'air_temp_23':1.05,
'air_temp_24':1.1,
'air_temp_25':1.15,
'air_temp_26':1.2,
'air_temp_27':1.25,
'air_temp_28':1.3,
'air_temp_29':1.35,
'air_temp_30':1.4,
'air_temp_1':2}

constant_dir = expanduser('~/Documents/temp/src/functions/constants/')

with open(join(constant_dir, 'sensor_heights.pkl'), 'wb') as f:
    pickle.dump(sensor_heights, f)