# Learnings – EEG Preprocessing (Session 1)

## Dataset Handling

- MATLAB `.mat` files often contain deeply nested structures.
- DREAMER dataset required careful inspection to correctly access EEG data.
- EEG stimulus data is stored separately from baseline information.

## EEG Data Format

- Raw EEG stimulus data is stored as `(time_samples, channels)`.
- MNE requires EEG data in `(channels, time)` format.

## Raw EEG Characteristics

- Raw EEG signals are highly noisy and contain large spikes.
- Noise sources include eye blinks, muscle movement, and electrical interference.

## Frequency-Domain Insight

- Power Spectral Density (PSD) is useful to identify noise patterns.
- A strong peak at 50 Hz corresponds to power-line noise (India).

## Filtering Insight

- Notch filtering at 50 Hz effectively removes power-line interference.
- Visual comparison of PSD before and after filtering is essential proof of signal cleaning.

## Key Takeaway

- EEG preprocessing is primarily about improving signal quality before feature extraction.
- Visual inspection is as important as numerical processing in EEG analysis.

## Band-pass Filtering

- EEG contains slow drift (<0.5 Hz) and high-frequency muscle noise (>45 Hz).
- Applying a 0.5–45 Hz band-pass filter improves signal quality.
- PSD plots help verify that non-neural frequencies are suppressed.
