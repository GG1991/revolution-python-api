import sys
sys.path.append("../qrs_detector/python")

import time
import numpy as np

import detection
from bitalino import BITalino

# The macAddress variable on Windows can be "XX:XX:XX:XX:XX:XX" or "COMX"
# while on Mac OS can be "/dev/tty.BITalino-XX-XX-DevB" for devices ending with the last 4 digits of the MAC address or "/dev/tty.BITalino-DevB" for the remaining
macAddress = "20:16:12:22:50:10"

# This example will collect data for 5 sec.
running_time = 10
    
batteryThreshold = 30
acqChannels = [0, 1, 2, 3, 4, 5]
samplingRate = 1000
nSamples = 10
digitalOutput = [0,0]
electro_channel = 5

# Connect to BITalino
device = BITalino(macAddress)

# Set battery threshold
device.battery(batteryThreshold)

# Read BITalino version
print(device.version())
    
# Start Acquisition
device.start(samplingRate, acqChannels)

file_ = open('result.dat','w') 
start = time.time()
end = time.time()
while (end - start) < running_time:

    bit_out = device.read(nSamples)
    print(bit_out)

    end = time.time()
    result = detection.detect(input_signal, 2000)
    for i in range(0,nSamples):
        file_.write(str(end - start) + "\t" + str(bit_out[i,5]) + "\t" + str(bit_out[i,6]) + "\n")

file_.close()
# Turn BITalino led on
device.trigger(digitalOutput)
    
# Stop acquisition
device.stop()
    
# Close connection
device.close()
