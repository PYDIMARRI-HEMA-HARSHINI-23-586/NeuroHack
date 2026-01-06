import scipy.io as sio
import numpy as np
from scipy.signal import welch

# ----------------------------
# Load dataset
# ----------------------------
data = sio.loadmat("data/DREAMER.mat")
dreamer = data["DREAMER"][0,0]
Data = dreamer["Data"]
sfreq = int(dreamer["EEG_SamplingRate"][0,0])

bands = {
    "theta": (4, 8),
    "alpha": (8, 13),
    "beta":  (13, 30)
}

def compute_psd(eeg, sfreq):
    psd_list = []
    for ch in range(eeg.shape[0]):
        freqs, psd = welch(eeg[ch], fs=sfreq, nperseg=sfreq * 2)
        psd_list.append(psd)
    return freqs, np.array(psd_list)

def band_power(psd, freqs, band):
    low, high = band
    idx = np.logical_and(freqs >= low, freqs <= high)
    return psd[:, idx].mean(axis=1)

X = []
y = []

# ----------------------------
# Loop through subjects & videos
# ----------------------------
for subj in range(Data.shape[1]):
    subject = Data[0, subj][0,0]
    EEG = subject["EEG"][0,0]
    
    baseline = EEG["baseline"]
    stimuli = EEG["stimuli"]
    
    valence_scores = subject["ScoreValence"].flatten()
    
    for vid in range(stimuli.shape[0]):
        base_eeg = baseline[vid,0].T
        stim_eeg = stimuli[vid,0].T
        
        freqs_b, psd_b = compute_psd(base_eeg, sfreq)
        freqs_s, psd_s = compute_psd(stim_eeg, sfreq)
        
        feature_vec = []
        for band in bands.values():
            stim_pow = band_power(psd_s, freqs_s, band)
            base_pow = band_power(psd_b, freqs_b, band)
            feature_vec.extend(stim_pow - base_pow)
        
        X.append(feature_vec)
        y.append(valence_scores[vid])

X = np.array(X)
y = np.array(y)

print("Feature matrix shape:", X.shape)
print("Labels shape:", y.shape)

# ----------------------------
# STEP 29: Binary Labeling
# ----------------------------
median_valence = np.median(y)
y_binary = (y > median_valence).astype(int)

print("Median valence:", median_valence)
print("Class distribution:", np.bincount(y_binary))

np.savez("data/eeg_features_valence.npz", X=X, y=y_binary)

