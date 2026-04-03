import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import butter, lfilter
from scipy.fft import fft, fftfreq

os.makedirs("plots", exist_ok=True)

fs, data = wavfile.read("input.wav")
data = data / np.max(np.abs(data))

plt.figure()
plt.plot(data)
plt.title("Noisy Signal")
plt.savefig("plots/time_signal.png")

N = len(data)
yf = fft(data)
xf = fftfreq(N, 1/fs)

plt.figure()
plt.plot(xf[:N//2], np.abs(yf[:N//2]))
plt.title("Frequency Spectrum")
plt.savefig("plots/frequency_spectrum.png")

def bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

b, a = bandpass(300, 3000, fs)
filtered = lfilter(b, a, data)

plt.figure()
plt.plot(filtered)
plt.title("Filtered Signal")
plt.savefig("plots/filtered_signal.png")

filtered = np.int16(filtered / np.max(np.abs(filtered)) * 32767)
wavfile.write("output.wav", fs, filtered)

print("Done")
