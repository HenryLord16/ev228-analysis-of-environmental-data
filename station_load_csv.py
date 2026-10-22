''' station_load_csv
Load a timeseries from a weather station CSV file.
'''
import pandas as pd

df = pd.read_csv('/Users/danielhueholt/Data/ev228_data/station/COS-Airport_maxT-minT-precip-snow_194801-202212.csv')