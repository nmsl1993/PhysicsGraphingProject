'''
Created on Jan 16, 2012

@author: noah
m = 0.2 kg, k = 80 N/m, b = 1 kg/s.
Furthermore, assume the following initial conditions: x0 = 0.5 m, v0 = -1.25 m/s.
'''
import numpy
from math import *
import matplotlib.pyplot as plt
import matplotlib as mp
import csv

m = 0.2; #kg
k = 80; #N/m
b = 1; #kg/s

x_not = 0.5; #m
v_not = -1.25; #m/s

timeMin = 0; #s
timeMax = 2.5; #s
dt = 0.001; #s

def acceleration(x, v):
    return -1*(k/m)*x - (b/m)*v
def createGraphs():
    xVSt = plt.figure()
    vVSt = plt.figure()
    genPoints(xVSt, vVSt)
    plt.show()
def genPoints(fig1, fig2):
    timeRange = numpy.arange(timeMin, timeMax, dt)
    xPoints = numpy.arange(timeMin, timeMax, dt)
    vPoints = numpy.arange(timeMin, timeMax, dt)
    x = x_not
    xPrime = v_not;
    xDoublePrime = acceleration(x, xPrime)
    for index, i in enumerate(timeRange):
        x = x + xPrime*dt
        xPrime = xPrime + xDoublePrime*dt
        xDoublePrime = acceleration(x, xPrime)
        xPoints[index] = x
        vPoints[index] = xPrime
    xvtDHOfig = setUpXvsT(fig1)
    vvtDHOfig = setUpVvsT(fig2)
    xvtDHOfig.plot(timeRange, xPoints)
    vvtDHOfig.plot(timeRange, vPoints)
def setUpVvsT(mainFig):
    DHOfig = mainFig.add_subplot(111, autoscale_on=False, xlim=(timeMin, timeMax), ylim=(4*v_not, 4*-1*v_not))
    DHOfig.set_title("Velocity vs Time in a damnped harmonic oscillator", fontsize = 14)
    DHOfig.set_xlabel("Time (seconds)", fontsize = 12)
    DHOfig.set_ylabel("Velocity (m/s)", fontsize = 12)
    majorLocator = mp.ticker.MultipleLocator((-1*v_not/2))
    minorLocator = mp.ticker.MultipleLocator((-1*v_not/6))
    DHOfig.yaxis.set_major_locator(majorLocator);
    DHOfig.yaxis.set_minor_locator(minorLocator);
    DHOfig.grid(True, linestyle='-')
    DHOfig.yaxis.set_major_formatter(plt.FormatStrFormatter("%.2f"))
    #DHOfig.yticks(locs, map(lambda x: "%.1f" % x, locs*1e9))
    return DHOfig

def setUpXvsT(mainFig):
    DHOfig = mainFig.add_subplot(111, autoscale_on=False, xlim=(timeMin, timeMax), ylim=(1.2*-1*x_not, 1.2*x_not))
    DHOfig.set_title("Position vs Time in a damnped harmonic oscillator", fontsize = 14)
    DHOfig.set_xlabel("Time (seconds)", fontsize = 12)
    DHOfig.set_ylabel("Position (m)", fontsize = 12)
    majorLocator = mp.ticker.MultipleLocator((x_not/3))
    minorLocator = mp.ticker.MultipleLocator((x_not/10))
    DHOfig.yaxis.set_major_locator(majorLocator);
    DHOfig.yaxis.set_minor_locator(minorLocator);
    DHOfig.grid(True, linestyle='-')
    DHOfig.yaxis.set_major_formatter(plt.FormatStrFormatter("%.2f"))
    #DHOfig.yticks(locs, map(lambda x: "%.1f" % x, locs*1e9))
    return DHOfig

createGraphs();