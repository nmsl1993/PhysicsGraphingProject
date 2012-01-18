
'''
Noah Levy Ain't So Simple Pendulum Graphs
Coded in python, uses matplotlib library to present a visual comparison between small angle approximation and true pendulum motion
GPLv3
'''
import numpy
from math import *
import matplotlib.pyplot as plt
import matplotlib as mp
import csv

dataPath = "aintSoSimpleresults.csv"
#dataPath = "test.csv"
g = 9.81; #m/s^2
length = 0.5; #m
mass = 1.0; #kg

dt = 0.001; #change in time per stepe
timeMin = 0.0; #start
timeMax = 2.84; #end

theta_not = radians(50); #I'm aware this is pi/2, but I think using radians() is more transparent.

omega = sqrt(g/length)

def smallAngleApproximation(timeRange):
    theta = theta_not
    thetaPrime = 0 #angular velocity
    thetaDoublePrime = SHOAcceleration(theta)#angular acceleration
    SHOPendulumList = numpy.arange(timeMin, timeMax, dt)
    for index, time in enumerate(timeRange):
        theta = pendulumStep(theta, thetaPrime)
        thetaPrime = pendulumVelocity(thetaPrime, thetaDoublePrime)
        thetaDoublePrime = SHOAcceleration(theta)
        #print theta;
        SHOPendulumList[index] = theta;
    return SHOPendulumList;
def SHOAcceleration(theta):
    return -1*(g/length)*theta
def pendulumMotion(timeRange):
    theta = theta_not
    thetaPrime = 0 #angular velocity
    thetaDoublePrime = pendulumAcceleration(theta)#angular acceleration
    truePendulumList = numpy.arange(timeMin, timeMax, dt)
    for index, time in enumerate(timeRange):
        theta = pendulumStep(theta, thetaPrime)
        thetaPrime = pendulumVelocity(thetaPrime, thetaDoublePrime)
        thetaDoublePrime = pendulumAcceleration(theta)
        #print theta;
        truePendulumList[index] = theta;
    return truePendulumList;
def pendulumAcceleration(theta):
    return -1*(g/length)*sin(theta)
def pendulumVelocity(thetaPrime, thetaDoublePrime):
    thetaPrime = thetaPrime + thetaDoublePrime*dt;
    return thetaPrime;
def pendulumStep(theta, thetaPrime):
    theta = theta + thetaPrime*dt;
    return theta;
def createGraphs():
    figures = plt.figure()
    smallAngleGraph(figures)
    
    plt.show()
def setUpChart(mainFig):
    smallAGfig = mainFig.add_subplot(111, autoscale_on=False, xlim=(timeMin, timeMax), ylim=(1.2*degrees(-1*theta_not), 1.2*degrees(theta_not)))
    smallAGfig.set_title("Small Angle Approximation vs Pendulum Motion", fontsize = 14)
    smallAGfig.set_xlabel("Time (seconds)", fontsize = 12)
    smallAGfig.set_ylabel("Amplitude (degrees from equilibrium)", fontsize = 12)
    if degrees(theta_not) >= 10:
        majorLocator = mp.ticker.MultipleLocator(int(degrees(theta_not)/3))
        minorLocator = mp.ticker.MultipleLocator(int(degrees(theta_not)/10))
    else:
        majorLocator = mp.ticker.MultipleLocator(2);
        minorLocator = mp.ticker.MultipleLocator(1);
    smallAGfig.yaxis.set_major_locator(majorLocator);
    smallAGfig.yaxis.set_minor_locator(minorLocator);
    smallAGfig.grid(True, linestyle='-')
    return smallAGfig

def smallAngleGraph(mainFig):
    timeRange = numpy.arange(timeMin, timeMax, dt)
    smallAngleApproxPoints = smallAngleApproximation(timeRange)
    pendPoints = pendulumMotion(timeRange)
    writeToCSV("time", timeRange, "small angle approximation", smallAngleApproxPoints, "true pendulum motion", pendPoints)
    smallAGfig = setUpChart(mainFig)
    smallAGfig.plot(timeRange, map(degrees, smallAngleApproxPoints))
    smallAGfig.plot(timeRange, map(degrees, pendPoints))
    legend = smallAGfig.legend(('Small Angle Approximation', 'Actual Pendulum Motion'),'best', shadow=True)
    
    #mainFig.legend(('Small Angle Approximation', 'Actual Pendulum Motion'),bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., shadow=True)
def writeToCSV(label1, list1, label2, list2, label3, list3):
    writer = csv.writer(open(dataPath, mode = 'wb') , dialect='excel');
    title = "Pendulum Motion at",  degrees(theta_not), "degrees"
    writer.writerow(title)
    writer.writerow([label1, label2, label3])
    for index ,i in enumerate(list1):
        writer.writerow([list1[index], list2[index], list3[index]]);   

createGraphs();
