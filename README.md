#  Advanced Audio Signal Recovery using Digital Signal Processing

---

##  Problem Statement

Real-world audio signals are often corrupted by noise due to transmission errors, environmental disturbances, or hardware limitations.  
This project aims to **recover an original signal hidden inside a noisy observation** using mathematically grounded Digital Signal Processing (DSP) techniques.

---

##  Mathematical Signal Model

We model the observed signal as:

x(t) = s(t) + n(t)

Where:

- x(t): observed noisy signal  
- s(t): original clean signal  
- n(t): additive noise (assumed stochastic, zero-mean)

---

##  Continuous Fourier Transform

To analyze frequency content:

X(f) = ∫ x(t) e^(-j2πft) dt

This transforms the signal from time domain → frequency domain.

---

##  Discrete Implementation (DFT)

Since the signal is digital:

X[k] = Σ x[n] e^(-j2πkn/N)

Where:

- N = number of samples  
- k = frequency index  

Efficiently computed using **Fast Fourier Transform (FFT)**:

Complexity: O(N log N)

---

##  Spectral Representation

Magnitude spectrum:

|X(f)| = √(Re(X)^2 + Im(X)^2)

Phase spectrum:

∠X(f) = tan⁻¹(Im(X)/Re(X))

---

##  Filter Design (Butterworth Bandpass)

We design a **Butterworth filter** due to its smooth frequency response.

### Transfer Function:

|H(f)|² = 1 / (1 + (f/fc)^(2n))

Where:

- fc = cutoff frequency  
- n = filter order  

---

##  Bandpass Constraint

We define:

300 Hz ≤ f ≤ 3000 Hz

### Why?

- Human speech lies in this band  
- Noise typically spreads across full spectrum  
- Removes:
  - low-frequency drift  
  - high-frequency noise  

---

##  Filtering Operation

In frequency domain:

Y(f) = H(f) · X(f)

This acts as a selective mask:

- Passband → retained  
- Stopband → attenuated  

---

##  Signal Reconstruction

Inverse transform:

y(t) = F⁻¹[Y(f)]

Reconstructs filtered signal in time domain.

---

##  Spectrogram Analysis (Time-Frequency Representation)

Spectrogram is computed as:

S(t, f) = |STFT(x(t))|²

Where STFT is Short-Time Fourier Transform:

STFT{x(t)} = ∫ x(τ) w(t - τ) e^(-j2πfτ) dτ

---

### Interpretation:

- X-axis → time  
- Y-axis → frequency  
- Color → magnitude  

---

##  Results Visualization

###  Noisy Signal (Time Domain)
![Time](./plots/time_signal.png)

---

###  Frequency Spectrum
![FFT](./plots/frequency_spectrum.png)

---

###  Filtered Signal
![Filtered](./plots/filtered_signal.png)

---

###  Spectrogram Before Filtering
![Before](./plots/spectrogram_before.png)

---

###  Spectrogram After Filtering
![After](./plots/spectrogram_after.png)

---

##  Signal-to-Noise Ratio (SNR)

SNR quantifies signal quality:

SNR = 10 log₁₀ (Ps / Pn)

Where:

- Ps = signal power  
- Pn = noise power  

---

### Power Calculation:

Signal power:

Ps = (1/N) Σ s[n]²  

Noise power:

Pn = (1/N) Σ n[n]²  

---

### Interpretation:

- Higher SNR → cleaner signal  
- Filtering reduces Pn → increases SNR  

---

##  Algorithm Pipeline

1. Load input.wav  
2. Normalize signal  
3. Compute FFT  
4. Analyze frequency components  
5. Design Butterworth bandpass filter  
6. Apply filter (convolution / transfer function)  
7. Compute spectrogram  
8. Calculate SNR  
9. Reconstruct output signal  
10. Save output.wav  

---

##  Implementation Details

- Language: Python  
- Libraries:
  - NumPy → numerical computation  
  - SciPy → signal processing  
  - Matplotlib → visualization  

---

##  Assumptions

- Noise is additive and uncorrelated  
- Signal is band-limited  
- System is linear and time-invariant (LTI)  

---

##  Limitations

- Fixed filter band (not adaptive)  
- Not suitable for non-stationary noise  
- Phase distortion possible  

---

##  Future Improvements

- Adaptive filtering (LMS, RLS)  
- Wavelet denoising  
- Deep learning-based reconstruction  
- Real-time processing  

---

##  Conclusion

This project demonstrates a **complete DSP pipeline**, combining:

- Mathematical modeling  
- Frequency-domain analysis  
- Optimal filter design  
- Time-frequency visualization  
- Quantitative performance evaluation (SNR)  

It highlights how **rigorous mathematical tools can recover meaningful signals from noisy environments**, a fundamental principle in communication systems, audio engineering, and signal intelligence.

---

##  Final Remark

This implementation bridges **theory and practice**, transforming abstract mathematical concepts into a working system capable of real-world signal recovery.
