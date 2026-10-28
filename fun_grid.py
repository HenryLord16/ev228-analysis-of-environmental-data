'''fun_grid
Functions for gridded data.
'''
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import numpy as np

def weight_by_latitude(da, latitude):
    ''' Weight gridded data by latitude '''
    weights = np.cos(np.deg2rad(latitude))
    da_weight = da.weighted(weights)

    return da_weight

def plot_map(da, latitude, longitude, colormap, projection, save_name=None):
    ''' Weight gridded data by latitude '''
    fig, ax = plt.subplots(1, 1, subplot_kw={"projection": projection})
    d_crs = ccrs.PlateCarree()
    image = ax.pcolormesh(
        longitude, latitude, da, transform=d_crs, cmap=colormap,
    )
    ax.coastlines()
    colorbar = plt.colorbar(image)
    colorbar.set_label('K')
    if save_name is not None:
        plt.savefig(save_name, dpi=400)
    else:
        return fig, ax
