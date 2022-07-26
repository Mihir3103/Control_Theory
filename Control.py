
import numpy as np
from scipy.integrate import odeint


g = 9.8

#HelloWorld
# The following function gives the ordinary differential
# equation that our plant follows. Do not meddle with this.
def f(x, t, theta):
    return (x[1], (-5 * g / 7) * np.radians(theta))


# Write your function here.
def solve(x,theta,target,Kc,Kd,Ki,K):
  x0 = np.zeros(2)
  x0[0] = x[0]
  t = np.linspace(0,1000,1001)
  setpoint = target
  position = np.zeros(1001)
  thetaa = np.zeros(1001)
  P = np.zeros(1001)
  I = np.zeros(1001)
  D = np.zeros(1001)
  for i in range(1,1001):
    e = setpoint - x0
    ts = [t[i-1],t[i]]
    dt = t[i] - t[i-1]
    x = odeint(f,x0,ts, args=(theta,))
    P[i] = Kc*e[0]
    I[i] = I[i-1] + Ki*e[0]*dt
    D[i] = Kd*(x[1][0] - x[0][0])/dt
    dtheta = -K*(P[i]-P[i-1] + I[i]-I[i-1]+ D[i] - D[i-1])
    if x[1][0]>300:
      x[1][0]= 300   
      x[1][1]=0
    elif x[1][0] < -300:
      x[1][0]= -300   
      x[1][1]=0
    if dtheta < -1:
      dtheta = -1
    elif dtheta > 1:
      dtheta = 1
    theta = theta + dtheta
    if theta < -15:
      theta = -15
    elif theta > 15:
      theta = 15
    
    
    x0 = x[1]
    position[i]=x[1][0]
    thetaa [i] = theta
  return (position , thetaa)
