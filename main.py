# How to plot using matplotlib and repl.it
#https://stackoverflow.com/questions/43452136/why-can-i-not-plot-using-python-on-repl-it

import matplotlib.pyplot as plt
import numpy as np

x1  = [1, 2, 3, 4, 5]
y1 =  [1, 2, 3, 4, 5]

x2  = [1, 2, 3, 4, 5]
y2 = [1, 4, 9, 16, 25]

plt.subplot(2,1,1)
plt.subplots_adjust(hspace=0.5)
plt.plot(x1,y1,'r')
plt.grid()
plt.xlabel('x1 axis')
plt.ylabel('y1 axis')
plt.title('linear')

plt.subplot(2,1,2)
plt.plot(x2,y2,'b')
plt.grid()
plt.xlabel('x2 axis')
plt.ylabel('y2 axis')
plt.title('quadratic')

#plt.show()
plt.savefig('plot.png') #This is must for plotting graphs in the web based environment

x  = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
z= np.random.standard_normal(1000)

plt.clf() #This is needed to remove the current figure for using it to plot different graph

plt.hist(z,bins = 20,label="histogram", color="blue")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("histogram Example")
plt.grid()
plt.legend()

#plt.show()
plt.savefig('hist.png') #This is must for plotting graphs in the web based environment