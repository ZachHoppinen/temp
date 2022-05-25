import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.dates as mdates
from matplotlib.animation import FuncAnimation
import numpy as np
import pandas as pd
from os.path import expanduser, join
import pickle

constant_dir = expanduser('~/Documents/temp/src/functions/constants/')

with open(join(constant_dir, 'sensor_heights.pkl'), 'rb') as f:
    sensor_heights = pickle.load(f)

def plottimeseries(ts_arr, sd_arr, t_arr, air_arr):
  # Clear the current plot figure
  plt.clf()
  plt.ylabel("Heights")
  ax = plt.gca()
  fig = plt.gcf()
  ## put in code to do extent/ticks correctly with t of times
  top = 1.4

  x_lims = pd.Series(t_arr).min(),  pd.Series(t_arr).max()
  x_lims = mdates.date2num(x_lims)
  plt.imshow(ts_arr, extent = (x_lims[0],  x_lims[1], 0, top), aspect = 'auto', interpolation= 'gaussian', vmax = 5, vmin = -10)
  ax.xaxis_date()
  date_format = mdates.DateFormatter('%D')

  ax.xaxis.set_major_formatter(date_format)

  # This simply sets the x-axis data to diagonal so it fits better.
  fig.autofmt_xdate()

  plt.plot(t_arr, sd_arr, color = 'red', linewidth = 2)
  plt.colorbar(label = 'Temps $\degree$ C')
  
  if pd.Series(sd_arr).max() > 1.4:
    top = pd.Series(sd_arr).max()
  else:
    top = 1.4

  ax.fill_between(t_arr, sd_arr, top, color = 'grey')
  ax.set_facecolor('grey')

  ax2 = fig.add_axes([0.125 ,0.9,0.62,0.1])
  air_arr = np.array(air_arr)
  ax2.imshow(air_arr.reshape(-1, air_arr.size), extent = (x_lims[0],  x_lims[1], 0, 1), aspect= 'auto', vmax = 5, vmin = -10)
  ax2.set_axis_off()
  ax2.set_ylabel('Free Air')

  plt.title('Measured Temps')

  return plt

def prep_arr(arr, old_arr,sd, old_sd, t, old_t, old_air):
  heights_temps = {sensor_heights[col]: temp for (col, temp) in arr[air_temp_cols].items() if sensor_heights[col] != 2}
  air_temp = arr['air_temp_1']
  arr = np.array(list(heights_temps.values())).reshape(len(heights_temps.values()),-1)

  if old_arr is not None:
    ts_arr = np.hstack([old_arr, arr])
  else:
    ts_arr = arr
  
  if old_air is not None:
    old_air.append(air_temp)
  else:
    old_air = [air_temp]

  if old_sd is not None:
    old_sd.append(sd)
  else:
    old_sd = [sd]
  
  if old_t is not None:
    old_t.append(t)
  else:
    old_t = [t]

  return ts_arr, old_sd, old_t, old_air


def animate(k, df):
    global air_temp_cols
    air_temp_cols = [c for c in df.columns if 'air_temp' in c]
    global ts_arr, sd_arr, t_arr, air_arr
    sd = df.iloc[k]['snow_depth_1']/1000
    t = df.index[k]
    if k%50 == 0:
        print(k)

    if k== 0:
        ts_arr, sd_arr, t_arr, air_arr = None,None,None,None
    ts_arr, sd_arr, t_arr, air_arr = prep_arr(df[air_temp_cols].iloc[k], ts_arr, sd = sd, old_sd = sd_arr ,t= t, old_t = t_arr, old_air = air_arr)
    
    if k!=0:
        plottimeseries(ts_arr, sd_arr, t_arr, air_arr)