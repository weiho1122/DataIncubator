
# coding: utf-8

# In[37]:

from bokeh.sampledata import us_states
from bokeh.plotting import *
import pandas as pd
from bokeh.palettes import GnBu9 as palette
from bokeh.models import LinearColorMapper, LogTicker, ColorBar

us_states = us_states.data.copy()
df = pd.read_csv(r'/home/jeffrey/DataIncubator/2015.csv')

del us_states["HI"]
del us_states["AK"]

state_xs = [us_states[code]["lons"] for code in us_states]
state_ys = [us_states[code]["lats"] for code in us_states]

colors = palette
color_mapper = LinearColorMapper(palette, low=1, high=10)

state_color = []
for state_id in us_states:
    rate = df.loc[df['State'] == state_id, 'MMBtu_2015_Spring'].values[0]
    idx = int(rate/140000000)-2
    state_color.append(colors[idx])

output_file("choropleth.html", title="US Total Energy Consumption 2011 Winter")

p = figure(title="US Total Energy Consumption 2015 Spring by State in 10e8 MMBtu", toolbar_location="left",
    plot_width=1100, plot_height=700)

p.patches(state_xs, state_ys, fill_color=state_color, fill_alpha=1,
    line_color="#884444", line_width=2)

color_bar = ColorBar(color_mapper=color_mapper, ticker=LogTicker(),
                     label_standoff=12, border_line_color=None, location=(0,0))

p.add_layout(color_bar, 'right')

show(p)


# In[ ]:



