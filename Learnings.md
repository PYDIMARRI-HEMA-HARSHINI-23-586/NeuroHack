# Learnings & Reflections – EEG Emotion Recognition Project

This file captures the raw learnings, mistakes, fixes, and key insights gained while
working on EEG-based emotion recognition using the DREAMER dataset. The focus is on
what went wrong, how it was corrected, and what was learned at each stage.

---

## 1. Dataset Handling & Initial Confusion

### What went wrong

- The DREAMER dataset is stored as a deeply nested MATLAB `.mat` structure.
- Initial attempts to directly access EEG data resulted in unexpected shapes such as
  empty arrays or scalar values.
- Baseline and stimulus EEG data were not organized as initially assumed.

### How it was fixed

- The dataset structure was inspected step-by-step using debug scripts.
- Shapes and data types were printed at each level of the hierarchy.
- The correct organization was identified as:

DREAMER → Data → Subject → EEG → {baseline, stimuli}

### Key takeaway

- Never assume the structure of biomedical datasets.
- Incremental inspection is critical when working with `.mat` files.

---

## 2. EEG Data Format Issues

### Observation

- EEG stimulus data was stored as `(time_samples, channels)`.
- Directly passing this format into MNE caused issues.

### Resolution

- EEG data was transposed to `(channels, time)` format before creating MNE `Raw` objects.

### Key takeaway

- Library-specific data format requirements must always be respected.
- Incorrect orientation can silently break downstream processing.

---

## 3. Raw EEG Characteristics Were Initially Misleading

### Initial reaction

- Raw EEG plots showed extreme spikes and irregular patterns.
- This initially appeared as corrupted or unusable data.

### Realization

- Raw EEG is naturally noisy.
- Eye blinks, muscle activity, and environmental electrical interference are expected.

### Key takeaway

- Noisy EEG does not imply poor data quality.
- Preprocessing is essential, not optional, for EEG-based machine learning.

---

## 4. Importance of Frequency-Domain Analysis

### What was unclear at first

- Time-domain plots did not clearly explain the source of noise.

### How clarity was achieved

- Power Spectral Density (PSD) plots revealed a strong peak at 50 Hz.
- This peak was identified as power-line noise (India).

### Key takeaway

- Frequency-domain analysis is crucial for diagnosing EEG noise.
- PSD plots provide strong visual justification for filtering decisions.

---

## 5. Filtering Insights & Order of Operations

### Learning

- A 50 Hz notch filter effectively removed power-line interference.
- A band-pass filter (0.5–45 Hz) removed slow baseline drift and high-frequency muscle noise.

### Important realization

- The order of filtering matters:

1. Notch filtering (power-line noise)
2. Band-pass filtering (brain-relevant frequencies)

### Key takeaway

- Filtering should be applied logically, not blindly.
- PSD plots are essential to validate each filtering step.

---

## 6. ICA Artifact Removal Was Not Straightforward

### Initial confusion

- After applying ICA, EEG signals still appeared noisy.
- This led to doubt about whether ICA had actually worked.

### Clarification

- ICA removes specific artifact sources (e.g., eye blinks), not all noise.
- Clean EEG does not mean smooth EEG.

### Additional limitation

- ICA scalp topographies could not be plotted due to missing electrode location
  information in the dataset.

### How it was handled

- Artifact components were identified using temporal patterns instead.
- This limitation was explicitly documented instead of forcing incorrect visualizations.

### Key takeaway

- ICA effectiveness should be judged by reduction of structured artifacts, not by visual smoothness.
- Honest documentation of limitations is better than artificial results.

---

## 7. Baseline Correction Changed Feature Interpretation

### Observation

- Absolute EEG band power values varied significantly across subjects.

### Realization

- Each subject has a unique resting-state brain activity pattern.
- Comparing raw band power across subjects is misleading.

### Resolution

- Baseline correction was applied:

Corrected Power = Stimulus Power − Baseline Power

### Key takeaway

- Baseline correction is essential to reduce subject-specific bias in EEG analysis.

---

## 8. Feature Engineering Was More Important Than Model Complexity

### What worked well

- Simple band power features (Theta, Alpha, Beta) were sufficient.
- Welch’s method produced stable and interpretable PSD estimates.

### Key takeaway

- In EEG-based ML, meaningful features matter more than complex models.

---

## 9. Class Imbalance Affected Model Evaluation

### Initial result

- Accuracy appeared reasonable, but F1-score was extremely low.
- The model was biased toward the majority class.

### How it was fixed

- Introduced class-weighted Logistic Regression.
- Accuracy decreased, but F1-score improved significantly.

### Key takeaway

- Accuracy alone is misleading for imbalanced datasets.
- F1-score provides a more reliable evaluation for affect recognition.

---

## 10. Final Reflection

### Overall realizations

- EEG preprocessing is the most challenging and critical phase.
- Visual validation is as important as numerical metrics.
- Moderate performance is expected due to noise, inter-subject variability, and subjective labels.

### Final takeaway

- Strong reasoning, transparent reporting, and correct methodology matter more than high accuracy in EEG-based emotion recognition.
