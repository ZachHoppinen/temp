import pandas as pd
import logging
log = logging.getLogger("analysis")
import numpy as np

def clean(csv_fp = '../../wx_data/winter_20_21.csv'):

    clean = True
    meteoio_cols = True
    df = pd.read_csv(csv_fp,sep = ',',header = 6, parse_dates=["Date_Time"],
        date_parser=lambda col: pd.to_datetime(col, utc=True))

    df['date_time'] = pd.to_datetime(df.Date_Time)
    station_id = df.Station_ID.mode()
    df = df.drop(['Date_Time', 'Station_ID'],axis = 1)
    df = df.set_index('date_time')

    for i in range(len(df.columns)):
        col = df.columns[i]
        unit = df.iloc[0][col]
        if unit == 'Celsius':
            df.iloc[0,i] = 'C'
        if unit == 'W/m**2':
            df.iloc[0,i] = 'W/M2'
        if unit == 'm/s':
            df.iloc[0,i] = 'M/S'
        if unit == 'Degrees':
            df.iloc[0,i] = 'DEG'
        if unit == 'volts':
            df.iloc[0,i] = 'VOLT'
        if unit == 'Millimeters':
            df.iloc[0,i] = 'MM'
    df.columns = df.columns.str.replace('set_','')

    # air temperature (TA)
    # relative humidity (RH)
    # wind speed (VW)
    # incoming short wave radiation (ISWR) and/or reflected short wave radiation (RSWR) or net short wave radiation (it must be called NET_SW in Smet files).
    # incoming long wave radiation (ILWR) and/or surface temperature (TSS)
    # precipitation (PSUM) and/or snow height (HS)
    # ground temperature (TSG, if available. Otherwise, you will have to use MeteoIO's data generators to generate a value) or geothermal heat flux
    # snow temperatures at various depths (TS1, TS2, etc if available and only for comparisons, see section Snow and/or soil temperatures)


    wx = df.iloc[1: , :]

    if clean:
        dropped = []
        for col in wx.columns:
            if wx[col].count() <50:
                log.info(f'less than 50 non-NAs in {col}. Dropping...')
                wx = wx.drop([col],axis = 1)
                dropped.append(col)
            if col not in dropped:
                wx[col] = wx[col].apply(pd.to_numeric, errors = 'ignore')

        cols = [i for i in wx.columns if 'air_temp' in i]
        for col in cols:
            wx.loc[wx[col]<-20, col] = np.nan #remove some crazy temp spikes that are almost certaintly not real

        wx.loc[wx['precip_accum_1']>800, 'precip_accum_1'] = wx.loc[wx['precip_accum_1']>800, 'precip_accum_1']/10 #remove some crazy temp spikes that are almost certaintly not real
        wx.loc[wx['snow_depth_1']>2000, 'snow_depth_1'] = wx.loc[wx['snow_depth_1']>2000, 'snow_depth_1']/10 #remove some crazy temp spikes that are almost certaintly not real
        wx.loc[wx['snow_depth_1']==1869.948, 'snow_depth_1'] = np.nan
        wx.loc[abs(wx['snow_depth_1'] - wx['snow_depth_1'].shift(18))>400, 'snow_depth_1'] = np.nan
        wx.loc[:,'snow_depth_1'] = wx.loc[:,'snow_depth_1'].interpolate()

    #make it hard to read column names in plotly
    units = {}
    for i in df.columns:
        units[i] = df[i].iloc[0]
    #df.columns = pd.MultiIndex.from_arrays((units.keys(),units.values()))
    for i in dropped:
        if i in units.keys():
            units.pop(i)
    line = list(units.values())

    wx.iloc[0] = line

    # as_list = wx.index.tolist().copy()
    # as_list[0] = 'Units'
    # wx.index = as_list.copy()

    units = wx.iloc[0]
    wx = wx.iloc[1:]

    for col in wx.columns:
        try:
            wx[col] = pd.to_numeric(wx[col])
        except:
            pass

    wx['snow_depth_1'] = wx['snow_depth_1']/1000
    wx['precip_accum_1'] = wx['precip_accum_1']/1000

    depths = np.arange(0,1.45,0.05)
    values = range(2,31)
    res = {values[i]: round(depths[i],2) for i in range(len(values))}
    for col in wx.columns:
        if 'temp' in col and 'surface' not in col and 'dew' not in col and 'soil' not in col and col != 'air_temp_1':
            depth = res[int(col.replace('air_temp_',''))]
            wx = wx.rename(columns={col : f'airtemp_{depth}'})
        if col == 'air_temp_1':
            wx = wx.rename(columns={col : f'airtemp_2.0'})
    return wx