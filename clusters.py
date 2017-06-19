import numpy as np
import sklearn.cluster as sk
import matplotlib.pyplot as mpl
import geospatialtools.gdal_tools as geo
import h5py as h5

def mask(array):
  return np.ma.masked_array(array,array==-9999)

def show(array):
  p = mpl.imshow(array)

def shape(array):
  temp = array.reshape(array.size)
  trim = temp[temp != -9999]
  return trim[:,np.newaxis]

sand = geo.read_raster('clusters/sand_mean_0_5.tif')
silt = geo.read_raster('clusters/silt_mean_0_5.tif')
clay = geo.read_raster('clusters/clay_mean_0_5.tif')
#sand,silt,clay = mask(sand),mask(silt),mask(clay)

x = sand.reshape(sand.size)
sand1 = np.copy(sand)
silt1 = np.copy(silt)
clay1 = np.copy(clay)

sand,silt,clay = shape(sand),shape(silt),shape(clay)
size = min(sand.shape[0],silt.shape[0],clay.shape[0])
soil = np.concatenate([sand[0:size],silt[0:size],clay[0:size]],axis=1)

model = sk.KMeans(n_clusters=10)
np.random.seed(0)
val = np.random.choice(np.arange(size),10000)
model.fit(soil[val,:])
p = model.predict(soil)

#unique = np.unique(p)
#new = np.zeros(p.shape)
#for u in unique:
#  new[p==u] = np.mean(soil[p==u])

copy = np.copy(x)
copy[x != -9999] = p#new
copy_right = np.reshape(copy,sand1.shape)
copy_right,sand1,silt1,clay1 = mask(copy_right),mask(sand1),mask(silt1),mask(clay1)

#copy_right_unique = np.unique(copy_right)

f = h5.File("Clustered_data.h5","w")
group1 = f.create_group("US Soil Data Clustered")
#group1['US Soil Data'] = copy_right
fpv = group1.create_dataset("US Soil Data",copy_right.shape,'i')
fpv[:] = copy_right
#data1 = np.copy(copy_right_unique)
#print(np.unique(copy_right))

group2 = f.create_group("US Soil Data")


#data2_sand = group2.create_dataset("Sand",'i')
#data2_silt = group2.create_dataset("Silt",'i')
#data2_clay = group2.create_dataset("Clay",'i')


exit()
fig = mpl.figure()
p1 = mpl.subplot(2,2,1)
show(copy_right)
p1.set_title("Clustered",fontweight='bold')
p2 = mpl.subplot(2,2,2)
show(sand1)
p2.set_title("Sand",fontweight='bold')
p3 = mpl.subplot(2,2,3)
show(silt1)
p3.set_title("Silt",fontweight='bold')
p4 = mpl.subplot(2,2,4)
show(clay1)
p4.set_title("Clay",fontweight='bold')
fig.savefig('Clustered.png')


I AM MAKING BIG CHANGES!!!!!
I AM MAKING OTHER CHANGES!!!!

