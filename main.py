from core.read_segment import read_seg
from core.mapping import trajectory2segment
from core.read_traj import traj_preprocess

import time

print("start")
cell, link_id, F_NODE = read_seg('data/incheon.geojson')
print("linkdata read")

traj = traj_preprocess('data/data_20200707.csv')
print("trajdata read")

start = time.time()
#for i in range(len(traj)):
for i in range(1):
    mapping_data = trajectory2segment(traj[i], cell, link_id, F_NODE)
#    print("---------------------------------------------------------------------------------------")
    print(len(mapping_data),mapping_data)
#    print("---------------------------------------------------------------------------------------")
    print(traj[i],len(traj[i]))
    print("---------------------------------------------------------------------------------------")
end = time.time() - start
#print(end)
