# EEG-Based Emotion Recognition – Progress Log

## Dataset

- Dataset: DREAMER
- EEG recorded using a 14-channel Emotiv headset
- 23 subjects × 18 audio-visual stimuli
- Each stimulus annotated with Valence, Arousal, and Dominance (VAD) ratings

---

## Work Completed So Far

### 1. Dataset Inspection & Structure Understanding

- Loaded the `.mat` file and inspected the DREAMER MATLAB structure.
- Identified hierarchical organization:
  - DREAMER → Data → Subject → EEG → stimuli
- Verified that EEG stimulus data is stored as time-series per channel.

---

### 2. EEG Extraction

- Extracted EEG data for a single subject and a single video stimulus.
- Final EEG shape confirmed as:
  - `(time_samples, channels) = (25472, 14)`
- Transposed EEG to `(channels, time)` format for MNE compatibility.

---

### 3. Raw EEG Visualization

- Converted EEG data into an MNE `Raw` object.
- Visualized unfiltered EEG signals across all 14 channels.
- Observed large amplitude fluctuations and transient spikes, indicating the presence of physiological and environmental noise.

---

### 4. Power Spectral Density (PSD) Analysis – Before Filtering

- Computed and visualized PSD of raw EEG signals.
- Identified a prominent peak around 50 Hz across multiple channels.

---

### 5. 50 Hz Notch Filtering

- Applied a 50 Hz notch filter to remove power-line interference.
- Compared PSD before and after filtering.
- Observed significant attenuation of the 50 Hz peak, confirming effective noise removal.

After applying a 50 Hz notch filter followed by a 0.5–45 Hz band-pass filter, low-frequency drift and high-frequency muscle artifacts were suppressed. PSD analysis confirms removal of non-neural frequency components while preserving theta, alpha, and beta band activity.

## ICA separates mixed EEG signals into independent sources; some correspond to brain activity, others to artifacts like eye blinks and muscle noise.

Independent Component Analysis (ICA) was applied to decompose EEG signals into independent sources. Due to the absence of electrode location information in the dataset, scalp topographies could not be generated. Artifact components were therefore identified based on their temporal characteristics. Components exhibiting large, slow deflections typical of eye-blink activity were excluded. Visual comparison of EEG signals before and after ICA confirms reduction of blink-related artifacts.

Although the EEG signals remain visually complex after ICA, the large, synchronized blink-related transients observed before ICA are reduced. ICA removes specific artifact sources rather than smoothing the signal, leading to more uniformly distributed neural activity.

## Current Status

- Dataset understanding: ✅
- EEG extraction: ✅
- Raw EEG visualization: ✅
- 50 Hz notch filtering: ✅
- Band-pass filtering: ⏳
- ICA artifact removal: ⏳
- Feature extraction: ⏳
- Classification & evaluation: ⏳
