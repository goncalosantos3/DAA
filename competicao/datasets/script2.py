import pandas as pd
import re

def toNan(d):
    return ''

def formatDtIso(d):
    s = re.search(r'(\d+\-\d+\-\d+)T(\d+\:\d+)', d)
    return s.group(1) + " " + s.group(2) + ":00 +0000 UTC"

bh = pd.read_csv('old/bragaHour.csv')
bd = pd.read_csv('old/bragaDay.csv')

# Renaming columns
bh.rename(columns={'time': 'dt_iso'}, inplace=True)
bh.rename(columns={'temperature_2m (°C)': 'temp'}, inplace=True)
bh.rename(columns={'relative_humidity_2m (%)': 'humidity'}, inplace=True)
bh.rename(columns={'apparent_temperature (°C)': 'feels_like'}, inplace=True)
bh.rename(columns={'pressure_msl (hPa)': 'sea_level'}, inplace=True)
bh.rename(columns={'surface_pressure (hPa)': 'grnd_level'}, inplace=True)
bh.rename(columns={'cloud_cover (%)': 'clouds_all'}, inplace=True)
bh.rename(columns={'wind_speed_10m (m/s)': 'wind_speed'}, inplace=True)

# Set "Date" feature to merge datasets on
dates = bh['dt_iso']
bh.insert(0, 'Date', dates)
bh['Date'] = bh['Date'].apply(pd.to_datetime)
bh['Date'] = bh['Date'].dt.strftime('%Y-%m-%d')

# Renaming columns
bd.rename(columns={'time': 'dt_iso'}, inplace=True)
bd.rename(columns={'apparent_temperature_min (°C)': 'temp_min'}, inplace=True)
bd.rename(columns={'apparent_temperature_max (°C)': 'temp_max'}, inplace=True)

# Set "Date" feature to merge datasets on
dates = bd['dt_iso']
bd.insert(0, 'Date', dates)

df = pd.merge(bh,bd, on='Date', how='outer')

# Add missing values
x = df['dt_iso_x']
df.insert(0, 'dt', x)
dts = df['dt'].apply(toNan)
df.pop('dt')
df.insert(0, 'dt', dts)

x = df['dt_iso_x']
df.insert(0, 'city_name', x)
cts = df['city_name'].apply(toNan)
df.pop('city_name')
df.insert(0, 'city_name', cts)

x = df['dt_iso_x']
df.insert(0, 'pressure', x)
prs = df['pressure'].apply(toNan)
df.pop('pressure')
df.insert(0, 'pressure', prs)

x = df['dt_iso_x']
df.insert(0, 'rain_1h', x)
rs = df['rain_1h'].apply(toNan)
df.pop('rain_1h')
df.insert(0, 'rain_1h', rs)

x = df['dt_iso_x']
df.insert(0, 'weather_description', x)
wds = df['weather_description'].apply(toNan)
df.pop('weather_description')
df.insert(0, 'weather_description', wds)

# Remove useless column
df.drop('dt_iso_y', inplace=True, axis=1)
df.rename(columns={'dt_iso_x': 'dt_iso'}, inplace=True)

# Format "dt_iso" feature
dts = df['dt_iso'].apply(formatDtIso)
df.pop('dt_iso')
df.insert(0, 'dt_iso', dts)

# Correct "clouds_all" feature
new_min = 0
new_max = 100
df['clouds_all'] = ((df['clouds_all'] - df['clouds_all'].min()) /
                            (df['clouds_all'].max() - df['clouds_all'].min()) *
                            (new_max - new_min) + new_min)
df['clouds_all'] = df['clouds_all'].round(2)

# Reorder columns
df = df[['Date', 'dt','dt_iso', 'city_name','temp','feels_like','temp_min','temp_max','pressure','sea_level','grnd_level','humidity','wind_speed','rain_1h','clouds_all','weather_description']]

# Remove "Date" feature
df.drop('Date', inplace=True, axis=1)

# Write csv file for the "missingMeteoData" dataset
df.to_csv('old/missingMeteoData.csv', index=False)