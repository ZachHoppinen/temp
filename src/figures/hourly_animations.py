import pandas as pd
import numpy as np
from numpy.fft import fft, ifft, fftfreq
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from os.path import join, expanduser, dirname, basename, exists
import pickle
import matplotlib.animation as animation
import matplotlib.dates as mdates
from matplotlib.animation import FuncAnimation
from animation import animate

constant_dir = expanduser('~/Documents/temp/src/functions/constants/')
meas_dir = expanduser('~/Documents/temp/data/snowschool/station/')
model_dir = expanduser('~/Documents/temp/data/snowschool/modeled/')

with open(join(meas_dir, 'df.pkl'), 'rb') as f:
    meas = pickle.load(f)

with open(join(constant_dir, 'sensor_heights.pkl'), 'rb') as f:
    sensor_heights = pickle.load(f)

with open(join(model_dir, 'temps.pkl'), 'rb') as f:
    model = pickle.load(f)

fig_dir = '/Users/zachkeskinen/Documents/temp/figures/'
anim_dir = '/Users/zachkeskinen/Documents/temp/figures/animations/'

anim = animation.FuncAnimation(plt.figure(dpi = 100), animate, frames=len(meas), fargs=(meas,'Measured Temps',),
                              interval=0.1, repeat_delay = 3)
anim.save(join(anim_dir, 'hourly_meas.gif'))

anim = animation.FuncAnimation(plt.figure(dpi = 100), animate, frames=len(model), fargs=(model,'Modeled Temps',),
                              interval=0.1, repeat_delay = 3)
anim.save(join(anim_dir, 'hourly_modeled.gif'))