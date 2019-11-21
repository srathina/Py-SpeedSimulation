# How to plot using matplotlib and repl.it
#https://stackoverflow.com/questions/43452136/why-can-i-not-plot-using-python-on-repl-it

import matplotlib.pyplot as plt
import numpy as np

time            = [0] #seconds
host_speed      = [130] #kmph
follow_speed    = [120] #kmph
host_bt         = 2 #seconds
host_acc        = -7  #m/s^2
follow_acc      = -5  #m/s^2
follow_rt       = 3 #seconds



for y in range(0,10,1):

    x = y+1

    time.append(x)

    if y >= host_bt:
        host_speed.append( ((host_speed[x-1]/3.6) + ( (time[x] - time[y]) * host_acc)) * 3.6 )
    else:
        host_speed.append(host_speed[x-1])

    if y >= follow_rt:
        follow_speed.append(((follow_speed[x-1]/3.6) + ( (time[x] - time[y]) * follow_acc)) * 3.6)
    else:
        follow_speed.append(follow_speed[x-1])

    print(time,host_speed,follow_speed)






plt.plot(time,host_speed,'r')
plt.plot(time,follow_speed,'b')
plt.ylim(0,150)
plt.xlim(0,10)
plt.xlabel('TIME')
plt.ylabel('SPEED')
plt.grid()
plt.title('SPEED SIMULATION')

#plt.show()
plt.savefig('Speed.png') #This is must for plotting graphs in the web based environment