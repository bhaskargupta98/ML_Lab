#Create a sinusoidal signal Asin(wt+phase)
import matplotlib.pyplot as plot
import numpy as np
time = np.arange(0,10,0.1);
amp = int(input("Enter Amplitude"))
w = int(input("Enter frequency"))
phase = int(input("Enter phase"))
fn = amp*np.sin(w*time+phase)
plot.plot(time,fn)
plot.show()
