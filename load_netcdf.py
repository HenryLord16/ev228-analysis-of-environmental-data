''' load_netcdf
Load a gridded dataset from a netCDF file.
'''
import xarray as xr
from icecream import ic
import numpy as np
import cartopy.crs as ccrs

import fun_eda_demo as fed
import fun_grid as fg

#  Import data
ds = xr.load_dataset('/Users/danielhueholt/Data/ev228_data/gridded/era5_t2m_202609.nc')
ic(ds)
da = ds.t2m
arr = da.data
dict_moments, dict_other = fed.descriptive_statistics(arr, axis='flat')
# ic(dict_moments, dict_other)
fg.plot_map(ds.t2m, ds.latitude, ds.longitude, 'plasma', ccrs.EqualEarth(), '/Users/danielhueholt/Documents/Figures/ev228_fig/era5_t2m_202609.png')