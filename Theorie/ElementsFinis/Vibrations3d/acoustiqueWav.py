
import numpy as np
from scipy.io.wavfile import write
vals       = np.loadtxt('om_amp.txt')
freqs = [int(x) for x in vals[:,0]]

samplerate = int(100000)

t = np.linspace(0., 4., samplerate)

amplitude = np.iinfo(np.int16).max
datas = np.zeros((len(t),),'f')
for i,fs in enumerate(freqs[:6]):
    datas += amplitude * vals[i,1]*np.sin(2. * np.pi * fs * t)

datas=datas.astype(np.int16)
from pylab import *
plot(t,datas)
show()
write("example.wav", samplerate, datas)
