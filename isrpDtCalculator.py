
from idar import *

# dtFilename ='/home/sandro/Documents/idarDtCalc/idarDtCalc/dem/OMIV/THERUI/THERUI.asc'
# sensors = isrpLoadSensorParameters('OMIV/THERUI','/home/sandro/Documents/idarDtCalc/idarDtCalc')
#demFilename ='/home/sandro/Documents/idarDtCalc/idarDtCalc/dem/OMIV/Séchilienne.asc'
#demFilenameG ='/home/sandro/Documents/idarDtCalc/idarDtCalc/dem/ADN/rogerpass-ritaglio.asc'

demFilename ='/home/sandro/Documents/idarDtCalc/idarDtCalc/dem/ADN/ADN_DTM_projwgs84.txt'


# demFilename ='/home/sandro/Documents/idarDtCalc/idarDtCalc/dem/ADN/RSPMNX/RSPMNX.asc'
# sensors = isrpLoadSensorParameters('ADN/RSPMNX','/home/sandro/Documents/idarDtCalc/idarDtCalc')

#dtFilename ='/home/sandro/Documents/idarDtCalc/idarDtCalc/dem/ADN/HRMCRO/HRMCRO.asc'
#sensors = isrpLoadSensorParameters('ADN/HRMCRO','/home/sandro/Documents/idarDtCalc/idarDtCalc')

# dtFilename ='/home/sandro/Documents/idarDtCalc/idarDtCalc/dem/ADN/CROPRL/CROPRL.asc'
# sensors = isrpLoadSensorParameters('ADN/CROPRL','/home/sandro/Documents/idarDtCalc/idarDtCalc')
#
dtFilename ='/home/sandro/Documents/idarDtCalc/idarDtCalc/dem/ADN/CROPRL/CROPRL.asc'
sensors = isrpLoadSensorParameters('ADN/CROPRL','/home/sandro/Documents/idarDtCalc/idarDtCalc')
#
# dtFilename ='/home/sandro/Documents/idarDtCalc/idarDtCalc/dem/ADN/WBYFDY/WBYFDY.asc'
# sensors = isrpLoadSensorParameters('ADN/WBYFDY','/home/sandro/Documents/idarDtCalc/idarDtCalc')

# dtFilename ='/home/sandro/Documents/idarDtCalc/idarDtCalc/dem/ADN/SMTMNX/SMTMNX.asc'
# sensors = isrpLoadSensorParameters('ADN/SMTMNX','/home/sandro/Documents/idarDtCalc/idarDtCalc')
#
#
#dtFilename ='/home/sandro/Documents/idarDtCalc/idarDtCalc/dem/ADN/RSPLPB/RSPLPB.asc'
#sensors = isrpLoadSensorParameters('ADN/RSPLPB','/home/sandro/Documents/idarDtCalc/idarDtCalc')
#
dtFilename ='/home/sandro/Documents/idarDtCalc/idarDtCalc/dem/ADN/RSPMNX/RSPMNX.asc'
sensors = isrpLoadSensorParameters('ADN/RSPMNX','/home/sandro/Documents/idarDtCalc/idarDtCalc')
#
dtFilename ='/home/sandro/Documents/idarDtCalc/idarDtCalc/dem/ADN/LPBAVC/LPBAVC.asc'
sensors = isrpLoadSensorParameters('ADN/LPBAVC','/home/sandro/Documents/idarDtCalc/idarDtCalc')

#dtFilename ='/home/sandro/Documents/idarDtCalc/idarDtCalc/dem/ADN/RPSRPC/RPSRPC.asc'
#sensors = isrpLoadSensorParameters('ADN/RPSRPC','/home/sandro/Documents/idarDtCalc/idarDtCalc')

dtFilename ='/home/sandro/Documents/idarDtCalc/idarDtCalc/dem/ADN/AVCRPS/AVCRPS.asc'
sensors = isrpLoadSensorParameters('ADN/AVCRPS','/home/sandro/Documents/idarDtCalc/idarDtCalc')



#seismic
sWnd=1250
sShift=125
smp=250
c=1500
defCorr=150
sRes=50
sRes1=170
dMin=0
dMax=4000
ritx=-1
rity=-1
s=True

#infrasound
sWnd=250
sShift=10
smp=50
c=330
defCorr=30
sRes=150
sRes1=170
dMin=0
dMax=8000
# che cosa è ritx?

s=False

#####
# fig = plt.figure(num=1,figsize=(12, 8))
# #
# ax1 = fig.add_subplot(121)
ritx = 3000
rity = 3000
xdem, ydem, zdem,xDemOrg,yDemOrg,zDemOrg,xL,xR,yT,yB= isrpLoadDem2(demFilename,sensors,ritx,rity)
#xdem, ydem, zdem,xDemOrg,yDemOrg,zDemOrg,xL,xR,yT,yB= isrpLoadDem(demFilenameG,sensors,ritx,rity)

print('pippo')
# plt.contourf(xdem,ydem, zdem, cmap="gray",levels=list(range(0, 5000, 60)))
# plt.title("Elevation Contours ")
# cbar = plt.colorbar(orientation="horizontal")
# plt.gca().set_aspect('equal', adjustable='box')
# lineMap, = plt.plot(np.nan,np.nan, linestyle='dashed', linewidth=1, color='b')
# ax1.plot(sensors['X'][7], sensors['Y'][7], marker='*', color='r', markersize=12)
# ax1.plot(sensors['X'][0], sensors['Y'][0], marker='*', color='b', markersize=12)
print('pippo')
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
               [0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
               [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
               [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                ])

# corrM=np.zeros([13,13])
# corrM[0:5,0:5]=1
# corrM[6:12,6:12]=1
# corrM=np.triu(corrM,1)
dT=isrpDemTravelDt(dtFilename,xdem,ydem,zdem,sensors,sRes,dMin,dMax,s)
loadT=np.load(dtFilename+'dT.npz')
dT=loadT['dT']
T=loadT['T']






dMap, sMap, dsMin, dsMax=isrpArrange2(demFilename,-dT,T,sensors,sShift,sWnd,smp/c,corrM,defCorr)
#dMap, sMap, dsMin, dsMax=isrpArrange3(demFilename,-dT,T,sensors,sShift,sWnd,smp/c,corrM,defCorr)
np.savez(dtFilename + 'fsdMap', dMap=dMap, sMap=sMap, minCorr=dsMin, maxCorr=dsMax,
         sWnd=sWnd, sShift=sShift, xdem=xdem, ydem=ydem, zdem=zdem, zDemOrg=zDemOrg,
         xDemOrg=xDemOrg,yDemOrg=yDemOrg,xL=xL,xR=xR,yT=yT,yB=yB,sensors=sensors, smp=smp,c=c)


