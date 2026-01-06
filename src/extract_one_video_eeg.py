import scipy.io as sio

data = sio.loadmat("data/DREAMER.mat")
dreamer = data["DREAMER"][0,0]
Data = dreamer["Data"]

# Subject 0
subject0 = Data[0,0][0,0]

EEG_struct = subject0["EEG"][0,0]

baseline = EEG_struct["baseline"]
stimuli = EEG_struct["stimuli"]

print("Baseline EEG shape (all videos):", baseline.shape)
print("Stimuli EEG shape (all videos):", stimuli.shape)

# Extract video 0
baseline_v0 = baseline[0]
stimuli_v0 = stimuli[0]

print("Baseline video 0 shape:", baseline_v0.shape)
print("Stimuli video 0 shape:", stimuli_v0.shape)
