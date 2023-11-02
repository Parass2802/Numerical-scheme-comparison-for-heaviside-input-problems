#Different schemes for solving problem with heaviside input
#Lax Wendroff

import numpy
from matplotlib import pyplot

#Domain
nx=51
tmax=1
xmax=4
c=1
sigma=0.5
dx=xmax/(nx-1)
dt=(sigma*dx)/c

nt=tmax/dt
x=numpy.linspace(0,xmax,nx)

tmax_an=tmax*sigma
nt_an=tmax_an/dt

#IC
u=numpy.zeros(nx)
u[0:int((xmax/2)/dx)+1]=2
u_an=u.copy()

#plotting IC
pyplot.figure(figsize=(11,7),dpi=300)
pyplot.xlabel('x',size=16)
pyplot.ylabel('u',size=16)
pyplot.plot(x,u,label='IC')

#Solution
un=u.copy()

#Upwind Scheme
for n in range(int(nt)):
    un=u.copy()
    u[1:-1]=un[1:-1]-(sigma/2)*(un[2:]-un[0:-2])+((sigma**2)/2)*(un[2:]-2*un[1:-1]+un[0:-2])
    
    #BC
    u[0]=2
    u[-1]=0
    
    if n%4==0:
        #plotting Results
        pyplot.plot(x,u,label='t='+ str(n)+'s')
    elif n==int(nt):
        pyplot.plot(x,u,label='t='+ str(n)+'s')

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
pyplot.title('1D Wave Eqn with Heaviside Input (Lax Wendroff)',size=16)
pyplot.tick_params(axis='both',labelsize=16)
