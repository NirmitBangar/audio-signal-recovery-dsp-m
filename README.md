#  Advanced Audio Signal Recovery using DSP

##  Overview
This project focuses on recovering a corrupted audio signal using advanced Digital Signal Processing techniques, including Fourier analysis, bandpass filtering, and spectral visualization.

---

##  Mathematical Model

x(t) = s(t) + n(t)

Where:
- s(t): original signal
- n(t): noise

---

##  Fourier Transform

X(f) = ∫ x(t)e^(-j2πft) dt

Used to analyze frequency components of the signal.

---

##  Filtering

Y(f) = H(f) · X(f)

Bandpass filter used:
300 Hz – 3000 Hz

---

##  Reconstruction

y(t) = F⁻¹[Y(f)]

---

##  Spectrogram Analysis 

Spectrogram shows how frequency content evolves over time.

Before filtering:
- Noise dominates across spectrum

After filtering:
- Signal band clearly visible

---

##  Signal-to-Noise Ratio (SNR)

SNR = 10 log10 (Ps / Pn)

Measured improvement stored in:

snr.txt

---

##  Results

### Noisy Signal
![Time](./plots/time_signal.png)

### Frequency Spectrum
![FFT](./plots/frequency_spectrum.png)

### Filtered Signal
![Filtered](./plots/filtered_signal.png)

### Spectrogram Before
![Before](./plots/spectrogram_before.png)

### Spectrogram After
![After](./plots/spectrogram_after.png)

---

##  Output

Recovered audio:

output.wav

---

##  Highlights

✔ Fourier Transform-based analysis  
✔ Butterworth Bandpass Filtering  
✔ Spectrogram visualization  
✔ Quantitative SNR improvement  
✔ End-to-end DSP pipeline  

---

##  Conclusion

This project demonstrates how mathematical signal processing techniques can effectively extract meaningful signals from noise, validated both visually and quantitatively.
