# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 09:58:31 2021

@author: Hengheng Zhang

E-Mail: hengheng.zhang@kit.edu

Function：

"""
import xarray as xr


dset = xr.open_dataset("ERA5_REANALYSIS_temperature_200306.nc")
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

fig = plt.figure(figsize=[12,5])

# 111 means 1 row, 1 col and index 1
ax = fig.add_subplot(111, projection=ccrs.PlateCarree(central_longitude=0))

dset['t2m'].plot(ax=ax,  cmap='jet',
                   transform=ccrs.PlateCarree())
ax.coastlines()

plt.show()

