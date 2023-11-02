#Different schemes for solving problem with heaviside input
#LeapFrog scheme

import numpy
from matplotlib import pyplot

#Domain
nx=101
tmax=1
xmax=5
c=1
sigma=0.5
dx=xmax/(nx-1)
dt=(sigma*dx)/c

nt=tmax/dt
x=numpy.linspace(0,xmax,nx)

tmax_an=tmax*sigma
nt_an=tmax_an/dt

#IC
u=numpy.zeros((nx,int(nt)))
u[0:int((xmax/2)/dx)+1,0]=2
u_an=u[:,0].copy()

#plotting IC
pyplot.figure(figsize=(11,7),dpi=300)
pyplot.xlabel('x',size=16)
pyplot.ylabel('u',size=16)
pyplot.plot(x,u[:,0],label='IC')


#Solution
un=u.copy()

#Initialise using Upwind Scheme
for n in range (1):
   
    
    u[1:-1,n+1]=u[1:-1,n]-((c*dt)/dx)*(u[1:-1,n]-u[0:-2,n])
        
    #BC
    u[0,:]=2
    u[-1,:]=0

#LeapFrog scheme
for n in range(1,int(nt)-1):
    
    
    u[1:-1,n+1]=u[1:-1,n-1]-((c*dt)/dx)*(u[2:,n]-u[0:-2,n])
    
    #BC
    u[0,:]=2
    u[-1,:]=0
    
    if n%4==0:
        #plotting Results
        pyplot.plot(x,u[:,n],label='t='+ str(n)+'s')
    elif n==int(nt):
        pyplot.plot(x,u[:,n],label='t='+ str(n)+'s')

#Analytical Sol
for n in range(int(nt_an)):
    un_an=u_an.copy()
    u_an[1:]=u_an[0:-1]
    
    #BC
    u_an[0]=2
    u_an[-1]=0

#plotting analytical solution
pyplot.plot(x,u_an,label='Analytical')
pyplot.legend(fontsize=16,loc='lower left')
pyplot.title('1D Wave Eqn with Heaviside Input (LeapFrog Scheme)',size=16)
pyplot.tick_params(axis='both',labelsize=16)
