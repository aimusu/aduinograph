import serial
import numpy as np
from matplotlib import pyplot as plt
from drawnow import *

sensorData = []
ser = serial.Serial('COM16', 9600)
plt.ion()
plt.rcParams["figure.figsize"]= [10,6]
cnt = 0
def makefig():
    plt.ylim(0,1040)
    plt.ylabel('Sensor Data (V)')
    plt.xlabel('Time')
    plt.title('Real Time MQ-6 Gas Sensor Data')
    plt.grid(True)
    if (sensorData[-1]) >= 700:
        #plt.plot(sensorData, 'gh-', label= 'Random number generation',linewidth=2,markerfacecolor='b',markersize= 8)
        plt.plot(sensorData, 'rh-', label= 'Warning Excess LPG Gas Detected!!!',linewidth=8,markerfacecolor='red',markersize= 18)
        plt.annotate('Current MQ-6 Gas Sensor Data : ' + str(sensorData[-1]) +' ppm',xy=(0.3, 860), xytext=(0.3, 860), fontsize=16,color='r')
    if (sensorData[-1]) > 500 and (sensorData[-1]) < 700:
        #plt.plot(sensorData, 'gh-', label= 'Random number generation',linewidth=2,markerfacecolor='b',markersize= 8)
        plt.plot(sensorData, 'rh-', label= 'LPG Gas Detected',linewidth=4,markerfacecolor='red',markersize= 12)
        plt.annotate('Current MQ-6 Gas Sensor Data : ' + str(sensorData[-1]) +' ppm',xy=(0.3, 860), xytext=(0.3, 860), fontsize=14,color='r')
    if (sensorData[-1]) <= 300:
        plt.plot(sensorData, 'gh-', label= 'MQ-6 Gas Sensor Data',linewidth=2,markerfacecolor='b',markersize= 8)
        plt.annotate('Current MQ-6 Gas Sensor Data : ' + str(sensorData[-1]) +' ppm',xy=(0.3, 860), xytext=(0.3, 860), fontsize=14)
    plt.legend(loc='upper left')

while True:
    while (ser.inWaiting() == 0):
        pass
    serial = int(ser.readline())
    sensorData.append(serial)
    drawnow(makefig)
    plt.pause(0.0000000001)
    cnt +=1
    if (cnt > 25):
        sensorData.pop(0)

    
