import scipy.io as sio
import numpy as np
import mne
import matplotlib.pyplot as plt
from mne.preprocessing import ICA

# Load data
data = sio.loadmat("data/DREAMER.mat")
dreamer = data["DREAMER"][0,0]
Data = dreamer["Data"]

# Pick subject 0, video 0
subject0 = Data[0,0][0,0]
EEG_struct = subject0["EEG"][0,0]
stimuli = EEG_struct["stimuli"]

eeg = stimuli[0,0]          # shape: (time, channels)
eeg = eeg.T                 # shape: (channels, time)

print("EEG final shape for MNE:", eeg.shape)

# Sampling frequency
sfreq = int(dreamer["EEG_SamplingRate"][0,0])

# Create channel names
ch_names = [f"EEG{i+1}" for i in range(eeg.shape[0])]
ch_types = ["eeg"] * len(ch_names)

# Create MNE info and Raw object
info = mne.create_info(ch_names=ch_names, sfreq=sfreq, ch_types=ch_types)
raw = mne.io.RawArray(eeg, info)

# Plot raw EEG (first sanity check)
raw.plot(duration=5, n_channels=14, title="Raw EEG (Unfiltered)")

# ----- STEP 13: 50 Hz Notch Filter -----

# PSD before notch (for comparison)
raw.plot_psd(fmax=60)

# Apply notch filter
raw_notch = raw.copy().notch_filter(freqs=50)

# PSD after notch
raw_notch.plot_psd(fmax=60)

# ----- STEP 14: Band-pass Filter (0.5–45 Hz) -----

# Apply band-pass filter on notch-filtered data
raw_bandpass = raw_notch.copy().filter(l_freq=0.5, h_freq=45)

# Plot PSD after band-pass filtering
raw_bandpass.plot_psd(fmax=60)




# =================================================
# STEP 15–19: ICA (Artifact Removal)
# =================================================



# Prepare data for ICA (slight high-pass for stability)
raw_for_ica = raw_bandpass.copy().filter(l_freq=1.0, h_freq=None)

# Fit ICA
ica = ICA(
    n_components=14,
    random_state=42,
    max_iter="auto"
)
ica.fit(raw_for_ica)

# Visualize ICA sources and components
ica.plot_sources(raw_for_ica)
# ica.plot_components()

# 👇 AFTER visually inspecting plots, choose components to exclude
# Example: eye-blink components
ica.exclude = [0]   # change based on what YOU observe

# Apply ICA cleaning
raw_ica_cleaned = raw_bandpass.copy()
ica.apply(raw_ica_cleaned)

# Compare before and after ICA
raw_bandpass.plot(duration=5, title="Before ICA")
raw_ica_cleaned.plot(duration=5, title="After ICA")





plt.show(block=True)
