# EEG-Based Emotion Recognition (DREAMER Dataset)

## Dataset

- **Dataset**: DREAMER
- **Signals**: EEG (14-channel Emotiv headset)
- **Participants**: 23 subjects
- **Stimuli**: 18 audio-visual clips per subject
- **Annotations**: Valence, Arousal, Dominance (VAD) self-reports

Project Setup & Installation

## Project Setup & Installation

### Prerequisites

- Python **3.8 or above**
- Git
- Virtual environment support (recommended)

### Step 1: Clone the Repository

```bash
git clone <your-repository-url>
cd NeuroHack

Step 2: Create and Activate Virtual Environment
python -m venv eeg_env


Windows

eeg_env\Scripts\activate


Linux / macOS

source eeg_env/bin/activate

Step 3: Install Dependencies
pip install -r requirements.txt


Required libraries include:

numpy

scipy

matplotlib

seaborn

pandas

scikit-learn

mne

Step 4: Download Dataset

Download the DREAMER dataset from:
https://drive.google.com/file/d/1RaOPoqrRaUEjFlaWsSrW1XHLSuZfOj0a/view

Place the file as:

data/DREAMER.mat

Step 5: Run the Pipeline (Suggested Order)
# Phase 1: Exploratory Analysis
python src/phase1_vad_inspect.py
python src/phase1_arousal_valence_plot.py
python src/phase1_vad_correlation.py
python src/phase1_vad_barplot.py

# Phase 2: EEG Preprocessing
python src/create_raw_and_plot.py

# Phase 3: Feature Extraction
python src/build_dataset.py

# Phase 4: Classification
python src/train_classifier.py

---

## Pipeline Overview

1. Dataset inspection and structure understanding
2. EEG extraction and raw signal visualization
3. EEG preprocessing
   - 50 Hz notch filtering
   - 0.5–45 Hz band-pass filtering
   - ICA-based artifact removal
   - Common Average Referencing (CAR)
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

## 4. Exploratory Analysis of Emotional Ratings (Phase 1)

### 4.1 Arousal–Valence Emotional Space

- Plotted stimuli ratings in a 2D arousal–valence space.
- Observed that ratings are distributed across the full emotional space, with no strong clustering, indicating diverse emotional responses to the stimuli.

### 4.2 VAD Distribution Analysis

- Computed mean Valence, Arousal, and Dominance scores across all subjects and stimuli.
- Bar plots indicate a relatively balanced distribution of emotional dimensions.

### 4.3 Correlation Analysis

- Pearson correlation analysis was performed between Valence, Arousal, and Dominance.
- A strong positive correlation was observed between Arousal and Dominance (r ≈ 0.69).
- Valence showed weak correlation with both Arousal and Dominance, suggesting relative independence of emotional pleasantness from activation and control dimensions.

---

## 5. EEG Preprocessing (Phase 2)

### 5.1 Power Spectral Density (PSD) – Before Filtering

- Computed and visualized PSD of raw EEG signals.
- Identified a prominent peak around **50 Hz**, corresponding to power-line interference.

### 5.2 50 Hz Notch Filtering

- Applied a 50 Hz notch filter to suppress power-line noise.
- PSD comparison before and after filtering showed significant attenuation of the 50 Hz peak.

### 5.3 Band-Pass Filtering (0.5–45 Hz)

- Applied a 0.5–45 Hz band-pass filter to remove slow baseline drift and high-frequency muscle artifacts.
- PSD analysis confirmed preservation of theta, alpha, and beta band activity.

---

## 6. ICA-Based Artifact Removal

Independent Component Analysis (ICA) was applied to decompose EEG signals into independent sources.

- ICA separated mixed EEG signals into components corresponding to neural activity and artifacts.
- Due to the absence of electrode location information in the dataset, scalp topographies could not be generated.
- Artifact components were identified using temporal characteristics.
- The rejected component exhibited large-amplitude, slow deflections consistent with eye-blink artifacts.
- Visual comparison of EEG signals before and after ICA confirmed reduction of blink-related transients.

Although EEG signals remain visually complex after ICA, ICA removes specific artifact sources rather than smoothing the signal.

---

## 7. Common Average Referencing (CAR)

- Common Average Referencing was applied after ICA.
- Each EEG channel was re-referenced to the global average across all channels.
- CAR reduces common-mode noise shared across electrodes and is particularly suitable for low-density EEG systems such as the 14-channel Emotiv headset.

---

## 8. Feature Extraction (Phase 3)

### 8.1 Power Spectral Density

- PSD was computed for each EEG channel using **Welch’s method**.

### 8.2 Band Power Features

- Band power features were extracted for:
  - **Theta**: 4–8 Hz
  - **Alpha**: 8–13 Hz
  - **Beta**: 13–30 Hz

### 8.3 Baseline Correction

- Baseline EEG segments were used to compute resting-state band power.
- Baseline correction was applied as:

Corrected Power = Stimulus Power − Baseline Power

- This reduces subject-specific bias and highlights stimulus-induced neural activity.

---

## 9. Affect Recognition (Phase 4)

### 9.1 Label Processing

- Continuous valence ratings were converted into binary classes (High vs Low Valence).
- Median-based thresholding was used to reduce bias and ensure balanced class separation.

### 9.2 Classification Setup

- **Classifier**: Logistic Regression
- **Class Weighting**: Balanced
- **Evaluation Strategy**: 5-fold Stratified Cross-Validation
- **Metrics**: Accuracy and F1-score

---

## 10. Results

- **Mean Accuracy**: 0.437
- **Mean F1-score**: 0.535

---
## 11. Phase 5 (Bonus): Band Power Insights

Mean theta, alpha, and beta power compared across valence classes

Alpha power tended to be higher during low-valence states

Beta power increased for high-valence samples

Confirms that frequency-domain EEG features encode affective information

## 12. Discussion

- The dataset exhibits mild class imbalance, with more low-valence samples than high-valence samples.
- Accuracy alone was not a reliable metric; therefore, F1-score was emphasized.
- Class-weighted Logistic Regression significantly improved minority-class recognition, reflected by a higher F1-score, at the cost of reduced overall accuracy.
- The moderate performance highlights the inherent difficulty of EEG-based emotion recognition and strong inter-subject variability.

---

## 13. Artifact Subspace Reconstruction (ASR) – Limitation

Artifact Subspace Reconstruction (ASR) is an automated EEG denoising technique that
repairs short-duration, high-amplitude artifacts by comparing signal statistics
against a clean reference subspace using a cutoff parameter (k).

In this work, ASR was not applied due to the absence of a reliable clean reference
segment and the lack of native ASR support in the MNE-Python framework. Instead,
artifact mitigation was achieved using a combination of band-pass filtering,
ICA-based artifact removal, and Common Average Referencing. Future work may explore
ASR-based denoising using EEGLAB-compatible pipelines.

---

## 14. Project Status Summary

- **Dataset Understanding**: ✅
  DREAMER dataset structure explored and validated; EEG and VAD annotations correctly extracted.

- **Exploratory VAD Analysis (Phase 1)**: ✅
  Arousal–Valence emotional space visualization and correlation analysis completed, revealing
  strong arousal–dominance coupling and weak valence dependency.

- **EEG Extraction**: ✅
  Multi-channel EEG signals successfully extracted and formatted for analysis using MNE.

- **EEG Preprocessing (Phase 2)**: ✅
  Signal cleaning performed using 50 Hz notch filtering, 0.5–45 Hz band-pass filtering,
  ICA-based artifact removal, and Common Average Referencing (CAR), with PSD-based validation.

- **Feature Extraction (Phase 3)**: ✅
  Power Spectral Density computed using Welch’s method; theta, alpha, and beta band power
  features extracted with baseline correction to reduce subject-specific bias.

- **Affect Recognition & Evaluation (Phase 4)**: ✅
  Valence-based emotion classification performed using class-weighted Logistic Regression
  with stratified cross-validation; performance evaluated using accuracy and F1-score.

- **Advanced Insights & Interpretation (Phase 5 – Partial)**: ✅
  Frequency-domain insights were derived by analyzing band power behavior across emotional
  conditions. Preprocessing effects on spectral quality were validated using PSD plots.
  Inter-subject variability and limitations of spatial analysis were critically discussed.
  Band power analysis across emotions
  Frequency-domain insight and interpretation


---
```
