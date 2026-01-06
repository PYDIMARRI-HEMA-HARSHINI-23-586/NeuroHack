import scipy.io as sio
import numpy as np

# Load dataset
data = sio.loadmat("data/DREAMER.mat")
dreamer = data["DREAMER"][0, 0]
Data = dreamer["Data"]

valence_all = []
arousal_all = []
dominance_all = []

# Loop through all subjects
for subj in range(Data.shape[1]):
    subject = Data[0, subj][0, 0]
    
    valence = subject["ScoreValence"]
    arousal = subject["ScoreArousal"]
    dominance = subject["ScoreDominance"]
    
    valence_all.append(valence.flatten())
    arousal_all.append(arousal.flatten())
    dominance_all.append(dominance.flatten())

# Convert to numpy arrays
valence_all = np.concatenate(valence_all)
arousal_all = np.concatenate(arousal_all)
dominance_all = np.concatenate(dominance_all)

print("Total samples:", len(valence_all))
print("Valence range:", valence_all.min(), "to", valence_all.max())
print("Arousal range:", arousal_all.min(), "to", arousal_all.max())
print("Dominance range:", dominance_all.min(), "to", dominance_all.max())
