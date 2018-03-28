import numpy as np
import matplotlib.pyplot as plt

## simple plotting
a = np.arange(10)
#plt.plot(a,2*a, a, a)
#plt.show()

# plot labels
#plt.plot(a,a)
#plt.ylabel('y axis')
#plt.title('title')
#plt.show()

# plot with legend
#plt.plot(a,a, label='my plot')
#plt.legend()
#plt.show()

# plot styles
#def f(x):
#    return np.exp(-x) * np.cos(2*np.pi*x)
#
#n = 25
#x = np.linspace(0,5, n)
#xx = np.linspace(0,5, 10*n)
#plt.plot(x, f(x), 'bo')
#plt.plot(xx, f(xx), 'k')
#plt.title('IX')
#plt.show()

# BONUS: uncomment lines below for above example with seaborn style plots (pip install seaborn)
#import seaborn as sns
#sns.set()
#def f(x):
#    return np.exp(-x) * np.cos(2*np.pi*x)
#
#n = 25
#x = np.linspace(0,5,n)
#xx = np.linspace(0,5, 10*n)
#plt.plot(xx, f(xx))
#plt.plot(x, f(x), 'o')
#plt.title('seaborn aesthetics')
#plt.show()

# scatter plots
# simple
#N = 50
#x = np.random.rand(N)
#y = np.random.rand(N)
#plt.scatter(x, y, c='k')
#plt.title('simple scatter plot')
#plt.show()

## fun scatter plot
#N = 50
#x = np.random.rand(N)
#y = np.random.rand(N)
#colors = np.random.rand(N)
#areas = np.pi * (15 * np.random.rand(N))**2 # radii 0 to 15 pt
#plt.scatter(x, y, s=areas, c=colors, alpha=0.5)
#plt.show()

import seaborn as sns
sns.set()

#from sines import sinkx
#from sines import *
import sines


x = np.linspace(0, 2*np.pi, 200)
for k in range(3):
    plt.plot(x, sines.sinkx(k,x))
#plt.show()

s = sines.Sine(2)
print(s.k)

# some work with sinkx





