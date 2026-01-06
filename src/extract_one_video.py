import scipy.io as sio
import numpy as np

# Load data
data = sio.loadmat("data/DREAMER.mat")
dreamer = data["DREAMER"][0,0]
Data = dreamer["Data"]

# Pick subject 0
subject0 = Data[0, 0][0, 0]

# Extract EEG and labels
EEG = subject0["EEG"]
valence = subject0["ScoreValence"]
arousal = subject0["ScoreArousal"]
dominance = subject0["ScoreDominance"]

print("EEG type:", type(EEG))
print("EEG shape:", EEG.shape)

print("Valence shape:", valence.shape)
print("Arousal shape:", arousal.shape)
print("Dominance shape:", dominance.shape)
