# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 11:44:44 2021

@author: Hengheng Zhang

E-Mail: hengheng.zhang@kit.edu

Function：

"""
import matplotlib.pyplot as plt
import xarray as xr    #读取nc文件
import numpy as np
import cartopy.crs as ccrs   #投影方式
import cartopy.feature as cfeat   #使用shp文件
from cartopy.io.shapereader import Reader  #读取自定的shp文件
from cartopy.mpl.ticker import LongitudeFormatter,LatitudeFormatter  #将x，y轴换成经纬度

plt.rcParams['font.sans-serif']=['SimHei']   #黑体，也可以替换为其他字体
obj = xr.open_dataset('2122h.nc')
# print(obj)
z = obj['z'][0]/98
z.attrs['units'] = 'dagpm'
u = obj['u'][0]
v = obj['v'][0]
t = obj['t'][0]-273.15
t.attrs['units'] = 'deg C'
print(z)
lat = obj['latitude'][:]
lon = obj['longitude'][:]
lons, lats = np.meshgrid(lon,lat)

proj = ccrs.PlateCarree()
fig = plt.figure(figsize=(9,6),dpi=150)
ax = fig.add_subplot(111, projection=ccrs.PlateCarree(central_longitude=0))


ax.set_xticks([70,85,100,115,130])
ax.set_yticks([10,20,30,40,50,60])
ax.xaxis.set_major_formatter(LongitudeFormatter())
ax.yaxis.set_major_formatter(LatitudeFormatter())
z_levels = np.arange(500, 580+10, 4)
ac = ax.contour(lons[120:320,280:560], lats[120:320,280:560], z[120:320,280:560], 
                levels=z_levels, extent='both', 
                colors='mediumblue', linewidths=0.8)
plt.clabel(ac, inline=True, fontsize=8, fmt='%.0f')


t_levels = np.arange(-40, 30, 4)
at = ax.contour(lons[120:320,280:560], lats[120:320,280:560], t[120:320,280:560], 
                levels=t_levels, extent='both',
                colors='red', linewidths=0.5, linestyle=np.where(t>=0,'-','--'))
plt.clabel(at, inline=True, fontsize=5, fmt='%.0f')

ax.barbs(lons[120:320:12,280:560:12], lats[120:320:12,280:560:12],
         u[120:320:12,280:560:12],v[120:320:12,280:560:12], 
         barb_increments={'half':2,'full':4,'flag':20}, zorder=5, length=5, linewidth=0.2)
ax.coastlines()
ax.set_title('2020年5月21日02时（世界时） 500hPa 温度（Temp） 高度（dagpm）',fontsize=12)
fig.show
fig.savefig('20052102_500hPa_天气图')
# country_shp = Reader('country1.shp')
# pro_shp = Reader('行政边界_省级.shp')

# fea_country = cfeat.ShapelyFeature(country_shp.geometries(), proj,
#                               edgecolor='darkolivegreen', facecolor='ivory')
# ax.add_feature(fea_country, linewidth=0.2, alpha=0.2)
# fea_pro = cfeat.ShapelyFeature(pro_shp.geometries(), proj,
#                               edgecolor='darkolivegreen', facecolor='none')
# ax.add_feature(fea_pro, linewidth=0.3, alpha=0.5)
# ax.add_feature(cfeat.OCEAN, alpha=0.5)