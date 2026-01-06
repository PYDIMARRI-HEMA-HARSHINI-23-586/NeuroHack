import scipy.io as sio
import numpy as np
import mne
from scipy.signal import welch

# Load dataset
data = sio.loadmat("data/DREAMER.mat")
dreamer = data["DREAMER"][0,0]
Data = dreamer["Data"]

sfreq = int(dreamer["EEG_SamplingRate"][0,0])

# Pick subject 0 (for now)
subject0 = Data[0,0][0,0]
EEG_struct = subject0["EEG"][0,0]

baseline = EEG_struct["baseline"]
stimuli = EEG_struct["stimuli"]

# Pick video 0
baseline_eeg = baseline[0,0]
stimulus_eeg = stimuli[0,0]

# Convert to (channels, time)
baseline_eeg = baseline_eeg.T
stimulus_eeg = stimulus_eeg.T

print("Baseline shape:", baseline_eeg.shape)
print("Stimulus shape:", stimulus_eeg.shape)

# ---------- STEP 24: PSD Computation (Welch) ----------

def compute_psd(eeg, sfreq):
    """
    eeg: numpy array (channels, time)
    returns: freqs, psd (channels, frequencies)
    """
    psd_list = []
    for ch in range(eeg.shape[0]):
        freqs, psd = welch(
            eeg[ch],
            fs=sfreq,
            nperseg=sfreq * 2  # 2-second windows
        )
        psd_list.append(psd)
    return freqs, np.array(psd_list)


# Compute PSD for baseline and stimulus
freqs_base, psd_base = compute_psd(baseline_eeg, sfreq)
freqs_stim, psd_stim = compute_psd(stimulus_eeg, sfreq)

print("PSD baseline shape:", psd_base.shape)
print("PSD stimulus shape:", psd_stim.shape)

# ---------- STEP 25: EEG Frequency Bands ----------

bands = {
    "theta": (4, 8),
    "alpha": (8, 13),
    "beta":  (13, 30)
}

# ---------- STEP 26: Band Power Extraction ----------

def band_power(psd, freqs, band):
    low, high = band
    idx = np.logical_and(freqs >= low, freqs <= high)
    return psd[:, idx].mean(axis=1)  # mean power per channel


# Compute band powers
features = {}

for band_name, band_range in bands.items():
    stim_power = band_power(psd_stim, freqs_stim, band_range)
    base_power = band_power(psd_base, freqs_base, band_range)
    
    # Baseline correction
    features[band_name] = stim_power - base_power

for band in features:
    print(f"{band} feature shape:", features[band].shape)
