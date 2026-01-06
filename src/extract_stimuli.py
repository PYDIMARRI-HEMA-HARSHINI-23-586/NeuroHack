import scipy.io as sio

data = sio.loadmat("data/DREAMER.mat")
dreamer = data["DREAMER"][0,0]
Data = dreamer["Data"]

# Subject 0
subject0 = Data[0,0][0,0]

EEG_struct = subject0["EEG"][0,0]
stimuli = EEG_struct["stimuli"]

print("Stimuli container shape:", stimuli.shape)

# Extract video 0 EEG (THIS is the real EEG)
stimuli_v0 = stimuli[0,0]

print("Stimuli video 0 type:", type(stimuli_v0))
print("Stimuli video 0 shape:", stimuli_v0.shape)
