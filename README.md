# EEG-Based Emotion Recognition (DREAMER Dataset)

## Dataset

- **Dataset**: DREAMER
- **Signals**: EEG (14-channel Emotiv headset)
- **Participants**: 23 subjects
- **Stimuli**: 18 audio-visual clips per subject
- **Annotations**: Valence, Arousal, Dominance (VAD) self-reports

---

## Pipeline Overview

1. Dataset inspection and structure understanding
2. EEG extraction and raw signal visualization
3. EEG preprocessing
   - 50 Hz notch filtering
   - 0.5–45 Hz band-pass filtering
   - ICA-based artifact removal
4. Feature extraction
   - Power Spectral Density (PSD)
   - Theta, Alpha, Beta band power
   - Baseline correction
5. Affect recognition (Valence classification)
6. Evaluation and analysis

---

## 1. Dataset Inspection & Structure Understanding

- Loaded the `.mat` file and inspected the hierarchical DREAMER MATLAB structure.
- Identified the organization as:

DREAMER → Data → Subject → EEG → {baseline, stimuli}

- Verified that EEG data for each stimulus is stored as multi-channel time-series signals.

---

## 2. EEG Extraction

- Extracted EEG data for individual subjects and stimuli.
- Confirmed EEG data shape as:

(time_samples, channels) = (25472, 14)

- Transposed EEG signals to `(channels, time)` format for compatibility with MNE-Python.

---

## 3. Raw EEG Visualization

- Converted EEG data into an MNE `Raw` object.
- Visualized unfiltered EEG signals across all channels.
- Observed large amplitude fluctuations and transient spikes, indicating the presence of physiological (eye blinks, muscle activity) and environmental noise.

---

## 4. Power Spectral Density (PSD) Analysis – Before Filtering

- Computed and visualized PSD of raw EEG signals.
- Identified a prominent peak around **50 Hz**, corresponding to power-line interference.

---

## 5. EEG Preprocessing

### 5.1 50 Hz Notch Filtering

- Applied a 50 Hz notch filter to suppress power-line noise.
- PSD comparison before and after filtering showed significant attenuation of the 50 Hz peak, confirming effective noise removal.

### 5.2 Band-Pass Filtering (0.5–45 Hz)

- Applied a 0.5–45 Hz band-pass filter to remove slow baseline drift and high-frequency muscle artifacts.
- PSD analysis confirmed suppression of non-neural frequency components while preserving brain-relevant theta, alpha, and beta activity.

---

## 6. ICA-Based Artifact Removal

Independent Component Analysis (ICA) was applied to decompose EEG signals into independent sources.

- ICA separated mixed EEG signals into components corresponding to neural activity and artifacts.
- Due to the absence of electrode location information in the dataset, scalp topographies could not be generated.
- Artifact components were identified using temporal characteristics.
- Components exhibiting large, slow deflections typical of eye-blink activity were excluded.
- Visual comparison of EEG signals before and after ICA confirmed reduction of blink-related artifacts.

Although EEG signals remain visually complex after ICA, the large synchronized blink-related transients observed before ICA were reduced. ICA removes specific artifact sources rather than smoothing the signal.

---

## 7. Feature Extraction

### 7.1 Power Spectral Density

- PSD was computed for each EEG channel using **Welch’s method** to obtain frequency-domain representations.

### 7.2 Band Power Features

- Band power features were extracted for:
  - **Theta**: 4–8 Hz
  - **Alpha**: 8–13 Hz
  - **Beta**: 13–30 Hz

### 7.3 Baseline Correction

- Baseline correction was applied by subtracting baseline band power from stimulus band power.
- This accounts for subject-specific resting-state differences and highlights stimulus-induced neural activity.

---

## 8. Affect Recognition (Valence Classification)

### Label Processing

- Continuous valence ratings were converted into binary classes (High vs Low Valence).
- Median-based thresholding was used to reduce bias and maintain balanced class separation.

---

## 9. Classification Setup

- **Classifier**: Logistic Regression
- **Class Weighting**: Balanced
- **Evaluation Strategy**: 5-fold Stratified Cross-Validation
- **Metrics**: Accuracy and F1-score

---

## 10. Results

- **Mean Accuracy**: 0.437
- **Mean F1-score**: 0.535

---

## 11. Discussion

- The dataset exhibits mild class imbalance, with more low-valence samples than high-valence samples.
- Accuracy alone was not a reliable metric; therefore, F1-score was emphasized.
- Class-weighted Logistic Regression significantly improved minority-class recognition, reflected in the higher F1-score, albeit at the cost of reduced overall accuracy.
- The moderate performance highlights the inherent difficulty of EEG-based emotion recognition and strong inter-subject variability.

---

## 12. Current Status

- Dataset understanding: ✅
- EEG extraction: ✅
- Raw EEG visualization: ✅
- Notch & band-pass filtering: ✅
- ICA artifact removal: ✅
- Feature extraction: ✅
- Classification & evaluation: ✅

---
