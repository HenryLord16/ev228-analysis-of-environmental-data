# High-dimensional gridded climate data
Gridded climate data refers to data that exists on an x-y grid. In climate applications the x and y dimensions are often longitude and latitude.
 Yesterday, we worked with a single 2-dimensional slice of a gridded climate dataset. But gridded climate data usually has more than two dimensions!

## Common additional dimensions
 * *Time* -- a gridded product will usually have many timesteps, each with its own slice of gridded data.
     * For example, the ERA5 reanalysis dataset includes a timestep for every month from 1948 to present
 * *Vertical levels* -- many geophysical quantities vary vertically
     * For example, atmospheric data varies with height and oceanic data with depth
     * Vertical dimensions may be in terms of physical height (i.e., some number of meters above the surface). They may also be in terms of pressure, temperature, or any other quantity that changes reliably with height.
 * *Realizations* -- certain datasets may include multiple realizations of their climate fields, each representing a possible manifestation of chaotic behavior in the Earth's climate system.

## How do we work with high-dimensional climate data?
The `xarray` package we used yesterday is designed to work with any-dimensional gridded climate data in the netCDF file format.

It is normal to work with gridded environmental data that has four or five dimensions: longitude, latitude, vertical levels, time, and realizations. It may be unintuitive to imagine a dataset with more than three dimensions, since we live in a three-dimensional world. 
Remember that "dimension" here only refers to "way in which the data varies"--it does not have to correspond to our physical spatial dimensions.

## Data visualization with high-dimensional climate data
Visualizing 3D, 4D, or 5D climate data can be challenging, since we usually only have two dimensions available for data visualization.
Thus, we usually focus on employing dimension reduction to remove enough dimensions to effectively visualize the data. This often involves averaging over certain dimension(s), or calculating another relevant descriptive statistic.

### Dimension reduction example
* [Link to temperature trends figure](https://zacklabe.com/wp-content/uploads/2026/01/annual_trend_2025_all_1990-2025.png)

The figure at the above link shows temperature trends in a 3-dimensional gridded climate dataset. Temperature in the original dataset varies in latitude, longitude, and time. In order to plot on this map, the time dimension is reduced by calculating a trend.

### Dimension reduction example 2
* [Link to trends by latitude figure](https://zacklabe.com/wp-content/uploads/2026/02/zonaltrend_t2m_era5_seasons_2025.png)

The figure at the above link shows temperature trends for each latitude from a 4-dimensional gridded climate dataset. Temperature in the original dataset varies in latitude, longitude, time, and by level. In order to plot the temperature trends for each latitude, the time dimension is reduced by calculating a trend, and the longitude dimension is reduced by calculating an average.

### Authorship and Acknowledgements
This document was written by Daniel Hueholt.
