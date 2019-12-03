
from isrp import *

#sensors = isrpLoadSensorParameters('ILL','/home/sandro/Documents/isrpDtCalculator')
#sensors = isrpLoadSensorParameters('rogerpass','/home/sandro/Documents/isrpDtCalculator')
sensors = isrpLoadSensorParameters('rogerpass','/home/sandro/Documents/isrpDtCalculator')
sensors = isrpLoadSensorParameters('OMIV','/home/sandro/Documents/isrpDtCalculator')
sensors = isrpLoadSensorParameters('rogerpassRSPMNX','/home/sandro/Documents/isrpDtCalculator')
sensors = isrpLoadSensorParameters('rogerpassRPSRPC','/home/sandro/Documents/isrpDtCalculator')
#demFilename ='/home/sandro/Documents/isrpDtCalculator/dem/ILL/illgraben-ritaglio.asc'
demFilename ='/home/sandro/Documents/isrpDtCalculator/dem/rogerpass/rogerpass-ritaglio.asc'
#demFilename ='/home/sandro/Documents/isrpDtCalculator/dem/rogerpassHRM/rogerpass-ritaglioHRM.asc'
demFilename ='/home/sandro/Documents/isrpDtCalculator/dem/OMIV/Séchilienne.asc'
demFilename ='/home/sandro/Documents/isrpDtCalculator/dem/rogerpassRSPMNX/rogerpass-ritaglioRSPMNX.asc'
demFilename ='/home/sandro/Documents/isrpDtCalculator/dem/rogerpassRPSRPC/rogerpass-ritaglioRPSRPC.asc'
#

sRes=150
sRes1=170
dMin=0
dMax=4000
fig = plt.figure(num=1,figsize=(12, 8))
#
# ax1 = fig.add_subplot(121)
xdem, ydem, zdem = isrpLoadDem(demFilename,sensors,dMax)
# plt.contourf(xdem,ydem, zdem, cmap="gray",levels=list(range(0, 5000, 60)))
# plt.title("Elevation Contours ")
# cbar = plt.colorbar(orientation="horizontal")
# plt.gca().set_aspect('equal', adjustable='box')
# lineMap, = plt.plot(np.nan,np.nan, linestyle='dashed', linewidth=1, color='b')
# ax1.plot(sensors['X'][7], sensors['Y'][7], marker='*', color='r', markersize=12)
# ax1.plot(sensors['X'][0], sensors['Y'][0], marker='*', color='b', markersize=12)
# ax2 = fig.add_subplot(122)
# lineProfile, = plt.plot(0, 0, linewidth=1, color='b')
# lineSound, = plt.plot(0, 0,marker='o', markersize=6, linestyle='dashed', linewidth=1, color='r')
# #ax2.set_xlim([0,20000])
# ax2.set_ylim([1000,5000])
# plt.grid(color='k', linestyle='-', linewidth=.1)
# plt.draw()
# plt.pause(0.1)

corrM=np.array([
               [1, 1, 1, 1],
               [1, 1, 1, 1],
               [1, 1, 1, 1],
               [1, 1, 1, 1]
                ])
corrM=np.array([
               [1, 1, 1, 1, 0, 0, 0, 0,0],
               [1, 1, 1, 1, 0, 0, 0, 0,0],
               [1, 1, 1, 1, 0, 0, 0, 0,0],
               [1, 1, 1, 1, 0, 0, 0, 0,0],
               [0, 0, 0, 0, 1, 1, 1, 1,1],
               [0, 0, 0, 0, 1, 1, 1, 1,1],
               [0, 0, 0, 0, 1, 1, 1, 1,1],
               [0, 0, 0, 0, 1, 1, 1, 1,1],
               [0, 0, 0, 0, 1, 1, 1, 1, 1]
                ])
corrM=np.array([
               [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
               [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
               [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
               [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
               [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
               [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
               [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
               [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
               [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
                ])

dT=isrpDemTravelDt(demFilename,xdem,ydem,zdem,sensors,sRes,dMin,dMax)
loadT=np.load(demFilename+'dT.npz')
dT=loadT['dT']
T=loadT['T']




#seismic
sWnd=750
sShift=125
smp=250
c=1200
#infrasound
sWnd=250
sShift=25
smp=50
c=330

dMap, sMap, dsMin, dsMax=isrpArrange2(demFilename,-dT,T,sensors,sShift,sWnd,smp/c)

np.savez(demFilename + 'dMap', dMap=dMap, sMap=sMap, minCorr=dsMin, maxCorr=dsMax,
         sWnd=sWnd, sShift=sShift, xdem=xdem, ydem=ydem, zdem=zdem, sensors=sensors, smp=smp)

fig = plt.figure(num=2,figsize=(12, 8))
aa=np.float64(dT[1,2,:,:].T)
plt.subplot(2,2,1)
plt.imshow(aa)
aa=np.float64(dT[3,2,:,:].T)
plt.subplot(2,2,2)
plt.imshow(aa)
aa=np.float64(dT[7,6,:,:].T)
plt.subplot(2,2,3)
plt.imshow(aa)
aa=np.float64(dT[7,8,:,:].T)
plt.subplot(2,2,4)
plt.imshow(aa)
plt.colorbar()
plt.draw()
plt.show()
