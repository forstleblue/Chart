''''

'''
from bokeh.plotting import figure
from bokeh.tile_providers import WMTSTileSource
from bokeh.plotting import figure, show, output_file
import pandas as pd
import numpy as np

USA = x_range,y_range = ((-13884029,-7453304), (2698291,6455972))

fig = figure(tools='pan, wheel_zoom', x_range=x_range, y_range=y_range)
fig.axis.visible = False

url = 'http://a.basemaps.cartocdn.com/dark_all/{Z}/{X}/{Y}.png'
attribution = "Map tiles by Carto, under CC BY 3.0. Data by OpenStreetMap, under ODbL"

fig.add_tile(WMTSTileSource(url=url, attribution=attribution))

show(fig)

def wgs84_to_web_mercator(df, lon="lon", lat="lat"):
    """Converts decimal longitude/latitude to Web Mercator format"""
    k = 6378137
    df["x"] = df[lon] * (k * np.pi/180.0)
    df["y"] = np.log(np.tan((90 + df[lat]) * np.pi/360.0)) * k
    return df

df = pd.DataFrame(dict(name=["Austin","NYC"],lon=[-97.7431,-74.0059],lat=[30.2672,40.7128]))
wgs84_to_web_mercator(df)

fig.circle(x=df['x'], y=df['y'],fill_color='blue', size=10)
show(fig)